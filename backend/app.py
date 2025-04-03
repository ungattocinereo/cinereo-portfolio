import os
import datetime
import json
import subprocess
import frontmatter # For parsing frontmatter
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app) # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['OBSIDIAN_VAULT_PATH'] = '/home/greg/cinereo-notes' # Path to the cloned Obsidian vault repo

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Cinereo Portfolio API!"})

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from the API!"})

# --- Models ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False) # Will store Markdown
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

    def to_dict(self, full=False):
        data = {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'created_at': self.created_at.isoformat() + 'Z', # ISO 8601 format
            'updated_at': self.updated_at.isoformat() + 'Z',
        }
        if full:
            data['content'] = self.content # Keep as Markdown for now
            data['is_published'] = self.is_published
        return data

# --- CLI Commands ---
@app.cli.command("seed_db")
def seed_db():
    """Seeds the database with sample data."""
    print("Seeding database...")
    post1 = Post(
        title="My First Blog Post",
        slug="my-first-blog-post",
        content="This is the content of my **first** blog post. It uses *Markdown*.",
        is_published=True
    )
    post2 = Post(
        title="Another Interesting Article",
        slug="another-interesting-article",
        content="Here's another article about something interesting.\n\n```python\nprint('Hello, World!')\n```",
        is_published=True
    )
    post3 = Post(
        title="Draft Post",
        slug="draft-post",
        content="This post is not published yet.",
        is_published=False
    )

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()
    print("Database seeded!")

# --- API Routes ---

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.filter_by(is_published=True).order_by(Post.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts])

@app.route('/api/posts/<string:slug>', methods=['GET'])
def get_post(slug):
    post = Post.query.filter_by(slug=slug, is_published=True).first_or_404()
    # The first_or_404() handles the None case, returning a 404 automatically.
    return jsonify(post.to_dict(full=True))

# --- Helper Functions ---
def process_markdown_files(repo_path):
    """
    Scans the repository path for markdown files, parses them,
    and updates the database.
    """
    print(f"Processing markdown files in {repo_path}...")
    processed_count = 0
    skipped_count = 0
    error_count = 0

    for subdir, _, files in os.walk(repo_path):
        # Skip .git directory and potentially others like .obsidian
        if '.git' in subdir.split(os.path.sep) or '.obsidian' in subdir.split(os.path.sep):
            continue

        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(subdir, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        post_fm = frontmatter.load(f)

                    metadata = post_fm.metadata
                    content = post_fm.content

                    # --- Data Validation ---
                    slug = metadata.get('slug')
                    title = metadata.get('title')
                    is_published = metadata.get('published', False) # Default to False if not present

                    if not slug:
                        print(f"Skipping {file_path}: Missing 'slug' in frontmatter.")
                        skipped_count += 1
                        continue
                    if not title:
                        print(f"Skipping {file_path}: Missing 'title' in frontmatter.")
                        skipped_count += 1
                        continue

                    # --- Database Update/Create ---
                    post = Post.query.filter_by(slug=slug).first()
                    if post:
                        # Update existing post
                        post.title = title
                        post.content = content
                        post.is_published = bool(is_published) # Ensure boolean type
                        print(f"Updating post: {slug}")
                    else:
                        # Create new post
                        post = Post(
                            title=title,
                            slug=slug,
                            content=content,
                            is_published=bool(is_published)
                        )
                        db.session.add(post)
                        print(f"Creating new post: {slug}")

                    db.session.commit()
                    processed_count += 1

                except frontmatter.YAMLParseError as e:
                    print(f"Error parsing frontmatter in {file_path}: {e}")
                    db.session.rollback() # Rollback potential partial adds
                    error_count += 1
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
                    db.session.rollback()
                    error_count += 1

    print(f"Markdown processing complete. Processed: {processed_count}, Skipped: {skipped_count}, Errors: {error_count}")
    return processed_count, skipped_count, error_count


@app.route('/api/webhook/git', methods=['POST'])
def git_webhook():
    """Receives webhook notifications from Git provider."""
    # TODO: Add signature verification for security
    payload = request.json
    print("Received Git webhook payload:")
    print(json.dumps(payload, indent=2))

    repo_path = app.config['OBSIDIAN_VAULT_PATH']

    if not os.path.isdir(repo_path):
        print(f"Error: Obsidian vault path '{repo_path}' does not exist or is not a directory.")
        return jsonify({"status": "error", "message": "Vault path not configured correctly."}), 500

    try:
        print(f"Pulling changes for repository at {repo_path}...")
        # Ensure the command runs within the specified repository directory
        result = subprocess.run(['git', 'pull'], cwd=repo_path, capture_output=True, text=True, check=True)
        print("Git pull successful:")
        print(result.stdout)

        # Process updated markdown files
        processed, skipped, errors = process_markdown_files(repo_path)
        message = f"Pulled changes successfully. Processed: {processed}, Skipped: {skipped}, Errors: {errors}."

        return jsonify({"status": "success", "message": message}), 200
    except subprocess.CalledProcessError as e:
        print(f"Error during git pull: {e}")
        print(f"Stderr: {e.stderr}")
        return jsonify({"status": "error", "message": "Git pull failed."}), 500
    except FileNotFoundError:
        print("Error: 'git' command not found. Make sure Git is installed and in the system's PATH.")
        return jsonify({"status": "error", "message": "'git' command not found."}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500


# --- Main Execution ---
if __name__ == '__main__':
    app.run(debug=True)
# Use an official Node.js runtime based on Debian/Ubuntu
FROM node:18-bookworm-slim

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Nuxt application
RUN npm run build -- --log-level verbose

# The final image doesn't need to run anything,
# we just need the build artifacts from the .output directory.
CMD ["echo", "Build complete. Artifacts are in /app/.output"]
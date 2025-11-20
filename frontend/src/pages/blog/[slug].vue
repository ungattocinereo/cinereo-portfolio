<template>
  <div class="blog-detail p-5 max-w-3xl mx-auto"> <!-- Styling -->
    <div v-if="pending">Loading post...</div>
    <div v-if="error" class="text-red-500">
      Error loading post: {{ error.message }}
      <!-- Display specific error if 404 -->
      <p v-if="error.statusCode === 404">The requested post could not be found.</p>
    </div>

    <article v-if="post">
      <h1 class="text-3xl font-bold mb-2 text-gray-800">{{ post.title }}</h1>
      <p class="text-sm text-gray-500 mb-6">
        Published on: {{ formatDate(post.created_at) }}
      </p>

      <!-- TODO: Render markdown content properly using a library like @nuxt/content or markdown-it -->
      <pre class="content bg-gray-100 p-4 rounded whitespace-pre-wrap break-words font-mono text-sm">{{ post.content }}</pre>

    </article>

    <NuxtLink to="/blog" class="inline-block mt-6 text-blue-600 hover:underline">
      &amp;larr; Back to Blog List
    </NuxtLink>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const slug = ref(route.params.slug); // Get slug from route params

// Define the API URL (consider moving to runtime config later)
const API_BASE_URL = 'http://127.0.0.1:5000/api';

// Fetch the specific post based on the slug
const { data: post, pending, error } = useFetch(`${API_BASE_URL}/posts/${slug.value}`, {
  key: `blogPost-${slug.value}`, // Unique key per post slug
  default: () => null,
  transform: (data) => {
    // Optional transformation
    return data;
  },
  // We can directly check the error status code if the fetch fails
});

function formatDate(dateString) {
  if (!dateString) return '';
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  try {
    return new Date(dateString).toLocaleDateString(undefined, options);
  } catch (e) {
    console.error("Error formatting date:", dateString, e);
    return "Invalid Date";
  }
}

// Note: useFetch automatically handles refetching if the key changes (e.g., slug changes),
// so manual watching of route params is often not needed like in the previous Vue Router example.
</script>

<style scoped>
/* Add specific styles if needed, beyond utility classes */
.content {
  line-height: 1.7;
}
</style>
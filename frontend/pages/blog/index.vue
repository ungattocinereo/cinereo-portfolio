<template>
  <div class="blog-list p-5"> <!-- Added padding utility class -->
    <h1 class="text-3xl font-bold mb-5">Blog Posts</h1> <!-- Example styling -->

    <!-- Using Nuxt's useFetch for data fetching -->
    <div v-if="pending">Loading posts...</div>
    <div v-if="error" class="text-red-500">
      Error loading posts: {{ error.message }}
    </div>

    <ul v-if="posts &amp;&amp; posts.length" class="list-none p-0">
      <li v-for="post in posts" :key="post.slug" class="mb-5 pb-3 border-b border-gray-200">
        <!-- NuxtLink is Nuxt's replacement for RouterLink -->
        <NuxtLink :to="`/blog/${post.slug}`" class="text-xl text-blue-600 hover:underline">
          {{ post.title }}
        </NuxtLink>
        <p class="text-sm text-gray-600 mt-1">
          Published on: {{ formatDate(post.created_at) }}
        </p>
      </li>
    </ul>
    <div v-else-if="!pending &amp;&amp; !error">No posts found.</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Define the API URL (consider moving to runtime config later)
const API_BASE_URL = 'http://127.0.0.1:5000/api';

// Use Nuxt's useFetch composable for data fetching
// It handles pending state, errors, and data automatically
const { data: posts, pending, error } = useFetch(`${API_BASE_URL}/posts`, {
  key: 'blogPosts', // Unique key for caching and refetching
  default: () => [], // Default value while loading or if fetch fails
  transform: (data) => {
    // Optional: transform data after fetching if needed
    return data;
  }
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

// No need for onMounted with useFetch, it runs automatically.
</script>

<style scoped>
/* Scoped styles remain similar, but consider using Tailwind if @nuxt/ui is installed */
.blog-list {
  max-width: 800px;
  margin: 0 auto;
}
/* Add any additional custom styles if needed */
</style>
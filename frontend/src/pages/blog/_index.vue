<template>
  <div class="blog-list p-5 max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-5">Blog Posts</h1>

    <ul class="list-none p-0">
      <!-- Static Post Entries -->
      <li class="mb-5 pb-3 border-b border-gray-200 flex items-start space-x-4">
        <div class="pt-1 text-indigo-600 dark:text-indigo-400">
          <PenLine class="w-6 h-6" />
        </div>
        <div>
          <a href="/blog/this-website-was-written-by-voice" class="text-xl text-blue-600 hover:underline">
            This Website Was Written by Voice
          </a>
          <p class="text-sm text-gray-600 mt-1">
            Published on: April 4, 2025 (Static)
          </p>
        </div>
      </li>

      <li class="mb-5 pb-3 border-b border-gray-200 flex items-start space-x-4">
        <div class="pt-1 text-indigo-600 dark:text-indigo-400">
          <Mic class="w-6 h-6" />
        </div>
        <div>
          <a href="/blog/voice-test-post" class="text-xl text-blue-600 hover:underline">
            Testing the Waters: My First Voice-Powered Post
          </a>
          <p class="text-sm text-gray-600 mt-1">
            Published on: April 4, 2025 (Static)
          </p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { Mic, PenLine } from 'lucide-vue-next';
import { useHead } from '@unhead/vue';

useHead({
  title: 'Blog - Cinereo',
  meta: [
    { name: 'description', content: 'Thoughts and articles by Gregory Smirnov.' }
  ]
})
</script>
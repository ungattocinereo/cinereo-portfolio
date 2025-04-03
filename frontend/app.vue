<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
// You can add global setup logic here if needed
// For example, setting up global meta tags
useHead({
  titleTemplate: (titleChunk) => {
    return titleChunk ? `${titleChunk} - Cinereo Portfolio` : 'Cinereo Portfolio';
  },
  htmlAttrs: {
    lang: 'en'
  },
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    // Add more global meta tags here
  ],
  link: [
    // Add global links like favicons here
    // { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
  ]
})
</script>

<style>
/* Global styles can go here */
/* Example: import a global CSS file */
/* @import '~/assets/css/main.css'; */

/* Basic body styling - Nuxt UI/Tailwind handles base styles */
/* If you need specific global body styles, add them here using standard CSS */
/* or import a dedicated CSS file */
body {
  /* Example: */
  /* font-family: 'Your Font Name', sans-serif; */
}
</style>

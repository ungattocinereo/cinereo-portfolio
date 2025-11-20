<template>
  <div class="project-template-secondary">
    <!-- 1. Hero Section -->
    <!-- 1. Hero Section (Fullscreen Intro) -->
    <section class="hero-section h-screen min-h-[600px] relative flex items-center bg-gray-800 text-white">
      <!-- Background Image with Overlay -->
      <div class="absolute inset-0">
          <img :src="heroImage" alt="Hero Background" class="w-full h-full object-cover opacity-50" loading="lazy">
          <div class="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent"></div> <!-- Optional Gradient Overlay -->
      </div>
      <!-- Content -->
      <div class="container mx-auto px-6 md:px-8 lg:px-12 relative z-10">
        <h1 class="text-5xl sm:text-6xl md:text-7xl lg:text-[100px] xl:text-[128px] font-bold mb-3 md:mb-4 text-left leading-tight">{{ title }}</h1>
        <p class="text-base sm:text-lg md:text-xl max-w-xl lg:max-w-2xl mb-2 text-left">{{ subtitle }}</p>
        <p class="text-xs sm:text-sm md:text-base text-left opacity-80">{{ date }}</p>
      </div>
      <!-- Scroll Down Icon -->
      <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 text-white animate-bounce z-10">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
        </svg>
      </div>
    </section>

    <!-- 2. Project Info Block (Left-Right Columns) -->
    <section class="project-info container mx-auto px-6 md:px-8 lg:px-12 py-12 md:py-20 grid md:grid-cols-2 gap-8 md:gap-12">
      <div class="left-column text-sm md:text-base">
        <h3 class="text-base md:text-lg font-semibold mb-2 uppercase tracking-wider text-gray-500">Client</h3>
        <p class="mb-6">{{ client }}</p>
        <h3 class="text-base md:text-lg font-semibold mt-4 mb-2 uppercase tracking-wider text-gray-500">Year</h3>
        <p>{{ year }}</p>
      </div>
      <div class="right-column text-sm md:text-base">
        <h3 class="text-base md:text-lg font-semibold mb-2 uppercase tracking-wider text-gray-500">Services</h3>
        <ul class="list-disc list-inside space-y-1">
          <li v-for="service in services" :key="service" class="text-gray-700">{{ service }}</li>
        </ul>
      </div>
    </section>

    <!-- 3. Project Description Section -->
    <section class="project-description container mx-auto px-6 md:px-8 lg:px-12 pb-12 md:pb-20">
      <h2 class="text-2xl md:text-3xl font-bold mb-4">{{ descriptionTitle }}</h2>
      <p class="text-base md:text-lg max-w-3xl leading-relaxed text-gray-700">{{ descriptionText }}</p>
    </section>

    <!-- 4. Fullscreen Image Section -->
    <section class="fullscreen-image pb-12 md:pb-20">
      <img :src="fullscreenImage" alt="Fullscreen Project Image" class="w-full h-auto object-cover block" loading="lazy">
    </section>

    <!-- 5. Content Label (e.g., “Gallery”) -->
    <section class="content-label container mx-auto px-6 md:px-8 lg:px-12 pb-6 md:pb-10 text-center">
      <h2 class="text-3xl md:text-4xl font-bold mb-2">{{ galleryLabelTitle }}</h2>
      <p v-if="galleryLabelSubtitle" class="text-base md:text-lg text-gray-500">{{ galleryLabelSubtitle }}</p>
    </section>

    <!-- 6. Interactive Image Gallery -->
    <section class="image-gallery pb-12 md:pb-20">
      <!-- Placeholder for gallery implementation -->
      <!-- Consider using Swiper.js or a similar library here -->
      <div class="container mx-auto px-6 md:px-8 lg:px-12">
        <p class="text-center text-gray-400 italic mb-6">[Interactive Image Gallery Placeholder - Requires JS library]</p>
        <!-- Basic grid fallback -->
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 md:gap-6">
           <img v-for="(image, index) in galleryImages" :key="index" :src="image.src" :alt="image.alt || 'Gallery image'" class="w-full h-auto object-cover rounded shadow-md hover:shadow-lg transition-shadow duration-300" loading="lazy">
        </div>
      </div>
    </section>

    <!-- 7. Additional Section (“Additionally”) -->
    <section class="additional-section bg-slate-50 py-12 md:py-20">
      <div class="container mx-auto px-6 md:px-8 lg:px-12">
        <h2 class="text-2xl md:text-3xl font-bold mb-6 md:mb-8 text-center">Additionally</h2>
        <!-- Flexible grid for additional images -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 md:gap-8">
           <img v-for="(image, index) in additionalImages" :key="index" :src="image.src" :alt="image.alt || 'Additional image'" class="w-full h-auto object-cover rounded shadow" loading="lazy">
        </div>
      </div>
    </section>

     <!-- Optional Prev/Next Navigation -->
     <nav class="project-navigation container mx-auto px-6 md:px-8 lg:px-12 py-8 md:py-12 flex justify-between border-t border-gray-200 mt-12 md:mt-20">
        <!-- Add logic/links for previous/next projects here -->
        <a href="#" class="text-gray-600 hover:text-black transition-colors duration-200">&larr; Previous Project</a>
        <a href="#" class="text-gray-600 hover:text-black transition-colors duration-200">Next Project &rarr;</a>
     </nav>

  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  title: {
    type: String,
    required: true,
    default: 'Project Title'
  },
  subtitle: {
    type: String,
    required: true,
    default: 'Project subtitle description.'
  },
  date: {
    type: String,
    required: true,
    default: 'YYYY'
  },
  heroImage: {
    type: String,
    required: true,
    default: '/placeholder-hero.jpg' // Default placeholder
  },
  client: {
    type: String,
    default: 'Client Name'
  },
  year: {
    type: String,
    default: 'YYYY'
  },
  services: {
    type: Array,
    default: () => ['Service 1', 'Service 2']
  },
  descriptionTitle: {
      type: String,
      default: 'About the Project'
  },
  descriptionText: {
    type: String,
    default: 'Detailed project description goes here.'
  },
  fullscreenImage: {
    type: String,
    default: '/placeholder-fullscreen.jpg' // Default placeholder
  },
  galleryLabelTitle: {
      type: String,
      default: 'Gallery'
  },
  galleryLabelSubtitle: {
      type: String,
      default: ''
  },
  galleryImages: {
    type: Array,
    default: () => [
        { src: '/placeholder-gallery-1.jpg', alt: 'Gallery Image 1'},
        { src: '/placeholder-gallery-2.jpg', alt: 'Gallery Image 2'},
        { src: '/placeholder-gallery-3.jpg', alt: 'Gallery Image 3'}
    ] // Array of image objects { src: '', alt: '' }
  },
  additionalImages: {
    type: Array,
    default: () => [
        { src: '/placeholder-additional-1.jpg', alt: 'Additional Image 1'},
        { src: '/placeholder-additional-2.jpg', alt: 'Additional Image 2'}
    ] // Array of image objects { src: '', alt: '' }
  }
});
</script>

<style scoped>
/* Scoped styles if needed, Tailwind is preferred */
.hero-section h1 {
  /* Example of potential custom style if Tailwind isn't enough */
  /* text-shadow: 1px 1px 3px rgba(0,0,0,0.5); */
}
/* Ensure z-index works */
.hero-section > div {
    position: relative;
    z-index: 1;
}
</style>
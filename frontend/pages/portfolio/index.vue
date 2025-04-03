<template>
  <div class="container mx-auto px-4 py-8">

    <!-- 1. Hero Section -->
    <section class="mb-16 text-center bg-gradient-to-r from-blue-500 to-purple-600 text-white py-20 rounded-lg shadow-xl">
      <h1 class="text-5xl font-extrabold mb-4">My Creative Projects</h1>
      <p class="text-xl text-blue-100">Exploring innovation through code and design.</p>
      <!-- Add more hero elements like images or buttons if desired -->
    </section>

    <!-- 2. Top 3 Projects -->
    <section class="mb-16">
      <h2 class="text-6xl sm:text-7xl md:text-8xl font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">Featured</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Project 1 -->
        <div v-for="i in 3" :key="'top-' + i" class="border dark:border-gray-700 rounded-lg overflow-hidden shadow-lg hover:shadow-2xl transition-shadow duration-300">
          <div class="bg-gray-200 dark:bg-gray-800 h-56 flex items-center justify-center">
            <Briefcase class="w-16 h-16 text-gray-400 dark:text-gray-600" />
            <!-- Placeholder for project image -->
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-3">Top Project {{ i }}</h3>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
              A brief description of this important project goes here. Highlighting key features and technologies used.
            </p>
            <button class="text-sm flex items-center text-blue-600 dark:text-blue-400 hover:underline font-medium">
              <ExternalLink class="w-4 h-4 mr-1" />
              View Details
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Text Columns Section -->
    <section class="mb-16 p-8 bg-gray-100 dark:bg-gray-800 rounded-lg shadow-inner">
       <h2 class="text-6xl sm:text-7xl md:text-8xl font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">Insights</h2>
      <div class="flex flex-col md:flex-row gap-8">
        <!-- Column 1 (1/2 width) -->
        <div class="md:w-1/2">
          <h3 class="text-xl font-semibold mb-4 text-gray-700 dark:text-gray-200">My Philosophy</h3>
          <p class="text-gray-600 dark:text-gray-400">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
          </p>
        </div>
        <!-- Columns 2 & 3 Container (1/2 width) -->
        <div class="md:w-1/2 flex flex-col sm:flex-row gap-8">
          <!-- Column 2 (1/4 total width) -->
          <div class="sm:w-1/2">
            <h3 class="text-xl font-semibold mb-4 text-gray-700 dark:text-gray-200">Process</h3>
             <p class="text-gray-600 dark:text-gray-400">
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
          </div>
          <!-- Column 3 (1/4 total width) -->
          <div class="sm:w-1/2">
             <h3 class="text-xl font-semibold mb-4 text-gray-700 dark:text-gray-200">Tools</h3>
             <p class="text-gray-600 dark:text-gray-400">
              Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Other Projects (Remaining 5) -->
    <section class="mb-16">
      <h2 class="text-6xl sm:text-7xl md:text-8xl font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">...and more</h2>
       <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
         <!-- Displaying projects 4 to 8 -->
        <div v-for="i in 5" :key="'other-' + (i + 3)" class="border dark:border-gray-700 rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300">
          <div class="bg-gray-200 dark:bg-gray-800 h-48 flex items-center justify-center">
             <Briefcase class="w-12 h-12 text-gray-400 dark:text-gray-600" />
             <!-- Placeholder for project image -->
          </div>
          <div class="p-4">
            <h3 class="font-semibold mb-2">Project {{ i + 3 }}</h3>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">
              Description for another project. Keep it concise.
            </p>
             <button class="text-xs flex items-center text-blue-600 dark:text-blue-400 hover:underline">
               <ExternalLink class="w-3 h-3 mr-1" />
               Learn More
             </button>
          </div>
        </div>
      </div>
      <!-- Note: Infinite scroll implementation requires more complex setup -->
    </section>

    <!-- 5. Why Me Section -->
    <section class="py-12 bg-gradient-to-r from-teal-50 to-blue-50 dark:from-gray-800 dark:to-gray-900 rounded-lg shadow-lg">
       <h2 class="text-3xl font-bold mb-10 text-center text-gray-800 dark:text-gray-100">Why Collaborate With Me?</h2>
      <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
        <div>
          <div class="bg-white dark:bg-gray-700 p-6 rounded-full w-16 h-16 mx-auto mb-4 flex items-center justify-center shadow-md">
            <Zap class="w-8 h-8 text-yellow-500" /> <!-- Example Icon -->
          </div>
          <h3 class="text-xl font-semibold mb-3 text-gray-700 dark:text-gray-200">Expertise</h3>
          <p class="text-gray-600 dark:text-gray-400">
            Deep knowledge in modern web technologies and best practices.
          </p>
        </div>
        <div>
           <div class="bg-white dark:bg-gray-700 p-6 rounded-full w-16 h-16 mx-auto mb-4 flex items-center justify-center shadow-md">
            <Users class="w-8 h-8 text-green-500" /> <!-- Example Icon -->
          </div>
          <h3 class="text-xl font-semibold mb-3 text-gray-700 dark:text-gray-200">Collaboration</h3>
          <p class="text-gray-600 dark:text-gray-400">
            Focused on clear communication and achieving shared goals.
          </p>
        </div>
        <div>
           <div class="bg-white dark:bg-gray-700 p-6 rounded-full w-16 h-16 mx-auto mb-4 flex items-center justify-center shadow-md">
            <Award class="w-8 h-8 text-red-500" /> <!-- Example Icon -->
          </div>
          <h3 class="text-xl font-semibold mb-3 text-gray-700 dark:text-gray-200">Quality</h3>
          <p class="text-gray-600 dark:text-gray-400">
            Delivering high-quality, maintainable, and scalable solutions.
          </p>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { Briefcase, ExternalLink, Zap, Users, Award } from 'lucide-vue-next';

// Placeholder data - replace with your actual project data
// You might fetch this from an API or define it here
const topProjects = [
  { id: 1, name: 'Top Project 1', description: '...' },
  { id: 2, name: 'Top Project 2', description: '...' },
  { id: 3, name: 'Top Project 3', description: '...' },
];

const otherProjects = [
  { id: 4, name: 'Project 4', description: '...' },
  { id: 5, name: 'Project 5', description: '...' },
  { id: 6, name: 'Project 6', description: '...' },
  { id: 7, name: 'Project 7', description: '...' },
  { id: 8, name: 'Project 8', description: '...' },
];

// Note: For infinite scroll, you'd typically load `otherProjects` incrementally
// based on scroll position, likely involving state management (e.g., useState)
// and potentially API calls.
</script>

<style scoped>
/* Add any component-specific styles here if needed */
</style>
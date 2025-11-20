<template>
  <div class="flex flex-col min-h-screen">
    <!-- Navigation Bar - Sticky with conditional background -->
    <header :class="headerClasses" class="sticky top-0 z-50 border-b border-gray-200 dark:border-gray-800 transition-all duration-300"> <!-- Removed static backdrop-filter -->
      <!-- Container back inside nav -->
      <nav class="container mx-auto px-4 py-3 flex justify-between items-center"> <!-- Restored container/padding -->
        <!-- Logo on the left -->
        <NuxtLink to="/" class="flex items-center">
          <LogoCinereo class="h-14 text-[#2A3238] dark:text-white" />
        </NuxtLink>

        <!-- Navigation and Social Links on the right -->
        <div class="flex items-center space-x-6 mt-3"> <!-- Added mt-1 to push down slightly -->
          <!-- Main Navigation -->
          <div class="flex items-center space-x-4">
            <NuxtLink
              to="/portfolio"
              class="flex items-center text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white font-nunito text-sm font-medium"
            >
              <BriefcaseBusiness class="w-4 h-4 mr-1" />
              Portfolio
            </NuxtLink>
            <NuxtLink
              to="/blog"
              class="flex items-center text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white font-nunito text-sm font-medium"
            >
              <ScrollText class="w-4 h-4 mr-1" />
              Blog
            </NuxtLink>
            <NuxtLink
              to="/about"
              class="flex items-center text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white font-nunito text-sm font-medium"
            >
              <Cat class="w-4 h-4 mr-1" />
              About
            </NuxtLink>
          </div>

          <!-- Divider -->
          <div class="hidden md:block h-4 border-l border-gray-300 dark:border-gray-700"></div> <!-- Hide on small screens, show on medium+ -->

          <!-- Social Media Links -->
          <div class="hidden md:flex items-center space-x-3"> <!-- Hide on small screens, show on medium+ -->
            <a
              href="https://www.linkedin.com/in/cinereo/"
              target="_blank"
              rel="noopener noreferrer"
              class="text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400"
            >
              <Linkedin class="w-4 h-4" />
            </a>
            <a
              href="https://instagram.com/cinereo"
              target="_blank"
              rel="noopener noreferrer"
              class="text-gray-500 dark:text-gray-400 hover:text-pink-600 dark:hover:text-pink-400"
            >
              <Instagram class="w-4 h-4" />
            </a>
            <a
              href="https://t.me/cinereo"
              target="_blank"
              rel="noopener noreferrer"
              class="text-gray-500 dark:text-gray-400 hover:text-blue-500 dark:hover:text-blue-300"
            >
              <Send class="w-4 h-4" />
            </a>
            <!-- Divider -->
            <div class="hidden md:block h-4 border-l border-gray-300 dark:border-gray-700"></div>
            <!-- Theme Toggle Component -->
            <ThemeToggle />
          </div>
        </div>
      </nav>
      <!-- Removed closing tag for inner container div -->
    </header>
    <!-- Removed closing tag for the wrapper div -->

    <!-- Main Content - Removed top padding -->
    <main class="flex-grow bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
      <slot />
    </main>

    <!-- Footer -->
    <AppFooter />
  </div>
</template>

<script setup>
// Import Lucid icons
import { BriefcaseBusiness, ScrollText, Cat, Linkedin, Instagram, Send } from 'lucide-vue-next';
import { ref, onMounted, onUnmounted, computed } from 'vue';
import ThemeToggle from '~/components/ThemeToggle.vue'; // Import ThemeToggle

// Import logo component
import LogoCinereo from '~/components/logos/logo-cinereo.svg?component';

// Import AppFooter component
import AppFooter from '~/components/AppFooter.vue';

// Navbar scroll behavior
const scrollY = ref(0);
const isScrolled = computed(() => scrollY.value > 0); // Trigger effect immediately on scroll

const handleScroll = () => {
  scrollY.value = window.scrollY;
  // console.log('Layout: handleScroll executed, scrollY:', scrollY.value); // <-- Remove log
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

const headerClasses = computed(() => {
  // Explicit classes for better compatibility
  let classes = '';
  if (isScrolled.value) {
    classes = 'bg-white/75 dark:bg-gray-900/75 backdrop-blur-md backdrop-filter -webkit-backdrop-filter shadow-sm';
  } else {
    classes = 'bg-transparent dark:bg-gray-900'; // Apply dark bg even when not scrolled
  }
  // console.log('Layout: headerClasses computed, isScrolled:', isScrolled.value, 'classes:', classes); // <-- Remove log
  return classes;
});
</script>

<style>
/* Import Nunito font */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400&display=swap');

/* Global styles */
body {
  margin: 0;
  font-family: 'Nunito', sans-serif;
}

/* Dark mode styles */
.dark {
  color-scheme: dark;
}

/* Font class */
.font-nunito {
  font-family: 'Nunito', sans-serif;
}

/* Active link styles */
.router-link-active {
  font-weight: 500;
}

/* Explicit backdrop-filter styles for better browser compatibility */
.backdrop-blur-md {
  -webkit-backdrop-filter: blur(12px) !important;
  backdrop-filter: blur(12px) !important;
}

.backdrop-filter {
  -webkit-backdrop-filter: blur(12px) !important;
  backdrop-filter: blur(12px) !important;
}

.-webkit-backdrop-filter {
  -webkit-backdrop-filter: blur(12px) !important;
}

/* Explicit background opacity styles */
.bg-white\/75 {
  background-color: rgba(255, 255, 255, 0.75) !important;
}

.dark .dark\:bg-gray-900\/75 {
  background-color: rgba(17, 24, 39, 0.75) !important;
}

/* Ensure the header has the correct stacking context for backdrop-filter */
header {
  isolation: isolate;
  will-change: backdrop-filter, background-color;
}
</style>
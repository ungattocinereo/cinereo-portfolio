<template>
  <div class="flex flex-col min-h-screen" :class="{ 'dark': isDark }">
    <!-- Navigation Bar - Sticky with conditional background -->
    <header :class="headerClasses" class="sticky top-0 z-50 border-b border-gray-200 dark:border-gray-800 transition-all duration-300"> <!-- Restored sticky, removed container/margin/styles -->
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

// Import logo component
import LogoCinereo from '~/components/logos/logo-cinereo.svg?component';

// Import AppFooter component
import AppFooter from '~/components/AppFooter.vue';

// Detect dark mode based on system preferences
const isDark = ref(false);

// Initialize dark mode on client side
onMounted(() => {
  // Check if user prefers dark mode
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    isDark.value = true;
  }
  
  // Listen for changes in system color scheme preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
    isDark.value = event.matches;
  });
});

// Navbar scroll behavior
const scrollY = ref(0);
const isScrolled = computed(() => scrollY.value > 0); // Trigger effect immediately on scroll

const handleScroll = () => {
  scrollY.value = window.scrollY;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

const headerClasses = computed(() => {
  // Restore conditional classes based on scroll
  return {
    'bg-white/75 dark:bg-gray-900/75 backdrop-blur-md shadow-sm': isScrolled.value,
    'bg-transparent dark:bg-gray-900': !isScrolled.value, // Apply dark bg even when not scrolled
  };
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
</style>
<template>
  <button
    @click="toggleTheme"
    class="theme-toggle hidden md:block p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 dark:focus:ring-offset-gray-800"
    aria-label="Toggle theme"
    role="switch"
    :aria-checked="isDark"
  >
    <transition name="fade" mode="out-in">
      <Sun v-if="isDark" key="sun" class="w-5 h-5" />
      <Moon v-else key="moon" class="w-5 h-5" />
    </transition>
  </button>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Sun, Moon } from 'lucide-vue-next' // Import icons

const isDark = ref(false)

const toggleTheme = () => {
  isDark.value = !isDark.value
  updateTheme()
}

const updateTheme = () => {
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
}

// Check local storage and system preference on mount
onMounted(() => {
  // console.log('ThemeToggle: onMounted hook executed.'); // <-- Remove log
  const savedTheme = localStorage.getItem('theme')
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches

  if (savedTheme) {
    isDark.value = savedTheme === 'dark'
  } else {
    isDark.value = prefersDark
  }
  // Apply the theme immediately on load
  updateTheme()

  // Optional: Listen for changes in system preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    // Only update if no theme is explicitly saved in localStorage
    if (!localStorage.getItem('theme')) {
      isDark.value = e.matches
      updateTheme()
    }
  })
})
</script>

<style scoped>
/* Add any component-specific styles here if needed */
.theme-toggle {
  /* Example styling - adjust as needed */
  background-color: transparent;
  border: none;
  cursor: pointer;
  color: inherit; /* Inherit color from parent */
  display: flex; /* Align icon center */
  align-items: center; /* Align icon center */
  justify-content: center; /* Align icon center */
}

/* Icon transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Adjust icon size if needed */
.theme-toggle svg {
  /* font-size: 1.25rem; /* Adjust size */
  /* display: inline-block; */
  transition: transform 0.2s ease;
}

.theme-toggle:hover svg {
    transform: scale(1.1);
}
</style>
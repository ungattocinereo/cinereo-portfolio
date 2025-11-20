/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./nuxt.config.{js,ts}",
    "./error.vue",
    "./node_modules/@nuxt/ui/**/*.vue"
  ],
  darkMode: 'class', // Enable class-based dark mode
  theme: {
    extend: {
      fontFamily: {
        raleway: ['Raleway', 'sans-serif'], // Add Raleway font family
      },
      backdropBlur: {
        md: '12px',
      },
      backgroundColor: {
        'white/75': 'rgba(255, 255, 255, 0.75)',
        'gray-900/75': 'rgba(17, 24, 39, 0.75)',
      },
    },
  },
  plugins: [],
  safelist: [
    'backdrop-blur-md',
    'backdrop-filter',
    'bg-white/75',
    'bg-transparent',
    'dark:bg-gray-900/75',
    'dark:bg-gray-900',
    '-webkit-backdrop-filter',
    'hidden',      // Add hidden
    'md:block',    // Add md:block
    'md:flex'      // Add md:flex
  ]
}
import svgLoader from 'vite-svg-loader'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@nuxt/content',
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    // '@nuxt/image', // Temporarily disabled due to build path issues
    '@nuxt/scripts',
    '@nuxtjs/tailwindcss',
    '@nuxt/image'
  ],
  css: [ // CSS imports
    'vue-easy-lightbox/dist/external-css/vue-easy-lightbox.css'
  ],
  build: {
    transpile: [
      'tsparticles',
      '@tsparticles/engine',
      '@tsparticles/path-svg',
      'lucide-vue-next'
    ]
  },
  vite: {
    plugins: [
      svgLoader() // Add the svgLoader plugin
    ],
    build: {
      // ssr: true // Explicitly enable SSR build for Vite <-- REMOVED/COMMENTED OUT
    },
    optimizeDeps: {
      include: ['tsparticles', '@tsparticles/engine', '@tsparticles/path-svg']
    }
  },
  experimental: {
    payloadExtraction: false
  },
  // Image module configuration
  image: {
    provider: 'ipxStatic', // Use ipxStatic for static generation
    // Optional: Define screen sizes if needed, otherwise defaults are used
    // screens: {
    //   xs: 320,
    //   sm: 640,
    //   md: 768,
    //   lg: 1024,
    //   xl: 1280,
    //   xxl: 1536,
    // },
  },
  nitro: {
    output: {
      publicDir: '.output/public'
    }
  },
  app: {
    head: {
      script: [
        {
          // hid: 'gtm', // <-- REMOVED
          innerHTML: `(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
          new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
          j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
          'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
          })(window,document,'script','dataLayer','GTM-K9XX2CL3');`,
          type: 'text/javascript'
        }
      ],
      noscript: [
        {
          // hid: 'gtm-noscript', // <-- REMOVED
          innerHTML: `<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K9XX2CL3"
          height="0" width="0" style="display:none;visibility:hidden"></iframe>`,
          tagPosition: 'bodyOpen'
        }
      ]
    }
  }
})
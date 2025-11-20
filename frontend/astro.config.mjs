// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import vue from '@astrojs/vue';
import svgLoader from 'vite-svg-loader';
import vercel from '@astrojs/vercel/static';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  adapter: vercel({
    webAnalytics: {
      enabled: true,
    },
  }),
  vite: {
    plugins: [
        tailwindcss(),
        svgLoader({
            defaultImport: 'component'
        })
    ],
    resolve: {
      alias: {
        '~': '/src',
      }
    }
  },

  integrations: [vue()]
});
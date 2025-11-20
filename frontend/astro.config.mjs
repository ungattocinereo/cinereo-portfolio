// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';
import vue from '@astrojs/vue';
import svgLoader from 'vite-svg-loader';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [
        tailwindcss(),
        svgLoader({
            defaultImport: 'component'
        })
    ]
  },

  integrations: [vue()]
});
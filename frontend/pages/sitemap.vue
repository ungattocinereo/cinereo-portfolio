<template>
  <div class="container mx-auto px-4 py-12">
    <h1 class="text-3xl font-bold font-raleway mb-8">Sitemap</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <!-- Main Pages -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-bold font-raleway mb-4 text-[#293036]">Main Pages</h2>
        <ul class="space-y-2 font-nunito">
          <li v-for="(link, index) in mainPages" :key="index">
            <NuxtLink :to="link.path" class="text-blue-600 hover:text-blue-800 flex items-center">
              <ChevronRight class="w-4 h-4 mr-1" />
              {{ link.name }}
            </NuxtLink>
          </li>
        </ul>
      </div>
      
      <!-- Portfolio Pages -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-bold font-raleway mb-4 text-[#293036]">Portfolio</h2>
        <ul class="space-y-2 font-nunito">
          <li>
            <NuxtLink to="/portfolio" class="text-blue-600 hover:text-blue-800 flex items-center">
              <ChevronRight class="w-4 h-4 mr-1" />
              Portfolio Overview
            </NuxtLink>
          </li>
          <li v-for="(link, index) in portfolioPages" :key="index">
            <NuxtLink :to="link.path" class="text-blue-600 hover:text-blue-800 flex items-center">
              <ChevronRight class="w-4 h-4 mr-1" />
              {{ link.name }}
            </NuxtLink>
          </li>
        </ul>
      </div>
      
      <!-- Blog Pages -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-bold font-raleway mb-4 text-[#293036]">Blog</h2>
        <ul class="space-y-2 font-nunito">
          <li>
            <NuxtLink to="/blog" class="text-blue-600 hover:text-blue-800 flex items-center">
              <ChevronRight class="w-4 h-4 mr-1" />
              Blog Overview
            </NuxtLink>
          </li>
          <li v-for="(link, index) in blogPages" :key="index">
            <NuxtLink :to="link.path" class="text-blue-600 hover:text-blue-800 flex items-center">
              <ChevronRight class="w-4 h-4 mr-1" />
              {{ link.name }}
            </NuxtLink>
          </li>
        </ul>
      </div>
      
      <!-- Legal Pages -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-bold font-raleway mb-4 text-[#293036]">Legal</h2>
        <ul class="space-y-2 font-nunito">
          <li v-for="(link, index) in legalPages" :key="index">
            <NuxtLink :to="link.path" class="text-blue-600 hover:text-blue-800 flex items-center">
              <ChevronRight class="w-4 h-4 mr-1" />
              {{ link.name }}
            </NuxtLink>
          </li>
        </ul>
      </div>
      
      <!-- XML Sitemap -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-bold font-raleway mb-4 text-[#293036]">XML Sitemap</h2>
        <p class="mb-4 font-nunito">For search engines, you can access our XML sitemap:</p>
        <a href="/sitemap.xml" target="_blank" class="text-blue-600 hover:text-blue-800 flex items-center font-nunito">
          <ExternalLink class="w-4 h-4 mr-1" />
          sitemap.xml
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ChevronRight, ExternalLink } from 'lucide-vue-next';

// Define the site structure
const mainPages = [
  { name: 'Home', path: '/' },
  { name: 'About', path: '/about' },
  { name: 'Portfolio', path: '/portfolio' },
  { name: 'Blog', path: '/blog' },
  { name: 'Contact', path: '/about#contact' }
];

const portfolioPages = [
  { name: 'Caffe Vittoria', path: '/portfolio/caffe-vittoria' },
  { name: 'Moressa', path: '/portfolio/moressa' },
  { name: 'Olivier', path: '/portfolio/olivier' },
  { name: 'QCierge', path: '/portfolio/qcierge' }
];

const blogPages = [
  { name: 'This Website Was Written By Voice', path: '/blog/this-website-was-written-by-voice' },
  { name: 'Voice Test Post', path: '/blog/voice-test-post' }
];

const legalPages = [
  { name: 'Privacy Policy', path: '/privacy-policy' },
  { name: 'Terms of Service', path: '/terms-of-service' }
];
</script>
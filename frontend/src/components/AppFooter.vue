<template>
  <footer class="bg-[#293036] text-white py-12 relative overflow-hidden">
    <!-- Container for the particles canvas -->
    <div id="footer-particles" class="absolute inset-0 z-0"></div>
    <div class="container mx-auto px-4 relative z-10"> <!-- Add relative z-10 to keep content above particles -->
      <!-- Footer Top Section -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-8">
        <!-- About Column -->
        <div>
          <h3 class="text-xl font-raleway font-bold mb-4">Cinereo</h3>
          <p class="text-gray-300 font-nunito mb-4">
            Creative professional based on the Amalfi Coast, specializing in web development, photography, and graphic design.
          </p>
          <div class="flex space-x-4">
            <a href="https://www.linkedin.com/in/cinereo/" target="_blank" rel="noopener noreferrer" class="text-gray-300 hover:text-white transition">
              <Linkedin class="w-5 h-5" />
            </a>
            <a href="https://instagram.com/cinereo" target="_blank" rel="noopener noreferrer" class="text-gray-300 hover:text-white transition">
              <Instagram class="w-5 h-5" />
            </a>
            <a href="https://t.me/cinereo" target="_blank" rel="noopener noreferrer" class="text-gray-300 hover:text-white transition">
              <Send class="w-5 h-5" />
            </a>
          </div>
        </div>
        
        <!-- Services Column -->
        <div>
          <h3 class="text-xl font-raleway font-bold mb-4">Services</h3>
          <ul class="space-y-2 font-nunito">
            <li>
              <a href="/portfolio" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Web Development
              </a>
            </li>
            <li>
              <a href="/portfolio" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Photography
              </a>
            </li>
            <li>
              <a href="/portfolio" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Graphic Design
              </a>
            </li>
            <li>
              <a href="/portfolio" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Hospitality Consulting
              </a>
            </li>
          </ul>
        </div>
        
        <!-- Quick Links Column -->
        <div>
          <h3 class="text-xl font-raleway font-bold mb-4">Quick Links</h3>
          <ul class="space-y-2 font-nunito">
            <li>
              <a href="/" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Home
              </a>
            </li>
            <li>
              <a href="/portfolio" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Portfolio
              </a>
            </li>
            <li>
              <a href="/blog" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Blog
              </a>
            </li>
            <li>
              <a href="/about" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                About
              </a>
            </li>
            <li>
              <a href="/about#contact" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Contact
              </a>
            </li>
          </ul>
        </div>
        
        <!-- Contact Column -->
        <div>
          <h3 class="text-xl font-raleway font-bold mb-4">Contact</h3>
          <ul class="space-y-3 font-nunito">
            <li class="flex items-start">
              <MapPin class="w-5 h-5 mr-2 mt-0.5 text-[#3e87f8]" />
              <span class="text-gray-300">Amalfi Coast, Italy</span>
            </li>
            <li class="flex items-start">
              <Mail class="w-5 h-5 mr-2 mt-0.5 text-[#3e87f8]" />
              <a href="mailto:hello@cinereo.it" class="text-gray-300 hover:text-white transition">hello@cinereo.it</a>
            </li>
            <li class="flex items-start">
              <MessageCircle class="w-5 h-5 mr-2 mt-0.5 text-[#3e87f8]" />
              <a href="https://t.me/cinereo" target="_blank" rel="noopener noreferrer" class="text-gray-300 hover:text-white transition">Telegram: @cinereo</a>
            </li>
          </ul>
        </div>
      </div>
      
      <!-- Footer Bottom Section -->
      <div class="pt-8 border-t border-gray-700 flex flex-col md:flex-row justify-between items-center">
        <p class="text-gray-400 font-nunito text-sm mb-4 md:mb-0">
          © 2006–2025 Gregory 'Cinereo' Smirnov. All rights reserved.
        </p>
        <div class="flex flex-wrap justify-center gap-4 text-sm font-nunito">
          <a href="/privacy-policy" class="text-gray-400 hover:text-white transition">Privacy Policy</a>
          <a href="/terms-of-service" class="text-gray-400 hover:text-white transition">Terms of Service</a>
          <a href="/sitemap" class="text-gray-400 hover:text-white transition">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'; // Added onBeforeUnmount
import {
  Linkedin,
  Instagram,
  Send,
  ChevronRight,
  MapPin,
  Mail,
  MessageCircle
} from 'lucide-vue-next';

// Particle logic is commented out for now to simplify the migration and build. 
// It can be re-enabled later with the correct Astro/Vue integration for particles.
</script>
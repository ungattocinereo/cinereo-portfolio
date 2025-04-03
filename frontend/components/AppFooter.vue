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
              <NuxtLink to="/services" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Web Development
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/services" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Photography
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/services" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Graphic Design
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/services" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Hospitality Consulting
              </NuxtLink>
            </li>
          </ul>
        </div>
        
        <!-- Quick Links Column -->
        <div>
          <h3 class="text-xl font-raleway font-bold mb-4">Quick Links</h3>
          <ul class="space-y-2 font-nunito">
            <li>
              <NuxtLink to="/" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Home
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/portfolio" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Portfolio
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/blog" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Blog
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/about" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                About
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/about#contact" class="text-gray-300 hover:text-white transition flex items-center">
                <ChevronRight class="w-4 h-4 mr-1" />
                Contact
              </NuxtLink>
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
              <a href="mailto:info@cinereo.it" class="text-gray-300 hover:text-white transition">info@cinereo.it</a>
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
          &copy; {{ new Date().getFullYear() }} Cinereo. All rights reserved.
        </p>
        <div class="flex flex-wrap justify-center gap-4 text-sm font-nunito">
          <NuxtLink to="/privacy-policy" class="text-gray-400 hover:text-white transition">Privacy Policy</NuxtLink>
          <NuxtLink to="/terms-of-service" class="text-gray-400 hover:text-white transition">Terms of Service</NuxtLink>
          <NuxtLink to="/sitemap" class="text-gray-400 hover:text-white transition">Sitemap</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import {
  Linkedin,
  Instagram,
  Send,
  ChevronRight,
  MapPin,
  Mail,
  MessageCircle
} from 'lucide-vue-next';
import { tsParticles } from "@tsparticles/engine";
import { loadFull } from "tsparticles"; // Required for loading the full particles engine

// Particle configuration options
const particlesOptions = ref({
  fullScreen: {
    enable: false // Important: particles are contained within the footer
  },
  background: {
    color: {
      value: 'transparent' // Make background transparent
    }
  },
  particles: {
    number: {
      value: 180, // Increased density (3x)
      density: {
        enable: true,
        area: 800
      }
    },
    color: {
      value: "#666666" // Darker grey color for ash/dust
    },
    shape: {
      type: "circle"
    },
    opacity: {
      value: 0.3, // More subtle opacity
      random: true,
    },
    size: {
      value: { min: 1, max: 2.5 }, // Smaller particles
      random: true,
    },
    move: {
      enable: true,
      speed: 0.4, // Slower movement
      direction: "none",
      random: true,
      straight: false,
      outModes: {
        default: "out" // Particles disappear when they go out of bounds
      }
    },
    links: {
        enable: false // No lines connecting particles
    }
  },
  interactivity: {
    detectsOn: "canvas",
    events: {
      onHover: {
        enable: false // No hover effects
      },
      onClick: {
        enable: false // No click effects
      },
      resize: true
    }
  },
  detectRetina: true
});

// Initialize particles on the client side after the component is mounted
onMounted(async () => {
  await loadFull(tsParticles); // Load all features

  await tsParticles.load({
    id: "footer-particles", // ID of the container div
    options: particlesOptions.value,
  });
});
</script>
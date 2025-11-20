<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-screen flex items-center justify-center bg-[url('/images/bg-hero-cinereo.webp')] bg-cover bg-bottom text-white before:absolute before:inset-0 before:z-0 dark:before:bg-black/20"> <!-- Added flex centering, removed padding -->
      <!-- Particle Container with explicit z-index -->
      <div id="hero-particles" class="absolute inset-0 z-0" style="z-index: 0;"></div>
      <div class="container mx-auto px-4 text-center relative z-10" style="z-index: 10;"> <!-- Add explicit z-index -->
        <div class="mx-auto">
          <div class="relative">
            <!-- Creative text as a separate div positioned relative to the container -->
            <div class="absolute w-full text-center bottom-20 md:bottom-2">
              <div class="text-[16vw] md:text-[14vw] lg:text-[14vw] font-raleway font-black text-outline-white text-outline-masked leading-none">Creative</div>
            </div>
            
            <!-- Main heading text -->
            <h1 class="relative text-4xl md:text-5xl lg:text-6xl font-raleway font-black mb-4 leading-tight pt-24 md:pt-20 z-10"> <!-- Increased desktop top padding -->
              Solutions for Digital Presence
            </h1>
          </div>
          <p class="text-lg md:text-xl mb-8 font-nunito max-w-3xl mx-auto">
            Graphic designer, photographer, web developer, and hotel manager based on the Amalfi Coast, Italy.
            Specializing in creating elegant digital experiences that combine aesthetics with functionality.
          </p>
          <div class="flex flex-wrap gap-4 justify-center">
            <NuxtLink to="/portfolio" class="bg-white text-[#293036] px-6 py-3 rounded-md font-nunito font-medium hover:bg-opacity-90 transition flex items-center">
              <Briefcase class="w-5 h-5 mr-2" />
              View Projects
            </NuxtLink>
            <NuxtLink to="/about#contact" class="border-2 border-white text-white px-6 py-3 rounded-md font-nunito font-medium hover:bg-white hover:bg-opacity-10 transition flex items-center">
              <MessageCircle class="w-5 h-5 mr-2" />
              Get in Touch
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Projects Section -->
    <section class="py-16 bg-white dark:bg-gray-900">
      <div class="container mx-auto px-4">
        <h2 class="title-header">Featured</h2>
        <!-- Subtitle removed -->
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- QR Concierge Project -->
          <div class="bg-white dark:bg-gray-800 rounded-lg overflow-hidden shadow-md hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300">
            <NuxtLink to="/portfolio/qcierge">
              <img src="/images/mockup-qrcierge.jpg" alt="QR Concierge Mockup" class="w-full h-48 object-cover" />
            </NuxtLink>
            <div class="p-6">
              <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">QR Concierge</h3>
              <p class="text-gray-600 dark:text-gray-300 mb-4 font-nunito">
                Digital concierge system using QR codes for hotels and tourism businesses.
              </p>
              <NuxtLink to="/portfolio/qcierge" class="text-[#003dff] dark:text-[#3e87f8] font-medium flex items-center hover:underline">
                <ExternalLink class="w-4 h-4 mr-1" /> <!-- Consider changing icon if it's now an internal link -->
                Visit Project
              </NuxtLink>
            </div>
          </div>
          
          <!-- WordPress Sites Project -->
          <div class="bg-white dark:bg-gray-800 rounded-lg overflow-hidden shadow-md hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300">
            <img src="/images/mockup-websites.jpg" alt="Tourism Websites Mockup" class="w-full h-48 object-cover" />
            <div class="p-6">
              <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Tourism Websites</h3>
              <p class="text-gray-600 dark:text-gray-300 mb-4 font-nunito">
                Collection of WordPress sites for tourism and local businesses on the Amalfi Coast.
              </p>
              <a href="#" class="text-[#003dff] dark:text-[#3e87f8] font-medium flex items-center hover:underline">
                <ExternalLink class="w-4 h-4 mr-1" />
                Visit Project
              </a>
            </div>
          </div>
          
          <!-- Interior Photography Project -->
          <div class="bg-white dark:bg-gray-800 rounded-lg overflow-hidden shadow-md hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300">
            <img src="/images/interior-photo.jpg" alt="Interior Photography Example" class="w-full h-48 object-cover" />
            <div class="p-6">
              <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Interior Photography</h3>
              <p class="text-gray-600 dark:text-gray-300 mb-4 font-nunito">
                Professional photography for hotels, villas, and restaurants on the Amalfi Coast.
              </p>
              <a href="#" class="text-[#003dff] dark:text-[#3e87f8] font-medium flex items-center hover:underline">
                <Image class="w-4 h-4 mr-1" />
                View Gallery
              </a>
            </div>
          </div>
        </div>
        
        <div class="mt-12 text-center">
          <NuxtLink to="/portfolio" class="inline-flex items-center text-[#003dff] dark:text-[#3e87f8] font-medium hover:underline">
            <FolderOpen class="w-5 h-5 mr-2" />
            View All Projects
            <ArrowRight class="w-4 h-4 ml-1" />
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Current Work Section -->
    <section class="py-16 bg-gray-100 dark:bg-gray-800">
      <div class="container mx-auto px-4">
        <h2 class="title-header">Current</h2>

        <p class="text-2xl md:text-3xl font-nunito font-bold text-left text-gray-800 dark:text-gray-200 max-w-3xl mb-4">
          I’m personally crafting each of these sites right now — real projects with real traffic.
        </p>
        <p class="text-base md:text-lg font-nunito text-left text-gray-600 dark:text-gray-400 max-w-2xl mb-12">
          Here’s a look at some of the projects I’m currently working on—each one built with care and purpose.
        </p>

        <div class="flex flex-wrap justify-center items-center gap-8 md:gap-12">
          <a href="https://amalfi.day" target="_blank" rel="noopener noreferrer" class="bg-white dark:bg-[#121826] rounded-full w-[255px] h-[85px] flex items-center justify-center transition-all duration-300 ease-in-out transform hover:-translate-y-1">
            <Amalfiday2Logo class="h-[3.3rem] text-[#2B3339] dark:text-gray-300 relative -top-1" />
          </a>
          <a href="https://atrani.ru" target="_blank" rel="noopener noreferrer" class="bg-white dark:bg-[#121826] rounded-full w-[255px] h-[85px] flex items-center justify-center transition-all duration-300 ease-in-out transform hover:-translate-y-1">
            <AtraniruLogo class="h-8 text-[#2B3339] dark:text-gray-300" />
          </a>
          <a href="https://alextione.it" target="_blank" rel="noopener noreferrer" class="bg-white dark:bg-[#121826] rounded-full w-[255px] h-[85px] flex items-center justify-center transition-all duration-300 ease-in-out transform hover:-translate-y-1">
            <AlextioneLogo class="h-8 text-[#2B3339] dark:text-gray-300" />
          </a>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section class="py-16 bg-gray-100 dark:bg-gray-800">
      <div class="container mx-auto px-4">
        <h2 class="title-header">Skills</h2>
        <!-- Subtitle removed -->
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <!-- Web Development Service -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
            <div class="w-12 h-12 bg-[#162cf1] rounded-full flex items-center justify-center mb-4">
              <Code class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Web Development</h3>
            <p class="text-gray-600 dark:text-gray-300 font-nunito">
              Custom websites and web applications built with modern technologies.
            </p>
          </div>
          
          <!-- Photography Service -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
            <div class="w-12 h-12 bg-[#162cf1] rounded-full flex items-center justify-center mb-4">
              <Camera class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Photography</h3>
            <p class="text-gray-600 dark:text-gray-300 font-nunito">
              Professional interior and landscape photography for hospitality businesses.
            </p>
          </div>
          
          <!-- Graphic Design Service -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
            <div class="w-12 h-12 bg-[#162cf1] rounded-full flex items-center justify-center mb-4">
              <Palette class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Graphic Design</h3>
            <p class="text-gray-600 dark:text-gray-300 font-nunito">
              Brand identity, print materials, and digital assets for your business.
            </p>
          </div>
          
          <!-- Hospitality Consulting Service -->
          <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
            <div class="w-12 h-12 bg-[#162cf1] rounded-full flex items-center justify-center mb-4">
              <Hotel class="w-6 h-6 text-white" />
            </div>
            <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Hospitality Consulting</h3>
            <p class="text-gray-600 dark:text-gray-300 font-nunito">
              Expert advice on hotel management and digital transformation.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Latest Blog Posts Section -->
    <section class="py-16 bg-white dark:bg-gray-900">
      <div class="container mx-auto px-4">
        <h2 class="title-header">Blog</h2>
        <!-- Subtitle removed -->
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Blog Post 1 -->
          <div class="relative bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
            <NuxtLink to="/blog/this-website-was-written-by-voice">
              <div class="h-48 bg-gray-200 dark:bg-gray-700 rounded-t-lg flex items-center justify-center">
                <Lightbulb class="w-40 h-40 text-[#1436f5] pointer-events-none" />
              </div>
            </NuxtLink>
            <div class="p-6">
              <div class="text-sm text-gray-500 dark:text-gray-400 mb-2 font-nunito">April 4, 2025</div>
              <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">This Website Was Written by Voice</h3>
              <p class="text-gray-600 dark:text-gray-300 mb-4 font-nunito line-clamp-3">
                Discover how this website was built entirely using voice commands and AI, a journey from WordPress to a modern, lightweight solution.
              </p>
              <NuxtLink to="/blog/this-website-was-written-by-voice" class="text-[#003dff] dark:text-[#3e87f8] font-medium flex items-center hover:underline">
                <BookOpen class="w-4 h-4 mr-1" />
                Read Article
              </NuxtLink>
            </div>
          </div>
          
          <!-- Blog Post 2 -->
          <div class="relative bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
            <NuxtLink to="/blog/voice-test-post">
              <div class="h-48 bg-gray-200 dark:bg-gray-700 rounded-t-lg flex items-center justify-center">
                <Mic class="w-40 h-40 text-[#1436f5] pointer-events-none" />
              </div>
            </NuxtLink>
            <div class="p-6">
              <div class="text-sm text-gray-500 dark:text-gray-400 mb-2 font-nunito">March 31, 2025</div>
              <h3 class="text-xl font-raleway font-bold mb-2 text-[#293036] dark:text-white">Testing the Waters: My First Voice-Powered Post</h3>
              <p class="text-gray-600 dark:text-gray-300 mb-4 font-nunito line-clamp-3">
                A test blog post created using voice commands and AI assistance.
              </p>
              <NuxtLink to="/blog/voice-test-post" class="text-[#003dff] dark:text-[#3e87f8] font-medium flex items-center hover:underline">
                <BookOpen class="w-4 h-4 mr-1" />
                Read Article
              </NuxtLink>
            </div>
          </div>
          
          <!-- Blog Post CTA -->
          <div class="bg-gradient-to-r from-[#162cf1] to-[#3e87f8] rounded-lg overflow-hidden shadow-lg flex items-center">
            <div class="p-8 text-white">
              <h3 class="text-2xl font-raleway font-bold mb-4">Want to read more?</h3>
              <p class="mb-6 font-nunito">
                Check out all articles in my blog covering web development, photography, and hospitality.
              </p>
              <NuxtLink to="/blog" class="bg-white text-[#003dff] px-6 py-3 rounded-md font-nunito font-medium hover:bg-opacity-90 transition inline-flex items-center">
                <BookOpen class="w-5 h-5 mr-2" />
                Visit the Blog
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact CTA Section -->
    <section class="py-16 bg-[#293036] text-white">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-raleway font-black mb-6">Let's Work Together</h2>
        <p class="text-lg max-w-2xl mx-auto mb-8 font-nunito">
          Have a project in mind or need professional services? Get in touch and let's create something amazing.
        </p>
        <NuxtLink to="/about#contact" class="bg-[#003dff] hover:bg-[#162cf1] text-white px-8 py-4 rounded-md font-nunito font-medium transition inline-flex items-center">
          <MessageCircle class="w-5 h-5 mr-2" />
          Contact Me
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import {
  Briefcase,
  MessageCircle,
  // QrCode, // Removed unused import
  // Globe,  // Removed unused import
  Camera,
  ExternalLink,
  Image,
  FolderOpen,
  ArrowRight,
  Code,
  Palette,
  Hotel,
  Lightbulb, // Added for blog post 1
  Mic,       // Added for blog post 2
  BookOpen
} from 'lucide-vue-next';

// We'll load tsParticles dynamically in onMounted

// Import Current Work Logos
import Amalfiday2Logo from '~/components/logos/Amalfiday2Logo.vue'; // Import new logo
import AtraniruLogo from '~/components/logos/AtraniruLogo.vue';
import AlextioneLogo from '~/components/logos/AlextioneLogo.vue';

// Particle configuration for Hero Section
const heroParticlesOptions = ref({
  fullScreen: {
    enable: false // Confine particles to the hero section container
  },
  background: {
    color: {
      value: 'transparent' // Use the section's gradient background
    }
  },
  particles: {
    number: {
      value: 800, // Increase slightly for visibility during debug
      density: {
        enable: true,
        area: 800 // Density area remains the same, leading to much higher visual density
      }
    },
    color: {
      value: "#ffffff" // White particles
    },
    shape: {
      type: "circle"
    },
    opacity: {
      value: { min: 0.04, max: 0.4 }, // Subtle and varying opacity
      random: true,
      animation: {
        enable: true,
        speed: 0.5,
        minimumValue: 0.1,
        sync: false
      }
    },
    size: {
      value: { min: 0.05, max: 2 }, // Very small particles
      random: true,
      animation: {
        enable: false, // Disable size animation for consistency with small size
        // speed: 1, // Not needed if disabled
        // minimumValue: 0.5, // Not needed if disabled
        sync: false
      }
    },
    move: {
      enable: true,
      speed: 1, // Base speed, path generator might override
      direction: "none", // Path will dictate direction
      random: false, // Path generator handles initial randomness/direction
      straight: false,
      outModes: {
        default: "out" // Change back to 'out' to prevent immediate destruction
      },
      attract: {
          enable: false, // Keep attract disabled
          rotateX: 600,
          rotateY: 1200
      },
      // --- Path Generator Configuration ---
      path: {
        enable: true,
        delay: { value: 0 }, // Start immediately
        // SVG path: Left-mid -> Curve under center -> Swirl right-mid
        // Simplified path for debugging: Straight horizontal line
        path: "M 0 50 L 100 50",
        clamp: false, // Allow particles to leave the canvas after path
        generator: "svgPathGenerator", // Use the SVG path generator
        options: { // Options specific to the path generator
          loop: true, // Loop the path for debugging visibility
          // Noise removed for debugging
          // Control speed along the path (adjust as needed)
          velocity: 1 // Slow down path movement significantly
        }
      }
      // --- End Path Generator Configuration ---
    },
    links: {
        enable: false // No lines
    }
  },
  interactivity: {
    detectsOn: "window", // Detect mouse events on the window/section area
    events: {
      onHover: {
        enable: true,
        mode: "repulse" // Gently push particles away on hover
      },
      onClick: {
        enable: false // No click effects
      },
      resize: true
    },
    modes: {
      repulse: {
        distance: 80, // Interaction distance
        duration: 0.4,
        factor: 30, // How strongly they are repulsed
        speed: 1,
        maxSpeed: 5,
        easing: "ease-out-quad"
      },
      bubble: { // Alternative hover effect (optional)
        distance: 100,
        size: 5,
        duration: 2,
        opacity: 0.8
      }
    }
  },
  detectRetina: true
});

// Initialize particles on the client side after the component is mounted
onMounted(async () => {
  // Ensure this runs only on the client
  if (process.client) {
    try {
      // Access the globally provided tsParticles instance from the plugin
      const nuxtApp = useNuxtApp();
      const tsParticles = nuxtApp.$tsParticles;

      if (!tsParticles) {
        console.error("tsParticles instance not available from plugin.");
        return;
      }

      // Check if the container exists
      const container = document.getElementById("hero-particles");
      if (!container) {
        console.error("Particles container not found in DOM");
        return;
      }

      // Load the particles configuration using the global instance
      const particlesInstance = await tsParticles.load({
        id: "hero-particles", // ID of the container div
        options: heroParticlesOptions.value,
      });

      if (particlesInstance) {
        console.log("Particles initialized successfully using plugin instance", particlesInstance);
      } else {
        console.error("Failed to initialize particles: No instance returned");
      }
    } catch (error) {
      console.error("Failed to initialize particles:", error);
    }
  }
});

// Cleanup particles on component unmount
onBeforeUnmount(async () => {
  if (process.client) {
    try {
      // Access the globally provided tsParticles instance from the plugin
      const nuxtApp = useNuxtApp();
      const tsParticles = nuxtApp.$tsParticles;

      if (!tsParticles) {
        console.error("tsParticles instance not available for cleanup.");
        return;
      }

      // Find the specific tsparticles instance by its container ID
      const instances = tsParticles.dom(); // Get all instances managed by the engine
      if (instances) {
        const instance = instances.find(i => i.id === "hero-particles");
        if (instance) {
          // Destroy the instance to free up resources
          await instance.destroy();
          console.log("Particles instance destroyed successfully");
        } else {
          console.log("No particles instance found with ID 'hero-particles' to destroy");
        }
      } else {
        console.log("No particles instances found in the DOM to destroy");
      }
    } catch (error) {
      console.error("Failed to cleanup particles:", error);
    }
  }
});
</script>

<style>
/* Import Raleway and Nunito fonts */
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@900&family=Nunito:wght@400;500;700&display=swap');

.font-raleway {
  font-family: 'Raleway', sans-serif;
}

.text-outline-white {
  /* Responsive border that's 4px on desktop and 1px on mobile */
  -webkit-text-stroke-width: clamp(1px, 0.5vw, 4px);
  -webkit-text-stroke-color: rgba(255, 255, 255, 0.95);
  -webkit-text-fill-color: transparent;
  color: white; /* Fallback for non-webkit */
  width: 100%;
  display: inline-block;
  transform: translateY(0.05em); /* Fine-tune vertical alignment */
}

.font-nunito {
  font-family: 'Nunito', sans-serif;
}

.text-outline-masked {
  mask-image: linear-gradient(to bottom, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.1) 100%);
  -webkit-mask-image: linear-gradient(to bottom, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.1) 100%);
  opacity: 0.95; /* Slightly reduce overall opacity to enhance the gradient effect */
  max-width: 100%; /* Ensure text doesn't overflow container */
  overflow: visible; /* Allow text to be fully visible */
}


/* Add line clamp utility if not already available */
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
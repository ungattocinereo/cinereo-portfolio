<template>
  <div> <!-- Removed container from main wrapper -->
    <!-- 1. Hero Section (Moved outside container) -->
    <section class="relative z-0 h-screen flex items-center justify-center text-white mb-16"> <!-- Changed height to fullscreen -->
      <!-- Video Background -->
      <video
        ref="videoRef"
        autoplay
        loop
        muted="muted"
        playsinline
        poster="/images/amalfi-timelapse-placeholder.webp"
        class="absolute inset-0 w-full h-full object-cover -z-20"
        aria-hidden="true"
      >
        <source src="/video/amalfi-timelapse-evening-fast.webm" type="video/webm">
      </video>
      <!-- Dark Overlay -->
      <div class="absolute inset-0 bg-black/60 -z-10"></div>

      <!-- Text Content -->
      <div class="relative z-10 container mx-auto px-4 text-center flex flex-col items-center justify-center h-full">
        <h1 class="text-[16vw] md:text-[14vw] lg:text-[14vw] font-raleway font-black text-outline-white text-outline-masked leading-none mb-4 opacity-0 animate-fade-in">
          Inspiration
        </h1>
        <p class="text-lg md:text-xl font-nunito max-w-3xl mx-auto opacity-0 animate-fade-in animation-delay-300">
          “From learning on a sluggish computer in my hometown publishing house during college to now creating everything from video edits to advanced web apps while overlooking the stunning Amalfi Coast—my journey proves that mastering the basics, no matter how primitive, builds the foundation for unlimited creative freedom.”
        </p>
      </div>
    </section>

    <!-- Rest of the content needs the container -->
    <div class="container mx-auto px-4 py-8"> <!-- Added container back for subsequent sections -->
      <!-- 2. Top 3 Projects -->
    <section class="mb-16">
      <h2 class="text-6xl sm:text-7xl md:text-8xl font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">Featured</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Project 1 -->
        <div v-for="project in topProjects" :key="project.id" class="border dark:border-gray-700 rounded-lg overflow-hidden shadow-md hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300">
          <img
            :src="project.image"
            :alt="`${project.name} Mockup`"
            class="w-full h-56 object-cover"
            loading="lazy"
          />
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-3">{{ project.name }}</h3>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
              {{ project.description }}
            </p>
            <NuxtLink v-if="project.link.startsWith(&apos;/&apos;)" :to="project.link" class="text-sm flex items-center text-blue-600 dark:text-blue-400 hover:underline font-medium">
              <ExternalLink class="w-4 h-4 mr-1" />
              View Details
            </NuxtLink>
            <a v-else :href="project.link" target="_blank" rel="noopener noreferrer" class="text-sm flex items-center text-blue-600 dark:text-blue-400 hover:underline font-medium">
              <ExternalLink class="w-4 h-4 mr-1" />
              Visit Project
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Text Columns Section -->
    <section class="mb-16 p-8 bg-gray-100 dark:bg-gray-800 rounded-lg shadow-inner">
       <h2 class="text-6xl sm:text-7xl md:text-8xl font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">Insights</h2>
      <div class="flex flex-col md:flex-row gap-8">
        <!-- Column 1 (1/2 width) -->
        <div class="md:w-1/2">
          <h3 class="text-xl font-semibold mb-4 text-gray-700 dark:text-gray-200">My Philosophy</h3>
          <p class="text-gray-600 dark:text-gray-400">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
          </p>
        </div>
        <!-- Columns 2 &amp; 3 Container (1/2 width) -->
        <div class="md:w-1/2 flex flex-col sm:flex-row gap-8">
          <!-- Column 2 (1/4 total width) -->
          <div class="sm:w-1/2">
            <h3 class="text-xl font-semibold mb-4 text-gray-700 dark:text-gray-200">Process</h3>
             <p class="text-gray-600 dark:text-gray-400">
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
          </div>
          <!-- Column 3 (1/4 total width) -->
          <div class="sm:w-1/2">
             <h3 class="text-xl font-semibold mb-4 text-gray-700 dark:text-gray-200">Tools</h3>
             <p class="text-gray-600 dark:text-gray-400">
              Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Other Projects -->
    <section class="mb-16">
      <h2 class="text-6xl sm:text-7xl md:text-8xl font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">...and more</h2>
       <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
         <!-- Displaying other projects -->
         <div v-for="project in otherProjects" :key="project.id" class="border dark:border-gray-700 rounded-lg overflow-hidden shadow-md hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300">
           <img
             :src="project.image"
             :alt="`${project.name} Thumbnail`"
             class="w-full h-48 object-cover"
             loading="lazy"
           />
           <div class="p-4">
             <h3 class="font-semibold mb-2">{{ project.name }}</h3>
             <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">
               {{ project.description }}
             </p>
             <NuxtLink v-if="project.link.startsWith(&apos;/&apos;)" :to="project.link" class="text-xs flex items-center text-blue-600 dark:text-blue-400 hover:underline font-medium">
               <ExternalLink class="w-3 h-3 mr-1" />
               View Details
             </NuxtLink>
              <a v-else :href="project.link" target="_blank" rel="noopener noreferrer" class="text-xs flex items-center text-blue-600 dark:text-blue-400 hover:underline font-medium">
               <ExternalLink class="w-3 h-3 mr-1" />
               Visit Project
             </a>
           </div>
         </div>
      </div>
      <!-- Note: Infinite scroll implementation requires more complex setup -->
    </section>

    <!-- 5. Collaborate Section -->
    <section class="py-12 mb-16"> <!-- Removed rounded-lg and shadow-lg -->
       <!-- Title aligned left, styled as per spec -->
       <h2 class="text-6xl sm:text-7xl md:text-8xl font-raleway font-black mb-12 text-transparent" style="-webkit-text-stroke: 2px #182bf4;">Collaborate</h2>
      <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-10"> <!-- Removed text-center -->
        <div>
          <!-- Removed old icon div -->
          <div class="flex items-center gap-2 mb-3"> <!-- Added flex container for icon + text -->
            <Brain class="w-8 h-8 text-blue-600 dark:text-blue-400 shrink-0" /> <!-- Added Brain icon -->
            <h3 class="text-3xl font-raleway font-black">Expertise</h3> <!-- Updated h3 style -->
          </div>
          <p class="text-gray-600 dark:text-gray-400 text-left"> <!-- Added text-left -->
            I have acquired extensive industry experience by mastering all processes since the early days when technology functioned in a completely different way. My career spans from hands-on work in a print shop to holding leadership roles such as director and manager within a dedicated design division of a large corporation. This journey has provided me with a deep understanding of every level and structure in the field.
          </p>
        </div>
        <div>
           <!-- Removed old icon div -->
           <div class="flex items-center gap-2 mb-3"> <!-- Added flex container for icon + text -->
             <Handshake class="w-8 h-8 text-green-600 dark:text-green-400 shrink-0" /> <!-- Added Handshake icon -->
             <h3 class="text-3xl font-raleway font-black">Collaboration</h3> <!-- Updated h3 style -->
           </div>
          <p class="text-gray-600 dark:text-gray-400 text-left"> <!-- Added text-left -->
            Working together is at the heart of what I do. My fluency in three languages—effortlessly switching between them—enhances my ability to communicate and collaborate. I excel in English at an exceptional level, hold a B2 certificate in Italian, and naturally, Russian is my native language. This multilingual capability enables me to gather diverse insights and act as an effective mediator among various teams.
          </p>
        </div>
        <div>
           <!-- Removed old icon div -->
           <div class="flex items-center gap-2 mb-3"> <!-- Added flex container for icon + text -->
             <Gem class="w-8 h-8 text-purple-600 dark:text-purple-400 shrink-0" /> <!-- Added Gem icon -->
             <h3 class="text-3xl font-raleway font-black">Quality</h3> <!-- Updated h3 style -->
           </div>
          <p class="text-gray-600 dark:text-gray-400 text-left"> <!-- Added text-left -->
            I am relentlessly committed to excellence. I am never fully satisfied with the initial outcome and am always driven to see how things can be improved. Constantly engaged with every project, I find innovative ways to enhance the work, ensuring that quality is elevated across all areas of my practice.
          </p>
        </div>
      </div>
    </section>

    </div> <!-- Close the container div for subsequent sections -->
  </div> <!-- Close the main wrapper div -->
</template>

<script setup>
import { ref, onMounted } from 'vue'; // Added ref and onMounted
import { Briefcase, ExternalLink, Zap, Users, Award, Brain, Handshake, Gem } from 'lucide-vue-next'; // Added Brain, Handshake, Gem
// Video ref
const videoRef = ref(null);

// Placeholder data - replace with your actual project data
// You might fetch this from an API or define it here
const topProjects = [
  { id: 1, name: 'QR Concierge', description: 'Digital concierge system using QR codes for hotels and tourism businesses.', image: '/images/mockup-qrcierge.jpg', link: '/portfolio/qcierge' },
  { id: 2, name: 'Tourism Websites', description: 'Collection of WordPress sites for tourism and local businesses on the Amalfi Coast.', image: '/images/mockup-websites.jpg', link: 'https://amalfi.day' },
  { id: 3, name: 'Interior Photography', description: 'Professional photography for hotels, villas, and restaurants.', image: '/images/interior-photo.jpg', link: '/portfolio' }, // Link to portfolio page section or specific gallery later
];

const otherProjects = [
  { id: 4, name: 'Le Palme Restaurant', description: 'Various design, photo, and video projects for a restaurant in Atrani.', image: '/images/portfolio/project-4/le-palme-atrani-new-menew-2020.jpg', link: '/portfolio/project-4' },
  { id: 5, name: 'Caffè Vittoria Menu', description: 'Creative menu design for a beachside café in Atrani.', image: '/images/portfolio/caffe-vittoria/thumbnail.jpg', link: '/portfolio/caffe-vittoria' },
  { id: 6, name: 'La Moressa Menu', description: 'Design and photography for a restaurant menu on the Amalfi Coast.', image: '/images/portfolio/moressa/header-bg.jpg', link: '/portfolio/moressa' },
  { id: 7, name: 'Olivier Menu Design', description: 'Elegant menu design for a gourmet restaurant in Sochi.', image: '/images/portfolio/olivier/menu-olivier-2017-3.jpg', link: '/portfolio/olivier' },
  // Add more projects here as needed
  // { id: 5, name: 'Project 5', description: '...', image: '/images/placeholder.jpg', link: '#' },
  // { id: 6, name: 'Project 6', description: '...', image: '/images/placeholder.jpg', link: '#' },
  // { id: 7, name: 'Project 7', description: '...', image: '/images/placeholder.jpg', link: '#' },
  // { id: 8, name: 'Project 8', description: '...', image: '/images/placeholder.jpg', link: '#' },
];

// Note: For infinite scroll, you'd typically load `otherProjects` incrementally
// based on scroll position, likely involving state management (e.g., useState)
// and potentially API calls.
// Attempt to play video on mount
onMounted(() => {
  if (videoRef.value) {
    // The play() method returns a Promise which may be rejected
    // if autoplay is disallowed. We'll catch potential errors.
    videoRef.value.play().catch(error => {
      console.error("Video autoplay failed:", error);
      // You could potentially show a play button here if needed
    });
  }
});
</script>

<style scoped>
/* Add any component-specific styles here if needed */

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  /* Apply the animation */
  animation: fadeIn 0.8s ease-out forwards;
}

/* Utility for delaying animation */
.animation-delay-300 {
  animation-delay: 300ms;
}

/* Re-apply Raleway/Nunito locally if needed, though they should be global */
/* @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@900&family=Nunito:wght@400;700&display=swap'); */

.font-raleway {
  font-family: 'Raleway', sans-serif;
}
.font-nunito {
  font-family: 'Nunito', sans-serif;
}

/* Re-apply outline styles locally if needed, though they should be global */
/*
.text-outline-white {
  -webkit-text-stroke-width: clamp(1px, 0.5vw, 4px);
  -webkit-text-stroke-color: rgba(255, 255, 255, 0.95);
  -webkit-text-fill-color: transparent;
  color: white;
  width: 100%;
  display: inline-block;
  transform: translateY(0.05em);
}

.text-outline-masked {
  mask-image: linear-gradient(to bottom, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.1) 100%);
  -webkit-mask-image: linear-gradient(to bottom, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.1) 100%);
  opacity: 0.95;
  max-width: 100%;
  overflow: visible;
}
*/
</style>
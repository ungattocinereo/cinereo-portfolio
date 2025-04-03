<template>
  <div class="container mx-auto px-4 py-8">

    <!-- Hero Section -->
    <section class="relative flex flex-col md:flex-row items-center mb-24 md:mb-32">
      <!-- Text Content -->
      <div class="md:w-2/3 relative z-10 mb-8 md:mb-0 md:pr-8">
        <h1 class="text-6xl sm:text-7xl md:text-8xl lg:text-9xl font-raleway font-black text-blue-700 mb-4 -ml-1 md:-ml-2" style="line-height: 0.9;">Gregory<br>Smirnov</h1>
        <p class="text-lg md:text-xl text-gray-700 font-nunito mt-6 max-w-md">
          Photographer, graphic and video designer based in Amalfi Coast, Italy. Master of communication in EnoGastronomy.
        </p>
      </div>
      <!-- Image with Hover Effect -->
      <div class="md:w-1/2 md:absolute md:right-0 md:top-0 md:h-full flex items-center justify-center md:justify-end perspective-1000">
        <img
          ref="heroImage"
          src="/images/about/gregory-smirnov.jpg"
          alt="Gregory Smirnov"
          class="rounded-lg shadow-lg w-full max-w-lg md:max-w-none md:h-auto transition-transform duration-300 ease-out"
          @mousemove="handleMouseMove"
          @mouseleave="resetTilt"
          style="transform-style: preserve-3d;"
        >
      </div>
    </section>

    <!-- Language Skills Section -->
    <section class="mb-16">
      <h2 class="title-header">Language</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
        <div>
          <div class="relative pt-1">
             <div class="text-2xl font-bold text-blue-700 mb-2">100%</div>
             <h4 class="text-lg font-raleway font-bold mb-2">I speak 🪆 Russian</h4>
             <p class="text-gray-600 font-nunito text-sm">I speak it perfectly with even some slang variations for central and south regions of Russia.</p>
          </div>
        </div>
         <div>
          <div class="relative pt-1">
             <div class="text-2xl font-bold text-pink-500 mb-2">99%</div>
             <h4 class="text-lg font-raleway font-bold mb-2">I speak 🏈 English</h4>
             <p class="text-gray-600 font-nunito text-sm">Use it basically to learn everything I know right now. From books to YouTube videos and tv shows.</p>
          </div>
        </div>
         <div>
          <div class="relative pt-1">
             <div class="text-2xl font-bold text-gray-700 mb-2">95%</div>
             <h4 class="text-lg font-raleway font-bold mb-2">Parlo 🍝 Italiano</h4>
             <p class="text-gray-600 font-nunito text-sm">Ho imparato per trasferirmi in Italia. Tengo un certificato B2 rilasciato dal Università Roma Tre in 2016.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section class="mb-16 bg-gray-100 p-8 rounded-lg">
       <div class="flex flex-col md:flex-row">
         <div class="md:w-1/2 md:pr-8">
            <h5 class="text-gray-500 font-raleway font-semibold mb-2">Gregory Smirnov</h5>
            <h2 class="text-4xl font-raleway font-black mb-4">Graphic design has been my prior passion.</h2>
            <p class="text-gray-700 font-nunito mb-8">
              I never stopped to learn more. I know photography all my life. I learnt video filmmaking, editing, web design and so on. Always trying to express myself in best and more brilliant way possible.
            </p>
            <div class="space-y-4">
              <SkillProgressBar skill="Print design" percentage="96" color="bg-gradient-to-r from-blue-600 to-pink-500" />
              <SkillProgressBar skill="Video Editing" percentage="80" color="bg-gradient-to-r from-blue-600 to-pink-500" />
              <SkillProgressBar skill="Digital Photo" percentage="93" color="bg-gradient-to-r from-blue-600 to-pink-500" />
              <SkillProgressBar skill="UI Design" percentage="73" color="bg-gradient-to-r from-blue-600 to-pink-500" />
              <SkillProgressBar skill="Web Design" percentage="86" color="bg-gradient-to-r from-blue-600 to-pink-500" />
            </div>
         </div>
          <div class="md:w-1/2 mt-8 md:mt-0">
             <img src="/images/about/gregory-avatar.jpg" alt="Design Skills" class="rounded-lg shadow-md object-cover h-full w-full">
          </div>
       </div>
    </section>

    <!-- Photo Equipment Section -->
    <section class="mb-16">
      <h2 class="title-header">Photo</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <EquipmentCard image="/images/about/sony-a7iii.jpg" title="Sony α7 III" description="My battle horse. The camera that make impossible possible." />
        <EquipmentCard image="/images/about/tamron-17-28.jpg" title="Tamron 17-28 mm F/2.8" description="Perfect for vlogging and interior photos." />
        <EquipmentCard image="/images/about/sony-40mm.jpg" title="Sony 40 mm F/2.5 G" description="Very sharp and beautiful prime Sony G-Lenses." />
        <EquipmentCard image="/images/about/viltrox-85mm.jpg" title="Viltrox 85mm F/1.8 II" description="Full-frame autofocus tele- lens." />
      </div>
    </section>

    <!-- Software Section -->
    <section class="mb-16">
       <h2 class="title-header">Software</h2>
       <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-8 mb-8">
         <SoftwareCard image="/images/about/photoshop-icon.png" title="Photoshop" percentage="99" color="bg-gradient-to-r from-blue-600 to-pink-500" />
         <SoftwareCard image="/images/about/indesign-icon.png" title="Indesign" percentage="99" color="bg-gradient-to-r from-blue-600 to-pink-500" />
         <SoftwareCard image="/images/about/illustrator-icon.png" title="Illustrator" percentage="96" color="bg-gradient-to-r from-blue-600 to-pink-500" />
         <SoftwareCard image="/images/about/xd-icon.png" title="XD" percentage="97" color="bg-gradient-to-r from-blue-600 to-pink-500" />
         <SoftwareCard image="/images/about/finalcut-icon.jpg" title="Final Cut" percentage="91" color="bg-gradient-to-r from-blue-500 to-cyan-400" />
         <SoftwareCard image="/images/about/motion-icon.jpg" title="Motion" percentage="89" color="bg-gradient-to-r from-blue-500 to-cyan-400" />
       </div>
        <p class="text-center text-gray-600 font-nunito">
          Also proficient in: Adobe Audition, Adobe Premiere Pro, Capture One, Apple Compressor, DxO PhotoLab 3, Apple Keynote, Apple Pages, Apple Numbers, Microsoft Excel, Microsoft Word, Microsoft PowerPoint, OBS, Facebook Ads, Google Ads, WordPress, WooCommerce.
        </p>
    </section>

     <!-- About Text Section -->
    <section class="mb-16">
      <div class="flex flex-col md:flex-row md:space-x-12 lg:space-x-16">
        <!-- Left Column: Intro Text -->
        <div class="md:w-1/2 lg:w-7/12 mb-8 md:mb-0">
          <h3 class="text-3xl md:text-4xl font-raleway font-normal leading-tight text-gray-800">
            I'm designer & photographer. Currently studying in Gambero Rosso Academy to be communication specialist of enogastronomy
          </h3>
        </div>

        <!-- Right Column: Design & Hospitality -->
        <div class="md:w-1/2 lg:w-5/12 flex flex-col sm:flex-row sm:space-x-8">
          <div class="sm:w-1/2 mb-8 sm:mb-0">
            <h4 class="text-xl font-raleway font-bold mb-3">Design</h4>
            <p class="text-gray-700 font-nunito text-sm mb-4">Before moving to Italy I worked in Sochi first as a designer, then as a head of design department.</p>
            <NuxtLink to="/portfolio" class="text-blue-600 hover:text-blue-800 font-raleway font-bold text-sm inline-flex items-center group">
              <span class="w-4 h-0.5 bg-blue-600 mr-2"></span>
              My portfolio
            </NuxtLink>
          </div>
          <div class="sm:w-1/2">
            <h4 class="text-xl font-raleway font-bold mb-3">Hospitality</h4>
            <p class="text-gray-700 font-nunito text-sm mb-4">I have a family business in Italy in hospitality field. It helps me to se people from around the world.</p>
            <a href="mailto:gregory@cinereo.it" class="text-blue-600 hover:text-blue-800 font-raleway font-bold text-sm inline-flex items-center group">
               <span class="w-4 h-0.5 bg-blue-600 mr-2"></span>
               Get in touch
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="mb-16">
       <h2 class="text-3xl font-raleway font-bold text-center mb-8">Contact Me</h2>
       <div class="flex flex-col md:flex-row">
          <div class="md:w-1/2 mb-8 md:mb-0 md:pr-8">
             <!-- Placeholder for Map - Implement using a library like Leaflet or Mapbox if needed -->
             <div class="bg-gray-200 h-64 md:h-full rounded-lg flex items-center justify-center text-gray-500">
                Map Placeholder
             </div>
          </div>
          <div class="md:w-1/2">
             <p class="text-gray-700 font-nunito mb-6">
                Currently, I'm focused on my new project, dedicated to the food & wine of the Campania region of Italy. You can find me on the Amalfi Coast, in Ravello or Atrani. If you have an interesting project, don't hesitate to write to me directly.
             </p>
             <h5 class="text-lg font-raleway font-bold mb-2">Write or call me</h5>
             <p class="text-gray-700 font-nunito mb-6">
                E-mail: <a href="mailto:gregory@cinereo.it" class="text-blue-600 hover:underline">gregory@cinereo.it</a><br>
                Telegram: <a href="http://t.me/cinereo" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">cinereo</a>
             </p>
             <!-- Contact Form Placeholder - Implement using a form library or service -->
             <div class="bg-gray-100 p-4 rounded-lg text-center text-gray-500">
                Contact Form Placeholder
             </div>
          </div>
       </div>
    </section>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// --- Hero Image Tilt Effect ---
const heroImage = ref(null);
const maxTilt = 8; // Max tilt angle in degrees

const handleMouseMove = (event) => {
  if (!heroImage.value) return;

  const { left, top, width, height } = heroImage.value.getBoundingClientRect();
  const x = event.clientX - left;
  const y = event.clientY - top;

  const centerX = width / 2;
  const centerY = height / 2;

  const deltaX = x - centerX;
  const deltaY = y - centerY;

  // Calculate tilt angles - invert Y tilt for natural feel
  const rotateY = (deltaX / centerX) * maxTilt;
  const rotateX = -(deltaY / centerY) * maxTilt;

  heroImage.value.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.03)`; // Slight scale for effect
};

const resetTilt = () => {
  if (heroImage.value) {
    heroImage.value.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
  }
};

// --- Helper Components ---

// Helper component for progress bars
const SkillProgressBar = {
  props: ['skill', 'percentage', 'color'],
  template: `
    <div class="mb-2">
      <div class="flex justify-between mb-1">
        <p class="font-raleway font-semibold text-sm">{{ skill }}</p>
        <span class="text-sm font-medium text-gray-500 dark:text-gray-400">{{ percentage }}%</span>
      </div>
      <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
        <div :class="['h-2.5 rounded-full', color]" :style="{ width: percentage + '%' }"></div>
      </div>
    </div>
  `
};

// Helper component for equipment cards
const EquipmentCard = {
  props: ['image', 'title', 'description'],
  template: `
    <div class="text-center">
      <img :src="image" :alt="title" class="w-full h-48 object-contain mb-4 rounded-lg bg-gray-50 p-2">
      <h5 class="text-lg font-raleway font-bold mb-1">{{ title }}</h5>
      <p class="text-gray-600 font-nunito text-sm">{{ description }}</p>
    </div>
  `
};

// Helper component for software cards
const SoftwareCard = {
   props: ['image', 'title', 'percentage', 'color'],
   template: `
    <div class="text-center">
       <img :src="image" :alt="title + ' icon'" class="w-16 h-16 mx-auto mb-2 object-contain">
       <p class="font-raleway font-semibold text-sm mb-1">{{ title }}</p>
       <div class="w-full bg-gray-200 rounded-full h-1.5 dark:bg-gray-700">
         <div :class="['h-1.5 rounded-full', color]" :style="{ width: percentage + '%' }"></div>
       </div>
       <span class="text-xs font-medium text-gray-500 dark:text-gray-400">{{ percentage }}%</span>
    </div>
   `
}

// Define components for use in the template (though not explicitly needed in <script setup>)
const components = { SkillProgressBar, EquipmentCard, SoftwareCard };

useHead({
  title: 'About - Cinereo',
  meta: [
    { name: 'description', content: 'Gregory Smirnov: Photographer, graphic and video designer based in Amalfi Coast, Italy. Master of communication in EnoGastronomy.' }
  ]
})
</script>

<style scoped>
/* Add perspective for the 3D effect */
.perspective-1000 {
  perspective: 1000px;
}

/* Ensure the image preserves 3D transformations */
img {
  transform-style: preserve-3d;
}

/* Add any other page-specific styles if needed */
.font-raleway { font-family: 'Raleway', sans-serif; }
.font-nunito { font-family: 'Nunito', sans-serif; }
</style>
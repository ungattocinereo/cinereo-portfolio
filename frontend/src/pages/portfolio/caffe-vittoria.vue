<template>
  <div class="text-black dark:bg-gray-900 dark:text-white">

    <!-- Page Header -->
    <header class="relative h-[350px] md:h-[450px] lg:h-[550px] xl:h-[650px] overflow-hidden">
      <div class="absolute inset-0 bg-black">
        <img
          src="/images/portfolio/caffe-vittoria/header-bg.jpg"
          alt="Caffè Vittoria Menu Header Background"
          class="w-full h-full object-cover opacity-60"
        >
      </div>
      <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/20 to-transparent"></div>
      <div class="relative z-10 h-full flex items-center justify-center text-center text-white">
        <div class="container mx-auto px-4">
          <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold mb-4 font-raleway tracking-tight">
            Beach Caffè Menu Design
          </h1>
          <p class="text-lg sm:text-xl md:text-2xl font-nunito font-semibold">
            Bright menu for local restaurant and beach
          </p>
        </div>
      </div>
       <!-- Scroll Down Arrow (Optional - Add if needed) -->
       <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-10">
         <a href="#content-start" class="block w-8 h-12 border-2 border-white rounded-full animate-bounce">
           <svg class="w-4 h-4 mx-auto mt-2 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
         </a>
       </div>
    </header>

    <main id="content-start" class="container mx-auto px-4 py-12 md:py-16 lg:py-20">

      <!-- Section: BEFORE -->
      <section class="mb-16 md:mb-24 lg:mb-32 bg-gray-100 dark:bg-gray-800 py-12 md:py-16 lg:py-20 px-4">
        <div class="max-w-3xl mx-auto text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway text-gradient-blue-pink">
            BEFORE: Basically this is what they had at the beginning
          </h2>
          <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito mb-8">
            It was a simple menu, made many years ago in the pre-COVID era. Like many menus on the Amalfi Coast, it worked, and business owners didn't prioritize updates. But times change.
          </p>
          <!-- Placeholder for the 'Old Menu' gallery -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <img src="/images/portfolio/caffe-vittoria/old-menu-1.jpg" alt="Old Menu Page 1" class="rounded shadow-md">
            <img src="/images/portfolio/caffe-vittoria/old-menu-2.jpg" alt="Old Menu Page 2" class="rounded shadow-md">
            <img src="/images/portfolio/caffe-vittoria/old-menu-3.jpg" alt="Old Menu Page 3" class="rounded shadow-md">
            <img src="/images/portfolio/caffe-vittoria/old-menu-4.jpg" alt="Old Menu Page 4" class="rounded shadow-md">
            <!-- Add more placeholders if needed -->
          </div>
        </div>
      </section>

      <!-- Section: AFTER -->
      <section class="mb-16 md:mb-24 lg:mb-32">
        <div class="max-w-3xl mx-auto text-center mb-12 md:mb-16">
          <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway text-gradient-purple-blue">
            AFTER: Creative design menu for little bar in town and beach area
          </h2>
          <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
            Now it's a huge menu printed on plastic (850x750mm), visible from a distance. Designed in an exaggerated, carnival style (as requested by the owner), each picture aims to entice passersby.
          </p>
        </div>

        <!-- Big Outside Menu Section -->
        <div class="flex flex-col md:flex-row items-center mb-16 md:mb-24 lg:mb-32">
          <div class="w-full md:w-1/3 lg:w-1/4 p-4 md:p-6 lg:p-8 order-2 md:order-1">
             <h1 class="text-5xl lg:text-7xl font-extrabold font-raleway mb-4 leading-tight text-outline">
               BIG <br><em>OUTSIDE</em><br> MENU
             </h1>
            <p class="text-gray-700 dark:text-gray-300 font-nunito">
              The challenge was creating a clean, bright menu showcasing everything offered, using many photos to attract tourists.
            </p>
          </div>
          <div class="w-full md:w-2/3 lg:w-3/4 order-1 md:order-2 mb-8 md:mb-0">
            <img src="/images/portfolio/caffe-vittoria/big-menu-mockup.jpg" alt="Big Outside Menu Mockup" class="rounded-lg shadow-xl w-full h-auto object-cover">
          </div>
        </div>

        <!-- Color & Material Section -->
        <section class="mb-16 md:mb-24 lg:mb-32 bg-gray-50 dark:bg-gray-800 py-12 md:py-16 lg:py-20 px-4">
          <div class="container mx-auto flex flex-col md:flex-row items-center">
            <div class="w-full md:w-2/5 mb-8 md:mb-0 md:pr-8 lg:pr-12">
              <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway">Color & Material</h2>
              <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
                With menus placed in the main square and the beach area, a high-contrast design was essential for readability day and night. The chosen colors pop against the surroundings.
              </p>
            </div>
            <div class="w-full md:w-3/5 grid grid-cols-3 gap-4">
              <div class="bg-black text-white p-6 rounded shadow-md flex flex-col justify-between h-48">
                <h5 class="font-bold font-raleway">Washed Black</h5>
                <p class="font-mono text-sm">#0a0204</p>
              </div>
              <div class="bg-[#ec008c] text-white p-6 rounded shadow-md flex flex-col justify-between h-48">
                 <h5 class="font-bold font-raleway">Magenta</h5>
                 <p class="font-mono text-sm">#ec008c</p>
              </div>
              <div class="bg-[#fcaf17] text-black p-6 rounded shadow-md flex flex-col justify-between h-48">
                 <h5 class="font-bold font-raleway">Orange Yellow</h5>
                 <p class="font-mono text-sm">#fcaf17</p>
              </div>
            </div>
          </div>
        </section>

        <!-- Large Menu Image -->
        <div class="mb-16 md:mb-24 lg:mb-32">
           <img src="/images/portfolio/caffe-vittoria/menu-flat-layout.jpg" alt="Full Menu Layout" class="rounded-lg shadow-xl w-full h-auto">
        </div>

        <!-- Gallery Section -->
        <section class="mb-16 md:mb-24 lg:mb-32">
          <div class="text-center mb-12 md:mb-16">
            <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway">
              This is my design you can find in the town and the beach area
            </h2>
          </div>
          <!-- Placeholder for the 'Menu Photos' gallery -->
           <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
             <img src="/images/portfolio/caffe-vittoria/menu-photo-1.jpg" alt="Menu Photo 1" class="rounded shadow-md object-cover aspect-[4/3]">
             <img src="/images/portfolio/caffe-vittoria/menu-photo-2.jpg" alt="Menu Photo 2" class="rounded shadow-md object-cover aspect-[4/3]">
             <img src="/images/portfolio/caffe-vittoria/menu-photo-3.jpg" alt="Menu Photo 3" class="rounded shadow-md object-cover aspect-[4/3]">
             <img src="/images/portfolio/caffe-vittoria/menu-photo-4.jpg" alt="Menu Photo 4" class="rounded shadow-md object-cover aspect-[4/3]">
           </div>
        </section>

        <!-- Digital Menu Section -->
        <section class="mb-16 md:mb-24 lg:mb-32 text-center">
           <h2 class="text-3xl md:text-4xl font-bold mb-6 font-raleway text-gradient-pink-orange">
             Due to new law every public place in Amalfi coast should have a menu safe for all the costumers, so I've made a digital menu and QR code to open it
           </h2>
           <!-- Placeholder for parallax image -->
           <div class="h-64 md:h-80 lg:h-96 bg-gray-300 rounded-lg shadow-lg flex items-center justify-center mb-8 bg-cover bg-center" style="background-image: url('/images/portfolio/caffe-vittoria/digital-menu-bg.jpg');">
             <a href="http://cinereo.ru/vittoria" target="_blank" rel="noopener noreferrer" class="inline-block px-8 py-4 bg-white text-black font-bold rounded-md shadow-lg transition duration-300 hover:bg-gray-200 hover:shadow-xl font-nunito uppercase tracking-wider text-lg">
               Open Digital Menu
             </a>
           </div>
        </section>

        <!-- Beach Area Menu Section -->
        <section class="mb-16 md:mb-24 lg:mb-32 flex flex-col md:flex-row items-center">
           <div class="w-full md:w-3/5 mb-8 md:mb-0 md:pr-12">
             <img src="/images/portfolio/caffe-vittoria/beach-menu-mockup.jpg" alt="Beach Area Menu Mockup" class="rounded-lg shadow-xl w-full h-auto">
           </div>
           <div class="w-full md:w-2/5">
             <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway">Same menu at the beach area of Atrani</h2>
           </div>
        </section>

        <!-- Pasticiotto Section -->
        <section class="flex flex-col md:flex-row items-center">
           <div class="w-full md:w-3/5 order-2 md:order-1">
             <blockquote class="border-l-4 border-pink-500 dark:border-pink-400 pl-6 italic text-xl md:text-2xl text-gray-700 dark:text-gray-300 font-nunito mb-4">
               "Some products are so unique that it was necessary to make a photo of them. For example, this one is Pasticiotto Atranese"
             </blockquote>
             <p class="text-gray-600 dark:text-gray-400 font-raleway font-bold">- Gregory Smirnov <span class="text-gray-500 dark:text-gray-400 font-normal">About this design</span></p>
           </div>
           <div class="w-full md:w-2/5 order-1 md:order-2 mb-8 md:mb-0 md:pl-12">
             <img src="/images/portfolio/caffe-vittoria/pasticiotto.jpg" alt="Pasticiotto Atranese" class="rounded-lg shadow-xl w-full h-auto">
           </div>
        </section>

      </section>

    </main>

    <!-- Project Navigation (Optional - Add if needed) -->
    <!-- <ProjectTemplateSecondary prev-slug="la-moressa" next-slug="couple-photography-amalfi-italy" /> -->

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Define SEO meta data if needed using useHead
useHead({
  title: 'Caffè Vittoria Menu Design - Cinereo Portfolio',
  meta: [
    { name: 'description', content: 'Creative menu design for Caffè Vittoria, a beachside café in Atrani, Amalfi Coast.' }
  ],
})

// Add any specific script logic here if required
</script>

<style scoped>
/* Add any component-specific styles here */
.text-gradient-blue-pink {
  background: linear-gradient(to right, #3452ff, #ff3366);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-gradient-purple-blue {
   background: linear-gradient(to right, #9b51e0, #0693e3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-gradient-pink-orange {
   background: linear-gradient(to right, #ec008c, #fcaf17);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-outline {
  -webkit-text-stroke: 1px black; /* Adjust color and width as needed */
  text-stroke: 1px black;
  color: transparent; /* Make the fill transparent */
}
.text-outline em {
   -webkit-text-stroke: 0;
   color: black; /* Or desired fill color for emphasized text */
   font-style: normal; /* Override italic if needed */
}

/* Ensure Raleway and Nunito fonts are loaded globally or import them here */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Raleway:ital,wght@0,400;0,500;0,700;0,800;0,900;1,400&display=swap');

h1, h2, h3, h4, h5, h6 {
  font-family: 'Raleway', sans-serif;
}

body, p, span, a, div, blockquote /* Add other elements as needed */ {
  font-family: 'Nunito', sans-serif;
}

/* Replicate specific styles if Tailwind doesn't cover them */
blockquote {
  /* Example: Add specific blockquote styling if needed */
}
</style>
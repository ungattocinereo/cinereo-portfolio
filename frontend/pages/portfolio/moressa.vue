<template>
  <div class="text-black dark:bg-gray-900 dark:text-white">

    <!-- Page Header -->
    <header class="relative h-[350px] md:h-[450px] lg:h-[550px] xl:h-[650px] overflow-hidden">
       <!-- Replicating caffe-vittoria structure -->
       <div class="absolute inset-0 bg-black"> <!-- Container div like caffe-vittoria -->
         <NuxtImg
           src="/images/portfolio/moressa/header-bg.jpg"
           alt="La Moressa Menu Header Background"
           class="w-full h-full object-cover opacity-60"
           sizes="100vw"
           format="webp"
           preload
         ></NuxtImg>
       </div>
       <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-black/20 to-transparent"></div> <!-- Re-added gradient overlay -->
       <!-- Text Content remains relative z-10 -->
       <div class="relative z-10 h-full flex items-center justify-start text-left text-white">
         <div class="container mx-auto px-4 md:pl-12 lg:pl-20 max-w-4xl">
            <div class="md:w-3/4 lg:w-1/2">
               <h1 class="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold mb-4 font-raleway tracking-tight">
                 Photos and design of menu for the restaurant
               </h1>
               <p class="text-lg sm:text-xl md:text-2xl font-nunito font-semibold">
                 Digital &amp; printable menu for one of the best restaurants in Amalfi Coast
               </p>
            </div>
         </div>
       </div>
        <!-- Scroll Down Arrow -->
        <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-10">
          <a href="#content-start" class="block w-8 h-12 border-2 border-white rounded-full animate-bounce">
            <svg class="w-4 h-4 mx-auto mt-2 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
          </a>
        </div>
     </header>

    <main id="content-start" class="container mx-auto px-4 py-12 md:py-16 lg:py-20">
      <div class="space-y-16 md:space-y-24 lg:space-y-32">

        <!-- Section 1: Intro Text -->
        <section class="max-w-3xl mx-auto text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway text-gradient-blue-teal">
            Printable and digital menu
          </h2>
          <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
            This is one of the most important restaurants in Praiano on the Amalfi Coast. The main target audience is foreign tourists. But even among the locals, the restaurant is famous for its pizza… I managed to make a light and very contrast menu that looks amazing both printed and on the smartphone.
          </p>
        </section>

        <!-- Section 2: La Moressa Text & Image -->
        <section class="flex flex-col md:flex-row items-center gap-8 md:gap-12 lg:gap-16">
          <div class="md:w-1/3 space-y-6 order-2 md:order-1 text-left">
            <h1 class="text-5xl md:text-6xl lg:text-7xl font-extrabold font-raleway leading-none text-outline">
              LA MORESSA <br><em class="text-gray-800 dark:text-gray-200 not-italic">RESTAURANT</em><br> MENU
            </h1>
            <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
              One of the best restaurants in Praiano (Amalfi coast).
            </p>
          </div>
          <div class="md:w-2/3 order-1 md:order-2">
            <NuxtImg
              src="/images/portfolio/moressa/la-moressa-italian-menu-2.jpg"
              alt="La Moressa Menu Mockup"
              class="w-full h-auto rounded-lg shadow-xl"
              sizes="100vw md:67vw"
              format="webp"
              loading="lazy"
            />
          </div>
        </section>

        <!-- Section 3: Color & Material -->
        <section class="bg-gray-100 dark:bg-gray-800 py-12 md:py-16 lg:py-20 px-4 rounded-lg shadow-inner">
          <div class="container mx-auto flex flex-col md:flex-row items-start gap-8 md:gap-12 lg:gap-16">
            <div class="w-full md:w-2/5 space-y-4">
              <h2 class="text-3xl md:text-4xl font-bold font-raleway text-gray-800 dark:text-gray-100">
                Color &amp; Material
              </h2>
              <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
                The new menu should follow the style of the old one. So I left it in Seal Brown. And to make the logo stand out brightly against this background, make Deep Saffron. The main menu should be written in very contrast and on a white background to improve its readability on the terrace at dusk.
              </p>
            </div>
            <div class="w-full md:w-3/5 grid grid-cols-3 gap-4 md:gap-6">
              <!-- Color Swatch 1 -->
              <div class="bg-[#542a15] text-white p-4 md:p-6 rounded-md shadow-md flex flex-col justify-between min-h-[150px] md:min-h-[180px]">
                <h5 class="font-bold font-raleway text-lg md:text-xl">Seal Brown</h5>
                <p class="font-mono text-sm opacity-80">#542a15</p>
              </div>
              <!-- Color Swatch 2 -->
              <div class="bg-[#f19b38] text-white p-4 md:p-6 rounded-md shadow-md flex flex-col justify-between min-h-[150px] md:min-h-[180px]">
                <h5 class="font-bold font-raleway text-lg md:text-xl">Deep Saffron</h5>
                <p class="font-mono text-sm opacity-80">#f19b38</p>
              </div>
              <!-- Color Swatch 3 -->
              <div class="bg-[#ffffff] text-gray-800 p-4 md:p-6 rounded-md shadow-md flex flex-col justify-between min-h-[150px] md:min-h-[180px] border border-gray-200 dark:border-gray-700">
                <h5 class="font-bold font-raleway text-lg md:text-xl">White</h5>
                <p class="font-mono text-sm opacity-80">#ffffff</p>
              </div>
            </div>
          </div>
        </section>

        <!-- Section 4: Features (Scrollable, Allergens, Fast Loading) -->
        <section class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12 lg:gap-16 items-start">
          <!-- Feature 1: Scrollable -->
          <div class="text-center space-y-4">
            <div class="inline-block p-4 bg-gray-100 dark:bg-gray-800 rounded-full shadow">
              <!-- Scroll Icon -->
              <svg class="w-10 h-10 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
            </div>
            <h4 class="text-xl md:text-2xl font-bold font-raleway">Scrollable Menu</h4>
            <p class="text-gray-700 dark:text-gray-300 font-nunito">
              Digital menu is an optimised PDF-file, located on Google Drive for guaranteed access.
            </p>
          </div>
          <!-- Feature 2: PDF Preview -->
          <div class="md:col-span-1 text-center">
             <div class="aspect-w-9 aspect-h-16 border dark:border-gray-700 rounded-lg overflow-hidden shadow-lg">
                <iframe src="https://drive.google.com/file/d/1Bsf52wdVvSJ3Zbjx3bOQsXX-bvphx0y9/preview" class="w-full h-full" title="La Moressa Digital Menu Preview"></iframe>
             </div>
          </div>
           <!-- Feature 3: Allergens & Loading -->
          <div class="text-center space-y-4">
             <div class="inline-block p-4 bg-gray-100 dark:bg-gray-800 rounded-full shadow">
               <!-- Info Icon -->
               <svg class="w-10 h-10 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
             </div>
             <h4 class="text-xl md:text-2xl font-bold font-raleway">Allergens & Fast Loading</h4>
             <p class="text-gray-700 dark:text-gray-300 font-nunito">
               Includes a clear allergen list. The entire menu is only 0.3Mb for quick loading.
             </p>
          </div>
        </section>

        <!-- Section 5: Printable Menu Text -->
        <section class="max-w-3xl mx-auto text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway">
            Printable menu perfectly fits the restaurant's terrace and pizza ordering area
          </h2>
        </section>

        <!-- Section 6: Image Gallery -->
        <section>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
            <NuxtImg src="/images/portfolio/moressa/gallery-1.jpg" alt="Gallery Image 1 - Menu on table" class="rounded-lg shadow-md w-full h-auto object-cover aspect-video sm:aspect-square lg:aspect-video" loading="lazy" format="webp" />
            <NuxtImg src="/images/portfolio/moressa/gallery-2.jpg" alt="Gallery Image 2 - Cocktail menu" class="rounded-lg shadow-md w-full h-auto object-cover aspect-video sm:aspect-square lg:aspect-video" loading="lazy" format="webp" />
            <NuxtImg src="/images/portfolio/moressa/gallery-3.jpg" alt="Gallery Image 3 - Menu detail" class="rounded-lg shadow-md w-full h-auto object-cover aspect-video sm:aspect-square lg:aspect-video" loading="lazy" format="webp" />
            <NuxtImg src="/images/portfolio/moressa/gallery-4.jpg" alt="Gallery Image 4 - Pizza menu" class="rounded-lg shadow-md w-full h-auto object-cover aspect-video sm:aspect-square lg:aspect-video" loading="lazy" format="webp" />
          </div>
        </section>

        <!-- Section 7: QR Code Text -->
        <section class="max-w-3xl mx-auto text-center">
           <h2 class="text-3xl md:text-4xl font-bold mb-4 font-raleway text-gradient-blue-teal">
             On every table, a small square with a QR code connects you directly to the menu
           </h2>
        </section>

        <!-- Section 8: QR Code Image (Parallax Effect) -->
        <section class="relative py-24 md:py-32 lg:py-40 bg-fixed bg-center bg-cover rounded-lg overflow-hidden shadow-xl" style="background-image: url(/images/portfolio/moressa/parallax-bg.jpg);">
           <div class="absolute inset-0 bg-black/40"></div>
           <div class="relative z-10 container mx-auto px-4 flex justify-center md:justify-end">
             <div class="w-3/4 sm:w-1/2 md:w-1/3 lg:w-1/4">
                <NuxtImg
                  src="/images/portfolio/moressa/qr-code.jpg"
                  alt="QR Code for La Moressa Menu"
                  class="rounded-lg shadow-2xl w-full h-auto aspect-square object-cover"
                  sizes="75vw sm:50vw md:33vw lg:25vw"
                  format="webp"
                  loading="lazy"
                />
             </div>
           </div>
        </section>

        <!-- Section 9: Printed Menu Mockups -->
        <section class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12 lg:gap-16 items-center">
           <div class="md:col-span-1">
              <NuxtImg
                src="/images/portfolio/moressa/printed-menu-1.jpg"
                alt="Printed Menu Mockup 1"
                class="rounded-lg shadow-lg w-full h-auto"
                sizes="100vw md:33vw"
                format="webp"
                loading="lazy"
              />
           </div>
           <div class="md:col-span-1 text-center">
              <h2 class="text-2xl md:text-3xl font-bold font-raleway text-gradient-pink-violet">
                This is how the printed menu looks. In reality, it's glossy and laminated.
              </h2>
           </div>
           <div class="md:col-span-1">
              <NuxtImg
                src="/images/portfolio/moressa/printed-menu-2.jpg"
                alt="Printed Menu Mockup 2"
                class="rounded-lg shadow-lg w-full h-auto"
                sizes="100vw md:33vw"
                format="webp"
                loading="lazy"
              />
           </div>
        </section>

      </div> <!-- End space-y -->
    </main> <!-- End container -->

  </div> <!-- End main wrapper -->
</template>

<script setup lang="ts">
import { NuxtImg } from '#components'; // Ensure NuxtImg is imported if not auto-imported

// Define page meta or other setup logic if needed
useHead({
  title: 'La Moressa Menu Design - Portfolio - Cinereo',
  meta: [
    { name: 'description', content: 'Design and photography for the digital and printable menu of La Moressa restaurant on the Amalfi Coast.' }
  ]
})
</script>

<style scoped>
/* Add any component-specific styles here */

/* Gradient Text Styles (similar to caffe-vittoria) */
.text-gradient-blue-teal {
  background: linear-gradient(to right, #0693e3, #7bdcb5); /* Example gradient */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-gradient-pink-violet {
   background: linear-gradient(to right, #f78da7, #9b51e0); /* Example gradient */
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Text Outline Style (similar to caffe-vittoria) */
.text-outline {
  -webkit-text-stroke: 1px #ffffff; /* Adjust color and width */
  text-stroke: 1px #ffffff;
  color: transparent; /* Make the fill transparent */
}
.text-outline em {
   -webkit-text-stroke: 0;
   color: inherit; /* Inherit color from parent or set specific */
   font-style: normal; /* Override italic if needed */
}


/* Basic parallax effect - consider a JS library for smoother results */
.bg-fixed {
  background-attachment: fixed;
}

/* Ensure fonts are loaded globally via nuxt.config or tailwind.config */
/* @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=Raleway:ital,wght@0,400;0,500;0,700;0,800;0,900;1,400&display=swap'); */

/* Font families are expected to be defined in tailwind.config.js */
/*
h1, h2, h3, h4, h5, h6 {
  font-family: 'Raleway', sans-serif;
}
body, p, span, a, div, blockquote {
  font-family: 'Nunito', sans-serif;
}
*/
</style>
<template>
  <div class="text-black dark:bg-gray-900 dark:text-white">

    <!-- No header section as requested, start directly with main content -->

    <main id="content-start">
      <div class="container mx-auto px-4 py-12 md:py-16 lg:py-20 space-y-16 md:space-y-24 lg:space-y-32">

        <!-- Section 1: Intro Text -->
        <section class="flex flex-col md:flex-row gap-8 md:gap-12 lg:gap-16">
          <div class="w-full md:w-1/4 lg:w-1/5 space-y-8">
            <div>
              <h5 class="font-black font-raleway text-lg mb-1 text-gray-600 dark:text-gray-400">Client</h5>
              <a href="https://anna-family.ru/oliver.html" class="text-blue-600 dark:text-blue-400 hover:underline font-nunito">Anna Family Group</a>
            </div>
            <div>
              <h5 class="font-black font-raleway text-lg mb-1 text-gray-600 dark:text-gray-400">Year</h5>
              <p class="font-nunito">2017</p>
            </div>
          </div>
          <div class="w-full md:w-1/4 lg:w-1/5 space-y-8">
             <div>
              <h5 class="font-black font-raleway text-lg mb-1 text-gray-600 dark:text-gray-400">What I did</h5>
              <ul class="list-disc list-inside font-nunito space-y-1">
                <li>Idea</li>
                <li>Mockup</li>
                <li>Preprint</li>
                <li>Translation to English</li>
              </ul>
            </div>
             <div>
              <h5 class="font-black font-raleway text-lg mb-1 text-gray-600 dark:text-gray-400">In my team</h5>
              <ul class="list-disc list-inside font-nunito space-y-1">
                <li>? Alexey Spasski</li>
                <li>✍️ Valeria Titcheva</li>
              </ul>
            </div>
          </div>
          <div class="w-full md:w-1/2 lg:w-3/5 space-y-4">
            <h2 class="text-3xl md:text-4xl lg:text-5xl font-black font-raleway text-gray-800 dark:text-gray-100">
              Elegant menu design with a lot of graphic elements
            </h2>
            <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
              Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place.
            </p>
          </div>
        </section>

        <!-- Section 2: Color & Material -->
        <section class="bg-gray-100 dark:bg-gray-800 py-12 md:py-16 lg:py-20 px-4 md:px-8 lg:px-12 rounded-lg shadow-inner">
          <div class="container mx-auto flex flex-col md:flex-row items-start gap-8 md:gap-12 lg:gap-16">
            <div class="w-full md:w-2/5 space-y-4">
              <h2 class="text-3xl md:text-4xl font-black font-raleway text-gray-800 dark:text-gray-100">
                Color &amp; Material
              </h2>
              <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
                For this hi-end class restaurant in Sochi, Russia I choose light wooden colors with a touch of craft paper. This made a perfect contrast in restaurants ambient made a menu pop-up.
              </p>
            </div>
            <div class="w-full md:w-3/5 grid grid-cols-3 gap-4 md:gap-6">
              <!-- Color Swatch 1 -->
              <div class="bg-[#6e3f23] text-white p-4 md:p-6 rounded-md shadow-md flex flex-col justify-between min-h-[150px] md:min-h-[180px]">
                <h5 class="font-black font-raleway text-lg md:text-xl">Pickled Bean</h5>
                <p class="font-mono text-sm opacity-80">#6e3f23</p>
              </div>
              <!-- Color Swatch 2 -->
              <div class="bg-[#d0cdc4] text-gray-800 p-4 md:p-6 rounded-md shadow-md flex flex-col justify-between min-h-[150px] md:min-h-[180px]">
                <h5 class="font-black font-raleway text-lg md:text-xl">Swirl</h5>
                <p class="font-mono text-sm opacity-80">#d0cdc4</p>
              </div>
              <!-- Color Swatch 3 -->
              <div class="bg-[#634f4b] text-white p-4 md:p-6 rounded-md shadow-md flex flex-col justify-between min-h-[150px] md:min-h-[180px]">
                <h5 class="font-black font-raleway text-lg md:text-xl">Jaded Earth</h5>
                <p class="font-mono text-sm opacity-80">#634f4b</p> <!-- Updated hex from original -->
              </div>
            </div>
          </div>
        </section>

        <!-- Section 3: Parallax Image -->
        <section class="relative h-[40vh] md:h-[50vh] lg:h-[60vh] bg-fixed bg-center bg-cover rounded-lg overflow-hidden shadow-xl" style="background-image: url(/images/portfolio/olivier/menu-olivier-2017-2.jpg);">
           <div class="absolute inset-0 bg-black/30"></div> <!-- Optional overlay -->
        </section>

        <!-- Section 4: Design and Mockup Text -->
        <section class="max-w-3xl mx-auto text-center">
          <h2 class="text-3xl md:text-4xl font-black mb-4 font-raleway text-gray-800 dark:text-gray-100">
            Design and mockup
          </h2>
          <p class="text-lg text-gray-700 dark:text-gray-300 font-nunito">
            It was about 16 versions of the menu till we’ve got to the final one. And only after that we was able to made an English version (main one is in Russian). Also in Russia we make additional 1 page seasonal menu which is slightly different.
          </p>
        </section>

        <!-- Section 6: Image Click-to-Zoom Grid -->
        <section>
           <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">
             <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-1-2.jpg')" class="block group cursor-pointer">
               <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-1-2.jpg" alt="Olivier Menu Mockup 1" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:33vw" />
             </a>
             <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-3.jpg')" class="block group cursor-pointer">
               <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-3.jpg" alt="Olivier Menu Mockup 2" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:33vw" />
             </a>
             <a @click.prevent="toggleZoom('/images/portfolio/olivier/oliver-new-menu-22.jpg')" class="block group cursor-pointer">
               <NuxtImg src="/images/portfolio/olivier/oliver-new-menu-22.jpg" alt="Olivier Menu Mockup 3" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:33vw" />
             </a>
           </div>
        </section>

        <!-- Section 7: Image Click-to-Zoom Grid -->
        <section class="bg-[#444349] py-12 md:py-16 lg:py-20 px-4 md:px-8 lg:px-12 rounded-lg shadow-inner">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
             <a @click.prevent="toggleZoom('/images/portfolio/olivier/olivier-wip-1.jpg')" class="block group cursor-pointer">
               <NuxtImg src="/images/portfolio/olivier/olivier-wip-1.jpg" alt="Olivier Menu Work in Progress 1" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:50vw" />
             </a>
             <a @click.prevent="toggleZoom('/images/portfolio/olivier/types-menu-olivier-2017.jpg')" class="block group cursor-pointer">
               <NuxtImg src="/images/portfolio/olivier/types-menu-olivier-2017.jpg" alt="Olivier Menu Types" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:50vw" />
             </a>
          </div>
        </section>

        <!-- Section 8: Explainer -->
        <section class="flex flex-col md:flex-row items-center gap-8 md:gap-12 lg:gap-16">
          <div class="w-full md:w-1/3 space-y-6">
            <h2 class="text-3xl md:text-4xl font-bold font-raleway text-gray-800 dark:text-gray-100">
              In addition I made a template for the seasonal menu
            </h2>
            <!-- Static representation of toggles -->
            <div class="space-y-4">
              <div>
                <h4 class="font-bold font-raleway text-xl mb-1">Summer 2016</h4>
                <p class="text-gray-700 dark:text-gray-300 font-nunito">Was made several menus for summer 2016 and we’ve choose this colorful one.</p>
              </div>
              <div>
                <h4 class="font-bold font-raleway text-xl mb-1">And then...</h4>
                <p class="text-gray-700 dark:text-gray-300 font-nunito">Using this template restaurant was able to make additional season menus for the rest of the year.</p>
              </div>
            </div>
          </div>
          <div class="w-full md:w-2/3">
            <NuxtImg
              src="/images/portfolio/olivier/summer-menu-2.jpg"
              alt="Olivier Seasonal Summer Menu"
              class="w-full h-auto rounded-lg shadow-xl"
              sizes="100vw md:67vw"
              format="webp"
              loading="lazy"
            />
          </div>
        </section>

      </div> <!-- End space-y container -->
    </main> <!-- End main content area -->

    <!-- Section 5: Full Width Image Grid -->
    <section class="bg-gray-800 dark:bg-black py-12 md:py-16 lg:py-20 shadow-inner">
      <div class="container mx-auto px-4 md:px-8 lg:px-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
        <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-eng-1.jpg')" class="block group cursor-pointer">
          <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-eng-1.jpg" alt="Olivier Menu English Page 1" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw sm:50vw lg:25vw" />
        </a>
        <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-eng-2.jpg')" class="block group cursor-pointer">
          <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-eng-2.jpg" alt="Olivier Menu English Page 2" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw sm:50vw lg:25vw" />
        </a>
        <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-4.jpg')" class="block group cursor-pointer">
          <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-4.jpg" alt="Olivier Menu Russian Page 1" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw sm:50vw lg:25vw" />
        </a>
        <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-5.jpg')" class="block group cursor-pointer">
          <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-5.jpg" alt="Olivier Menu Russian Page 2" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw sm:50vw lg:25vw" />
        </a>
      </div>
    </section>

    <!-- Continue with remaining sections inside a container -->
    <div class="container mx-auto px-4 py-12 md:py-16 lg:py-20 space-y-16 md:space-y-24 lg:space-y-32">
      <!-- Section 6 was here, now moved inside this container -->
      <!-- Section 7 was here, now moved inside this container -->
      <!-- Section 8 was here, now moved inside this container -->
      <section> <!-- Section 6 -->
         <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">
           <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-1-2.jpg')" class="block group cursor-pointer">
             <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-1-2.jpg" alt="Olivier Menu Mockup 1" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:33vw" />
           </a>
           <a @click.prevent="toggleZoom('/images/portfolio/olivier/menu-olivier-2017-3.jpg')" class="block group cursor-pointer">
             <NuxtImg src="/images/portfolio/olivier/menu-olivier-2017-3.jpg" alt="Olivier Menu Mockup 2" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:33vw" />
           </a>
           <a @click.prevent="toggleZoom('/images/portfolio/olivier/oliver-new-menu-22.jpg')" class="block group cursor-pointer">
             <NuxtImg src="/images/portfolio/olivier/oliver-new-menu-22.jpg" alt="Olivier Menu Mockup 3" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:33vw" />
           </a>
         </div>
      </section>
      <section class="bg-[#444349] py-12 md:py-16 lg:py-20 px-4 md:px-8 lg:px-12 rounded-lg shadow-inner"> <!-- Section 7 -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
           <a @click.prevent="toggleZoom('/images/portfolio/olivier/olivier-wip-1.jpg')" class="block group cursor-pointer">
             <NuxtImg src="/images/portfolio/olivier/olivier-wip-1.jpg" alt="Olivier Menu Work in Progress 1" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:50vw" />
           </a>
           <a @click.prevent="toggleZoom('/images/portfolio/olivier/types-menu-olivier-2017.jpg')" class="block group cursor-pointer">
             <NuxtImg src="/images/portfolio/olivier/types-menu-olivier-2017.jpg" alt="Olivier Menu Types" class="rounded-lg shadow-md w-full h-auto object-cover transition-transform duration-300 group-hover:scale-105" loading="lazy" format="webp" sizes="100vw md:50vw" />
           </a>
        </div>
      </section>
      <section class="flex flex-col md:flex-row items-center gap-8 md:gap-12 lg:gap-16"> <!-- Section 8 -->
        <div class="w-full md:w-1/3 space-y-6">
          <h2 class="text-3xl md:text-4xl font-black font-raleway text-gray-800 dark:text-gray-100">
            In addition I made a template for the seasonal menu
          </h2>
          <!-- Static representation of toggles -->
          <div class="space-y-4">
            <div>
              <h4 class="font-black font-raleway text-xl mb-1">Summer 2016</h4>
              <p class="text-gray-700 dark:text-gray-300 font-nunito">Was made several menus for summer 2016 and we’ve choose this colorful one.</p>
            </div>
            <div>
              <h4 class="font-black font-raleway text-xl mb-1">And then...</h4>
              <p class="text-gray-700 dark:text-gray-300 font-nunito">Using this template restaurant was able to make additional season menus for the rest of the year.</p>
            </div>
          </div>
        </div>
        <div class="w-full md:w-2/3">
          <NuxtImg
            src="/images/portfolio/olivier/summer-menu-2.jpg"
            alt="Olivier Seasonal Summer Menu"
            class="w-full h-auto rounded-lg shadow-xl"
            sizes="100vw md:67vw"
            format="webp"
            loading="lazy"
          />
        </div>
      </section>
    </div> <!-- End container for sections 6, 7, 8 -->

    <!-- Zoomed Image Modal with Transition -->
    <Transition name="fade">
      <div v-if="zoomedImageSrc"
           class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4 backdrop-blur-sm"
           @click="toggleZoom(null)">
        <img :src="zoomedImageSrc"
             alt="Zoomed Image"
             class="max-w-[95vw] max-h-[95vh] object-contain rounded-lg shadow-xl cursor-pointer"
             @click.stop /> <!-- Prevent closing when clicking the image itself -->
      </div>
    </Transition>

    <!-- Project Navigation Placeholder - Needs integration with global layout/component -->
    <!-- <div class="bottom_controls"> ... </div> -->

  </div> <!-- End main wrapper -->
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { NuxtImg } from '#components'; // Ensure NuxtImg is imported if not auto-imported

// Define page meta
useHead({
  title: 'Olivier Restaurant Menu Design - Portfolio - Cinereo',
  meta: [
    { name: 'description', content: 'Elegant menu design for Olivier, a gourmet restaurant, featuring multiple versions and seasonal templates.' }
  ]
})

// State for zoomed image
const zoomedImageSrc = ref<string | null>(null);

// Function to toggle zoom state
function toggleZoom(src: string | null) {
  zoomedImageSrc.value = src;
}

// Function to handle keydown events (for Escape key)
function handleKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape' && zoomedImageSrc.value) {
    toggleZoom(null);
  }
}

// Add/remove event listener for Escape key
onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown);
});
</script>

<style scoped>
/* Add any component-specific styles here if needed */

/* Basic parallax effect - consider a JS library for smoother results */
.bg-fixed {
  background-attachment: fixed;
}

/* Ensure fonts are loaded globally via nuxt.config or tailwind.config */

/* Fade transition for the modal */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
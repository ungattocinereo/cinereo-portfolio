<template>
  <div class="bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 min-h-screen">
    <!-- Header/Title Section -->
    <header class="py-16 md:py-24 bg-gray-100 dark:bg-gray-800 text-center"> <!-- Changed background -->
      <div class="container mx-auto px-4">
        <h1 class="text-4xl md:text-5xl font-raleway font-black text-gray-900 dark:text-white mb-4">
          Testing the Waters: My First Voice-Powered Post
        </h1>
        <p class="text-lg md:text-xl text-gray-700 dark:text-gray-300">
          Can I create something beautiful just by speaking? Let's find out.
        </p>
        <div class="flex justify-center space-x-6 mt-8 text-indigo-600 dark:text-indigo-400">
          <Icon name="lucide:qr-code" class="w-16 h-16" />
          <Icon name="lucide:mic" class="w-16 h-16" />
          <Icon name="lucide:laptop" class="w-16 h-16" />
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <article class="container mx-auto px-4 py-12 md:py-20 max-w-3xl">
      <!-- Introduction -->
      <section class="mb-12 md:mb-16">
        <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900 dark:text-white">
          <Icon name="lucide:globe" class="w-7 h-7 mr-3 text-blue-600 dark:text-blue-400" />
          1. Hello World — Let’s Start the Journey
        </h2>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          I hope you can see me. Hi, world! <Icon name="lucide:hand" class="inline-block w-5 h-5 text-yellow-500" />
        </p>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          This is where I begin. A tiny post, created almost for myself — but also for anyone curious enough to scroll this far.
        </p>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          I’m testing whether I can write, design, and publish something meaningful just by speaking. No typing. No clicking through design tools. Just my microphone, my thoughts, and a large language model doing the heavy lifting.
        </p>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
          It’s a strange and exciting new world. I’m stepping into it — one voice command at a time.
        </p>
      </section>

      <hr class="border-gray-200 dark:border-gray-700 my-12 md:my-16">

      <!-- The Experiment -->
      <section class="mb-12 md:mb-16">
        <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900 dark:text-white">
          <Icon name="lucide:beaker" class="w-7 h-7 mr-3 text-purple-600 dark:text-purple-400" />
          2. A Voice, A Code, A QR
        </h2>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-6">
          Three symbols define this experiment:
        </p>
        <ul class="space-y-4 mb-6">
          <li class="flex items-start">
            <Icon name="lucide:qr-code" class="w-6 h-6 mr-3 mt-1 text-indigo-600 dark:text-indigo-400 flex-shrink-0" />
            <div>
              <strong class="font-semibold">QR code</strong> — for linking the real and digital worlds
            </div>
          </li>
          <li class="flex items-start">
            <Icon name="lucide:mic" class="w-6 h-6 mr-3 mt-1 text-red-600 dark:text-red-400 flex-shrink-0" />
            <div>
              <strong class="font-semibold">Voice</strong> — for replacing keyboard and mouse
            </div>
          </li>
          <li class="flex items-start">
            <Icon name="lucide:laptop" class="w-6 h-6 mr-3 mt-1 text-green-600 dark:text-green-400 flex-shrink-0" />
            <div>
              <strong class="font-semibold">Web development</strong> — for building this little corner of the internet
            </div>
          </li>
        </ul>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          This post is also a prompt in disguise — a technical spec, sent to a language model, asking:
        </p>
        <blockquote class="border-l-4 border-indigo-500 dark:border-indigo-400 pl-4 py-2 my-4 italic text-gray-600 dark:text-gray-400">
          Can you take my voice and make it look good?
        </blockquote>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
          Apparently, yes.
        </p>
      </section>

      <hr class="border-gray-200 dark:border-gray-700 my-12 md:my-16">

      <!-- The Plan -->
      <section>
        <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900 dark:text-white">
          <Icon name="lucide:map" class="w-7 h-7 mr-3 text-teal-600 dark:text-teal-400" />
          3. The Plan Is… There Is No Plan
        </h2>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          This isn’t about having a perfect structure or even a clear goal. It’s about seeing what happens when I stop waiting for the right moment and just hit “record.”
        </p>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          Will I build a full blog this way?
          Will anyone read it?
          Will it matter?
        </p>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed mb-4">
          I don’t know yet. But it already feels like a step forward.
        </p>
        <p class="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
          Let’s see where it leads.
        </p>
      </section>
    </article>
  </div>
</template>

<script setup lang="ts">
// Import Lucide icons if using nuxt-icon
// Ensure nuxt-icon is installed and configured

// Set page metadata
useHead({
  title: 'Testing the Waters: My First Voice-Powered Post | Cinereo Blog',
  meta: [
    { name: 'description', content: 'A test blog post created using voice commands and AI assistance.' }
  ]
})

// Import Raleway font if not globally available
// import '@fontsource/raleway/900.css';
</script>

<style scoped>
/* Add Raleway font-family if needed */
.font-raleway {
  font-family: 'Raleway', sans-serif;
}

/* Add any other component-specific styles here if needed */
</style>
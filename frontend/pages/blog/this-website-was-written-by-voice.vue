<template>
  <div class="bg-white dark:bg-gray-900 py-12 sm:py-16">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
      <article class="prose prose-lg dark:prose-invert mx-auto">
        <h1 class="text-4xl font-bold tracking-tight text-gray-900 dark:text-white sm:text-5xl mb-8 text-center">
          This Website Was Written by Voice
        </h1>

        <section class="mb-12">
          <h2 class="flex items-center text-2xl font-semibold text-gray-800 dark:text-gray-200 mb-4">
            <Lightbulb class="w-6 h-6 mr-3 text-indigo-600 dark:text-indigo-400" />
            1. The Idea: Talking My Way Into Web Development
          </h2>
          <p>Hey there! This is the very first post on this site — and it’s a special one. Why? Because this entire website, from concept to code, was built using my voice. Literally.</p>
          <p>A month ago, I jumped into a little experiment. I created a simple book landing page — <a href="http://book.atrani.ru" target="_blank" rel="noopener noreferrer" class="text-indigo-600 dark:text-indigo-400 hover:underline">book.atrani.ru</a> — using Trae, an app released by TikTok. It uses Claude 3.7, a powerful language model, to help you write anything: from essays to software code. This was my first real attempt to see what building something with AI could feel like.</p>
          <p>Before that? I was firmly in the WordPress camp. Even earlier, I used Squarespace. And before that — good old hand-coded HTML. But when I say “before,” I mean ten years ago. Today, I still run several active WordPress projects — you’ll find links to them right on the homepage. They’re solid, they work well. Even the previous version of this very website was built with WordPress and served me faithfully for years.</p>
          <p>But things move forward. I wanted something lighter. Faster. Cleaner. And that’s exactly what I ended up building.</p>
        </section>

        <hr class="my-8 border-gray-300 dark:border-gray-700" />

        <section class="mb-12">
          <h2 class="flex items-center text-2xl font-semibold text-gray-800 dark:text-gray-200 mb-4">
            <Target class="w-6 h-6 mr-3 text-indigo-600 dark:text-indigo-400" />
            2. The Challenge: Building Without Design Tools
          </h2>
          <p>Here’s the twist: I challenged myself to build this entire site without using any design tools.</p>
          <p>Now, that might sound odd, considering I’m a designer by trade. I always have Figma, Photoshop, Illustrator open. But this time, I wanted to try something different. I wanted to see: can I describe my vision of beauty and function to an AI — and have it understand me?</p>
          <p>Could I “talk” a website into existence?</p>
          <p>Turns out… I could.</p>
          <p>It was such an interesting mental exercise — to shape something visual through words. To give instructions not with sketches or mockups, but with voice and text prompts. In just about a week, the entire site came to life — or at least the version you’re seeing right now (as of April 4, 2025).</p>
        </section>

        <hr class="my-8 border-gray-300 dark:border-gray-700" />

        <section class="mb-12">
          <h2 class="flex items-center text-2xl font-semibold text-gray-800 dark:text-gray-200 mb-4">
            <Calendar class="w-6 h-6 mr-3 text-indigo-600 dark:text-indigo-400" />
            3. The Present: Before the Tourist Season Hits
          </h2>
          <p>We’re just a few weeks away from the start of tourist season, and since I spend 90% of my time managing my guesthouse during summer, I won’t be able to focus on this site much then. But for now, while there’s still a bit of breathing room, I’m pushing to finish and publish it fully.</p>
          <p>This blog post? Also dictated. Just like the rest of the site. It’s fast, it’s natural, it feels more alive. Until now, I’ve been doing all my journaling in Obsidian using voice. This is the first time I’m sharing that process publicly.</p>
          <p>Honestly, I don’t expect many people to read this — maybe just a few friends. Most of my Instagram followers speak Russian. Others, Italian. A few people understand English. But in the end, none of that really matters.</p>
          <p>This is my first voice-written post on this site.<br>
          Thanks for stopping by.<br>
          Let’s get in touch. 😊</p>
        </section>
      </article>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Lightbulb, Target, Calendar } from 'lucide-vue-next';

// Optional: Define meta tags for SEO
useHead({
  title: 'This Website Was Written by Voice - Cinereo',
  meta: [
    { name: 'description', content: 'Discover how this website was built entirely using voice commands and AI, a journey from WordPress to a modern, lightweight solution.' }
  ]
})
</script>

<style scoped>
/* Add any component-specific styles here if needed */
.prose p {
  margin-bottom: 1.25em; /* Adjust paragraph spacing */
}
</style>
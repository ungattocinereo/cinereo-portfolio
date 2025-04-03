<template>
  <div>
    <ProjectTemplateSecondary v-if="projectData" v-bind="projectData" />
    <div v-else class="container mx-auto px-4 py-16 text-center">
      <p>Loading project data or project not found...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import ProjectTemplateSecondary from '~/components/ProjectTemplateSecondary.vue';

const route = useRoute();
const projectData = ref(null);

// Placeholder function to simulate fetching data based on slug
const fetchProjectData = async (slug) => {
  console.log(`Fetching data for slug: ${slug}`);
  // In a real app, replace this with an API call or CMS query
  // Example: const data = await $fetch(`/api/projects/${slug}`);
  // For now, return placeholder data based on a dummy slug check
  if (slug === 'georgian-restaurant') {
    return {
      // Using default placeholders defined in the component for now
      title: 'Georgian Restaurant',
      subtitle: 'I made a menu, design of it, photos and mock-up for one of the most famous Georgian restaurants in the town of Sochi in Russia.',
      date: '2024',
      // heroImage: '/images/portfolio/georgian-restaurant/hero.jpg', // Use default
      client: 'Georgian Taste Restaurant',
      year: '2024',
      services: ['Menu Design', 'Photography', 'Mockup Creation', 'Prepress'],
      descriptionTitle: 'Crafting the Culinary Experience',
      descriptionText: 'The goal was to create a visually appealing menu that reflects the authentic Georgian cuisine and atmosphere of the restaurant. High-quality photography and elegant typography were key elements.',
      // fullscreenImage: '/images/portfolio/georgian-restaurant/fullscreen.jpg', // Use default
      galleryLabelTitle: 'Menu & Mockups',
      galleryLabelSubtitle: 'A closer look at the design details.',
      // galleryImages: [ // Use default
      //   { src: '/images/portfolio/georgian-restaurant/gallery-1.jpg', alt: 'Menu Spread' },
      //   { src: '/images/portfolio/georgian-restaurant/gallery-2.jpg', alt: 'Menu Detail' },
      //   { src: '/images/portfolio/georgian-restaurant/gallery-3.jpg', alt: 'Restaurant Mockup' },
      //   { src: '/images/portfolio/georgian-restaurant/gallery-4.jpg', alt: 'Photo Detail' }
      // ],
      // additionalImages: [ // Use default
      //   { src: '/images/portfolio/georgian-restaurant/additional-1.jpg', alt: 'Additional Mockup 1' },
      //   { src: '/images/portfolio/georgian-restaurant/additional-2.jpg', alt: 'Additional Mockup 2' }
      // ]
    };
  } else {
      // Return default/fallback data or null if project not found
       return {
        title: 'Sample Project',
        subtitle: 'This is a sample project description.',
        date: '2025',
        heroImage: '/placeholder-hero.jpg',
        client: 'Sample Client',
        year: '2025',
        services: ['Web Design', 'Development'],
        descriptionTitle: 'About This Sample',
        descriptionText: 'This page uses the secondary project template.',
        fullscreenImage: '/placeholder-fullscreen.jpg',
        galleryLabelTitle: 'Gallery',
        galleryImages: [ { src: '/placeholder-gallery-1.jpg' }, { src: '/placeholder-gallery-2.jpg' } ],
        additionalImages: [ { src: '/placeholder-additional-1.jpg' } ]
      };
  }
};

onMounted(async () => {
  const slug = route.params.slug;
  if (slug) {
    projectData.value = await fetchProjectData(slug);
  }
});
</script>

<style scoped>
/* Add any page-specific styles if needed */
</style>
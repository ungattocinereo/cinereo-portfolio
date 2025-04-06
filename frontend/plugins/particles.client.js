// This plugin initializes tsParticles on the client side
import { loadFull } from "tsparticles";

export default defineNuxtPlugin(async (nuxtApp) => {
  // Only run on client side
  if (process.client) {
    try {
      // Dynamically import the engine
      const { tsParticles } = await import("@tsparticles/engine");
      
      // Initialize the engine
      await loadFull(tsParticles);
      
      // Make tsParticles available globally
      nuxtApp.provide('tsParticles', tsParticles);
      
      console.log("tsParticles initialized successfully in plugin");
    } catch (error) {
      console.error("Failed to initialize tsParticles in plugin:", error);
    }
  }
});
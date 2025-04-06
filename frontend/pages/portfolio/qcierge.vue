<template>
  <div class="bg-white text-gray-800">
    <!-- Hero Section -->
    <section class="relative py-16 md:py-24 bg-gradient-to-br from-[#1436f5] to-[#3352eb] text-white overflow-hidden">
      <div class="container mx-auto px-4 z-10 relative">
        <div class="max-w-3xl mx-auto text-center text-white">
          <h1 class="text-4xl md:text-5xl font-raleway font-black mb-4">
            QCierge: QR Concierge
          </h1>
          <p class="text-lg md:text-xl text-indigo-100 mb-8">
            A Simpler, Frictionless Way to Request Help in Hospitality.
          </p>
          <img src="/images/mockup-qrcierge.jpg" alt="QCierge Mockup" class="rounded-lg shadow-xl mx-auto max-w-full md:max-w-2xl">
        </div>
      </div>
      <!-- Background shapes (Adjusted for new gradient) -->
      <div class="absolute top-0 left-0 w-64 h-64 bg-blue-400 rounded-full opacity-20 -translate-x-16 -translate-y-16"></div>
      <div class="absolute bottom-0 right-0 w-80 h-80 bg-indigo-400 rounded-full opacity-20 translate-x-20 translate-y-20"></div>
    </section>

    <!-- Main Content -->
    <div class="container mx-auto px-4 py-12 md:py-20">
      <div class="max-w-4xl mx-auto">

        <!-- Overview -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:info" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Overview
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed mb-4">
            Have you ever felt uncomfortable asking hotel staff for extra towels or reporting an untidy shared kitchen? Today, many of us strive to remain polite and unobtrusive, sometimes at the expense of our comfort. QCierge (short for QR Concierge) removes the friction from such interactions.
          </p>
          <p class="text-lg text-gray-700 leading-relaxed mb-4">
            By simply scanning a QR code and tapping a button, guests can send quick, anonymous requests to the hotel’s administrative team. No additional apps required. No awkward face-to-face conversations.
          </p>
          <p class="text-lg text-gray-700 leading-relaxed">
            This concept was envisioned by me (the idea/vision) and brilliantly executed in collaboration with programmer Kirill Kazakov. We combined minimalistic design principles with instant QR code technology to create an easy-to-use mini web app that is already in beta testing at <a href="http://qr.amalfi.day" target="_blank" class="text-blue-600 hover:underline">qr.amalfi.day</a>.
          </p>
        </section>

        <!-- The Core Idea -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:lightbulb" class="w-7 h-7 mr-3 text-[#1436f5]" />
            The Core Idea
          </h2>
          <ul class="space-y-4">
            <li class="flex items-start">
              <Icon name="lucide:user-check" class="w-6 h-6 mr-3 mt-1 text-green-600 flex-shrink-0" />
              <div>
                <h3 class="font-semibold text-lg">Guest Anonymity</h3>
                <p class="text-gray-700">People often feel shy about directly asking for extra services or reporting minor problems. QCierge addresses this by providing a one-tap, no-hassle method.</p>
              </div>
            </li>
            <li class="flex items-start">
              <Icon name="lucide:bell-ring" class="w-6 h-6 mr-3 mt-1 text-red-600 flex-shrink-0" />
              <div>
                <h3 class="font-semibold text-lg">Immediate Assistance</h3>
                <p class="text-gray-700">Once a request is made, hotel administrators see it instantly in their group chat. They can respond in person or fulfill the request behind the scenes.</p>
              </div>
            </li>
            <li class="flex items-start">
              <Icon name="lucide:gift" class="w-6 h-6 mr-3 mt-1 text-purple-600 flex-shrink-0" />
              <div>
                <h3 class="font-semibold text-lg">Reward Through Gratitude</h3>
                <p class="text-gray-700">With a nod to gamification, each request is met with a simple but heartfelt “Thank You” message. It’s a small reward for helping the hotel maintain high standards.</p>
              </div>
            </li>
          </ul>
        </section>

        <!-- How It Works -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:workflow" class="w-7 h-7 mr-3 text-[#1436f5]" />
            How It Works
          </h2>
          <ol class="space-y-6">
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:qr-code" class="w-5 h-5 mr-2 text-gray-600" />
                1. Scanning the Code
              </h3>
              <p class="text-gray-700 ml-7">Each room, suite, or common area (kitchen, bathroom) has a printed, laminated QR code. A quick scan with any smartphone camera launches the QCierge web interface—no downloads or installation required.</p>
            </li>
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:mouse-pointer-click" class="w-5 h-5 mr-2 text-gray-600" />
                2. Choosing a Request
              </h3>
              <p class="text-gray-700 ml-7 mb-2">Guests see concise options like “Change our shower towels,” “Please clean the room,” or even “Problem with the cat.”</p>
              <p class="text-gray-700 ml-7">One tap is all it takes. The guest immediately sees a friendly “Thank You” page, confirming their request was received.</p>
            </li>
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:send" class="w-5 h-5 mr-2 text-gray-600" />
                3. Instant Notifications to Staff
              </h3>
              <p class="text-gray-700 ml-7 mb-2">Behind the scenes, the hotel’s staff or administration gets a real-time message in their dedicated group chat. The notification indicates which room or area submitted the request and what service is needed.</p>
              <p class="text-gray-700 ml-7">There is currently no direct chat reply to the guest. For most small hotels, it’s enough that staff are on-site and can quickly address the request.</p>
            </li>
          </ol>
        </section>

        <!-- Philosophy & Gamification -->
        <section class="mb-12 md:mb-16 p-6 bg-blue-50 rounded-lg border border-blue-200">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:gamepad-2" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Philosophy & Gamification
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed mb-4">
            My personal vision is to turn everyday tasks into a game—a concept I call the gamification of life. By designing an interface so simple that a guest only has to tap a button for a big “thank you,” we make them feel good about contributing to the hotel’s upkeep.
          </p>
          <p class="text-lg text-gray-700 leading-relaxed">
            In essence, QCierge stands for two core ideas:
          </p>
          <ul class="list-disc list-inside mt-4 space-y-2 text-lg text-gray-700">
            <li>Lowering the friction between guests and service staff so that no one feels uncomfortable.</li>
            <li>Rewarding participation—guests get that instant sense of satisfaction for taking a brief moment to help the hotel stay in tip-top shape.</li>
          </ul>
        </section>

        <!-- Technical Highlights -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:code-2" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Technical Highlights
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed mb-4">
            Although the original idea was mine, Kirill Kazakov made key decisions on how to implement the system most effectively. Here’s a quick breakdown of the technology stack and setup:
          </p>
          <ul class="space-y-3 list-disc list-inside text-lg text-gray-700">
            <li><strong>Mini Web App:</strong> A lightweight, fast-loading site that behaves like an app in a mobile browser.</li>
            <li><strong>QR Codes:</strong> Automatically generated short links for each apartment, kitchen, or bathroom. Hotel owners can print and laminate them at home without extra cost.</li>
            <li><strong>Instant Alerts:</strong> Requests get pushed to a group chat in real time, ensuring immediate visibility for staff.</li>
            <li><strong>No Additional Downloads:</strong> Because it’s a web-based solution, guests don’t have to install anything—scan, tap, done.</li>
          </ul>
        </section>

        <!-- Setting It Up -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:settings" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Setting It Up for Your Property
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed mb-6">
            One of the main strengths of QCierge is its simplicity for hoteliers. After signing up or contacting us for setup:
          </p>
          <ol class="space-y-6">
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:link" class="w-5 h-5 mr-2 text-gray-600" />
                1. Get Your Short Links
              </h3>
              <p class="text-gray-700 ml-7 mb-1">Each room or apartment receives a unique short link (for example, qr.amalfi.day/r101 for Room 101).</p>
              <p class="text-gray-700 ml-7">Common areas (kitchens, bathrooms) get their own dedicated links too.</p>
            </li>
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:printer" class="w-5 h-5 mr-2 text-gray-600" />
                2. Print the QR Codes
              </h3>
              <p class="text-gray-700 ml-7 mb-1">We provide ready-to-print QR codes that correspond to each link.</p>
              <p class="text-gray-700 ml-7">You can print them on regular paper, laminate them, or even put them in stylish frames—whatever fits your décor.</p>
            </li>
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:map-pin" class="w-5 h-5 mr-2 text-gray-600" />
                3. Place Them Anywhere
              </h3>
              <p class="text-gray-700 ml-7 mb-1">Stick them on fridges, bathroom mirrors, bedside tables, or doors.</p>
              <p class="text-gray-700 ml-7 mb-1">You can create small, discreet labels for more private areas.</p>
              <p class="text-gray-700 ml-7">No special hardware needed—just a printer and perhaps some lamination.</p>
            </li>
            <li>
              <h3 class="font-semibold text-lg mb-2 flex items-center">
                <Icon name="lucide:message-square" class="w-5 h-5 mr-2 text-gray-600" />
                4. Receive Requests in Your Chat
              </h3>
              <p class="text-gray-700 ml-7 mb-1">Add the relevant staff (front desk, housekeepers, or anyone else) to a group chat or Telegram channel (or whichever messaging system you prefer).</p>
              <p class="text-gray-700 ml-7">Once a QR code is scanned and a service is requested, the entire group instantly sees the request.</p>
            </li>
          </ol>
        </section>

        <!-- Why QCierge Matters -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:thumbs-up" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Why QCierge Matters
          </h2>
          <ul class="space-y-3 list-disc list-inside text-lg text-gray-700">
            <li><strong>A Better Guest Experience:</strong> By reducing barriers to communication, QCierge ensures that issues are tackled quickly.</li>
            <li><strong>Anonymous Feedback:</strong> Guests can highlight problems like an unclean kitchen or malfunctioning amenities without feeling judged.</li>
            <li><strong>Operational Efficiency:</strong> Staff can coordinate and respond in real time, boosting overall service speed.</li>
            <li><strong>Scalable & Low-Cost:</strong> The setup is straightforward and can be rolled out to multiple properties or across multiple rooms with minimal overhead.</li>
          </ul>
        </section>

        <!-- Where We Are Now -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:activity" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Where We Are Now
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed">
            Currently, QCierge is in a beta state at <a href="http://qr.amalfi.day" target="_blank" class="text-blue-600 hover:underline">qr.amalfi.day</a>. Despite its simplicity, it has already proven effective in small-scale trials. Guests appreciate the freedom of making requests from their phone, while owners see how easy it is to stay on top of guest needs.
          </p>
        </section>

        <!-- Future Plans -->
        <section class="mb-12 md:mb-16">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:rocket" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Future Plans
          </h2>
          <ul class="space-y-3 list-disc list-inside text-lg text-gray-700">
            <li><strong>Enhanced Customization:</strong> Adding more request types, custom icons, and multi-language support.</li>
            <li><strong>Optional Guest Feedback Loop:</strong> While many hotels prefer a no-reply approach, we’re considering an opt-in direct message feature for more detailed conversations.</li>
            <li><strong>Gamification Extensions:</strong> Perhaps awarding virtual badges or loyalty points for guests who regularly help maintain shared spaces.</li>
            <li><strong>Integration with Other Systems:</strong> Connecting QCierge to property management systems (PMS) for advanced scheduling and housekeeping integration.</li>
          </ul>
        </section>

        <!-- Get Involved -->
        <section class="mb-12 md:mb-16 p-6 bg-blue-50 rounded-lg border border-blue-200">
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:users" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Get Involved or Try It Yourself
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed mb-4">
            If you’re a hotel owner, a B&amp;B manager, or simply someone curious about frictionless guest-staff communication, QCierge offers a fresh take on an old challenge. Its minimalistic design and quick setup make it an ideal fit for small properties seeking modern guest interaction tools.
          </p>
          <ul class="space-y-3 list-disc list-inside text-lg text-gray-700">
            <li><strong>Contact for Setup:</strong> Reach out via our site at <a href="http://qr.amalfi.day" target="_blank" class="text-blue-600 hover:underline">qr.amalfi.day</a></li>
            <li><strong>Contribute Ideas:</strong> We’re always open to suggestions for improvements or additional features.</li>
            <li><strong>Join Our Beta:</strong> If you want to run a pilot test at your property, let us know!</li>
          </ul>
        </section>

        <!-- Conclusion -->
        <section>
          <h2 class="text-3xl font-raleway font-black mb-6 flex items-center text-gray-900">
            <Icon name="lucide:sparkles" class="w-7 h-7 mr-3 text-[#1436f5]" />
            Conclusion
          </h2>
          <p class="text-lg text-gray-700 leading-relaxed">
            QCierge—created through a partnership of my conceptual vision and Kirill Kazakov’s development expertise—is a simple yet powerful solution that revolutionizes how guests and staff communicate in hospitality settings. By combining instant QR scanning with minimal user inputs, we’ve crafted an environment where everyone feels comfortable asking for help, making each stay more enjoyable. And that, in essence, is the heart of QCierge: fostering smoother interactions, happier guests, and a more efficient service staff—one QR code at a time.
          </p>
        </section>

      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Assuming Nuxt Icon is installed and configured
// If not, you might need to install it (`npm install nuxt-icon`) and add it to modules in nuxt.config.ts
// Or import icons manually as SVG components

// Import Raleway font if not globally available
// You might need to add this to your main CSS or Nuxt config
// import '@fontsource/raleway/900.css';

// Set page metadata
useHead({
  title: 'QCierge - Portfolio | Cinereo',
  meta: [
    { name: 'description', content: 'Portfolio page detailing the QCierge project - a simple QR code based concierge system for hospitality.' }
  ]
})
</script>

<style scoped>
/* Add Raleway font-family if needed */
.font-raleway {
  font-family: 'Raleway', sans-serif;
}

/* Add any other component-specific styles here if needed */
</style>
<template>
  <div>
    <welcome />

    <recent-projects v-if="false" />

    <services v-if="false" />

    <about-me v-if="false" />

    <get-in-touch v-if="false" />
  </div>
</template>

<script>
  export default {
    name: 'CoreView',

    components: {
      AboutMe: () => import('@/components/AboutMe'),
      GetInTouch: () => import('@/components/GetInTouch'),
      RecentProjects: () => import('@/components/RecentProjects'),
      Services: () => import('@/components/Services'),
      Welcome: () => import('@/components/Welcome'),
    },
  }
</script>

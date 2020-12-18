<template>
  <v-app-bar
    v-scroll="onScroll"
    :color="!isScrolling ? 'transparent' : 'white'"
    fixed
    flat
  >
    <v-slide-x-transition>
      <v-img
        v-if="showLogo"
        :src="require('@/assets/logo.png')"
        class="shrink"
        contain
        height="50"
      />
    </v-slide-x-transition>

    <v-spacer />

    <v-btn
      v-if="
        $route.name != 'Home' &&
        $route.name != 'Auth' &&
        $route.name != 'About' &&
        $route.name != 'RegisterStudent' &&
        $route.name != 'RegisterOrganizator' &&
        $route.name != 'RegisterTeacher'
      "
      color="primary"
      :to="{
        name: 'Home'
      }"
    >
      Выход
    </v-btn>
    <social-media />
  </v-app-bar>
</template>

<script>
  export default {
    name: 'CoreAppBar',

    components: {
      SocialMedia: () => import('@/components/SocialMedia'),
    },

    data: () => ({
      showLogo: false,
      isScrolling: false,
    }),

    methods: {
      onScroll () {
        const offset = window.pageYOffset
        this.isScrolling = offset > 50
        this.showLogo = offset > 200
      },
    },
  }
</script>

<template>
  <v-app>
    <!-- <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar> -->
    <core-app-bar />

    <v-main class="main-app">
      <!-- <core-view /> -->
      <router-view></router-view>
    </v-main>

    <core-footer />

    <!-- <v-main>
      <HelloWorld/>
    </v-main> -->
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',

  components: {
    CoreAppBar: () => import('@/components/core/AppBar'),
    CoreFooter: () => import('@/components/core/Footer'),
  },

  beforeCreate: function() {
    console.log(this.$hostname)
  },

  data: () => ({
    //
  })
}
</script>

<style lang="scss">
  .main-app {
    min-height: 90vh;
  }

  .container-flex {
    display: flex;
    flex-direction: column;
    justify-content: center;
    // align-items: center;
    height: 100%;

    &__content {
      margin: auto;
    }
  }
</style>

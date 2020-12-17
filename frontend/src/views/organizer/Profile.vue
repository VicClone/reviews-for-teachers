<template>
  <v-container class="container-flex">
    <section v-if="organizer || organizerFetch">
      <v-row justify="center">
        <v-col md="6">
          <v-card
            class="mx-auto"
            max-width="600"
            tile
          >
            <v-img
              height="100%"
              src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
            >
              <v-row
                align="end"
                class="fill-height"
              >
                <v-col
                  align-self="start"
                  class="pa-0"
                  cols="12"
                >
                  <v-avatar
                    class="profile"
                    color="grey"
                    size="164"
                  >
                    <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
                  </v-avatar>
                </v-col>
                <v-col class="py-0">
                  <v-list-item
                    color="rgba(0, 0, 0, .4)"
                    dark
                  >
                    <v-list-item-content>
                      <v-list-item-title class="title">
                        {{ organizer.name }}
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        {{ organizer.email }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-col>
              </v-row>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify-center>
        <v-col md6 class="btns">
          <v-btn
            class="btns__btn"
            :to="{
              name: 'ReviewsOrganizer',
              params: {
                id: organizer.id
              }
            }"
          >
            Посмотреть отзывы
          </v-btn>
          <v-btn class="btns__btn">
            Рейтинг преподавателей
          </v-btn>
          <v-btn
            class="btns__btn"
            :to="{
              name: 'List'
            }"
          >
            Списки
          </v-btn>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>


<style lang="scss">
  .btns {
    display: flex;
    justify-content: center;

    &__btn {
      margin: 0 20px;
    }
  }
</style>

<script>
export default {
  data: () => ({
    organizer: null,
  }),
  computed: {
    organizerFetch() {
      this.getOrganizer()
    }
  },
  methods: {
    getOrganizer() {
      fetch(`${this.$hostname}/api/v1/organizers/?id=${this.$route.params.id}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.organizer = data[0]
        });
    },

    sendForm() {
      if (this.form.name && this.form.email && this.form.password) {
        console.log(this.form);
        fetch(`${this.$hostname}/api/v1/organizer/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify(this.form)
        })
        .then(resolve => {
          console.log('form send');
        })
        .catch(error => {
          console.error(error)
        })
      }
    }
  }

}
</script>

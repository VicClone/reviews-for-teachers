<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="6">
          {{ studentFetch }}
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
                        Иван Иванов
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        Курсы по маркетингу
                      </v-list-item-subtitle>
                      <v-list-item-subtitle>
                        ivan@mail.com
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
              name: 'ReviewsTeacher'
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
    student: null,
  }),
  computed: {
    studentFetch() {
      this.getStudent()
    },
  },
  methods: {
    getStudent() {
      fetch(`${this.$hostname}/api/v1/student/?id=${this.$route.params.id}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.teachers = data;
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

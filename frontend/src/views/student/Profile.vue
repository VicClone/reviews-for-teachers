<template>
  <v-container class="container-flex">
    <section v-if="student || studentFetch">
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
                        {{ student.name }}
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        {{ student.group.organizer.name }}
                      </v-list-item-subtitle>
                      <v-list-item-subtitle>
                        {{ student.group.name }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-col>
              </v-row>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col md="6">
          <v-data-table
              v-if="(answers || answersFetch) && (reviews || reviewsFetch)"
              :headers="headers"
              :items="reviews"
              :search="search"
            >
              <template v-slot:item.actions="{ item }">
                <v-btn
                  depressed
                  small
                  :to="{
                    name: 'ReviewStudent',
                    params: {
                      id: student.id
                    },
                    query: {
                      review: item.id
                    }
                  }"
                >
                  Открыть
                </v-btn>
              </template>
            </v-data-table>
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
    search: '',
    answers: null,
    headers: [
      {
        text: 'Дата старта',
        align: 'start',
        sortable: false,
        value: 'dateStart',
      },
      {
        text: 'Дата окончания',
        align: 'start',
        sortable: false,
        value: 'dateEnd',
      },
      { text: 'Предмет', value: 'subject.name' },
      { text: 'Преподаватель', value: 'teacher.name' },
      { text: 'Открыть', value: 'actions', sortable: false },
    ],
    reviews: null,
  }),

  computed: {
    studentFetch() {
      this.getStudent()
    },
    reviewsFetch() {
      this.getReviews(this.student.group.id)
    },
    answersFetch() {
      this.getAnswers(this.student.id)
    },
  },

  methods: {
    getStudent() {
      fetch(`${this.$hostname}/api/v1/students/${this.$route.params.id}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.student = data
        });
    },

    getReviews(groupId) {
      fetch(`${this.$hostname}/api/v1/reviews/?group=${groupId}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.reviews = data.filter(item => this.checkAnswers(item, this.answers));
          // this.reviews = data;
        });
    },

    getAnswers(studentId) {
      console.log('asdfasdf')
      fetch(`${this.$hostname}/api/v1/answers/?student=${studentId}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.answers = data;
        });
    },

    checkAnswers(review, answers) {
      for (const answer of answers) {
        console.log(answer.review, review.id)

        if (answer.review === review.id) {
          return false
        }
      }

      return true
    }
  }
}
</script>

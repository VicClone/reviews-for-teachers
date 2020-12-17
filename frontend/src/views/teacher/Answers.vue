<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="8">
          <v-card>
            <v-card-title>
              Отзывы
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
              v-if="answers.length || answersFetch"
              :headers="headers"
              :items="answers"
              :search="search"
            >
              <template v-slot:item.actions="{ item }">
                <v-btn
                  depressed
                  small
                  :to="{
                    name: 'ReviewTeacher'
                  }"
                >
                  Открыть
                </v-btn>
              </template>
            </v-data-table>
          </v-card>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Дата',
            align: 'start',
            sortable: false,
            value: 'date',
          },
          { text: 'Имя', value: 'name' },
          { text: 'Оценка', value: 'rating' },
          { text: 'Предмет', value: 'subject' },
          { text: 'Преподаватель', value: 'teacher' },
          { text: 'Открыть', value: 'actions', sortable: false },
        ],

        answers: [],
      }
    },

    computed: {
      answersFetch() {
        this.getAnswers()
      },

      reviewsFetch() {
        this.getReviews()
      },
    },

    methods: {
      getReviews() {
        fetch(`${this.$hostname}/api/v1/reviews/?teacher=${this.$route}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            console.log(data)
            this.teacher = data;
          });
      },

      getAnswers() {
        fetch(`${this.$hostname}/api/v1/answers/`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            const allAnswers = data;
            const answerForTeacher = data.filter(item => item.review.teacher.id == this.$route.params.id)
            console.log(answerForTeacher);

            for (const answer of answerForTeacher) {
              this.answers.push(
                {
                  date: answer.date,
                  name: answer.student.name,
                  rating: answer.rating,
                  subject: answer.review.subject.name,
                  teacher: answer.review.teacher.name,
                }
              )
            }
          });
      }
    }

  }
</script>

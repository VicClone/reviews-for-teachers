<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="8">
          <v-card>
            <v-card-title>
              Ответы
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
                    name: 'AnswerDetail',
                    params: {
                      id: item.id
                    }
                  }"
                >
                  Открыть
                </v-btn>
              </template>
            </v-data-table>

            <v-card-actions class="pb-5">
              <v-btn
                color="primary"
                class="ma-auto"
                :to="{
                  name: 'ReviewDetail',
                  params: {
                    id: $route.params.id
                  }
                }"
              >
                Посмотреть отзыв
              </v-btn>
            </v-card-actions>
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
    },

    methods: {
      getAnswers() {
        fetch(`${this.$hostname}/api/v1/answers/?review=${this.$route.params.id}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            const allAnswers = data;

            for (const answer of allAnswers) {
              this.answers.push(
                {
                  id: answer.id,
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

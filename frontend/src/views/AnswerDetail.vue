<template>
  <v-container class="container-flex">
    <section v-if="answer || answerFetch">
      <v-row justify="center">
        <v-col md="5">
          <v-form>
            <v-card>
              <v-card-text>
                <v-card-title>
                  {{ answer.student.name }}
                </v-card-title>
                <div class="d-flex justify-space-between align-center">
                  <p class="ma-0">
                    Доступность и понятность изложения материала
                  </p>
                  <v-rating
                    color="warning"
                    hover
                    length="5"
                    size="35"
                    :value="answer.availability"
                    readonly
                  ></v-rating>
                </div>
                <div class="d-flex justify-space-between align-center">
                  <p class="ma-0">
                    Увлекательность изложения материала
                  </p>
                  <v-rating
                    color="warning"
                    hover
                    length="5"
                    size="35"
                    :value="answer.fascination"
                    readonly
                  ></v-rating>
                </div>
                <div class="d-flex justify-space-between align-center">
                  <p class="ma-0">
                    Сложность изученного материала
                  </p>
                  <v-rating
                    color="warning"
                    hover
                    length="5"
                    size="35"
                    :value="answer.сomplexity"
                    readonly
                  ></v-rating>
                </div>
                <div class="d-flex justify-space-between align-center">
                  <p class="ma-0">
                    Новизна изученного материала
                  </p>
                  <v-rating
                    color="warning"
                    hover
                    length="5"
                    size="35"
                    :value="answer.novelty"
                    readonly
                  ></v-rating>
                </div>
                <div class="d-flex justify-space-between align-center">
                  <p class="ma-0">
                    Заинтересованность предметом
                  </p>
                  <v-rating
                    color="warning"
                    hover
                    length="5"
                    size="35"
                    :value="answer.interest"
                    readonly
                  ></v-rating>
                </div>
                <v-textarea
                  outlined
                  name="input-7-4"
                  label="Отзыв"
                  class="mt-5"
                  :value="answer.text"
                  readonly
                ></v-textarea>
                <div class="d-flex justify-space-between align-center">
                  <h3 class="ma-0">
                    Итоговая оценка
                  </h3>
                  <v-rating
                    color="warning"
                    hover
                    length="5"
                    size="35"
                    :value="answer.rating"
                    readonly
                  ></v-rating>
                </div>
                <div class="d-flex flex-column align-end">
                  Дата отзыва: <time>{{answer.date}}</time>
                </div>
              </v-card-text>

              <v-card-actions class="pb-5">
              <v-btn
                color="primary"
                class="ma-auto"
                :to="{
                  name: 'ReviewAnswers',
                  params: {
                    id: answer.review.id
                  }
                }"
              >
                Все ответы
              </v-btn>
            </v-card-actions>
            </v-card>
          </v-form>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    answer: null,
    formReview: {
      date: '',
      availability: 0,
      fascination: 0,
      сomplexity: 0,
      novelty: 0,
      interest: 0,
      text: '',
      rating: 0,
      review: 0,
      student: 0,
    }
  }),

  computed: {
      answerFetch() {
        this.getAnswer()
      },
    },

  methods: {
    getAnswer() {
      fetch(`${this.$hostname}/api/v1/answers/?id=${this.$route.params.id}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.answer = data[0]
        })
    }
  }

}
</script>

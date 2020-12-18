<template>
  <v-container class="container-flex">
    <section v-if="review || reviewFetch">
      <v-row justify="center">
        <v-col md="6">
          <v-card class="mt-5 pa-5">
            <v-card-title>
              {{ review.name }}
            </v-card-title>
            <v-card-subtitle>
              <p>
                Дата начала опроса: <b>{{ review.dateStart }}</b>
              </p>
              <p>
                Дата конца опроса: <b>{{ review.dateEnd }}</b>
              </p>
              <p>
                Группа: <b>{{ review.group.name }}</b>
              </p>
              <p>
                Предмет: <b>{{ review.subject.name }}</b>
              </p>
              <p>
                Преподаватель: <b>{{ review.teacher.name }}</b>
              </p>
            </v-card-subtitle>
            <v-card-text v-if="answers.length || answersFetch">
              <p>
                Количество ответов: <b>{{ answers.length }}</b>
              </p>
              <br>
              <h3>Средние оценки</h3>
              <div class="d-flex justify-space-between align-center">
                <p class="ma-0">
                  Доступность и понятность изложения материала
                </p>
                <v-rating
                  color="warning"
                  hover
                  length="5"
                  size="35"
                  :value="averageRating.availability"
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
                  :value="averageRating.fascination"
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
                  :value="averageRating.сomplexity"
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
                  :value="averageRating.novelty"
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
                  :value="averageRating.interest"
                  readonly
                ></v-rating>
              </div>
              <div class="d-flex justify-space-between align-center">
                <h3 class="ma-0">
                  Общая оценка
                </h3>
                <v-rating
                  color="warning"
                  hover
                  length="5"
                  size="35"
                  :value="averageRating.rating"
                  readonly
                ></v-rating>
              </div>
              <!-- <div class="d-flex flex-column align-end">
                <time>20.11.2020</time>
                <span>Анонимный отзыв</span>
              </div> -->
            </v-card-text>
            <!-- <v-card-actions class="pb-5">
              <v-btn color="primary" class="ma-auto">
                График оценок
              </v-btn>
            </v-card-actions> -->

            <v-card-actions class="pb-5">
              <v-btn
                color="primary"
                class="ma-auto"
                :to="{
                  name: 'ReviewAnswers',
                  params: {
                    id: $route.params.id
                  }
                }"
              >
                Посмотреть ответы
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
        review: null,
        answers: [],
        averageRating: {
          availability: 0,
          fascination: 0,
          сomplexity: 0,
          novelty: 0,
          interest: 0,
          rating: 0,
        },
        criteries: [
          'availability',
          'fascination',
          'сomplexity',
          'novelty',
          'interest',
          'rating',
        ]
      }
    },

    computed: {
      reviewFetch() {
        this.getReview()
      },

      answersFetch() {
        this.getAnswers()
      },
    },

    methods: {
      getReview() {
        fetch(`${this.$hostname}/api/v1/reviews/?id=${this.$route.params.id}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            console.log(data)
            this.review = data[0]
          });
      },

      getAnswers() {
        fetch(`${this.$hostname}/api/v1/answers/?review=${this.$route.params.id}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            console.log(data)
            this.answers = data
            this.getAverge(this.answers);
          });
      },

      getAverge(answers) {
        for (const answer of answers) {
          for (const critery of this.criteries) {
            this.averageRating[critery] += answer[critery]
          }
        }

        for (const critery of this.criteries) {
          this.averageRating[critery] /= answers.length;
          this.averageRating[critery] = Math.round(this.averageRating[critery])
        }

        console.log(this.averageRating);
      }

    }

  }
</script>

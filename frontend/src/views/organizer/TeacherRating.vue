<template>
  <v-container>
    <section v-if="teacher || teacherFetch">
      <v-row>
        <v-col md="3">
          <v-card class="pa-5">
            <v-card-title>
              Рейтинг преподавателя
            </v-card-title>
            <v-card-text
              style="font-size: 16px;"
            >
              <p>
                {{ teacher.name }}
              </p>
              <p>
                Группы:
                <span v-for="group in teacher.groups" :key="group.id">
                  {{ group.name }},
                </span>
              </p>
              <p>
                Предметы:
                <span v-for="subject in teacher.subjects" :key="subject.id">
                  {{ subject.name }},
                </span>
              </p>
              <p>
                Всего отзывов: {{teacherAnswers.length}}
              </p>
              <p>
                Общая оценка: {{avergeRating}}
              </p>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col md="9" v-if="teacherAnswers.length || answersFetch">
          <v-row v-if="(teacher && reviewsAnswers.length) || reviewsFetch">
            <v-col v-for="chart in charts" :key="chart.name" md="6">
              <v-card
                class="mx-auto text-center"
                color="#5b5c79"
                dark
                max-width="600"
              >
                <v-card-text>
                  <v-sheet color="#f3eeec">
                    <v-sparkline
                      :value="chart.value"
                      :labels="chart.labels"
                      color="#5b5c79"
                      height="100"
                      padding="24"
                      line-width="2"
                    >
                    </v-sparkline>
                  </v-sheet>
                </v-card-text>

                <v-card-text>
                  <div class="display-1 font-weight-thin">
                    {{ criteriesTranslate[chart.name] }}
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      teacher: null,
      teacherAnswers: [],
      avergeRating: 0,
      reviews: [],
      chart: {
        labels: [
          '12am',
          '3am',
          '6am',
          '9am',
          '12pm',
          '3pm',
          '6pm',
          '9pm',
        ],
        value: [
          200,
          675,
          410,
          390,
          310,
          460,
          250,
          240,
        ],
      },

      // chartRating: null,
      // chartAvailability: null,
      // chartFascination: null,
      // chartComplexity: null,
      // chartNovelty: null,
      // chartInterest: null,

      reviewsAnswers: [],

      charts: [],

      criteries: [
          'availability',
          'fascination',
          'сomplexity',
          'novelty',
          'interest',
          'rating',
        ],

      criteriesTranslate: {
        'availability': 'Доступность и понятность изложения материала',
        'fascination': 'Увлекательность изложения материала',
        'сomplexity': 'Сложность изученного материала',
        'novelty': 'Новизна изученного материала',
        'interest': 'Заинтересованность предметом',
        'rating': 'Общая оценка',
      }

    }
  },

  computed: {
    teacherFetch() {
      this.getTeacher()
    },

    answersFetch() {
      this.getAnswers()
    },

    reviewsFetch() {
      this.getReviews()
    }
  },

  methods: {
    getTeacher() {
      fetch(`${this.$hostname}/api/v1/teachers/${this.$route.params.teacher}`)
        .then((response) => {
          return response.json();
        })
        .then(data => {
          this.teacher = data;
        })
    },

    getAnswers() {
      fetch(`${this.$hostname}/api/v1/answers/`)
        .then((response) => {
          return response.json();
        })
        .then(data => {
          this.teacherAnswers = data.filter(item => item.review.teacher.id === this.teacher.id)

          this.getAvergeRating(this.teacherAnswers)
        })
    },

    getAvergeRating(answers) {
      if (answers.length === 0) return 0
      if (answers.length === 1) return answers[0].rating

      const allRating = answers.reduce((sum, current) => sum + current.rating, 0)

      this.avergeRating = Math.round(allRating / answers.length * 100) / 100
    },

    getReviews() {
      fetch(`${this.$hostname}/api/v1/reviews/?teacher=${this.teacher.id}`)
        .then((response) => {
          return response.json();
        })
        .then(data => {
          const sortReviews = data.sort(function (a, b) {
            const dateA = new Date(a.dateStart);
            const dateB = new Date(b.dateStart);

            return dateA - dateB;
          })
          this.filterAnsersForReviews(sortReviews, this.teacherAnswers)
        })
    },

    filterAnsersForReviews(reviews, answers) {
      for (const review of reviews) {
        const answerFiltered = answers.filter(item => item.review.id === review.id)
        const reviewAnswers = {
          date: review.dateStart,
          answers: answerFiltered,
        }

        reviewAnswers.averge = this.getAverge(answerFiltered)

        this.reviewsAnswers.push(reviewAnswers)
      }

      this.createCharts(this.reviewsAnswers)
    },

    getAverge(answers) {
      const averageRating = {
        availability: 0,
        fascination: 0,
        сomplexity: 0,
        novelty: 0,
        interest: 0,
        rating: 0,
      }

      if (answers.length === 0) {
        return averageRating;
      }

      for (const answer of answers) {
        for (const critery of this.criteries) {
          averageRating[critery] += answer[critery]
        }
      }

      for (const critery of this.criteries) {
        averageRating[critery] /= answers.length;
        averageRating[critery] = Math.round(averageRating[critery])
      }

      return averageRating;
    },

    createCharts(reviews) {
      for (const critery of this.criteries) {
        const chart = {
          name: critery,
          value: [],
          labels: [],
        }

        for (const review of reviews) {
          chart.value.push(review.averge[critery])
          chart.labels.push(review.date)
        }

        this.charts.push(chart)
      }

      // console.log(this.charts)
    }
  }

}
</script>

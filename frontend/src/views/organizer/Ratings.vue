<template>
  <v-container class="container-flex">
    <section v-if="teachers.length || teachersFetch">
      <v-row justify="center">
        <v-col md="8">
          <v-card>
            <v-card-title>
              Рейтинг преподавателей
            </v-card-title>

            <v-card-subtitle>
              Всего отзывов: {{answers.length}}
            </v-card-subtitle>

            <v-data-table
              v-if="answers.length || answersFetch"
              :headers="headers"
              :items="answersFilterTeachers"
              :search="search"
            >
              <template v-slot:item.rating="{ item }">
                <v-rating
                  class="list__item-rating"
                  color="warning"
                  hover
                  length="5"
                  size="35"
                  :value="item.rating"
                  readonly
                ></v-rating>
              </template>
              <template v-slot:item.actions="{ item }">
                <v-btn
                  depressed
                  small
                  :to="{
                    name: 'ReviewDetail',
                    params: {
                      id: item.id
                    }
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
  data() {
    return {
      teachers: [],
      answers: [],
      answersFilterTeachers: [],

      search: '',
      headers: [
        {
          text: 'Имя',
          align: 'start',
          value: 'name',
        },
        { text: 'Количество отзывов', align: 'center', value: 'count' },
        { text: 'Рейтинг', align: 'center', value: 'rating' },
        { text: 'Открыть', align: 'center', value: 'actions', sortable: false },
      ],
    }
  },

  computed: {
    teachersFetch() {
      this.getTeachers()
    },

    answersFetch() {
      this.getAnswers()
    },
  },

  methods: {
    getTeachers() {
      fetch(`${this.$hostname}/api/v1/teachers/?id=${this.$route.params.id}`)
        .then((response) => {
          return response.json();
        })
        .then(data => {
          console.log(data);
          this.teachers = data;
        })
    },

    getAnswers() {
      fetch(`${this.$hostname}/api/v1/answers/`)
        .then((response) => {
          return response.json();
        })
        .then(data => {
          console.log(data)
          this.answers = data
          this.filterAnswers(this.teachers, this.answers)
        })
    },

    filterAnswers(teachers, answers) {
      for (const teacher of teachers) {
        const answersFiltered = answers.filter(item => item.review.teacher.id === teacher.id);

        const teacherAnswers = {
          id: teacher.id,
          name: teacher.name,
          count: answersFiltered.length,
          answers: answersFiltered,
        }

        this.answersFilterTeachers.push(teacherAnswers);
      }

      // console.log(this.answersFilterTeachers, 'answers');
      this.setAvergeRating(this.answersFilterTeachers);
    },

    setAvergeRating(answersTeachers) {
      for (const teacher of answersTeachers) {
        teacher['rating'] = this.getAvergeRating(teacher.answers)
      }
    },

    getAvergeRating(answers) {
      if (answers.length === 0) {
        return 0
      }

      if (answers.length === 1) {
        return answers[0].rating
      }

      const sum = answers.reduce((sum, current) => sum + current.rating, 0)

      return Math.round(sum / answers.length);
    },
  }


}
</script>

<style lang="scss">
  .list {
    &__item {
      display: flex;
      justify-content: space-between;

      &-name {
        margin-right: auto;
      }

      &-rating  {
        margin: 0 auto;
      }

      &-btn {
        margin-left: auto;
      }
    }
  }
</style>

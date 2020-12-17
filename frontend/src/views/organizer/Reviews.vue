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
              v-if="reviews.length || reviewsFetch"
              :headers="headers"
              :items="reviews"
              :search="search"
            >
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
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Дата начала',
            align: 'start',
            sortable: false,
            value: 'dateStart',
          },
          { text: 'Дата окончания', value: 'dateEnd' },
          { text: 'Название', value: 'name' },
          { text: 'Предмет', value: 'subject' },
          { text: 'Преподаватель', value: 'teacher' },
          { text: 'Открыть', value: 'actions', sortable: false },
        ],

        reviews: [],
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
        console.log(this.$route.params.id);

        fetch(`${this.$hostname}/api/v1/reviews/`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            console.log(data)
            const reviewsOrganizer = data.filter(item => item.teacher.organizer)
            for (const review of reviewsOrganizer) {
              this.reviews.push({
                id: review.id,
                dateStart: review.dateStart,
                dateEnd: review.dateEnd,
                name: review.name,
                subject: review.subject.name,
                teacher: review.teacher.name,
              })
            }
          });
      },
    }

  }
</script>

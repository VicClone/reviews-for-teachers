<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="5">
          <v-form>
            <v-card>
              <v-card-text>
                <v-card-title>
                  Оставить отзыв
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
                    :value="3"
                    v-model="formReview.availability"
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
                    :value="3"
                    v-model="formReview.fascination"
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
                    :value="3"
                    v-model="formReview.сomplexity"
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
                    :value="3"
                    v-model="formReview.novelty"
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
                    :value="3"
                    v-model="formReview.interest"
                  ></v-rating>
                </div>
                <v-textarea
                  outlined
                  name="input-7-4"
                  label="Отзыв"
                  value=""
                  class="mt-5"
                  v-model="formReview.text"
                ></v-textarea>
                <v-checkbox
                  label="Сделать отзыв анонимным"
                ></v-checkbox>
              </v-card-text>
              <v-card-actions class="pb-5">
                <v-btn
                  @click="sendReview()"
                  color="primary"
                  class="ma-auto"
                >
                  Отправить
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

  methods: {
    sendReview() {
      this.formReview.review = this.$route.query.review
      this.formReview.student = this.$route.params.id

      const currentDate = new Date();
      this.formReview.date = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`

      this.formReview.rating =
        (this.formReview.availability + this.formReview.fascination + this.formReview.сomplexity + this.formReview.novelty + this.formReview.interest) / 5

      this.formReview.rating = Math.round(this.formReview.rating)

      let validForm = true

      for (const key in this.formReview) {
        if (!this.formReview[key]) validForm = false
      }

      if (validForm) {

        fetch(`${this.$hostname}/api/v1/answer/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify(this.formReview)
        })
        .then(resolve => {
          console.log('form send');

          this.$router.push({ name: 'ProfileStudent', params: { id: this.$route.params.id } })

        })
        .catch(error => {
          console.error(error)
        })
      }
    }
  }

}
</script>

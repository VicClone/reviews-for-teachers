<template>
  <v-container class="container-flex">
    <v-row justify="center">
      <v-col md="4">
        <v-card class="px-10 py-5">
          <v-card-title>
            Регистрация преподавателя
          </v-card-title>
          <v-form>
            <v-text-field
              :counter="40"
              label="ФИО"
              outlined
              required
              v-model="form.name"
            >
            </v-text-field>
            <v-select
              v-if="organizers.length || organizersFetch"
              :items="organizers"
              item-value="id"
              item-text="name"
              label="Курс"
              outlined
              required
              v-model="form.organizer"
            ></v-select>
            <v-text-field
              :counter="30"
              label="E-mail"
              outlined
              required
              type="email"
              v-model="form.email"
            >
            </v-text-field>
            <v-text-field
              label="Пароль"
              outlined
              required
              type="password"
              v-model="form.password"
            >
            </v-text-field>
            <v-card-actions>
              <v-btn
                class="ma-auto"
                depressed
                color="primary"
                @click="sendForm()"
              >
                Зарегистрироваться
              </v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import { controllers } from 'chart.js';
export default {
  data: () => ({
    form: {
      name: '',
      email: '',
      organizer: 0,
      password: '',
    },
    organizers: [],
  }),

  computed: {
    organizersFetch() {
      this.getOrganizers()
    },
  },

  methods: {
    getOrganizers() {
      fetch(`${this.$hostname}/api/v1/organizers/`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.organizers = data;
        });
    },

    sendForm() {
      if (this.form.name && this.form.email && this.form.password && this.form.organizer) {
        fetch(`${this.$hostname}/api/v1/teacher/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify(this.form)
        })
        .then(response => {

          console.log('form send');
          return response.json();
        })
        .then(data => {
          console.log(data);
          this.$router.push({ name: 'ProfileTeacher', params: { id: data.id }})
        })
        .catch(error => {
          console.error(error)
        })
      }
    }
  }

}
</script>

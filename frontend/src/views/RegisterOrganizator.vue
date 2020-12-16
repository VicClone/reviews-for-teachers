<template>
  <v-container class="container-flex">
    <v-row justify="center">
      <v-col md="4">
        <v-card class="px-10 py-5">
          <v-card-title>
            Регистрация организатора
          </v-card-title>
          <v-form>
            <v-text-field
              :counter="30"
              label="Название курса"
              outlined
              required
              v-model="form.name"
            >
            </v-text-field>
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
              :counter="30"
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
export default {
  data: () => ({
    form: {
      name: '',
      email: '',
      password: '',
    }
  }),
  methods: {
    sendForm() {
      if (this.form.name && this.form.email && this.form.password) {
        console.log(this.form);
        fetch('http://localhost:8000/api/v1/organizer/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify(this.form)
        })
        .then(resolve => {
          console.log('form send');
        })
        .catch(error => {
          console.error(error)
        })
      }
    }
  }

}
</script>

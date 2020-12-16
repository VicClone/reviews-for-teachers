<template>
  <v-container class="container-flex">
    <v-row justify="center">
      <v-col md="4" style="display: flex; flex-direction: column;">
        <v-card style="margin: auto;" class="px-10 py-5">
          <v-card-title>
            Авторизация
          </v-card-title>
          <v-form>
            <v-select
              :items="userTypes"
              item-value="id"
              item-text="name"
              v-model="formAuth.userType"
              outlined
            >

            </v-select>
            <v-text-field
              label="Email"
              outlined
              required
              v-model="formAuth.login"
            >
            </v-text-field>
            <v-text-field
              label="Пароль"
              outlined
              required
              v-model="formAuth.password"
            >
            </v-text-field>
            <v-card-actions>
              <v-btn
                class="ma-auto"
                depressed
                color="primary"
                @click="sendAuth()"
              >
                Вход
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
    userTypes: [
      {
        id: 1,
        name: 'Организатор'
      },
      {
        id: 2,
        name: 'Преподаватель'
      },
      {
        id: 3,
        name: 'Студент'
      },
    ],
    formAuth: {
      userType: 1,
      login: '',
      password: '',
    }
  }),

  methods: {
    sendAuth() {
      if (this.formAuth.userType === 1) {
        this.authOrganizer()
      }

      if (this.formAuth.userType === 2) {
        this.authTeacher()
      }

      if (this.formAuth.userType === 3) {
        this.authStudent()
      }
    },

    // ${this.$hostname}/api/v1/organizers/?login=test@ceramic3d.ru&password=1234566

    authOrganizer() {
      fetch(`${this.$hostname}/api/v1/organizers/?login=${this.formAuth.login}&password=${this.formAuth.password}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          if (data.length) {
            this.$router.push({ name: 'ProfileOrganizer', params: { id: data[0].id }})
          }
        });
    },

    authTeacher() {
      fetch(`${this.$hostname}/api/v1/teachers/?login=${this.formAuth.login}&password=${this.formAuth.password}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          if (data.length) {
            this.$router.push({ name: 'ProfileTeacher', params: { id: data[0].id }})
          }
        });
    },

    authStudent() {
      fetch(`${this.$hostname}/api/v1/students/?login=${this.formAuth.login}&password=${this.formAuth.password}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
          if (data.length) {
            this.$router.push({ name: 'ProfileStudent', params: { id: data[0].id }})
          }
        });
    }
  }
}
</script>

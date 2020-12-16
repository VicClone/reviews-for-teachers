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
            >
            </v-text-field>
            <v-text-field
              :counter="10"
              label="Код организации"
              outlined
              required
            >
            </v-text-field>
            <v-text-field
              :counter="20"
              label="Должность"
              outlined
              required
            >
            </v-text-field>
            <v-text-field
              :counter="30"
              label="E-mail"
              outlined
              required
              type="email"
            >
            </v-text-field>
            <v-text-field
              label="Пароль"
              outlined
              required
              type="password"
            >
            </v-text-field>
            <v-text-field
              label="Повторите пароль"
              outlined
              required
              type="password"
            >
            </v-text-field>
            <v-card-actions>
              <v-btn
                class="ma-auto"
                depressed
                color="primary"
                :to="{
                  name: 'ProfileTeacher'
                }"
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

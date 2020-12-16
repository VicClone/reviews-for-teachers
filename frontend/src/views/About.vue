<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="6" class="ma-auto">
          <p class="text-center">
            Данный сервис является инструментом<br>
            для сбора данных о качестве образовательного процесса.<br>
          </p>
          <p class="text-center">
            Желаете зарегистрироваться?
          </p>
        </v-col>
      </v-row>
      <v-row justify="center">
        <h3>Кто вы?</h3>
      </v-row>
      <v-row justify="center">
        <v-col md="2" class="d-flex">
          <v-btn
            depressed
            class="ma-auto"
            color="light-blue lighten-4"
            :to="{
              name: 'RegisterStudent'
            }"
          >
            Студент
          </v-btn>
        </v-col>
        <v-col md="2" class="d-flex">
          <v-btn
            depressed
            class="ma-auto"
            color="cyan lighten-4"
            :to="{
              name: 'RegisterTeacher'
            }"
          >
            Преподаватель
          </v-btn>
        </v-col>
        <v-col md="2" class="d-flex">
          <v-btn
            depressed
            class="ma-auto"
            color="teal lighten-4"
            :to="{
              name: 'RegisterOrganizator'
            }"
          >
            Организатор
          </v-btn>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>

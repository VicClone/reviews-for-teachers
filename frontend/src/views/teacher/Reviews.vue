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
              :headers="headers"
              :items="desserts"
              :search="search"
            >
              <template v-slot:item.actions="{ item }">
                <v-btn
                  depressed
                  small
                  :to="{
                    name: 'ReviewTeacher'
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
            text: 'Дата',
            align: 'start',
            sortable: false,
            value: 'date',
          },
          { text: 'Имя', value: 'name' },
          { text: 'Оценка', value: 'rating' },
          { text: 'Предмет', value: 'subject' },
          { text: 'Преподаватель', value: 'teacher' },
          { text: 'Открыть', value: 'actions', sortable: false },
        ],
        desserts: [
          {
            date: '20.11.2020',
            name: 'Вася Пупкин',
            rating: 5,
            subject: 'Маркетинг',
            teacher: 'Петр Сергеич',
          },
          {
            date: '20.11.2020',
            name: 'Вася Пупкин',
            rating: 5,
            subject: 'Маркетинг',
            teacher: 'Петр Сергеич',
          },
          {
            date: '20.11.2020',
            name: 'Вася Пупкин',
            rating: 5,
            subject: 'Маркетинг',
            teacher: 'Петр Сергеич',
          },
          {
            date: '20.11.2020',
            name: 'Вася Пупкин',
            rating: 4,
            subject: 'Маркетинг',
            teacher: 'Петр Сергеич',
          },
          {
            date: '20.11.2020',
            name: 'Вася Пупкин',
            rating: 5,
            subject: 'Маркетинг',
            teacher: 'Петр Сергеич',
          },
          {
            date: '20.11.2020',
            name: 'Вася Пупкин',
            rating: 5,
            subject: 'Маркетинг',
            teacher: 'Петр Сергеич',
          },
        ],
      }
    },
  }
</script>

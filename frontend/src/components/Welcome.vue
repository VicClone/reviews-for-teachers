<template>
  <section
    id="welcome"
    class="overflow-hidden"
  >
    <v-row no-gutters>
      <v-col
        class="hidden-sm-and-down"
        md="6"
      >
        <v-img
          :src="require('@/assets/welcome.png')"
          height="100vh"
        />
      </v-col>

      <v-col
        class="align-content-space-between layout wrap"
        cols="12"
        md="6"
        :pa-5="$vuetify.breakpoint.smAndDown"
      >
        <base-bubble-1
          style="transform: rotate(180deg) translateY(25%)"
        />

        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="10"
            md="6"
          >
            <base-heading>Добро пожаловать!</base-heading>
            <base-text>
              Наша цель - устранить недопонимание между учащимися и преподавателями.<br>
              Если Вы учащийся, на нашем сайте Вы можете оставить отзыв своему преподавателю, оценить пройденные занятия и курсы.<br>
              Если Вы преподаете – посмотрите отзывы своих учеников, узнайте их мнение о предмете,  оцените уровень вовлеченности в учебный процесс.<br>
              Если  Вы руководитель образовательной программы – наш сервис позволит оценивать работу ваших сотрудников.
            </base-text>
            <v-btn
              color="primary"
              class="mt-4"
              :to="{
                name: 'Auth'
              }"
            >
              Авторизация
            </v-btn>
            <v-btn
              color="primary"
              class="mt-4 ml-4"
              :to="{
                name: 'About'
              }"
            >
              Регистрация
            </v-btn>
          </v-col>
        </v-row>

        <base-bubble-2
          style="transform: rotate(180deg) translate(-200px, -15%)"
        />
      </v-col>
    </v-row>
  </section>
</template>

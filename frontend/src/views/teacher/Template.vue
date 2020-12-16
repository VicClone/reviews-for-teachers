<template>
  <v-container class="container-flex">
    <section>
      <h2>Шаблон опроса</h2>
      <v-row>
        <v-col md="3">
          <v-card
            class="mx-auto"
            tile
          >
            <v-list>
              <v-subheader>Выберите предмет</v-subheader>
              <v-list-item-group
                color="primary"
              >
                <v-list-item v-for="index in 5" :key="index">
                  <v-list-item-icon>
                    <v-icon>mdi-school</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>
                      Предмет {{ index }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>
          <v-card
            class="mx-auto mt-5"
            tile
          >
            <v-list>
              <v-subheader>Выберите преподавателя</v-subheader>
              <v-list-item-group
                color="primary"
              >
                <v-list-item v-for="i in 5" :key="i">
                  <v-list-item-icon>
                    <v-icon>mdi-account</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>
                      Сотрудник {{ i }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>
        </v-col>
        <v-col md="4">
          <v-form>
            <v-card>
              <v-card-title>
                  Повторяющийся опрос
              </v-card-title>
              <v-card-text>
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
                  ></v-rating>
                </div>
                <v-textarea
                  outlined
                  name="input-7-4"
                  label="Отзыв"
                  value=""
                  class="mt-5"
                ></v-textarea>
              </v-card-text>
            </v-card>
          </v-form>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>

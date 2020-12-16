<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="6">
          <v-card
            class="mx-auto"
            max-width="600"
            tile
          >
            <v-img
              height="100%"
              src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
            >
              <v-row
                align="end"
                class="fill-height"
              >
                <v-col
                  align-self="start"
                  class="pa-0"
                  cols="12"
                >
                  <v-avatar
                    class="profile"
                    color="grey"
                    size="164"
                  >
                    <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
                  </v-avatar>
                </v-col>
                <v-col class="py-0">
                  <v-list-item
                    color="rgba(0, 0, 0, .4)"
                    dark
                  >
                    <v-list-item-content>
                      <v-list-item-title class="title">
                        Иван Иванов
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        Курсы по маркетингу
                      </v-list-item-subtitle>
                      <v-list-item-subtitle>
                        ivan@mail.com
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-col>
              </v-row>
            </v-img>
          </v-card>

          <v-card class="mt-5">
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
                  :value="2"
                  readonly
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
                  readonly
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
                  readonly
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
                  :value="5"
                  readonly
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
                  :value="4"
                  readonly
                ></v-rating>
              </div>
              <v-textarea
                outlined
                name="input-7-4"
                label="Отзыв"
                value="Всё было просто отлично, замечаний нет"
                readonly
                class="mt-5"
              >
              </v-textarea>
              <div class="d-flex flex-column align-end">
                <time>20.11.2020</time>
                <span>Анонимный отзыв</span>
              </div>
            </v-card-text>
            <v-card-actions class="pb-5">
              <v-btn color="primary" class="ma-auto">
                График оценок
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </section>
  </v-container>
</template>

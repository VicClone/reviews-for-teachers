<template>
  <v-container class="container-flex">
    <section v-if="teacher || teacherFetch">
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
                    v-if="teacher || teacherFetch"
                  >
                    <v-list-item-content>
                      <v-list-item-title class="title">
                        {{teacher.name}}
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        {{teacher.organizer.name}}
                      </v-list-item-subtitle>
                      <v-list-item-subtitle>
                        {{teacher.email}}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-col>
              </v-row>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col md="6">
          <v-row justify="center">
            <v-col md="4">
              <v-card
                class="mx-auto"
                tile
              >
                <v-list>
                  <v-subheader>Список предметов</v-subheader>
                  <v-list-item-group
                    color="primary"
                  >
                    <v-list-item
                      v-for="subject in teacher.subjects"
                      :key="subject.id"
                      @click="subjectId = subject.id"
                    >
                      <v-list-item-icon>
                        <v-icon>mdi-school</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>
                          {{subject.name}}
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card>
            </v-col>
            <v-col md="4">
              <v-card
                class="mx-auto"
                tile
              >
                <v-list>
                  <v-subheader>Список групп</v-subheader>
                  <v-list-item-group
                    color="primary"
                  >
                    <v-list-item
                      v-for="group in teacher.groups"
                      :key="group.id"
                      @click="groupId = group.id"
                    >
                      <v-list-item-icon>
                        <v-icon>mdi-account-multiple</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>
                          {{ group.name }}
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card>
            </v-col>
          </v-row>
          <v-row justify-center>
            <v-col md12 class="btns">
              <v-btn
                class="btns__btn"
                @click="dialogReview = true"
              >
                Создать опрос
              </v-btn>
              <v-btn
                class="btns__btn"
                :to="{
                  name: 'ReviewsTeacher',
                }"
              >
                Посмотреть отзывы
              </v-btn>
              <v-btn
                v-if="false"
                class="btns__btn"
                :to="{
                  name: 'RatingTeacher',
                  params: {
                    id: teacher.id
                  }
                }"
              >
                Рейтинг предметов
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </section>

    <v-dialog
      v-model="dialogReview"
      max-width="400px"
    >
      <v-card class="px-10 py-5" v-if="teacher">
        <v-card-title>
          Создать опрос
        </v-card-title>
        <v-form>
          <v-text-field
            :counter="60"
            label="Название опроса"
            outlined
            required
            v-model="formReview.name"
          >
          </v-text-field>
          <v-select
            :items="teacher.subjects"
            item-value="id"
            item-text="name"
            label="Предмет"
            outlined
            required
            v-model="formReview.subject"
          ></v-select>
          <v-select
            :items="teacher.groups"
            item-value="id"
            item-text="name"
            label="Группа"
            outlined
            required
            v-model="formReview.group"
          ></v-select>
          <v-text-field
            label="Дата начала"
            type="date"
            outlined
            required
            v-model="formReview.dateStart"
          >
          </v-text-field>
          <v-text-field
            label="Дата конца"
            type="date"
            outlined
            required
            v-model="formReview.dateEnd"
          >
          </v-text-field>
          <v-card-actions>
            <v-btn
              class="ma-auto"
              depressed
              color="primary"
              @click="createReview()"
            >
              Создать
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
  </v-container>
</template>


<style lang="scss">
  .btns {
    display: flex;
    justify-content: center;

    &__btn {
      margin: 0 20px;
    }
  }
</style>

<script>
export default {
  data: () => ({
    teacher: null,
    subjectId: '',
    groupId: '',
    formReview: {
      name: '',
      dateStart: 0,
      dateEnd: 0,
      subject: 0,
      group: 0,
      teacher: 0,
    },
    dialogReview: false,
    organizer: null,
  }),

  computed: {
    teacherFetch() {
      this.getTeacher()
    },

    organizerFetch() {
      this.getOrganizer()
    },
  },

  methods: {
    getTeacher() {
      fetch(`${this.$hostname}/api/v1/teachers/${this.$route.params.id}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.teacher = data;
        });
    },
    getOrganizer() {
      fetch(`${this.$hostname}/api/v1/organizers/?id=${this.teacher.organizer}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data)
          this.teacher = data;
        });
    },
    createReview() {
      this.formReview.teacher = this.teacher.id

      if (this.formReview.name
        && this.formReview.dateStart
        && this.formReview.dateEnd
        && this.formReview.group
        && this.formReview.subject
        && this.formReview.teacher) {
        fetch(`${this.$hostname}/api/v1/review/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify(this.formReview)
        })
          .then(resolve => {
            console.log('form send');
            this.dialogReview = false
          })
          .catch(error => {
            console.error(error)
          })
      }
    }
  }
}
</script>

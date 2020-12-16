<template>
  <v-container class="container-flex">
    <section>
      <v-row justify="center">
        <v-col md="3">
          <v-card
            class="mx-auto"
            tile
          >
            <v-list v-if="teachers.length || teachersFetch">
              <v-subheader>Список сотрудников</v-subheader>
              <v-list-item-group
                color="primary"
              >
                <v-list-item v-for="(teacher, i) in teachers" :key="i">
                  <v-list-item-icon>
                    <v-icon>mdi-account</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ teacher.name }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
            <v-divider></v-divider>
            <v-card-actions class="d-flex flex-column">
              <v-btn
                class="ma-2"
                @click="dialogAddTeacher = true"
              >
                Добавить сотрудника
              </v-btn>
              <v-btn class="ma-2">
                Рейтинг сотрудников
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col md="3">
          <v-card
            class="mx-auto"
            tile
          >
            <v-list v-if="subjects.length || subjectsFetch">
              <v-subheader>Список предметов</v-subheader>
              <v-list-item-group
                color="primary"
              >
                <v-list-item v-for="(subject, i) in subjects" :key="i">
                  <v-list-item-icon>
                    <v-icon>mdi-school</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ subject.name }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
            <v-divider></v-divider>
            <v-card-actions class="d-flex flex-column">
              <v-btn
                class="ma-2"
                @click="dialogAddSubject = true"
              >
                Добавить предмет
              </v-btn>
              <v-btn class="ma-2">
                Рейтинг предметов
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col md="3">
          <v-card
            class="mx-auto"
            tile
          >
            <v-list v-if="groups.length || groupsFetch">
              <v-subheader>Список групп</v-subheader>
              <v-list-item-group
                color="primary"
              >
                <v-list-item v-for="(group, i) in groups" :key="i">
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
            <v-divider></v-divider>
            <v-card-actions class="d-flex flex-column">
              <v-btn
                class="ma-2"
                @click="dialogAddGroup = true"
              >
                Добавить группу
              </v-btn>
              <v-btn class="ma-2">
                Рейтинг групп
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </section>
    <v-dialog
      v-model="dialogAddTeacher"
      max-width="600px"
    >
      <v-card class="px-10 py-5">
        <v-card-title>
          Добавить сотрудника
        </v-card-title>
        <v-form>
          <v-text-field
            :counter="40"
            label="ФИО"
            outlined
            required
            v-model="formTeacher.name"
          >
          </v-text-field>
          <v-text-field
            :counter="30"
            label="E-mail"
            outlined
            required
            type="email"
            v-model="formTeacher.email"
          >
          </v-text-field>
          <v-text-field
            label="Пароль"
            outlined
            required
            type="password"
            v-model="formTeacher.password"
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
              @click="sendFormTeacher()"
            >
              Добавить
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="dialogAddSubject"
      max-width="400px"
    >
      <v-card class="px-10 py-5">
        <v-card-title>
          Добавить предмет
        </v-card-title>
        <v-form>
          <v-text-field
            :counter="40"
            label="Название предмета"
            outlined
            required
            v-model="formSubject.name"
          >
          </v-text-field>
          <v-select
            :items="this.teachers"
            item-value="id"
            item-text="name"
            label="Преподаватель"
            outlined
            required
            v-model="formSubject.teacher"
          ></v-select>
          <v-card-actions>
            <v-btn
              class="ma-auto"
              depressed
              color="primary"
              @click="sendFormSubject()"
            >
              Добавить
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="dialogAddGroup"
      max-width="400px"
    >
      <v-card class="px-10 py-5">
        <v-card-title>
          Добавить группу
        </v-card-title>
        <v-form>
          <v-text-field
            :counter="40"
            label="Название группы"
            outlined
            required
            v-model="formGroup.name"
          >
          </v-text-field>
          <v-card-actions>
            <v-btn
              class="ma-auto"
              depressed
              color="primary"
              @click="sendFormGroup"
            >
              Добавить
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      dialogAddTeacher: false,
      dialogAddSubject: false,
      dialogAddGroup: false,
      teachers: [],
      subjects: [],
      groups: [],
      formTeacher: {
        name: '',
        email: '',
        password: '',
      },

      formSubject: {
        name: '',
        teacher: '',
      },

      formGroup: {
        name: '',
      },
    }),

    computed: {
      teachersFetch() {
        this.getTeachers()
      },

      subjectsFetch() {
        this.getSubjects()
      },

      groupsFetch() {
        this.getGroups()
      },
    },


    methods: {
      getTeachers() {
        fetch(`http://localhost:8000/api/v1/teachers/?id=${this.$route.params.id}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            console.log(data)
            this.teachers = data;
          });
      },

      getSubjects() {
        fetch(`http://localhost:8000/api/v1/subjects/?organizer=${this.$route.params.id}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            this.subjects = data;
          });
      },

      getGroups() {
        fetch(`http://localhost:8000/api/v1/groups/?organizer=${this.$route.params.id}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            this.groups = data;
          });
      },

      sendFormTeacher() {
        if (this.formTeacher.name && this.formTeacher.email && this.formTeacher.password) {
          this.formTeacher.organizer = this.$route.params.id

          fetch('http://localhost:8000/api/v1/teacher/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(this.formTeacher)
          })
          .then(resolve => {
            console.log('form send');
            this.getTeachers()
            this.dialogAddTeacher = false
          })
          .catch(error => {
            console.error(error)
          })
        }
      },

      sendFormSubject() {
        console.log(this.formSubject);
        if (this.formSubject.name && this.formSubject.teacher) {
          this.formSubject.organizer = this.$route.params.id

          fetch('http://localhost:8000/api/v1/subject/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(this.formSubject)
          })
          .then(resolve => {
            console.log('form send');
            this.getSubjects()
            this.dialogAddSubject = false
          })
          .catch(error => {
            console.error(error)
          })
        }
      },


      sendFormGroup() {
        if (this.formGroup.name) {
          this.formGroup.organizer = this.$route.params.id

          fetch('http://localhost:8000/api/v1/group/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify(this.formGroup)
          })
          .then(resolve => {
            console.log('form send');
            this.getGroups()
            this.dialogAddGroup = false
          })
          .catch(error => {
            console.error(error)
          })
        }
      },
    }
  }
</script>

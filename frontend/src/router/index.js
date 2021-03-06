import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register-organizator',
    name: 'RegisterOrganizator',
    component: () => import('../views/RegisterOrganizator.vue')
  },
  {
    path: '/register-teacher',
    name: 'RegisterTeacher',
    component: () => import('../views/RegisterTeacher.vue')
  },
  {
    path: '/register-student',
    name: 'RegisterStudent',
    component: () => import('../views/RegisterStudent.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/organizer/:id/profile/',
    name: 'ProfileOrganizer',
    component: () => import('../views/organizer/Profile.vue')
  },
  {
    path: '/organizer/:id/list',
    name: 'List',
    component: () => import('../views/organizer/List.vue')
  },
  {
    path: '/organizer/:id/ratings',
    name: 'RatingsOrganizer',
    component: () => import('../views/organizer/Ratings.vue')
  },
  {
    path: '/organizer/:id/reviews',
    name: 'ReviewsOrganizer',
    component: () => import('../views/organizer/Reviews.vue')
  },
  {
    path: '/organizer/:id/teacher-rating/:teacher',
    name: 'TeacherRating',
    component: () => import('../views/organizer/TeacherRating.vue')
  },
  {
    path: '/teacher/:id/profile',
    name: 'ProfileTeacher',
    component: () => import('../views/teacher/Profile.vue')
  },
  {
    path: '/teacher/:id/reviews',
    name: 'ReviewsTeacher',
    component: () => import('../views/teacher/Reviews.vue')
  },
  {
    path: '/review/:id',
    name: 'ReviewDetail',
    component: () => import('../views/ReviewDetail.vue')
  },
  {
    path: '/review/:id/answers',
    name: 'ReviewAnswers',
    component: () => import('../views/Answers.vue')
  },
  {
    path: '/answer/:id',
    name: 'AnswerDetail',
    component: () => import('../views/AnswerDetail.vue')
  },
  {
    path: '/teacher/rating',
    name: 'RatingTeacher',
    component: () => import('../views/teacher/Rating.vue')
  },
  {
    path: '/teacher/template',
    name: 'TemplateTeacher',
    component: () => import('../views/teacher/Template.vue')
  },

  {
    path: '/student/:id/profile',
    name: 'ProfileStudent',
    component: () => import('../views/student/Profile.vue')
  },
  {
    path: '/student/:id/review',
    name: 'ReviewStudent',
    component: () => import('../views/student/Review.vue')
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../views/Auth.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

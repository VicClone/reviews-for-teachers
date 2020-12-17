import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import './plugins/base'
import vuetify from './plugins/vuetify'
import {isProduction} from './env.js'

Vue.config.productionTip = isProduction

Vue.prototype.$hostname = (Vue.config.productionTip) ? 'http://91.201.53.186:8000' : 'http://localhost:8000'

console.log(isProduction);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

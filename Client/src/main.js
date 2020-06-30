import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { TokenService } from '@/services/storage.service'
import { AxiosService } from '@/services/http'

import 'buefy/dist/buefy.css'
import './assets/styles/main.scss'
import Buefy from 'buefy'
import Vuelidate from 'vuelidate'
import dateFilter from '@/filters/date.filter'

Vue.use(Buefy)
Vue.use(Vuelidate)
Vue.filter('time', dateFilter)

Vue.config.productionTip = false

// Если токен существует, установить заголовок
if (TokenService.getToken()) {
  AxiosService.setHeader()
}
// Монтирование Axios перехватчика запросов
AxiosService.mount401Interceptor()

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'buefy/dist/buefy.css'
import './assets/styles/main.scss'
import { Input, Button } from 'buefy'

Vue.use(Input)
Vue.use(Button)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

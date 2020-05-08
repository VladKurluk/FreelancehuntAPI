import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import 'buefy/dist/buefy.css'
import './assets/styles/main.scss'
// import { Input, Button, Loading, Tag, Field, Select, Pagination } from 'buefy'
import Buefy from 'buefy'
// Компонент для Сайдбар меню
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import dateFilter from '@/filters/date.filter'

// Vue.use(Input)
// Vue.use(Field)
// Vue.use(Select)
// Vue.use(Button)
// Vue.use(Loading)
// Vue.use(Tag)
// Vue.use(Pagination)
Vue.use(VueSidebarMenu)
Vue.use(Buefy)
Vue.filter('time', dateFilter)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

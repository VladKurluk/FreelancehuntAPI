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
    path: '/profile',
    name: 'profile',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "profile" */ '../views/freelancehunt/Profile.vue')
  },
  {
    path: '/all_frelancers',
    name: 'frelancersList',
    component: () => import(/* webpackChunkName: "frelancersList" */ '../views/freelancehunt/FreelancersList.vue')
  },
  {
    path: '/freelance_ua',
    name: 'parser',
    component: () => import(/* webpackChunkName: "parser" */ '../views/parser/ParsingList.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import FrL from '../views/freelancehunt/FreelancersList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/frelance_api',
    name: 'frelanceApi',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/freelancehunt/Profile.vue'),
    children: [
      {
        path: 'freelancers',
        component: FrL
      }
    ]
  },
  {
    path: '/parser',
    name: 'parser',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/parser/ParsingList.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

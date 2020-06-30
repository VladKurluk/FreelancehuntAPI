import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import { TokenService } from '@/services/storage.service'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    meta: {
      layout: 'auth',
      public: true, // Разрешить доступ даже если не залогинен
      onlyWhenLoggedOut: true
    },
    component: () => import(/* webpackChunkName: "login" */ '@/views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    meta: {
      layout: 'auth',
      public: true, // Разрешить доступ даже если не залогинен
      onlyWhenLoggedOut: true
    },
    component: () => import(/* webpackChunkName: "register" */ '@/views/Register.vue')
  },
  {
    path: '/',
    name: 'Home',
    meta: {
      layout: 'main',
      public: true // Разрешить доступ даже если не залогинен
    },
    component: Home
  },
  {
    path: '/profile',
    name: 'profile',
    meta: { layout: 'main' },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "profile" */ '../views/freelancehunt/Profile.vue')
  },
  /* {
    path: '/all_frelancers',
    name: 'frelancersList',
    meta: { layout: 'main' },
    component: () => import(/* webpackChunkName: "frelancersList" * '../views/freelancehunt/FreelancersList.vue')
  }, */
  /* {
    path: '/freelance_ua',
    name: 'parser',
    meta: { layout: 'main' },
    component: () => import(/* webpackChunkName: "parser" * '../views/parser/ParsingList.vue')
  }, */
  {
    path: '/test',
    name: 'test',
    meta: { layout: 'main' },
    component: () => import(/* webpackChunkName: "test" */ '../views/Test.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // Защита роутов
  const isPublic = to.matched.some(record => record.meta.public)
  const onlyWhenLoggedOut = to.matched.some(record => record.meta.onlyWhenLoggedOut)
  const loggedIn = !!TokenService.getToken()

  if (!isPublic && !loggedIn) {
    return next({
      path: '/login',
      query: { redirect: to.fullPath } // Сохранение защищенного роута, для редиректа на него после логина
    })
  }

  // Не позволяет пользователю посещать страницу входа или страницу регистрации, если он вошел в систему
  if (loggedIn && onlyWhenLoggedOut) {
    return next('/')
  }

  next()
})

export default router

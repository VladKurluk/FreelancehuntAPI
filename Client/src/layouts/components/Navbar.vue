<template>
  <b-navbar :fixed-top='true' :shadow="true">
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img
          src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
          alt="Lightweight UI components for Vue.js based on Bulma"
        />
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item tag="router-link" :to="{ path: '/' }">Главная</b-navbar-item>
      <b-navbar-dropdown label="Фрилансхант">
        <b-navbar-item tag="router-link" :to="{ path: '/profile' }">Профиль</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/all_frelancers' }">Фрилансеры</b-navbar-item>
      </b-navbar-dropdown>
      <b-navbar-dropdown label="Фриланс.юа">
        <b-navbar-item tag="router-link" :to="{ path: '/freelance_ua' }">Парсер</b-navbar-item>
      </b-navbar-dropdown>
    </template>

    <template slot="end" v-if="$store.getters.loggedIn">
      <b-navbar-item tag="div">
        <div class="buttons">
          <router-link :to="{ path: '/register' }" class="button is-primary">
            <strong>Регистрация</strong>
          </router-link>
          <router-link :to="{ path: '/login' }"  class="button is-light">Вход</router-link>
        </div>
      </b-navbar-item>
    </template>
    <template slot="end" v-else>
      <b-navbar-dropdown :label="setUserName">
        <b-navbar-item tag="router-link" :to="{ path: '/test' }">Test protected route</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/' }">2</b-navbar-item>
      </b-navbar-dropdown>
      <b-navbar-item tag="div">
        <div class="buttons">
          <button @click="logout" class="button is-primary">
            <strong>Выход</strong>
          </button>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data: () => ({}),
  methods: {
    ...mapActions('auth', [
      'logout'
    ])
  },
  computed: {
    ...mapState('auth', [
      'userName'
    ]),
    setUserName () {
      return localStorage.getItem('user_name')
    }
  }
}
</script>

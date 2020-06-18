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

    <template slot="end">
      <b-navbar-item tag="div">
        <div class="buttons">
          <router-link :to="{ path: '/register' }" class="button is-primary">
            <strong>Регистрация</strong>
          </router-link>
          <router-link :to="{ path: '/login' }"  class="button is-light">Вход</router-link>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  data: () => ({})
}
</script>

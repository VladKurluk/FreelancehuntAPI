<template>
  <section>
    <form class="card auth-card" @submit.prevent="submitHandler">
      <h1 class="title is-3">Вход в аккаунт</h1>
      <!-- Email -->
      <b-field
        label="Email"
        :label-position="labelPosition"
        :type="(($v.email.$dirty && !$v.email.required) || ($v.email.$dirty && !$v.email.email)) ? 'is-danger' : ''"
        :message="(($v.email.$dirty && !$v.email.required) || ($v.email.$dirty && !$v.email.email)) ? 'Не корректный Email' : ''"
      >
        <b-input type="text" :use-html5-validation="false" v-model.trim="email" maxlength="30"></b-input>
      </b-field>
      <!-- Пароль -->
      <b-field
        label="Пароль"
        :label-position="labelPosition"
        :type="(($v.password.$dirty && !$v.password.required) || ($v.password.$dirty && !$v.password.minLength)) ? 'is-danger' : ''"
        :message="(($v.password.$dirty && !$v.password.required) || ($v.password.$dirty && !$v.password.minLength)) ? `Поле должно содержать не менее ${$v.password.$params.minLength.min} символов. Введено ${password.length} символов. ` : ''"
      >
        <b-input v-model="password" type="password" maxlength="30" password-reveal></b-input>
      </b-field>
      <b-button
        tag="button"
        :loading="loading"
        native-type="submit"
        class="button is-primary button_auth"
      >Войти</b-button>
      <hr />
      <p class="center">
        Еще нет аккаунта?
        <router-link to="/register">Зарегистрировать!</router-link>
      </p>
    </form>
  </section>
</template>

<script>
import { email, required, minLength } from 'vuelidate/lib/validators'

export default {
  name: 'Registration',
  data: () => ({
    email: '',
    password: '',
    labelPosition: 'on-border',
    loading: false,
    disableBtn: true
  }),
  validations: {
    email: { email, required },
    password: { required, minLength: minLength(6) }
  },
  methods: {
    async submitHandler () {
      if (this.$v.$invalid) {
        this.$v.$touch()
        return
      }

      this.loading = true
      await this.$store.dispatch('auth/login', {
        email: this.email,
        password: this.password
      })
      this.loading = false
    }
  }
}
</script>

<style lang="scss">
.auth-card {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  border-radius: 4px;
}
</style>

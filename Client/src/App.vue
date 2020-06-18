<template>
  <div id="app">
    <component :is='layout'>
      <router-view/>
    </component>
  </div>
</template>

<script>
import AuthLayout from '@/layouts/Auth'
import MainLayout from '@/layouts/Main'
export default {
  data: () => ({}),
  components: {
    AuthLayout,
    MainLayout
  },
  computed: {
    layout () {
      // console.log(this.$route.meta)
      return (this.$route.meta.layout || 'auth') + '-layout'
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

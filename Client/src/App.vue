<template>
  <div id="app">
    <component :is="layout">
      <router-view />
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
      return (this.$route.meta.layout || 'auth') + '-layout'
    }
  }
}
</script>

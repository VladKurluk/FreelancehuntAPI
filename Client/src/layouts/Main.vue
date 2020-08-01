<template>
  <main class="main-layout">
    <app-navbar />
    <router-view />
    <app-footer />
  </main>
</template>

<script>
import AppNavbar from '@/layouts/components/Navbar.vue'
import AppFooter from '@/layouts/components/Footer.vue'

export default {
  name: 'MainLayout',
  components: {
    AppNavbar,
    AppFooter
  }
}
</script>

<style lang="scss">
.main-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;

  .app-footer {
    margin-top: auto;
  }
}
</style>

<template>
  <main>
    <navbar />
    <router-view />
  </main>
</template>

<script>
import navbar from '@/components/global/Navbar'

export default {
  name: 'MainLayout',
  components: {
    navbar
  }
}
</script>

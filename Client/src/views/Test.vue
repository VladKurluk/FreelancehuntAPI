<template>
  <h1>Test protected rout: {{data}}</h1>
</template>

<script>
import { axiosInstance } from '@/services/http.js'
export default {
  data: () => ({
    data: null
  }),
  async mounted () {
    const response = await axiosInstance.get('/auth/protected')
    this.data = response.data.Auth
  }
}
</script>

<template>
  <div class="container">
    <div class="columns">
      <div class="column is-6">
        <div v-if="data.length !== 0" class="card">
          {{ data }}
        </div>
        <b-loading v-else :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false"></b-loading>
      </div>
    </div>
  </div>
</template>

<script>
import { axiosParserInst } from '@/utils/http.js'

export default {
  name: 'ParserList',
  data: () => ({
    data: [],
    isLoading: true,
    isFullPage: true
  }),
  methods: {
    getProfileData () {
      axiosParserInst.get('parser')
        .then(response => (this.data = response.data))
    }
  },
  created () {
    this.getProfileData()
    this.isLoading = !this.isLoading
  }
}
</script>

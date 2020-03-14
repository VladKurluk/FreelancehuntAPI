<template>
  <div class="container">
    <div class="columns">
      <div class="column is-11">
        <!-- <b-field label="Email"
          type="is-primary"
          message="This email is invalid">
          <b-input type="email"
            value="john@"
            maxlength="30"></b-input>
        </b-field> -->
        {{ data }}
      </div>
      <div class="column is-1 has-background-warning">
        <b-button type="is-primary" @click="getData">Click Me</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInst from '../utils/http.js'

export default {
  data: () => ({
    data: []
  }),
  methods: {
    getData () {
      axiosInst.get('curent_profile')
        .then(response => (this.data = response.data))
    }
  }
}
</script>

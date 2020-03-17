<template>
<div>
  <div class="container">
    <div class="columns">
      <div class="column is-6">
        <div v-if="data.length !== 0" class="card">
          <!-- <div class="card-image">
            <figure class="image is-4by3">
              <img src="https://bulma.io/images/placeholders/1280x960.png" alt="Placeholder image">
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="data.data.attributes.avatar.small.url" alt="Placeholder image">
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{`${data.data.attributes.first_name} ${data.data.attributes.last_name}`}}</p>
                <p class="subtitle is-6"><a :href="data.data.links.self.web" target="_blank">Смотреть профиль</a></p>
              </div>
            </div>

            <div class="content">
              {{data.data.attributes.cv}} <a>@bulmaio</a>.
              <a href="#">#css</a> <a href="#">#responsive</a>
              <br>
              <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
            </div>
          </div> -->
          {{ data }}
        </div>
        <b-loading v-else :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false"></b-loading>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { axiosInst } from '@/utils/http.js'

export default {
  name: 'FreelancersList',
  data: () => ({
    data: [],
    isLoading: true,
    isFullPage: true
  }),
  methods: {
    getProfileData () {
      axiosInst.get('freelancers')
        .then(response => (this.data = response.data))
    }
  },
  created () {
    this.getProfileData()
    this.isLoading = !this.isLoading
  }
}
</script>

<style lang="scss" scoped>
</style>

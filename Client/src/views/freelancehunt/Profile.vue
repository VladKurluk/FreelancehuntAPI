<template>
<div>
  <div class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-6">
          <div v-if="data.length !== 0" class="card">
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img :src="data.data.attributes.avatar.small.url" alt="Placeholder image">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">{{`${data.data.attributes.first_name} ${data.data.attributes.last_name}`}}</p>
                  <p class="subtitle is-6">{{`${data.data.type}`}}</p>
                  <!-- <p class="subtitle is-6"><a :href="data.data.links.self.web" target="_blank">Смотреть профиль на Freelancehunt</a></p> -->
                </div>
              </div>

              <div class="content">
                {{data.data.attributes.cv}}
                <br>
                  <a>@bulmaio</a>
                  <a href="#">#css</a>
                  <a href="#">#responsive</a>
                <br>
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
              </div>
            </div>
          </div>
          <!-- <b-loading v-else :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false"></b-loading> -->
        </div>

        <feed-list></feed-list>

        <!-- <div class="column is-6">
          <div v-if="feed.length !== 0" class="card">
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img :src="data.data.attributes.avatar.small.url" alt="Placeholder image">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">{{`${data.data.attributes.first_name} ${data.data.attributes.last_name}`}}</p>
                  <p class="subtitle is-6">{{`${data.data.type}`}}</p>
                  <p class="subtitle is-6"><a :href="data.data.links.self.web" target="_blank">Смотреть профиль на Freelancehunt</a></p>
                </div>
              </div>

              <div class="content">
                {{data.data.attributes.cv}}
                <br>
                  <a>@bulmaio</a>
                  <a href="#">#css</a>
                  <a href="#">#responsive</a>
                <br>
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
              </div>
            </div>
          </div>
          <b-loading v-else :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false"></b-loading>
        </div> -->
      </div>
    </div>
  </div>
  <router-view />
</div>
</template>

<script>
import { axiosInst } from '@/utils/http.js'
import FeedList from '@/components/Feed'

export default {
  components: {
    FeedList
  },
  data: () => ({
    data: [],
    isLoading: true,
    isFullPage: true
  }),
  methods: {
    async getProfileData () {
      await axiosInst.get('curent_profile')
        .then(response => (this.data = response.data))
    },
    async getFeedData () {
      await axiosInst.get('my_feed')
        .then(response => (this.feed = response.data.data))
    }
  },
  async created () {
    await this.getProfileData()
    this.isLoading = !this.isLoading
  }
}
</script>

<style lang="scss" scoped>
</style>

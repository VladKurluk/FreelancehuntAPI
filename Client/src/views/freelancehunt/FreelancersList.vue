<template>
<div class="section">
  <div class="container">
    <div class="columns">
      <div class="column is-4">
        <skills @skill="getFrelancersBySkill"/>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="columns">
      <div class="column is-12" v-if="data.length !== 0">
        <div class="box" v-for="person in data.data" :key="person.id">
          <article class="media">
            <div class="media-left">
              <figure class="image is-64x64">
                <img :src="person.attributes.avatar.small.url" alt="Image">
                <figcaption>{{person.attributes.rating}}</figcaption>
              </figure>
            </div>
            <div class="media-content">
              <div class="content">
                <p>
                  <strong>{{`${person.attributes.first_name} ${person.attributes.last_name} `}}</strong>
                  <small>@{{person.attributes.login }} </small>
                  <small>Профиль создан: {{person.attributes.created_at | time('time')}}</small>
                  <br>
                  {{person.attributes.cv}}
                </p>
                <p>
                  <b-taglist>
                    <b-tag
                      v-for="skill in person.attributes.skills"
                      :key="skill.id"
                      type="is-warning"
                    >
                      {{skill.name}}
                    </b-tag>
                  </b-taglist>
                </p>
              </div>
              <nav class="level is-mobile">
                <div class="level-left">
                  <a class="level-item" aria-label="reply" :href="person.links.self.web" target="_blank">
                    <span class="icon is-small">
                      <i class="fas fa-reply" aria-hidden="true"></i>
                    </span>
                  </a>
                  <!-- <a class="level-item" aria-label="retweet">
                    <span class="icon is-small">
                      <i class="fas fa-retweet" aria-hidden="true"></i>
                    </span>
                  </a>
                  <a class="level-item" aria-label="like">
                    <span class="icon is-small">
                      <i class="fas fa-heart" aria-hidden="true"></i>
                    </span>
                  </a> -->
                </div>
              </nav>
            </div>
          </article>
        </div>
      </div>
      <b-loading v-if="isLoading" :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false"></b-loading>
    </div>
  </div>
  <div class="container" v-if="data.links">
    <div class="columns">
      <div class="column is-12">
        <b-pagination
          :total="getPages"
          :current.sync="current"
          :range-before="rangeBefore"
          :range-after="rangeAfter"
          :order="order"
          :size="size"
          :simple="isSimple"
          :rounded="isRounded"
          :per-page="perPage"
          :icon-prev="prevIcon"
          :icon-next="nextIcon"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          @change="setPage">
        </b-pagination>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { axiosInstance } from '@/services/http.js'
import skills from '@/components/SkillList'

export default {
  name: 'FreelancersList',
  components: {
    skills
  },
  data: () => ({
    data: [],
    isLoading: true,
    isFullPage: false,
    skillId: null,
    // Pagination variables
    current: 1,
    perPage: 1,
    rangeBefore: 1,
    rangeAfter: 1,
    order: '',
    size: '',
    isSimple: false,
    isRounded: false,
    prevIcon: 'chevron-left',
    nextIcon: 'chevron-right'
  }),
  methods: {
    async getProfileData () {
      await axiosInstance.get('freelancers')
        .then(response => (this.data = response.data))
    },
    async getFrelancersBySkill (data) {
      this.skillId = data
      await axiosInstance.post('freelancers', {
        id: data,
        page: 1
      })
        .then(response => (this.data = response.data))
    },
    async setPage (value) {
      this.isLoading = true
      await axiosInstance.post('freelancers', {
        id: this.skillId,
        page: value
      })
        .then(response => (this.data = response.data))
      this.isLoading = false
    }
  },
  computed: {
    getPages () {
      if (this.data.links.last) {
        const totalPage = this.data.links.last
        return Number(totalPage.slice(totalPage.indexOf('page[number]=') + 13, totalPage.length))
      }
      return true
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

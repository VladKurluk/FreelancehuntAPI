<template>
  <div class="column is-6 feed">
    <div class="card" v-if="feedList.length">
      <h4 class="title is-3">Последние 40 проектов.</h4>
      <div class="box" v-for="feed in feedList" :key="feed.id">
        <article class="media">
          <div class="media-left" v-if="feed.attributes.from">
            <figure class="image is-64x64">
              <img :src="feed.attributes.from.avatar.small.url" alt="Image">
            </figure>
          </div>
          <div class="media-content">
            <div class="content">
              <p>
                <a
                  v-if="feed.attributes.from"
                  :href="feed.attributes.from.self"
                  target="_blank"
                >
                  Заказчик: {{ `${feed.attributes.from.first_name} ${feed.attributes.from.last_name}` }}
                </a>
                <small>Проект добавлен: {{ feed.attributes.created_at | time('time') }}</small>
                <br>
                {{feed.attributes.message | getProjectDescription}}
                <br>
                <a :href="getLink(feed.attributes.message)" target="_blank">Ссылка на проект</a>
              </p>
            </div>
            <!-- <nav class="level is-mobile">
              <div class="level-left">
                <a class="level-item" aria-label="reply">
                  <span class="icon is-small">
                    <i class="fas fa-reply" aria-hidden="true"></i>
                  </span>
                </a>
                <a class="level-item" aria-label="retweet">
                  <span class="icon is-small">
                    <i class="fas fa-retweet" aria-hidden="true"></i>
                  </span>
                </a>
                <a class="level-item" aria-label="like">
                  <span class="icon is-small">
                    <i class="fas fa-heart" aria-hidden="true"></i>
                  </span>
                </a>
              </div>
            </nav> -->
          </div>
        </article>
      </div>
    </div>

    <div v-else-if="error" class="card">
      <h4 class="title is-4">Ошибка Freelancehunt API 2.0</h4>
      <div class="box is-danger">
        <article class="media">
          <div class="media-content">
            <div class="content has-text-danger">
              <p>
                <strong class="has-text-danger">Код ошибки: {{error.status}}</strong>&nbsp;&nbsp;
                <strong class="has-text-danger">Сообщение ошибки: {{error.title}}</strong>
              </p>
            </div>
          </div>
        </article>
      </div>
    </div>
    <b-loading v-else :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false"></b-loading>
  </div>
</template>

<script>
import { axiosInstance } from '@/services/http.js'

export default {
  name: 'FeedList',
  data: () => ({
    feedList: [],
    error: null,
    isFullPage: false,
    isLoading: true
  }),
  methods: {
    async getFeedData () {
      await axiosInstance.get('/my_feed')
        .then(response => {
          if (response.data.data) {
            this.feedList = response.data.data
          } else {
            this.error = response.data.error
          }
        })
    },
    getLink (value) {
      return value.slice(value.indexOf('"') + 1, value.lastIndexOf('"'))
    }
  },
  filters: {
    getProjectDescription (value) {
      return value.slice(value.indexOf('>') + 1, value.lastIndexOf('<'))
    }
  },
  async created () {
    await this.getFeedData()
    this.isLoading = !this.isLoading
  }
}
</script>

<style lang="scss" scoped>
.feed {
  position: relative;
  height: 500px;
  overflow-y: scroll;
  .card {
    padding: 5px;

    .title.is-3 {
      position: sticky;
      top: -12px;
      background: #fff;
      width: 100%;
      z-index: 5;
    }
  }

  .box {
    &:last-child {
      margin-bottom: 10px;
    }
  }
}
</style>

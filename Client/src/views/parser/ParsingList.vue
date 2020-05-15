<template>
  <div class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-12">
          <h1 class="is-size-3 has-text-centered">Парсер сайта <a href="https://freelance.ua/orders/" target="_blank">freelance.ua</a></h1>
          <img class="frelanceua-logo" src="../../assets/FreelanceUa.png" alt="">
        </div>
      </div>
      <div class="columns is-multiline is-mobile">
        <div class="column is-half">
          <p class="is-size-5 has-text-left">Выбери категорию</p>
          <div class="buttons buttons-category">
            <b-button type="is-info" size="is-small" @click="category = 'verstka'">Верстка</b-button>
            <b-button type="is-info" size="is-small" @click="category = 'web-development'">Веб-программирование</b-button>
            <b-button type="is-info" size="is-small" @click="category = 'prikladnoj-programmist'">Прикладное программирование</b-button>
            <b-button type="is-info" size="is-small" @click="category = 'sajt-pod-kljuch'">Сайт «под ключ»</b-button>
            <b-button type="is-info" size="is-small" @click="category = 'refinement-sites'">Доработка сайтов</b-button>
          </div>
        </div>
        <div class="column is-half">
          <p class="is-size-5 has-text-left">Или запиши транслитерацию категории</p>
          <div class="columns">
            <div class="column is-6">
              <b-field label="Транслитерация категории">
                <b-input v-model="category"></b-input>
              </b-field>
            </div>
            <div class="column is-4">
              <b-field label="Кол-во страниц">
                <b-input v-model.number="pageCount"></b-input>
              </b-field>
            </div>
            <div class="column is-2">
              <b-button type="is-warning" @click="parsing" class="parse-btn">Cпарсить</b-button>
            </div>
          </div>
        </div>
      </div>
      <div class="columns is-multiline is-mobile" >
        <div class="column is-12" v-show="data.page_total && !data.error">
          <p class="is-size-4 has-text-left">Спаршено страниц <span class="tag is-warning">{{data.page_total}}</span><br />Получено заказов <span class="tag is-warning">{{data.total}}</span>
          </p>
        </div>
        <div class="column is-12">
          <b-table
            v-if="data.result && !parseProgress"
            :data="data.result"
            ref="table"
            paginated
            per-page="20"
            :opened-detailed="defaultOpenedDetails"
            detailed
            detail-key="id"
            :show-detail-icon="showDetailIcon"
            :row-class="(row, index) => row.pro === true && 'order-pro'"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page">
            <template slot-scope="props">
              <b-table-column field="id" label="ID" width="40" numeric sortable>
                {{ props.row.id }}
              </b-table-column>

              <b-table-column field="title" label="Заголовок" width="400">
                <template v-if="showDetailIcon">
                  <a :href="props.row.link" target="_blank">
                    {{ props.row.title }}
                  </a>
                </template>
                <template v-else>
                  <a @click="toggle(props.row)">
                    {{ props.row.title }}
                  </a>
                </template>
              </b-table-column>

              <b-table-column field="price" label="Цена" sortable>
                {{ props.row.price }}
              </b-table-column>

              <b-table-column field="work_type" label="Type" sortable>
                <b-tooltip :label="props.row.work_type" type="is-info">
                  <b-icon
                    v-if="props.row.work_type === 'Постоянная работа'"
                    icon="briefcase"
                    size="is-small">
                  </b-icon>
                  <b-icon
                    v-else
                    icon="briefcase-outline"
                    size="is-small">
                  </b-icon>
                </b-tooltip>
              </b-table-column>

              <b-table-column field="date" label="Опубликовано" sortable centered>
                <span class="tag is-success">
                  {{ props.row.published }}
                </span>
              </b-table-column>

              <b-table-column label="Дедлайн">
                {{  props.row.active_to }}
              </b-table-column>

              <b-table-column field="offers" label="Кол-во откликов" sortable>
                {{  props.row.offers }}
              </b-table-column>

              <b-table-column label="Действия">
                <b-tooltip label="В избранное" type="is-info">
                  <b-button type="is-success" icon-right="star" @click="save(props.row)"/>
                </b-tooltip>
              </b-table-column>
            </template>

            <template slot="detail" slot-scope="props">
              <article class="media">
                <div class="media-content">
                  <div class="content">
                    <p>
                      <strong>Город: {{ props.row.city }}</strong>
                      <!-- <small>@{{ props.row.user.first_name }}</small>
                      <small>31m</small> -->
                      <br>
                      {{ props.row.description }}
                    </p>
                  </div>
                </div>
              </article>
            </template>
          </b-table>
          <div v-if="data.error && !parseProgress" class="is-size-4 has-text-center has-text-danger has-background-grey-lighter">
            <p>Ошибка парсинга: {{data.error}}</p>
            <p class="has-text-black-ter">Проверьте правильность параметров</p>
          </div>
          <b-progress v-show="parseProgress" size="is-medium" type="is-success"></b-progress>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FreelanceUa',
  data: () => ({
    category: '',
    pageCount: 0,
    parseProgress: false,
    defaultOpenedDetails: [0],
    showDetailIcon: true
  }),
  computed: {
    data () {
      return this.$store.state.parser.parsingResult
    }
  },
  methods: {
    async parsing () {
      this.parseProgress = true
      await this.$store.dispatch('getProfileData', {
        category: this.category,
        page: this.pageCount
      })
      this.parseProgress = false
    },
    toggle (row) {
      this.$refs.table.toggleDetails(row)
    },
    save (row) {
      this.$buefy.notification.open({
        message: `Заказ "${row.title}" добавлен в избранное!`,
        type: 'is-success'
      })
    }
  }
}
</script>

<style lang="scss">
tr.order-pro {
  background: hsl(348, 100%, 61%);
  color: #fff;

  a {
    color: #fff;
  }
}
</style>

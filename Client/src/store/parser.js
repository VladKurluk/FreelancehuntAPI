import { axiosParserInst } from '@/services/http.js'

export default {
  state: {
    parsingResult: []
  },
  mutations: {
    updateData (state, payload) {
      state.parsingResult = payload
    }
  },
  actions: {
    async getProfileData ({ commit }, { category, page }) {
      await axiosParserInst.post('freelance_ua', {
        category,
        page
      })
        .then(response => (commit('updateData', response.data)))
    }
  }
}

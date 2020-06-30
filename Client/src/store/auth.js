/* It is auth.module.js file in Vue project. Which is located into src/store folder. It is Vuex file */
import { AuthService, AuthenticationError } from '@/services/auth.service'
import { TokenService } from '@/services/storage.service'
import router from '../router'
import { ToastProgrammatic as Toast } from 'buefy'

const state = {
  authenticating: false,
  accessToken: TokenService.getToken(),
  authenticationErrorCode: 0,
  authenticationError: '',
  refreshTokenPromise: null, // Holds the promise of the refresh token
  registrationProcess: false,
  registrationSuccess: false,
  registrationErrorCode: 0,
  registrationError: '',
  userName: ''
}

const getters = {
  loggedIn: (state) => {
    return !!state.accessToken
  },

  authenticating: (state) => {
    return state.authenticating
  }
}

const actions = {
  async registration ({ commit }, data) {
    commit('registrationRequest')

    try {
      const response = await AuthService.registration(data)
      commit('registerSuccess')
      router.push('/login')
      Toast.open({
        duration: 2500,
        message: response.data.message,
        position: 'is-top-right',
        type: 'is-success'
      })
    } catch (e) {
      if (e instanceof AuthenticationError) {
        commit('registerError', {
          errorCode: e.errorCode,
          errorMessage: e.message
        })
      }

      Toast.open({
        duration: 2500,
        message: e.message,
        position: 'is-top-right',
        type: 'is-danger'
      })
    }
  },
  async login ({ commit }, userData) {
    commit('loginRequest')

    try {
      const authResponse = await AuthService.login(userData)

      commit('loginSuccess', authResponse)
      // Редирект пользователя на страницу, которую он пытался посетить, или на домашнюю страницу.
      router.push(router.history.current.query.redirect || '/')

      return true
    } catch (e) {
      if (e instanceof AuthenticationError) {
        commit('loginError', {
          errorCode: e.errorCode,
          errorMessage: e.message
        })
      }

      Toast.open({
        duration: 2500,
        message: e.message,
        position: 'is-top-right',
        type: 'is-danger'
      })

      return false
    }
  },
  logout ({ commit }) {
    AuthService.logout()
    commit('logoutSuccess')
    router.push('/login')
  },
  refreshToken ({ commit, state }) {
    // If this is the first time the refreshToken has been called, make a request
    // otherwise return the same promise to the caller
    if (!state.refreshTokenPromise) {
      const p = AuthService.refreshToken()
      commit('refreshTokenPromise', p)

      // Wait for the AuthService.refreshToken() to resolve. On success set the token and clear promise
      // Clear the promise on error as well.
      p.then(
        response => {
          commit('refreshTokenPromise', null)
          commit('refreshTokenSuccess', response)
        },
        _error => {
          commit('refreshTokenPromise', null)
        }
      )
    }

    return state.refreshTokenPromise
  }
}

const mutations = {
  registrationRequest (state) {
    state.registrationProcess = true
    state.registrationError = ''
    state.registrationErrorCode = 0
  },

  loginRequest (state) {
    state.authenticating = true
    state.authenticationError = ''
    state.authenticationErrorCode = 0
  },

  registerSuccess (state) {
    state.registrationSuccess = true
    state.registrationProcess = false
  },

  loginSuccess (state, data) {
    state.accessToken = data.access_token
    state.userName = data.username
    state.authenticating = false
  },

  refreshTokenSuccess (state, data) {
    state.accessToken = data
    state.authenticating = false
  },

  registerError (state, { errorCode, errorMessage }) {
    state.registrationProcess = false
    state.registrationErrorCode = errorCode
    state.registrationError = errorMessage
  },

  loginError (state, { errorCode, errorMessage }) {
    state.authenticating = false
    state.authenticationErrorCode = errorCode
    state.authenticationError = errorMessage
  },

  logoutSuccess (state) {
    state.accessToken = ''
  },

  refreshTokenPromise (state, promise) {
    state.refreshTokenPromise = promise
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

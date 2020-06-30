import axios from 'axios'
import store from '@/store'
import { TokenService } from './storage.service'

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/v1',
  timeout: 5000
})

const AxiosService = {
  setHeader () {
    axiosInstance.defaults.headers.common.Authorization = `Bearer ${TokenService.getToken()}`
  },
  removeHeader () {
    axios.defaults.headers.common = {}
  },
  _401interceptor: null,
  mount401Interceptor () {
    this._401interceptor = axiosInstance.interceptors.response.use(
      (response) => {
        // Запрос через интерцептор.
        return response
      },
      async (error) => {
        if (error.request.status === 401) {
          // Обработка. Если код ошибки 401 (неавторизован).
          if (error.config.url === 'http://127.0.0.1:5000/api/v1/auth/refresh_token') {
            // Токен обновления (refresh_token) просрочен. Разлогин.
            await store.dispatch('auth/logout')
            throw error
          } else {
            // Обновление токена доступа (access_token)
            try {
              await store.dispatch('auth/refreshToken')
              // Выполняеться повторный запрос с обновленным токеном и перехваченными параметрами.
              return axiosInstance({
                method: error.config.method,
                url: error.config.url,
                data: error.config.data
              })
            } catch (e) {
              // Обновление токена не удалось. Пропускаем ошибку.
              throw error
            }
          }
        }

        // Если код ошибки не 401, пропускаем ее как есть.
        throw error
      }
    )
  },
  unmount401Interceptor () {
    // Интерцептор размонтирован. Перехват запросов не осуществляеться.
    axios.interceptors.response.eject(this._401interceptor)
  }
}

export { axiosInstance, AxiosService }

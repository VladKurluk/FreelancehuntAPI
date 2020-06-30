/* It is auth.service.js file in Vue project. Which is located into src/services folder */
import { axiosInstance, AxiosService } from '@/services/http.js'
import { TokenService } from '@/services/storage.service'

// Класс кастомных ошибок прт авторизации/регистрации
class AuthenticationError extends Error {
  constructor (errorCode, message) {
    super(message)
    this.name = this.constructor.name
    this.message = message
    this.errorCode = errorCode
  }
}

const AuthService = {
  /**
   * Регистрация пользователя.
   * @returns axios response
   * @throws AuthenticationError
   **/
  registration: async function (data) {
    try {
      return await axiosInstance.post('/auth/register', data)
    } catch (error) {
      throw new AuthenticationError(error.response.data.status, error.response.data.message)
    }
  },
  /**
   * Авторизация в системе и сохранение токенов (доступа и обновления).
   * @returns axios response
   * @throws AuthenticationError
   **/
  login: async function (data) {
    try {
      const response = await axiosInstance.post('/auth/login', data)

      TokenService.saveToken(response.data.access_token)
      TokenService.saveRefreshToken(response.data.refresh_token)
      AxiosService.setHeader()

      // Монтирование Axios перехватчика запросов
      // AxiosService.mount401Interceptor()

      return response.data
    } catch (error) {
      throw new AuthenticationError(error.response.data.status, error.response.data.message)
    }
  },
  /**
   * Обновление токена доступа (access_token).
   * @returns access_token
   * @throws AuthenticationError
   **/
  refreshToken: async function () {
    const refreshToken = await TokenService.getRefreshToken()

    try {
      // Подмена заголовка запроса токеном обновления (refresh_token)
      axiosInstance.defaults.headers.common.Authorization = `Bearer ${refreshToken}`
      const response = await axiosInstance.post('/auth/refresh_token')
      TokenService.saveToken(response.data.access_token)
      // Обновление заголовка запроса обновленным токеном доступа (access_token)
      AxiosService.setHeader()
      return response.data.access_token
    } catch (error) {
      throw new AuthenticationError(error.response.data.status, error.response.data.message)
    }
  },
  /**
   * Выход из системы, удаление токенов из хранилища.
   * И удаление заголовка `Authorization Bearer <token>`.
   **/
  logout () {
    TokenService.removeToken()
    TokenService.removeRefreshToken()
    AxiosService.removeHeader()

    // Отмонтирование Axios перехватчика запросов
    AxiosService.unmount401Interceptor()
  }
}

export {
  AuthService,
  AuthenticationError
}

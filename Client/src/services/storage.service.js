/* It is storage.service.js file in Vue project.
*  Which is located into src/services folder
*/
const TOKEN_KEY = 'access_token'
const REFRESH_TOKEN_KEY = 'refresh_token'
const USER_NAME = 'user_name'

/**
 * Сохранение, удаление и доступ к токенам, которые храняться в localStorage.
 **/
const TokenService = {
  getToken () {
    return localStorage.getItem(TOKEN_KEY)
  },

  saveToken (accessToken) {
    localStorage.setItem(TOKEN_KEY, accessToken)
  },

  removeToken () {
    localStorage.removeItem(TOKEN_KEY)
  },

  getRefreshToken () {
    return localStorage.getItem(REFRESH_TOKEN_KEY)
  },

  saveRefreshToken (refreshToken) {
    localStorage.setItem(REFRESH_TOKEN_KEY, refreshToken)
  },

  removeRefreshToken () {
    localStorage.removeItem(REFRESH_TOKEN_KEY)
  },

  saveUserName (name) {
    localStorage.setItem(USER_NAME, name)
  },

  removeUserName () {
    localStorage.removeItem(USER_NAME)
  }

}

export {
  TokenService
}

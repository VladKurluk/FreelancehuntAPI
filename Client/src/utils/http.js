import axios from 'axios'

const axiosInst = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/v1/',
  timeout: 1000
})

export default axiosInst

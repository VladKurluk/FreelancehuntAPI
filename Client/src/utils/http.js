import axios from 'axios'

const axiosInst = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/v1/',
  timeout: 1000
})

const axiosParserInst = axios.create({
  baseURL: 'http://127.0.0.1:5000/'
})

export { axiosInst, axiosParserInst }

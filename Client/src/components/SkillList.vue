<template>
  <b-field label="Специализация">
    <b-select placeholder="Выбрать специализацию" @input="setSkill">
      <option
        v-for="option in data"
        :value="option.id"
        :key="option.id"
      >
        {{ option.name }}
      </option>
    </b-select>
  </b-field>
</template>

<script>
import { axiosInst } from '@/services/http.js'
export default {
  name: 'skills',
  data: () => ({
    data: []
  }),
  methods: {
    async getSkills () {
      await axiosInst.get('skills')
        .then(response => (this.data = response.data.data))
    },
    setSkill (val) {
      this.$emit('skill', val)
    }
  },
  async created () {
    await this.getSkills()
  }
}
</script>

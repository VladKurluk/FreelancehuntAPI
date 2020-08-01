<template>
  <main class="auth-layout">
    <router-view class="auth-layout__form" />
    <app-footer />
  </main>
</template>

<script>
import AppFooter from '@/layouts/components/Footer.vue'
export default {
  components: {
    AppFooter
  }
}
</script>

<style lang="scss">
.auth-layout {
  display: grid;
  grid-template-areas:
                      "form"
                      "footer";
  background-color: rgba(70, 107, 132, 0.95);

  &__form {
    grid-area: form;
    height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  &__footer {
    grid-area: footer;
    height: 100px;
  }
}

@media all and (max-width: 480px) {
  .auth-layout {
    &__footer {
      max-width: 480px;
      min-height: 100px;
      height: auto;
    }
  }
}
</style>

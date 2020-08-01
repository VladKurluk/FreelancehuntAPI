<template>
  <footer class="auth-layout__footer app-footer">
    <div class="app-footer__info">
      <p class="app-footer__link-in-text">
        Сайт работает на фреймворках
        <a
          href="https://flask.palletsprojects.com/en/1.1.x/"
          target="_blank"
        >Flask</a> и
        <a href="https://ru.vuejs.org/" target="_blank">Vue.js</a>
      </p>
      <p class="app-footer__link-icon-in-text">
        Разработал:
        <a
          href="https://www.linkedin.com/in/%D0%B2%D0%BB%D0%B0%D0%B4%D0%B8%D1%81%D0%BB%D0%B0%D0%B2-%D0%BA%D1%83%D1%80%D0%BB%D1%83%D0%BA-71849a139/"
          target="_blank"
        >
          <b-icon icon="linkedin-box"></b-icon>
        </a>
      </p>
    </div>
    <div class="app-footer__copyright">&copy; {{new Date().getFullYear()}} Все права защищены.</div>
    <div class="app-footer__links">
      <a
        class="app-footer__icon-link"
        href="https://github.com/VladKurluk/FreelancehuntAPI"
        target="_blank"
      >
        <b-icon icon="github-circle"></b-icon>
      </a>
    </div>
  </footer>
</template>

<style lang="scss">
.app-footer {
  width: 100%;
  padding: 10px 30px;
  background-color: #24292e;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: hsla(0, 0%, 100%, 0.7);

  &__info {
    width: 33%;
    text-align: left;
  }

  &__copyright {
    width: 33%;
    text-align: center;
  }

  &__links {
    width: 33%;
    text-align: right;
  }

  &__icon-link {
    color: hsla(0, 0%, 100%, 0.7);

    &:hover {
      color: #4f728a;
    }
  }

  &__link-in-text {
    a {
      text-decoration: underline;
      color: #4f728a !important;
    }
  }

  &__link-icon-in-text {
    display: flex;
    align-items: center;
    margin-top: 5px;

    a {
      margin-left: 15px;
      color: hsla(0, 0%, 100%, 0.7);
      align-self: baseline;

      &:hover {
        color: #4f728a;
      }
    }
  }
}

@media all and (max-width: 992px) {
  .app-footer {
    &__info {
      width: 50%;
    }
    &__copyright {
      width: 40%;
      text-align: right;
    }
    &__links {
      width: 10%;
    }
  }
}

@media all and (max-width: 480px) {
  .app-footer {
    flex-direction: column;
    padding: 10px;
    &__info {
      width: 100%;
      text-align: left;
    }
    &__copyright {
      width: 100%;
      text-align: left;
    }
    &__links {
      width: 100%;
      text-align: center;
    }
  }
}
</style>

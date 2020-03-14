<template>
  <div id="app">
    <sidebar-menu :menu="menu" />
    <router-view/>
  </div>
</template>

<script>
export default {
  data: () => ({
    menu: [
      {
        header: true,
        title: 'Navigation',
        hiddenOnCollapse: true
      },
      {
        href: '/',
        title: 'Home Page',
        icon: 'fa fa-user'
      },
      {
        href: '/frelance_api',
        title: 'Freelancehunt',
        icon: 'fa fa-chart-area',
        child: [
          // {
          //   href: '/charts/sublink',
          //   title: 'Sub Link'
          // }
        ]
      }
    ]
  })
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

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
        icon: 'fa fa-chart-area'
      },
      {
        href: '/profile',
        title: 'Profile',
        icon: 'fa fa-user',
        child: [
          {
            href: '/all_frelancers',
            title: 'Freelancers list',
            icon: 'fas fa-users'
          }
        ]
      },
      {
        href: '/parser',
        title: 'Parsing',
        icon: 'fas fa-server'
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

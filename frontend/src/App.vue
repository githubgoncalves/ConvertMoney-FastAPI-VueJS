<template>
  <div id="app">
    <Dashboard />
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Dashboard from './components/Dashboard.vue'

export default {
  name: 'App',
  components: {
    Dashboard
  },
  data: () => ({
    //
  }),
  mounted() {
    document.title = "Convert Money";
  }
};
</script>

<style>
  @import './assets/styles/global.css';
</style>
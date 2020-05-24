<template>
  <div id="app">
    <nav-bar />
        <router-view/>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar
  }
}

</script>

<!--
black: #080f0fff;
white: #fcfcfcff;
teal: #1b9aaaff;
orange: #ffa400ff;
green: #31e981ff;
-->


<style scoped>
  #app {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    font-family: 'Open Sans', sans-serif;
    background-color: #080f0fff;
  }
</style>

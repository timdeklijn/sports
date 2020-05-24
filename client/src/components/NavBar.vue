<template>
  <div class="nav">
    <a class="active"><router-link to="/">Sports</router-link></a>
    <a><router-link to="/exercises">Exercises</router-link></a>
  </div>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped>
.nav {
  width: 100%;
  margin: 0;
  padding: 0;
  background-color: #080f0fff;
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.nav a {
  float: left;
  color: #fcfcfcff;
  text-align: center;
  padding: 0.25rem 2.0rem;
  text-decoration: none;
  font-size: 1.5rem;
}

/* Change the color of links on hover */
.nav a:hover {
  color: #fcfcfcff;
  background-color: #1b9aaaff;
}

/* Add a color to the active/current link */
.nav a.active {
  background-color: #1b9aaaff;
  color: #fcfcfcff;
}

</style>

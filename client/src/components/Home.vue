<template>
  <div class="container">
    <div class="container-content">
      <h1>Home</h1>
      <p>This is the home component</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
h1 {
  text-align: center;
  font-size: 3rem;
  color: #1b9aaaff;
}
p {
  color: #fcfcfcff;
}
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80%;
}
</style>

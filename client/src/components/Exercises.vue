<template>
  <div class="container">
    <div class="container-content">
      <h1>Exercises</h1>
      <p>A list of all regiestered exercises as well as a form to register an exercise.</p>
    <div>
    <form>
      <p>Name of the Exercise:
        <input type="text">
      </p>
      <p>Link to the exercise:
        <input type="text">
      </p>
      <p>Description of the exercise (in Markdown):
        <textarea rows="20" cols="70"></textarea>
      </p>
    </form>
  </div>
  </div>
    </div>
</template>

<script>
export default {
  name: 'Exercises'
}
</script>

<style scoped>
h1 {
  text-align: center;
  font-size: 4rem;
  color: #1b9aaaff;
}
p {
  color: #fcfcfcff;
  font-size: 1.25rem;
}
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80%;
}

</style>

<template>
      <footer class="mt-5 bg-dark">
          <div class="container">
              <p>&copy; {{ year }} Apex Management Services Ltd. | All Rights Reserved</p>
          </div>
      </footer>
</template>

<script>
export default {
    data() {
      return {
          year: (new Date).getFullYear()
      }        
    }
}
</script>

<style>
    footer{
        color: whitesmoke;
        position: fixed;
        bottom:0;
        width: 100%;
        padding: 1.5em;
    }

</style>
<template>
  <div class="about container">
    <h2>About</h2>
    <p>This is an about page.</p>
  </div>
</template>

<script>

export default{

  created(){
    const menuitems = document.querySelectorAll(" ul li a");

    menuitems.forEach((menuitem)=>{
        menuitem.classList.remove("active");
    });

    document.querySelector("ul li a#about").classList.add("active");
  }
}

</script>

<style>
</style>

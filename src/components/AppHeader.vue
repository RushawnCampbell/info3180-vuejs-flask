<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container-fluid">
      <section id="brandcombo">
       
        <RouterLink v-if=isauth to="/search">  <img id="logo" src="../assets/images/apex-logo.png"/> </RouterLink>
        <RouterLink v-else to="/">  <img id="logo" src="../assets/images/apex-logo.png"/> </RouterLink>
      </section>

      <section id="menuitems">
          <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" v-if=!isauth id="home" class="nav-link ">HOME</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink  id="about" class="nav-link" to="/about">ABOUT</RouterLink>
            </li>

            <li id="search" v-if=isauth class="nav-item">
              <RouterLink id="search" class="nav-link" to="/search">SEARCH</RouterLink>
            </li>

            <li id="signout" v-if=isauth class="nav-item">
              <RouterLink  id="signout" class="nav-link" to="/signout">SIGN OUT </RouterLink>
            </li>
            <li id="signin" v-else>
            <RouterLink id="signin" class="nav-link" to="/signin">SIGN IN</RouterLink>
            </li>
          </ul>
        </div>
      </section>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";


export default {
    data() {
        return {
          uid: sessionStorage.getItem('uid'),
          isauth: sessionStorage.getItem('isauth')
        };
    },
    created(){

    let self = this;
    setInterval(()=>{
       if (sessionStorage.getItem('isauth') == 'true'){
          self.isauth = true;
       }
       else{
          self.isauth = false;
       }
    }, 500);
    
    }
}
</script>

<style>
/* Add any component specific styles here */

header{
  margin-bottom: 0;
}
img#logo{
  width: 20rem;
  margin: 0 1em 0 1em;
}

nav, div.container-fluid{
  display: flex;
  flex-flow: row wrap;
  justify-content: space-evenly;
}

div.container-fluid section#brandcombo, section#menuitems{
  display: flex;
  flex-flow: row wrap;
  align-items: center;
}

a#logotext{
  font-size: 2em;
  color: #DF0909;
}
</style>
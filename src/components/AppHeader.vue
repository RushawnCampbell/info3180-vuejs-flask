<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
      <img id="carlogo" src="../assets/carlogo.png"/>
      <a class="navbar-brand" href="/">United Auto Sales</a>
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
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>

            <li  id="addcar" v-if="`${isauth}` == 'true'" class="nav-item" >
              <RouterLink class="nav-link" to="/cars/new">Add Car</RouterLink>
            </li>

            <li id="explore" v-if="`${isauth}` == 'true'" class="nav-item" >
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>

            <li id="profile" v-if="`${isauth}` == 'true'" class="nav-item">
              <RouterLink class="nav-link" :to="{path: '/users/'+ uid}" >My Profile</RouterLink>
            </li>

          <li id="logout" v-if="`${isauth}` == 'true'" class="nav-item">
            <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
          </li>
          <li id="login" v-else>
          <RouterLink class="nav-link" to="/login">Login</RouterLink>
          </li>

          <li id="logout" v-if="`${isauth}` == 'true'" class="nav-item">
          </li>
          <li id="login" v-else>
          <RouterLink class="nav-link" to="/register">Register</RouterLink>
          </li>

          </ul>
        </div>
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
          isauth: localStorage.getItem('authed')
        };
    },
    created(){

    let self = this;
    setInterval(()=>{
       self.isauth = localStorage.getItem('authed');
    }, 1000);
    
    }
}
</script>

<style>
/* Add any component specific styles here */

header{
  margin-bottom: 0;
}
img#carlogo{
  width: 1.25rem;
  margin: 0 1em 0 1em;

}
.hide{
    visibility: none;
}

.show{
    visibility: visible;
}
</style>
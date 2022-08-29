<template>
   <div id="rowcontentimg">
    <section class="content">

      <h3> SKIPTRACING PORTAL</h3>
        <RouterLink  to="/signin" class=" btn btn-success">Sign in</RouterLink>
        <span>OR</span>
        <RouterLink to="/about" class=" btn btnsignin">Learn More</RouterLink>
        
    
    </section>
  

    <section class="image">
          <img src="../assets/images/skiptracehome.png"/>
    </section>
   </div>
</template>



<script>
 


</script>


<style>
/* Add any component specific styles here */

*{
  box-sizing: content-box;
  padding: 0;
  margin: 0;
}

.btn{
  width: 30%;
}

.btn:hover{
  color: whitesmoke;
}

.btnsignin{
  background: #0E086D;
  color: #fff;
}

div#rowcontentimg {
  display: flex;
  flex-flow: row wrap;
  width:100%;
  height: 80%;
  margin:0;
  padding:0;

}

section.image{
  display: flex;
  width: 50%;
  height:80%;
}

section.image img{
  width: 100%;
  height:80%;
}

section.content{
  display: flex;
  flex-flow: column wrap;
  width:50%;
  justify-content: center;
  align-items: center;
  
}

section.content h3{
  color: #666;
 
}
section.content a{
  margin: 1em 0 1em 0;
  font-size: 1.5em;
  font-weight:900;
  border-radius: 2em;
}
</style>
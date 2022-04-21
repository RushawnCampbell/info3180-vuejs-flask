<script>
import CarList from "../components/CarList.vue";
import Search from "../components/Search.vue";
export default {
    data() {
      return[]; 
    },
    components: {Search, CarList}        
};
</script>

<template>
<section id="exploreparent">
<h3>Explore</h3>
<Search/>
<CarList/>
</section>
    
</template>

<style>
h3{
    font-weight: bold;
}
section#exploreparent{
    width: 70%;
    display: flex;
    flex-flow: column wrap;
    margin: auto;
}
</style>
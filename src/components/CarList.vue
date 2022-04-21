<template>

<div id="carsparent">
    <div v-for= "car in cars" class="card">
        <img class="card-img-top" v-bind:src= car.photo v-bind:alt=car.car_type>
        <div class="card-body">
            <section class="card-title"> <span>{{ car.year }} {{car.make}}</span> <span id="pricespan"><img src="../assets/price-tag.png" /> {{car.price}}</span></section>
            <p class="card-text">{{car.model}}</p>
            <button  class=" btn-primary" > <RouterLink :to="{path: '/cars/'+ car.id}" class="nav-link ">view more details</RouterLink> </button>
        </div>
    </div>
</div>

</template>

<script>
export default {
    data() {
        return {
            cars: [],
            searchTerm: ''
        };
    },
    created() {
        let self = this;
        fetch('/api/cars',
        {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            console.log(data);
            self.cars = data;
        });
    },
};
</script>

<style>


div#carsparent{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-column-gap: 2em;
    width: 100%;
    margin-top: 2em;
    justify-content: center;
    justify-items: center;
    align-content: center;
    align-items: center;
}

div.card{
    width: 100%;
}

section.card-title{
    display: flex;
    flex-flow: row wrap;
}

span#pricespan{
    background: #41B883;
    color: #fff;
    margin-left: 1em;
    width: fit-content;
    padding: 0.05em 0.3em 0.05em 0.3em;
    border-radius: 0.5em;
}

span#pricespan img{
    width: 1em;
}
button a{
  color: #fff !important;
  padding:0;
  margin: 0;
}

button{
    padding:.05em;
    border-radius: .5em;
    width: 100%;
    margin-top: 2rem;
}

</style>
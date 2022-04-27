<template>


<section id="exploreparent">
    <section id="msg" class=" form-control alert hide" >
        {{messages}}
    </section>
    <div class="usercard">
        <section class="userphoto"> 
             <img v-bind:src="`/uploads/${user.photo}`" v-bind:alt=user.username >
        </section>
        <section class="usercontent"> 
            <h3>{{user.name}}</h3>
            <span id="username">@{{user.username}}</span>
            <p>{{user.biography}}</p>
            <section class="inforow">
                <div class="infoitem"><label>Email</label> <span>{{user.email}}</span></div>
            </section>
            <section class="inforow">
                <div class="infoitem"><label>Location</label> <span>{{user.location}}</span></div>
            </section>

            <section class="inforow">
                <div class="infoitem"><label>Joined</label> <span>{{user.date_joined}}</span></div>
            </section>
            
        </section>
 </div>

    <h3>Cars Favourited</h3>
    <div id="usercarsparent">
        <div v-for= "car in cars" class="card">
            <img class="card-img-top" v-bind:src= car.photo v-bind:alt=car.car_type>
            <div class="card-body">
                <section class="card-title"> <span>{{ car.year }} {{car.make}}</span> <span id="pricespan"><img src="../assets/price-tag.png" /> {{car.price}}</span></section>
                <p class="card-text">{{car.model}}</p>
                <button class="cardbtn btn-primary" > <RouterLink :to="{path: '/cars/'+ car.id}" class="nav-link ">view more details</RouterLink> </button>
            </div>
        </div>
    </div>

</section>

</template>

<script>
export default {
    data() {
        return {
            messages: '',
            cars: [],
            user:{}
        };
    },
    created() {
        let self = this;
        let stat = 0;
        let alertcontainer =  document.querySelector('section#msg');
        fetch(`/api/users/${sessionStorage.getItem('uid')}`,
        {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        })
        .then(function(response) {
            stat = response.status;
            return response.json();
        })
        .then(function(data) {
            if(stat == 200){
                self.user = data;
            }
            else if (stat == 401){
                self.messages = data.message;   
                alertcontainer.classList.remove('alert-success');
                alertcontainer.classList.add('alert-danger');
                alertcontainer.classList.remove('hide');
                alertcontainer.classList.add('show');
            }
        });

        fetch(`/api/users/${sessionStorage.getItem('uid')}/favourites`,
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
            if(stat == 200){
                self.cars = data;
            }
            else if (stat == 401){
                self.messages = data.message;   
                alertcontainer.classList.remove('alert-success');
                alertcontainer.classList.add('alert-danger');
                alertcontainer.classList.remove('hide');
                alertcontainer.classList.add('show');
            }
        });
    },
};
</script>

<style>


div#usercarsparent{
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

button.cardbtn{
    padding:.05em;
    border-radius: .5em;
    width: 100%;
    margin-top: 2rem;
}

h3{
    font-weight: bold;
}
section#exploreparent{
    width: 70%;
    display: flex;
    flex-flow: column wrap;
    margin: auto;
}

div.usercard{
    display: flex;
    flex-flow: row wrap;
    width: 100%;
    margin: 4em auto;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;
}

section.userphoto{
    width: 25%;
    padding: 2em;
    display: flex;
    flex-flow: column wrap;
    align-items: flex-start;
    justify-items: center;
}
section.usercontent{
    display: grid;
    grid-template-columns: 1fr;
    width: 75%;
    align-items: start;
    justify-content: start;
    padding: 1.5em;
    margin-bottom:4em;
}

section.usercontent p{
    margin-top: 1em;
}

h3{
    font-weight: bold;
    margin-bottom: 0;
}

section.inforow{
   display: flex;
   flex-flow: row wrap;
   width: 80%;
}

div.infoitem{
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
    width: 100%;
}

div.infoitem label{
    width:50%;
}

div.infoitem span{
    width:50%;
}

div.infoitem span{
    text-align: left;
}


span#username, p, label{
    color: #949599;
}
span#username{

    font-weight: bold;
}

div.usercard section.userphoto img{
   width: 80%;
   border-radius: 50%;
}


</style>
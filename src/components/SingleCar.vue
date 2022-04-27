<template>
<section id="msg" class=" form-control alert hide" >
    {{messages}}
</section>
 <div class="singlecarparent">
    <section class="singlecarphoto"> 
        <img v-bind:src="`/uploads/${car.photo}`" v-bind:alt=car.car_type >
    </section>
    <section class="singlecarcontent"> 
        <h3> {{car.year}} {{car.make}}</h3>
        <span id="model">{{car.model}}</span>
        <p>{{car.description}}</p>
        <section class="carinforow">
            <div class="carinfoitem"><label>Color</label> <span>{{car.colour}}</span></div>
            <div class="carinfoitem"><label>Body Type</label> <span>{{car.car_type}}</span></div>
        </section>
        <section class="carinforow">
            <div class="carinfoitem"><label>Price</label> <span>{{car.price}}</span></div>
            <div class="carinfoitem"><label>Transmission</label> <span>{{car.transmission}}</span></div>
        </section>

        <section  id="interact" class="carinforow">
        <button type="submit" class="btn_ btn-success" >Email Owner</button>
        <button id="likebtn" type="submit" v-on:click="addfave" class="btn_ btn-success" ><img class="unfavourited" src="../assets/like.svg"></button>
        </section>
        
    </section>
 </div>
</template>
<script>
export default {
    data() {
        return {
            messages: '',
            car: {},
            favourited: false,
        };
    },
    methods: {

        addfave(){
            let self = this;
            let stat = 0;
            let alertcontainer =  document.querySelector('section#msg');
            fetch(`/api/cars/${this.$route.params.car_id}`,
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
                self.car = data
            });
          
            fetch(`/api/cars/${this.$route.params.car_id}/favourite`,
            {
                method: 'POST',
                body: JSON.stringify({
                    "car_id": self.car.id,
                    "user_id": sessionStorage.getItem('uid')
                }),
                headers: {
                    'Accept': 'application/json',
                    'X-CSRFToken': this.csrf_token,
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
            })
            .then(function(response) {
                stat = response.status
                return response.json();
            })
            .then(function(data) {
                const likeimage =  document.querySelector("button#likebtn img");
                if (stat == 200){
                    self.messages = data.message;
                    likeimage.classList.remove("unfavourited");
                    likeimage.classList.add("favourited");
                    alertcontainer.classList.add('alert-success');
                    alertcontainer.classList.remove('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show'); 
                }
                else if (stat == 201){
                    self.messages= data.message; 
                    likeimage.classList.remove("favourited");
                    likeimage.classList.add("unfavourited");  
                    alertcontainer.classList.remove('alert-success');
                    alertcontainer.classList.add('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');      
                }
                else{
                    self.messages = data.message;
                    alertcontainer.classList.remove('alert-success');
                    alertcontainer.classList.add('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');
                }
            });
        },

        getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    self.csrf_token = data.csrf_token;
                })
            
        }

    },
    created() {
        this.getCsrfToken();
        let self = this;
        let stat = 0;
       
        fetch(`/api/cars/${this.$route.params.car_id}`,
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
            self.car = data;
        });

        fetch(`/api/checkfavourite/${this.$route.params.car_id}`,
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
            self.favourited = data.message;
            const likeimage =  document.querySelector("button#likebtn img");
            if(self.favourited){
                likeimage.classList.remove("unfavourited");
                likeimage.classList.add("favourited");
            }
            else{
                likeimage.classList.remove("favourited");
                likeimage.classList.add("unfavourited");
            }
        });


        
    },
};

</script>

<style>
div.singlecarparent{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    width: 70%;
    margin: 4em auto;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 0.0625em 0.0625em, rgba(0, 0, 0, 0.25) 0px 0.125em 0.5em, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset;
}

section.singlecarcontent{
    display: grid;
    grid-template-columns: 1fr;
    width: 100%;
    align-items: start;
    justify-content: start;
    padding: 1.5em;
}

section.singlecarcontent p{
    margin-top: 1em;
}

div.singlecarparent section.singlecarphoto img{
   height:100%;
   width: 100%;
   object-fit:inherit;
}
h3{
    font-weight: bold;
    margin-bottom: 0;
}

section.carinforow{
   display: flex;
   flex-flow: row wrap;
   width: 100%;
}

section.carinforow div.carinfoitem{
    display: flex;
    flex-flow: row wrap;
    justify-content: flex-start;
    width: 50%;
}

section.carinforow div.carinfoitem label{
    width:50%;
}

section#interact{
    width: 100%;
}

button#likebtn{
    background: none;
}

.favourited{
    filter: grayscale(0%);
    width: 2em;
}

.unfavourited{
    filter: grayscale(100%);
    width: 2em;
}


div.singlecarparent button{
    align-self: end;
}

.btn_{
    margin-top: 1em;
    padding:4px 24px;
    border: none;
    border-radius: 4px;
    width: 35%;
}

section p, span#model, label{
    color: #949599;
}
span#model{
    font-weight: bold;
}

</style>
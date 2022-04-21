<template>

<form @submit.prevent="searchCar" id="searchForm">
        <div class="row">
            <div class="form-group col-md-5">
                <label for="inputEmail4">Email</label>
                <input type="email" class="form-control" id="inputEmail4" placeholder="Email">
            </div>
            <div class="form-group col-md-5">
                <label for="inputPassword4">Password</label>
                <input type="password" class="form-control" id="inputPassword4" placeholder="Password">
            </div>
             <div class="col-auto">
                <button class="btn btn-success">Search</button>
             </div>
             
        </div>
</form>


</template>

<script>
export default {
    data() {
        return {
            cars: [],
            searchTerm: ''
        };
    },
    methods: {

        searchCar(){
            let searchForm = document.getElementById('searchForm');
            let form_data = new FormData(searchForm);
            let self = this;
            let alertcontainer =  document.querySelector('span#msg');
            fetch('/api/register', {

                method: 'GET',
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    'X-CSRFToken': this.csrf_token
                }
              })
              .then((response)=>{
                  return response.json();
              })
              .then((data)=>{
                  
                console.log(data);
                alertcontainer.classList.add('alert-success');
                alertcontainer.classList.remove('alert-danger');
                alertcontainer.innerHTML= "User Registered Successfully";
                alertcontainer.classList.add('show');

              })
        },
        getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
            
        },
    
    },
    methods: {
         getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
    },
    created() {
        this.getCsrfToken();
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

form#searchForm{
    padding:2em;
    margin-top: 2em;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
}

div.row{
    align-items: center;
    justify-content: center;
}

form button{
    margin-top: 1em;
}


</style>
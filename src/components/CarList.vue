<template>
    <h2>Hello</h2>
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
            let registerForm = document.getElementById('registerForm');
            let form_data = new FormData(registerForm);
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
            console.log(data.message);
            console.log(sessionStorage.getItem('token'));
            self.cars = data.cars;
        });
    },
};
</script>

<style>


</style>
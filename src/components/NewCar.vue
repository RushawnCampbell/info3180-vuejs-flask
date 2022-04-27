<template>
    <div class="width">
        <h3>Add New Car</h3>
      <div class="text-left card_">
        <section id="msg" class=" form-control alert hide" >
                <li v-for="message in messages">
                     {{message}}
                </li>
        </section>
        <form @submit.prevent="addCarForm" method="POST" id="addCarForm" enctype = "multipart/form-data">
            <div class="d-inline-flex w_full ">
                <div class="mb-3  space_between w_full">
                    <label for="make" class="form-label">Make</label>
                    <input type="text" class="form-control w_full" name="make" id="make" >
                </div>
                <div class="mb-3 w_full">
                    <label for="model" class="form-label">Model</label>
                    <input type="text" class="form-control w_full"  name="model" id="model">
                </div>
            </div>

            <div class="d-inline-flex w_full">
                <div class="mb-3 space_between w_full">
                    <label for="colour" class="form-label">Colour</label>
                    <input type="text" class="form-control w_full"  name="colour" id="colour" >
                </div>

                <div class="mb-3 w_full">
                    <label for="year" class="form-label">Year</label>
                    <input type="number" min="1000" max="2100" class="form-control w_full"  name="year" id="year" >
                </div>
            </div>

            <div class="d-inline-flex w_full">
                <div class="mb-3 space_between w_full">
                    <label for="colour" class="form-label">Price</label>
                    <input type="number" step="0" class="form-control w_full"  name="price" id="price" >
                </div>

                <div class="mb-3 w_full">
                    <label class="form-label" for="car_type">Car Type</label>
                    <select class="form-control" id="car_type" name="car_type">
                    <option>Hatchback</option>
                    <option>Sedan</option>
                    <option>SUV</option>
                    <option>MUV</option>
                    <option>Coupe</option>
                    <option>Convertible</option>
                    <option>Pickup Truck</option>
                    </select>
                </div>
            </div>

            <div class="mb-3 w_full">
                <label class="form-label" for="transmission">Transmission</label>
                <select class="form-control" id="transmission" name="transmission">
                <option>Automatic</option>
                <option>Manual</option>
                </select>
            </div>
            <div class="mb-3 w_full">
                    <label for="description" class="form-label">Description</label>
                    <textarea  class="form-control"  name="description" id="description" ></textarea>
            </div>
            <div class="mb-3 w_full">
                <label for="photo" class="form-label">Upload Photo</label> <br>
                <input type="file" class="btn btn-light" id="photo"  name="photo" > <br/>
            </div>
            <button type="submit" class="btn_ btn-success" >Save</button>
        </form>
      </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            messages: []
        };
    },
    methods: {

        addCarForm(){
            let addCarForm = document.getElementById('addCarForm');
            let form_data = new FormData(addCarForm);
            let self = this;
            let alertcontainer =  document.querySelector('section#msg');
            let inputfields = document.querySelectorAll('div input');
            let descfield = document.querySelector('#description');
            let stat = 0;
            fetch('/api/cars', {

                method: 'POST',
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    'X-CSRFToken': this.csrf_token,
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
              })
              .then((response)=>{
                  stat= response.status;
                  return response.json();
              })
              .then((data)=>{
                inputfields.forEach((inp)=> {
                    inp.value = "";
                });
                descfield.value= "";


                if  (stat == 201){
                    self.messages = [];
                    self.messages.push("New Car Added Successfully");
                    alertcontainer.classList.add('alert-success');
                    alertcontainer.classList.remove('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');
                    const routetoview = setTimeout(()=>{
                        this.$router.push('/explore');
                        clearTimeout(routetoview);
                    }, 3000);
                }
                else if (stat == 200){
                    let errorlist = data;
                    self.messages = [];
                    for (let err=0; err<errorlist.length; err++){
                        self.messages.push(errorlist[err]);
                    }        
                    alertcontainer.classList.remove('alert-success');
                    alertcontainer.classList.add('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');
                }
                else{
                    self.messages = [];
                    self.messages.push(data.message);
                    alertcontainer.classList.remove('alert-success');
                    alertcontainer.classList.add('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');
                }

              })
        },
         getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    self.csrf_token = data.csrf_token;
                })
            
        },
    
    },
    created() {
        this.getCsrfToken();
    },
};
</script>

<style>

.hide{
    display:none;
}

.show{
    display: block;
}

.width{
  width: 36rem;
  padding-right: 0.75rem;
  padding-left: 0.75rem;
  margin-right: auto;
  margin-left: auto;
}
.space_between{
    margin-right: 10px;
}
.w_full{
    width:100%;
}
.btn_{
    margin-top: 1em;
    padding:4px 24px;
    border: none;
    border-radius: 4px;
}

.card_{
    margin-top:2em;
    padding:1em;
    border-radius: 6px;
    box-shadow: 2px 2px 10px 4px  rgba(0,0,0,.1);
    border: 2px solid transparent;
}
h3{
    font-weight: bold;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

input[type=number]{
    -moz-appearance: textfield;
}

@media screen and (max-width:800px){
  .width{
    width: 100%;
  }
  
}

</style>
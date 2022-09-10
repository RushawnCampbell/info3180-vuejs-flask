<template>
   
    <section id="addskiparent">
        <section id="msg" class=" form-control alert hide" >
            {{messages}}
        </section>
        <form @submit.prevent="addrecord" method="POST" id="addskip">
            <h4>Please fill all available information in the form below.</h4>
                <h4 class="subtitle">PERSONAL INFO</h4>
                <section id="personalinfo">
                    <div class="form-group">
                        <label for="firstname">First Name</label><br>
                        <input type="text" class="form-control" id="firstname" placeholder="eg. Rory" name="first_name" >
                    </div>
                    <div class="form-group">
                        <label for="middlename">Middle Name</label><br>
                        <input type="password" class="form-control" id="middlename" placeholder="eg. Frederick"  name="middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname" placeholder="eg. Higgs" name="last_name" >
                    </div>
                    <div class="form-group">
                        <label for="nib">N.I.B#</label><br>
                        <input type="password" class="form-control" id="nib" placeholder="eg. 12345678" name="nib" >
                    </div>
                    <div class="form-group">
                        <label for="dob">D.O.B</label><br>
                        <input type="date" class="form-control" id="dob" placeholder="eg. "  name="dob" >
                    </div>
                    <div class="form-group">
                        <label for="marital_status">Marital Status</label><br>
                        <input type="password" class="form-control" id="marital_status"  name="marital_status" >
                    </div>

                    <div class="form-group">
                        <label for="gender">Gender</label><br>
                        <input type="text" class="form-control" id="gender"  name="gender" :value=singlerec.gender>
                    </div>
                    
                    <div class="form-group">
                        <label for="homephone">Home Phone</label><br>
                        <input type="phone" class="form-control" id="homephone" placeholder="242-XXX-XXXX"  name="home_phone" >
                    </div>
                    <div class="form-group">
                        <label for="cellphone">Cell Phone</label><br>
                        <input type="password" class="form-control" id="cellphone"  placeholder="242-XXX-XXXX" name="cell_phone" >
                    </div>
                    <div class="form-group">
                        <label for="workphone">Work Phone</label><br>
                        <input type="password" class="form-control" id="workphone" placeholder="242-XXX-XXXX" name="work_phone" >
                    </div>
                    <div class="form-group">
                        <label for="streetaddress">Street Address</label>
                        <textarea class="form-control" id="streetaddress" placeholder="123 Example St" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">City</label><br>
                        <input type="password" class="form-control" id="city" placeholder="eg. Nassau"  name="city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Country</label><br>
                        <input type="password" class="form-control" id="country" placeholder="eg. Bahamas"  name="country" >
                    </div>
                 
                </section>

                <h4 class="subtitle">EMPLOYER INFO</h4>
                <section id="personalinfo">
                    <div class="form-group">
                        <label for="firstname">First Name</label><br>
                        <input type="text" class="form-control" id="firstname"  name="emp_first_name" >
                    </div>
                    <div class="form-group">
                        <label for="middlename">Middle Name</label><br>
                        <input type="password" class="form-control" id="middlename"  name="emp_middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname"  name="emp_last_name" >
                    </div>
                   
                    <div class="form-group">
                        <label for="workphone">Phone</label><br>
                        <input type="password" class="form-control" id="workphone"  name="emp_phone" >
                    </div>
            
                    <div class="form-group">
                        <label for="empstreetaddress">Street Address</label>
                        <textarea class="form-control" id="empstreetaddress" name="emp_street_address" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">City</label><br>
                        <input type="password" class="form-control" id="city"  name="emp_city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Country</label><br>
                        <input type="password" class="form-control" id="country"  name="emp_country" >
                    </div>
                 
                </section>


                <h4 class="subtitle">NEXT OF KIN INFO</h4>
                <section id="personalinfo">
                    <div class="form-group">
                        <label for="firstname">First Name</label><br>
                        <input type="text" class="form-control" id="firstname"  name="kin_first_name" >
                    </div>
                    <div class="form-group">
                        <label for="middlename">Middle Name</label><br>
                        <input type="password" class="form-control" id="middlename"  name="kin_middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname"  name="kin_last_name" >
                    </div>
                    <div class="form-group">
                        <label for="homephone">Home Phone</label><br>
                        <input type="password" class="form-control" id="homephone"  name="kin_home_phone" >
                    </div>
                    <div class="form-group">
                        <label for="cellphone">Cell Phone</label><br>
                        <input type="password" class="form-control" id="cellphone"  name="kin_cell_phone" >
                    </div>
                    <div class="form-group">
                        <label for="workphone">Work Phone</label><br>
                        <input type="password" class="form-control" id="workphone"  name="kin_work_phone" >
                    </div>
                    <div class="form-group">
                        <label for="streetaddress">Street Address</label>
                        <textarea class="form-control" name="kin_street_address" id="streetaddress" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">City</label><br>
                        <input type="password" class="form-control" id="city"  name="kin_city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Country</label><br>
                        <input type="password" class="form-control" id="country"  name="kin_country" >
                    </div>

                    <div class="form-group">
                        <label for="firstname">Employer First Name</label><br>
                        <input type="text" class="form-control" id="firstname"  name="kin_emp_first_name" >
                    </div>
                    <div class="form-group">
                        <label for="middlename">Employer Middle Name</label><br>
                        <input type="password" class="form-control" id="middlename"  name="kin_emp_middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Employer Last Name</label><br>
                        <input type="text" class="form-control" id="lastname"  name="kin_emp_last_name" >
                    </div>
                   
                    <div class="form-group">
                        <label for="workphone">Employer Phone</label><br>
                        <input type="password" class="form-control" id="workphone"  name="kin_emp_phone" >
                    </div>
            
                    <div class="form-group">
                        <label for="empstreetaddress">Employer Street Address</label>
                        <textarea class="form-control" id="empstreetaddress" name="kin_emp_street_address" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">Employer City</label><br>
                        <input type="password" class="form-control" id="city"  name="kin_emp_city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Employer Country</label><br>
                        <input type="password" class="form-control" id="country"  name="kin_emp_country" >
                    </div>
                 
                </section>
                <button type="submit" class="btn btn-success mb-2">ADD</button>
        </form>
    </section>

</template>
<script>
export default {
    data() {
        return {
            messages:'',
            csrf_token: '',
            isauth: false
        };
    },
    methods: {
        addrecord(){
            let addrecForm = document.getElementById('addskip');
            let form_data = new FormData(addrecForm);
            let self = this;
            let stat = 0;
            let alertcontainer =  document.querySelector('section#msg');
            let inputfields = document.querySelectorAll('div input');
            fetch('/api/addrec', {
                method: 'POST',
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
                    'X-CSRFToken': self.csrf_token,
                }
              })
              .then((response)=>{
                  stat = response.status;
                  return response.json();
              })
              .then((data)=>{
                  
                  if (stat == 200){
                      sessionStorage.setItem('token', data.token);
                      sessionStorage.setItem('first_name', data.first_name);
                      sessionStorage.setItem('role', data.role);
                      sessionStorage.setItem('isauth', true);
                      inputfields.forEach((inp)=> {
                      inp.value = "";
                        });

                    self.messages = "SKIPTRACE RECORD ADDED SUCCESSFULLY"; 
                    alertcontainer.classList.add('alert-success');
                    alertcontainer.classList.remove('alert-danger');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');

                       
                  }
                  else if (stat == 401){
                        self.messages = data.message;   
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
            
        }
    
    },
    created() {
       this.getCsrfToken();
    }
};
</script>
<style>
form#addskip{
    margin: 0;
    display: flex;
    flex-flow: column wrap;
    width: 60%;
    
}

form#addskip h4:nth-child(2){
    margin:0 !important;
}


section#personalinfo{
    display: grid;
    grid-template-columns: repeat(2,1fr);
    grid-column-gap: 5em;
    grid-row-gap: 2em;
}

h4.subtitle{
    margin: 2em 0;
    background: #666;
    color: #fff;
    width: 100%;
    text-align: center;
}

section#addskiparent{
    display: flex;
    flex-flow: column wrap;
    align-items: center;
    width: 100%;
    margin-bottom: 10em;
    
}
</style>
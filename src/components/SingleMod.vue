<template>
   
    <section id="modskiparent">
        <section id="msg" class=" form-control alert hide" >
            {{messages}}
        </section>
        <form @submit.prevent="modrecord" v-if="issingle" method="POST" id="modskip">
            <h4>Edit the appropriate fields the save your changes</h4>
                <h4 class="subtitle">PERSONAL INFO</h4>
                <section id="personalinfo">
                    <div class="form-group">
                        <label for="firstname">First Name</label><br>
                        <input type="text" class="form-control" id="firstname" placeholder="eg. Rory" name="first_name" :value=singlerec.first_name>
                    </div>
                    <div class="form-group">
                        <label for="middlename">Middle Name</label><br>
                        <input type="text" class="form-control" id="middlename" placeholder="eg. Frederick"  name="middle_name" :value=singlerec.middle_name>
                    </div>
                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname" placeholder="eg. Higgs" name="last_name" :value=singlerec.last_name>
                    </div>
                    <div class="form-group">
                        <label for="nib">N.I.B#</label><br>
                        <input type="text" class="form-control" id="nib" placeholder="eg. 12345678" name="nib" :value=singlerec.nib>
                    </div>
                    <div class="form-group">
                        <label for="dob">D.O.B</label><br>
                        <input type="date" class="form-control" id="dob" placeholder="eg. "  name="dob" :value=singlerec.dob >
                    </div>
                    <div class="form-group">
                        <label for="marital_status">Marital Status</label><br>
                        <input type="text" class="form-control" id="marital_status"  name="marital_status" :value=singlerec.marital_status>
                    </div>

                    <div class="form-group">
                        <label for="gender">Gender</label><br>
                        <input type="text" class="form-control" id="gender"  name="gender" :value=singlerec.gender>
                    </div>

                    <div class="form-group">
                        <label for="homephone">Home Phone</label><br>
                        <input type="phone" class="form-control" id="homephone" placeholder="242-XXX-XXXX"  name="home_phone" :value=singlerec.home_phone>
                    </div>
                    <div class="form-group">
                        <label for="cellphone">Cell Phone</label><br>
                        <input type="text" class="form-control" id="cellphone"  placeholder="242-XXX-XXXX" name="cell_phone" :value=singlerec.middle_phone>
                    </div>
                    <div class="form-group">
                        <label for="workphone">Work Phone</label><br>
                        <input type="text" class="form-control" id="workphone" placeholder="242-XXX-XXXX" name="work_phone" :value=singlerec.work_phone>
                    </div>
                    <div class="form-group">
                        <label for="streetaddress">Street Address</label>
                        <textarea class="form-control" id="streetaddress" placeholder="123 Example St" rows="2"> {{singlerec.street_address}}</textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">City</label><br>
                        <input type="text" class="form-control" id="city" placeholder="eg. Nassau"  name="city" :value=singlerec.city>
                    </div>
                    <div class="form-group">
                        <label for="country">Country</label><br>
                        <input type="text" class="form-control" id="country" placeholder="eg. Bahamas"  name="country" :value=singlerec.country>
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
                        <input type="text" class="form-control" id="middlename"  name="emp_middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname"  name="emp_last_name" >
                    </div>
                   
                    <div class="form-group">
                        <label for="workphone">Phone</label><br>
                        <input type="text" class="form-control" id="workphone"  name="emp_phone" >
                    </div>
            
                    <div class="form-group">
                        <label for="empstreetaddress">Street Address</label>
                        <textarea class="form-control" id="empstreetaddress" name="emp_street_address" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">City</label><br>
                        <input type="text" class="form-control" id="city"  name="emp_city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Country</label><br>
                        <input type="text" class="form-control" id="country"  name="emp_country" >
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
                        <input type="text" class="form-control" id="middlename"  name="kin_middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname"  name="kin_last_name" >
                    </div>
                    <div class="form-group">
                        <label for="homephone">Home Phone</label><br>
                        <input type="text" class="form-control" id="homephone"  name="kin_home_phone" >
                    </div>
                    <div class="form-group">
                        <label for="cellphone">Cell Phone</label><br>
                        <input type="text" class="form-control" id="cellphone"  name="kin_cell_phone" >
                    </div>
                    <div class="form-group">
                        <label for="workphone">Work Phone</label><br>
                        <input type="text" class="form-control" id="workphone"  name="kin_work_phone" >
                    </div>
                    <div class="form-group">
                        <label for="streetaddress">Street Address</label>
                        <textarea class="form-control" name="kin_street_address" id="streetaddress" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">City</label><br>
                        <input type="text" class="form-control" id="city"  name="kin_city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Country</label><br>
                        <input type="text" class="form-control" id="country"  name="kin_country" >
                    </div>

                    <div class="form-group">
                        <label for="firstname">Employer First Name</label><br>
                        <input type="text" class="form-control" id="firstname"  name="kin_emp_first_name" >
                    </div>
                    <div class="form-group">
                        <label for="middlename">Employer Middle Name</label><br>
                        <input type="text" class="form-control" id="middlename"  name="kin_emp_middle_name" >
                    </div>
                    <div class="form-group">
                        <label for="lastname">Employer Last Name</label><br>
                        <input type="text" class="form-control" id="lastname"  name="kin_emp_last_name" >
                    </div>
                   
                    <div class="form-group">
                        <label for="workphone">Employer Phone</label><br>
                        <input type="text" class="form-control" id="workphone"  name="kin_emp_phone" >
                    </div>
            
                    <div class="form-group">
                        <label for="empstreetaddress">Employer Street Address</label>
                        <textarea class="form-control" id="empstreetaddress" name="kin_emp_street_address" rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="city">Employer City</label><br>
                        <input type="text" class="form-control" id="city"  name="kin_emp_city" >
                    </div>
                    <div class="form-group">
                        <label for="country">Employer Country</label><br>
                        <input type="text" class="form-control" id="country"  name="kin_emp_country" >
                    </div>
                 
                </section>
                <button type="submit" class="btn btn-success mb-2">SAVE</button>
        </form>
    </section>

</template>
<script>
export default {
    data() {
        return {
            messages:'',
            csrf_token: '',
            isauth: false,
            issingle: false,
            singlerec: ''
        };
    },
    methods: {
        modrecord(){
            let modrecForm = document.getElementById('modskip');
            let form_data = new FormData(modrecForm);
            let self = this;
            let stat = 0;
            let alertcontainer =  document.querySelector('section#msg');
            let inputfields = document.querySelectorAll('div input');
            fetch(`/api/modrecord?recid=${this.$route.params.recid}`, {
                method: 'POST',
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
                    'X-CSRFToken': self.csrf_token,
                }
            })
            .then((response)=>{
                stat =  response.status
                return response.json();
            })
            .then((data)=>{

                if (stat == 200){
                    this.messages =  data.message;
                }
                else if (stat == 201){
                    this.messages =  data.message;
                }
                else if (stat == 401){
                    this.messages =  data.message;
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
       if (sessionStorage.getItem('isauth') == 'true'){
            this.isauth = true;
            let stat = 0;

            fetch(`/api/getrecord?recid=${this.$route.params.recid}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                }
            })
            .then((response)=>{
                stat =  response.status
                return response.json();
            })
            .then((data)=>{

                if (stat == 200){
                    this.issingle = true;
                    this.singlerec = data;
                }

            })
       }
    }
};
</script>
<style>
form#modskip{
    margin: 0;
    display: flex;
    flex-flow: column wrap;
    width: 60%;
    
}

form#modskip h4:nth-child(2){
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

section#modskiparent{
    display: flex;
    flex-flow: column wrap;
    align-items: center;
    width: 100%;
    margin: 5em 0em 10em 0em;
    
}
</style>
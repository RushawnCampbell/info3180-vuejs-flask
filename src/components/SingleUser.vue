<template>
   
    <section id="moduserarent">
        <section id="msg" class=" form-control alert hide" >
            {{messages}}
        </section>
        <form @submit.prevent="modrecord" v-if="issingle" method="POST" id="moduser">
            <section class="headingcont">
                <h4>Edit the appropriate fields then save your changes</h4>
                <RouterLink  to="/adminhub" v-on:click="backhandler" class="btn">BACK TO USER LIST</RouterLink> 
                <RouterLink  to="/adminhub" class="btn">BACK TO ADMIN HUB</RouterLink>
            </section>
                <section id="personalinfo">
                    <div class="form-group">
                        <label for="firstname">First Name</label><br>
                        <input type="text" class="form-control" id="firstname" placeholder="eg. Rory" name="first_name" :value=singlerec.first_name>
                    </div>

                    <div class="form-group">
                        <label for="lastname">Last Name</label><br>
                        <input type="text" class="form-control" id="lastname" placeholder="eg. Higgs" name="last_name" :value=singlerec.last_name>
                    </div>
                    <div class="form-group">
                        <label for="username">Username</label><br>
                        <input type="text" class="form-control" id="username" placeholder="eg. user123" name="username" :value=singlerec.username>
                    </div>
                    <div class="form-group col-md-4">
                        <label for="role">Role</label>
                        <select id="role" class="form-control" name="role">
                            <option>Choose A Role</option>
                            <option id="admin" value="Admin">Admin</option>
                            <option id="skiptracer" value="Skiptracer">Skiptracer</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="email">E-mail</label><br>
                        <input type="email" class="form-control" id="email"  name="email" :value=singlerec.email>
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
        backhandler(){
            sessionStorage.setItem("isbackactivateview", true);
            sessionStorage.setItem('isback', true);
            this.$router.push('/adminhub');
        },

        backadminhandler(){
            sessionStorage.setItem("isbackactivateview", false);
            this.$router.push('/adminhub');
        },

        modrecord(){
            let modrecForm = document.getElementById('moduser');
            let form_data = new FormData(modrecForm);
            let self = this;
            let stat = 0;
            let alertcontainer =  document.querySelector('section#msg');
            let inputfields = document.querySelectorAll('div input');
            fetch(`/api/moduser?recid=${this.$route.params.recid}`, {
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
                    alertcontainer.classList.remove('alert-danger');
                    alertcontainer.classList.add('alert-success');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');

                    fetch(`/api/getusers?recid=${this.$route.params.recid}`, {
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
                else if (stat == 201 || stat == 401){
                    this.messages =  data.message;
                    alertcontainer.classList.add('alert-danger');
                    alertcontainer.classList.remove('alert-success');
                    alertcontainer.classList.remove('hide');
                    alertcontainer.classList.add('show');
                }

                window.scrollTo(0,0);

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

            fetch(`/api/getusers?recid=${this.$route.params.recid}`, {
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

                    let formchecker = setInterval(()=>{
                        if (document.contains(document.querySelector("form#moduser"))){
                            //skiptraceropt = document.querySelector("option#skiptracer");
                            //adminopt = document.querySelector("option#admin");

                            if (data.role == 'Admin' ){
                               // adminopt.setAttribute('selected', true);
                                //skiptraceropt.setAttribute('selected', false);
                                document.querySelector("select#role").value="Admin"
                            }
                            else  if (data.role == 'Skiptracer' ){
                               // skiptraceropt.setAttribute('selected', true);
                                //adminopt.setAttribute('selected', false);
                                document.querySelector("select#role").value="Skiptracer"
                            }
                            clearInterval(formchecker);
                        }
                    },0);

                }

            })
       }
    }
};
</script>
<style>

section#msg{
width: 60%;
text-align: center;
}

form#moduser{
    margin: 0;
    display: flex;
    flex-flow: column wrap;
    width: 60%;
    
}

form#moduser h4:nth-child(2){
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

section#moduserarent{
    display: flex;
    flex-flow: column wrap;
    align-items: center;
    width: 100%;
    margin: 2em 0em 10em 0em;
    
}

section.headingcont{
    display: flex;
    flex-flow: row wrap;
    justify-items: center;
    justify-content: space-between;
    margin: 0 0 1em 0;
}

section.headingcont a.btn{
    width: fit-content;
    background: #0E086D;
    color: #fff;
    font-weight: bold;
}
</style>
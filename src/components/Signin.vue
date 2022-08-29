<template>
    <section class="formcombo">
    <h2>Sign in to access your portal.</h2>
    <section id="msg" class=" form-control alert hide" >
        {{messages}}
    </section>
        <form @submit.prevent="signin" method="POST" id="signinForm">
            <div class="form-group">
                <label for="username">Username</label><br>
                <input type="text" class="form-control" id="username"  name="username" >
            </div>
            <div class="form-group">
                <label for="pasword">Password</label><br>
                <input type="password" class="form-control" id="password"  name="password" >
            </div>
            <button type="submit" class="btn btn-success mb-2">Sign in</button>
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
        signin(){
            let signinForm = document.getElementById('signinForm');
            let form_data = new FormData(signinForm);
            let self = this;
            let stat = 0;
            let alertcontainer =  document.querySelector('section#msg');
            let inputfields = document.querySelectorAll('div input');
            fetch('/api/auth/signin', {
                method: 'POST',
                body: form_data,
                headers: {
                    "Accept": "application/json",
                    'X-CSRFToken': this.csrf_token
                }
              })
              .then((response)=>{
                  stat = response.status;
                  return response.json();
              })
              .then((data)=>{
                  
                  if (stat == 200){
                      sessionStorage.setItem('token', data.token);
                      sessionStorage.setItem('isauth', true);
                      inputfields.forEach((inp)=> {
                      inp.value = "";
                        });
                      fetch('/api/uid', {
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
                            sessionStorage.setItem('uid', data.message);
                        });

                        this.$router.push('/search')
                       
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

form#signinForm div{
    margin-bottom: 1em;;
}

form#signinForm input{
    box-shadow: rgba(0, 0, 0, 0.18) 0px 2px 4px;
    width: 92%;
}

form#signinForm button{
    width: 92%;
    background: #0E086D;
    color: #fff;
}

form#signinForm button:hover{
  color: whitesmoke;
}


section.formcombo h2{
    text-align: center;
    margin-bottom: 1em;
    font-weight: bold;
    color: #666;
}

section.formcombo{
    display: flex;
    flex-flow: column wrap;
    width: 28%;
    margin-top: 22vh;
    margin-left: 35vw;

}
form#signinForm{
    box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
    padding: 2em 1em;
}

.hide{
    display:none;
}

.show{
    display: block;
}

</style>
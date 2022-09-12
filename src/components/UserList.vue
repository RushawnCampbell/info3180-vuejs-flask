<template>

    <section v-if="isresults" id="msg" class=" form-control alert " >
        <span>{{messages}}</span>  <!--<button v-on:click= "searchagain" id="searchagain" class=" btn btn-success"> SEARCH AGAIN</button>-->
    </section>

    <section v-if="isresults" class="resultcontainer">

        <div id="recorditem" v-for= "rec in slicedrecords" >
            <img class="recorditem" src="../assets/images/user.png" >
            <div class="rowinfo"><span class="fieldtitle">Username</span> <span> {{rec.username}} </span></div>
            <div class="rowinfo"><span class="fieldtitle">First Name</span> <span> {{rec.first_name}} </span></div>
            <div class="rowinfo"><span class="fieldtitle">Last Name</span> <span> {{rec.last_name}} </span></div>
            <div class="rowinfo"><span class="fieldtitle">E-mail</span> <span> {{rec.email}} </span></div>
            <div class="rowinfo"><span class="fieldtitle">Role</span> <span> {{rec.role}} </span></div>
            <div class="rowinfo btnrow"><RouterLink v-on:click="pageidreaper" :to= "`/singleuser/${rec.user_id}`" class=" btn btnmod ">MODIFY USER</RouterLink></div>
        </div>


    </section>

    <div v-if="isresults" id="pagination">
        <button v-for="page in pagination" v-on:click="pagehandler(page)" class="btnsignin pagebtn" :id="page"> {{page}}</button>
    </div>  

</template>
<script>
export default {
 data() {
     return {
        messages:'',
        csrf_token: '',
        isauth: false,
        isresults: false,
        records: [],
        slicedrecords: [],
        pagination: [],
        datalen: 0,
        totalpages: 0,
        leftovers: 0,
        pagelimit: 10
     };
 },
 methods: {

        pagehandler(id){

            this.slicedrecords = this.records.slice( ( parseInt(id) * this.pagelimit) - (this.pagelimit), (parseInt(id) * this.pagelimit));
            const btns =  document.querySelectorAll(".pagebtn");
            btns.forEach((bt)=>{

                if (bt.getAttribute('id') == id){
                    bt.classList.remove('regcolor');
                    bt.classList.add('currcolor');
                }
                else{
                    bt.classList.remove('currcolor');
                    bt.classList.add('regcolor');
                }
            });
        },

        pageidreaper(){

            const pgbtns =  document.querySelectorAll("div#pagination button");
            for (let bt = 0; bt < pgbtns.length; bt++){
                if(pgbtns[bt].classList.contains("currcolor")){
                    sessionStorage.setItem('reapedid', pgbtns[bt].getAttribute('id'));
                    break;
                }
            }
        },

        searchagain(){
            this.$router.push('/search');
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
      
        fetch('api/getusers', {
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
        .then((data) => {
            if(stat == 200){
                this.isresults = true;
                data.forEach((rec)=>{
                    this.records.push(rec);
                });

                this.datalen = data.length;
                this.totalpages = Math.floor(this.datalen / this.pagelimit);
                this.leftovers = this.datalen % this.pagelimit;

                if (this.leftovers > 0){
                    this.totalpages += 1;
                }

                for(let pg = 1; pg <= this.totalpages; pg++){
                    this.pagination.push(pg);
                }
                this.messages = `${data.length} USER ACCOUNTS FOUND`;
                if (sessionStorage.getItem('isback') != 'true'){
                    this.slicedrecords = this.records.slice(0, 10);
                    let firstchecker = setInterval(()=>{
                        if (document.contains(document.querySelector("div#pagination")) ){
                            const firstpage = document.querySelector(".pagebtn");
                            firstpage.classList.add('currcolor');
                            firstpage.classList.remove('regcolor');
                            clearInterval(firstchecker);
                        }
                    },0);
                }
                else if (sessionStorage.getItem('isback') == 'true'){


                    let backchecker = setInterval(()=>{
                        if (document.contains(document.querySelector("div#pagination")) ){
                            const pgbtns =  document.querySelectorAll("div#pagination button");
                            this.slicedrecords = this.records.slice( ( parseInt(sessionStorage.getItem('reapedid')) * this.pagelimit) - (this.pagelimit), (parseInt(sessionStorage.getItem('reapedid')) * this.pagelimit));
                            
                            pgbtns.forEach((bt)=>{
                                if (bt.getAttribute('id') == sessionStorage.getItem('reapedid')){
                                    bt.classList.remove('regcolor');
                                    bt.classList.add('currcolor');
                                }
                                else{
                                    bt.classList.remove('currcolor');
                                    bt.classList.add('regcolor');
                                }
                            });
                            clearInterval(backchecker);
                        }
                    },0);
                    sessionStorage.setItem('isback', 'false');
                }

                let messagechecker =  setInterval(()=>{
                    if (document.contains(document.querySelector('section#msg'))){
                      const alertcontainer =  document.querySelector('section#msg');
                      alertcontainer.classList.remove('alert-danger');
                      alertcontainer.classList.add('alert-success');
                      alertcontainer.classList.remove('hide');
                      alertcontainer.classList.add('show');
                      clearInterval(messagechecker);
                    }
                },0);
            
            }
            else if (stat == 201 || stat == 401){
                this.isresults = true;
                let messagechecker =  setInterval(()=>{
                    if (document.contains(document.querySelector('section#msg'))){
                      const alertcontainer =  document.querySelector('section#msg');
                      this.messages = data.message;
                      alertcontainer.classList.add('alert-danger');
                      alertcontainer.classList.remove('alert-success');
                      alertcontainer.classList.remove('hide');
                      alertcontainer.classList.add('show');
                       clearInterval(messagechecker);
                    }
                },0);

            }


        })


    }

}
};
</script>

<style>

.currcolor{
background: #fff !important;
color: #0E086D !important;
}

.btnmod {

background:#d9534f !important;
width: 9rem;
color: #fff;
font-weight: bold;
}

.regcolor{
background: #0E086D !important;
color: #fff !important;
}


div.rowinfo{
margin-right: 1.2em;
}

</style>
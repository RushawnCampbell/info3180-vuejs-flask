<template>

        <section v-if="isresults" id="msg" class=" form-control alert " >
            <span>{{messages}}</span>  <button v-on:click= "searchagain" id="searchagain" class=" btn btn-success"> SEARCH AGAIN</button>
        </section>

        <section v-if="isresults" class="resultcontainer">

            <div id="recorditem" v-for= "rec in slicedrecords" >
                <img class="recorditem" src="../assets/images/user.png" >
                <div class="rowinfo"><span class="fieldtitle">First Name</span> <span> {{rec.first_name}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">Last Name</span> <span> {{rec.last_name}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">D.O.B.</span> <span> {{rec.dob}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">NIB#</span> <span> {{rec.nib}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">Home Phone </span> <span> {{rec.home_phone}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">Cell Phone </span> <span> {{rec.cell_phone}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">Work Phone </span> <span> {{rec.work_phone}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">Street Address </span> <span> {{rec.street_address}} </span></div>
                <div class="rowinfo"><span class="fieldtitle">City </span> <span> {{rec.city}} </span></div>
                <RouterLink v-on:click="pageidreaper" :to= "`/singleresult/${rec.record_id}`" class=" btn btnsignin">MORE INFO </RouterLink>
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
            
            fetch(sessionStorage.getItem('queryurl'), {
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
                    const alertcontainer =  document.querySelector('section#msg');
                    this.messages = `${data.length} RECORDS FOUND`;

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

                }
                else if (stat == 201 || stat == 401){
                    this.isresults = true;
                    this.messages = data.message;
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

.regcolor{
    background: #0E086D !important;
    color: #fff !important;
}
 
 </style>
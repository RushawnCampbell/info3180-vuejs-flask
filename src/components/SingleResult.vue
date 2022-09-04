<template>
     <div v-if="issingle" id="singleresult">
        <section id="singlebanner">
            <img id="singleimg" src="../assets/images/user.png"/>
            <h2 id="firstname">{{singlerec.first_name}}</h2>
            <h2 id="lastname">{{singlerec.last_name}}</h2>
            <button id="backresults" v-on:click="backhandler"  class="btn btnsignin">BACK TO RESULTS</button>  
        </section>

        <section id="infoparent">

            <section class="inforow">
                <span class="infoitem"><b>MIDDLE NAME:</b></span>
                <span class="infoitem" id="inforowmiddle">{{singlerec.middle_name}}</span>
            </section>

            <section class="inforow" >
                <span class="infoitem"><b>D.O.B:</b></span>
                <span class="infoitem" id="inforowdob">{{singlerec.dob}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>NIB#:</b></span>
                <span class="infoitem" id="inforownib">{{singlerec.nib}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>GENDER:</b></span>
                <span class="infoitem" id="inforowgender">{{singlerec.gender}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>MARITAL STATUS:</b></span>
                <span class="infoitem" id="inforowmar">{{singlerec.marital_status}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>HOME PH#:</b></span>
                <span class="infoitem" id="inforowhphone">{{singlerec.home_phone}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>CELL PH#:</b></span>
                <span class="infoitem" id="inforowcphone">{{singlerec.cell_phone}}</span>
            </section>

            <section class="inforow" >
                <span class="infoitem"><b>WORK PH#:</b></span>
                <span class="infoitem" id="inforowwphone">{{singlerec.work_phone}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>STREET ADDRESS:</b></span>
                <span class="infoitem" id="inforowsaddress">{{singlerec.street_address}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>CITY:</b></span>
                <span class="infoitem" id="inforowcity">{{singlerec.city}}</span>
            </section>

            <section class="inforow">
                <span class="infoitem"><b>COUNTRY:</b></span>
                <span class="infoitem"  id="inforowcountry">{{singlerec.country}}</span>
            </section>

        </section>

</div>
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
            sessionStorage.setItem('isback', true);
            this.$router.push('/mainresult');
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


</style>
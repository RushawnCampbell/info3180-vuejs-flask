<script>

    import AddSkip from "../components/AddSkip.vue";
    import ModSkip from "../components/ModSkip.vue";
    import UserList from "../components/UserList.vue";
    
    
    export default {
        data() {
          return{
             isadmin: false,
             isadd: false,
             ismod: false,
             ismanage: false
          }; 
        },
        methods:{

          addskip(){

            if (this.isadd ){
              document.querySelector("button#addskip").classList.remove("selected");
              this.isadd = false;
              this.ismanage =  false;
              this.ismod= false
            }
            else{
              document.querySelector("button#addskip").classList.add("selected");
              this.isadd = true;
              this.ismod = false;
              this.ismanage =  false;
            }

            document.querySelector("button#modskip").classList.remove("selected");
            document.querySelector("button#manuser").classList.remove("selected");

          },
          modskip(){

            if (this.ismod ){
              document.querySelector("button#modskip").classList.remove("selected");
              this.ismod = false;
              this.isadd =  false;
              this.ismanage =  false;
            }
            else{
              document.querySelector("button#modskip").classList.add("selected");
              this.isadd =  false;
              this.ismanage =  false;
              this.ismod = true;
            }

            document.querySelector("button#addskip").classList.remove("selected");
            document.querySelector("button#manuser").classList.remove("selected");

          },

          manageuser(){
            if (this.ismanage ){
              document.querySelector("button#manuser").classList.remove("selected");
              this.ismod = false;
              this.ismanage =  false;
              this.isadd =  false;
            }
            else{
              document.querySelector("button#manuser").classList.add("selected");
              this.isadd =  false;
              this.ismod = false;
              this.ismanage =  true;
            }

            document.querySelector("button#addskip").classList.remove("selected");
            document.querySelector("button#modskip").classList.remove("selected");
          }
        },
        created(){
           if (sessionStorage.getItem('role') == 'Admin'){
              this.isadmin = true;
           }
           else{
              this.isadmin = false;
           }

           let isbackactivatechecker =  setInterval(()=>{
                if (sessionStorage.getItem("isbackactivateview") == 'true'){

                  this.ismod = false;
                  this.ismanage =  true;
                  this.isadd =  false;
                  
                  clearInterval(isbackactivatechecker);
                }
           },0);
        },
        components: {AddSkip, ModSkip, UserList}        
    };
 </script>
    
    <template>
  
    <section class="main" v-if="isadmin">
      <h2 class="title">What Would You Like To Do?</h2>
      <div  class="btn-group" role="group" aria-label="Button Controls">
              <button id="addskip" v-on:click="addskip" type="button" class="btn btnsignin">ADD A RECORD</button>
              <button id="modskip"  v-on:click="modskip" type="button" class="btn btnsignin">MODIFY RECORDS</button>
              <button id="manuser" v-on:click="manageuser" type="button" class="btn btnsignin">MANAGE USERS</button>
      </div>
      <AddSkip v-if="isadd"/>
      <ModSkip v-if="ismod"/> 
      <UserList v-if="ismanage"/> 
    </section>  
 
    </template>
    
    <style> 
  section.main{
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
    
  }

  h2.title{
    text-align: center;
  }

  div.btn-group{
    margin-bottom: 2em;
    color: #666;
  }

  .selected{
    color: #0E086D !important;
    background: #fff !important;
  }
    </style>
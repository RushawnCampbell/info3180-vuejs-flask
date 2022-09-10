<script>

    import AddSkip from "../components/AddSkip.vue";
    import ModSkip from "../components/ModSkip.vue";
    
    
    export default {
        data() {
          return{
             isadmin: false,
             isadd: false,
             ismod: false,
          }; 
        },
        methods:{

          addskip(){

            if (this.isadd ){
              this.isadd = false;
              this.ismod= false
            }
            else{
              this.isadd = true;
              this.ismod = false;
            }

          },
          modskip(){

            if (this.ismod ){
              this.ismod = false;
              this.isadd =  false;
            }
            else{
              this.isadd =  false;
              this.ismod = true;
            }

          }
        },
        created(){
           if (sessionStorage.getItem('role') == 'Admin'){
              this.isadmin = true;
           }
           else{
              this.isadmin = false;
           }
        },
        components: {AddSkip, ModSkip}        
    };
 </script>
    
    <template>
  
    <section class="main" v-if="isadmin">
      <h2 class="title">What Would You Like To Do?</h2>
      <div  class="btn-group" role="group" aria-label="Button Controls">
              <button id="quickmode" v-on:click="addskip" type="button" class="btn btnsignin">ADD A RECORD</button>
              <button id="advmode"  v-on:click="modskip" type="button" class="btn btnsignin">MODIFY RECORDS</button>
              <button id="advmode" type="button" class="btn btnsignin">MANAGE USERS</button>
      </div>
      <AddSkip v-if="isadd"/>
      <ModSkip v-if="ismod"/> 
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
    </style>
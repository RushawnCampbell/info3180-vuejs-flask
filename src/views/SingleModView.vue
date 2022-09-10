<script>

    import SingleMod from "../components/SingleMod.vue";
    
    
    export default {
        data() {
          return{
             isadmin: false,
          }; 
        },
        created(){
           if (sessionStorage.getItem('role') == 'Admin'){
              this.isadmin = true;
           }
           else{
              this.isadmin = false;
           }
        },
        components: {SingleMod}        
    };
 </script>
    
    <template>
    
    <SingleMod v-if="isadmin" />
 
    </template>
    
    <style>
    </style>
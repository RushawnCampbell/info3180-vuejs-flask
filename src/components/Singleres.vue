<template>
   <h3>HEYO!</h3>
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


</style>
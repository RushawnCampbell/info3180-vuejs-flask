<template>
</template>
<script>

export default {
    data() {
        return {
            csrf_token: ''
        };
    },
    methods:{

        logout(){
            fetch('/api/auth/signout', {
            method: 'GET',
            headers: {
                "Accept": "application/json",
                'X-CSRFToken': this.csrf_token,
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
            })
            .then((response)=>{
                return response.json();
            })
            .then((data)=>{
                sessionStorage.clear();
                sessionStorage.setItem('isauth', false);
                this.$router.push('/signin');
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
    created(){
        this.getCsrfToken();
        this.logout();
    }
};
</script>
<style>
</style>
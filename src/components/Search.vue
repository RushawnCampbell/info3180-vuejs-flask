<template>


    <section v-if=isauth id="skiptraceparent">

        <div class="greetcont">
            <h2>Hello {{firstname}}</h2>
            <RouterLink v-if=isadmin to="/adminhub" class="btn btnsignin">VISIT ADMIN HUB</RouterLink>
        </div>
        <div id="QuickSearchForm">
            <form @submit.prevent="search('quick')" v-if=isquick id="divrow">
                <div  class="form-inline">
                    <h3 for="quicksearch">SKIPTRACE SEARCH QUICK MODE</h3>
                    <input class="btn" type="text" v-model="quicksearch"  name="quicksearch" id="quicksearch"
                        placeholder="search anything">
                        <button class="btn btn-success"> QUICK SEARCH</button>

                </div>

            </form>

            <form @submit.prevent="search('advance')" v-if=!isquick id="advsearchparent">
                <h3 for="quicksearch">SKIPTRACE SEARCH ADVANCE MODE </h3>
                <span style="color:#666;">Toggle the filters to customize your search.</span><br /><br />
                <div id="filters">

                    <div class="form-check form-switch" id="firstname">
                        <label class="form-check-label" for="flexSwitchCheckDefault">First Name</label>
                        <input v-on:click="switchandler('firstname')" class="form-check-input firstname" type="checkbox"
                            id="flexSwitchCheckDefault">
                    </div>

                    <div class="form-check form-switch" id="lastname">
                        <label class="form-check-label" for="flexSwitchCheckDefault">Last Name</label>
                        <input v-on:click="switchandler('lastname')" class="form-check-input lastname" type="checkbox"
                            id="flexSwitchCheckDefault">
                    </div>

                    <div class="form-check form-switch" id="dob">
                        <label class="form-check-label" for="flexSwitchCheckDefault">D.O.B</label>
                        <input v-on:click="switchandler('dob')" class="form-check-input dob" type="checkbox"
                            id="flexSwitchCheckDefault">
                    </div>

                    <div class="form-check form-switch" id="nib">
                        <label class="form-check-label" for="flexSwitchCheckDefault">NIB#</label>
                        <input v-on:click="switchandler('nib')" class="form-check-input nib" type="checkbox"
                            id="flexSwitchCheckDefault">
                    </div>

                </div>
                <div id="advsearch">

                    <div v-if="`${isfirst}` == 'true'" class="inputcombo">
                        <label>First Name</label>
                        <input type="text" id="firstname" name="firstname" />
                    </div>
                    <div v-if="`${islast}` == 'true'" class="inputcombo">
                        <label>Last Name</label>
                        <input type="text" id="lastname" name="lastname" />
                    </div>
                    <div v-if="`${isnib}` == 'true'" class="inputcombo">
                        <label>NIB#</label>
                        <input type="text" id="nib" name="nib" />
                    </div>
                    <div v-if="`${isdob}` == 'true'" class="inputcombo">
                        <label>D.O.B</label>
                        <input type="text" id="dob" name="dob" />
                    </div>

                </div>
                <div v-if=showsearch id="advbtn">
                    <button class="btn btn-success"> Search</button>
                </div>

            </form>


        </div>
        <br />
        <div id="btngrp" class="btn-group" role="group" aria-label="Button Controls">
            <button id="quickmode" v-on:click="quickmode" type="button" class="btn disabled">QUICK MODE</button>
            <button id="advmode" v-on:click="advmode" type="button" class="btn">ADVANCE MODE</button>
        </div>

    </section>

    <section class="warning" v-else>
        <h2 class="text-danger"> You must be signed in to access this area.</h2>
        <RouterLink class="btn btnsignin" to="/signin">CLICK HERE TO SIGN IN</RouterLink>
    </section>

</template>

<script>
var joinedurl;
var urlparms = ['/api/advancesearch?'];
export default {
    data() {
        return {
            messages: '',
            csrf_token: '',
            quicksearch: '',
            isquick: true,
            isfirst: false,
            firstname: '',
            islast: false,
            isdob: false,
            isnib: false,
            isauth: false,
            isadmin: '',
            showsearch: false
        };
    },
    methods: {

        search(searchtype) {

            if (searchtype == "quick") {

                const qitem = document.querySelector("input#quicksearch").value;
                sessionStorage.setItem('queryurl', `/api/quicksearch?quicksearchquery=${qitem}`);
                this.$router.push('/mainresult');

            }
            else if (searchtype == "advance") {

                if (this.isfirst) {
                    let fname = document.querySelector("div input#firstname").value;

                    for (let i = 0; i < urlparms.length; i++) {
                        if (urlparms[i].startsWith("&firstname=")) {
                            urlparms[i] = `&firstname=${fname}`;
                            break;
                        }
                        else if (urlparms[i].startsWith("firstname=")) {
                            urlparms[i] = `firstname=${fname}`;
                            break;
                        }
                        else {
                            if (urlparms.length > 1) {
                                urlparms.push(`&firstname=${fname}`);
                                break;
                            }
                            else {
                                urlparms.push(`firstname=${fname}`);
                                break;
                            }
                        }
                    }
                    joinedurl = urlparms.join('');

                }


                if (this.islast) {
                    let lname = document.querySelector("div input#lastname").value;
                    for (let i = 0; i < urlparms.length; i++) {
                        if (urlparms[i].startsWith("&lastname=")) {
                            urlparms[i] = `&lastname=${lname}`;
                            break;
                        }
                        else if (urlparms[i].startsWith("lastname=")) {
                            urlparms[i] = `lastname=${lname}`;
                            break;
                        }
                        else {
                            if (urlparms.length > 1) {
                                urlparms.push(`&lastname=${lname}`);
                                break;
                            }
                            else {
                                urlparms.push(`lastname=${lname}`);
                                break;
                            }
                        }
                    }
                    joinedurl = urlparms.join('');

                }


                if (this.isdob) {
                    let dob = document.querySelector("div input#dob").value;

                    for (let i = 0; i < urlparms.length; i++) {
                        if (urlparms[i].startsWith("&dob=")) {
                            urlparms[i] = `&dob=${dob}`;
                            break;
                        }
                        else if (urlparms[i].startsWith("dob=")) {
                            urlparms[i] = `dob=${dob}`;
                            break;
                        }
                        else {
                            if (urlparms.length > 1) {
                                urlparms.push(`&dob=${dob}`);
                                break;
                            }
                            else {
                                urlparms.push(`dob=${dob}`);
                                break;
                            }
                        }
                    }
                    joinedurl = urlparms.join('');

                }

                if (this.isnib) {
                    let nib = document.querySelector("div input#nib").value;

                    for (let i = 0; i < urlparms.length; i++) {
                        if (urlparms[i].startsWith("&nib=")) {
                            urlparms[i] = `&nib=${nib}`;
                            break;
                        }
                        else if (urlparms[i].startsWith("nib=")) {
                            urlparms[i] = `nib=${nib}`;
                            break;
                        }
                        else {
                            if (urlparms.length > 1) {
                                urlparms.push(`&nib=${nib}`);
                                break;
                            }
                            else {
                                urlparms.push(`nib=${nib}`);
                                break;
                            }
                        }
                    }
                    joinedurl = urlparms.join('');

                }

                sessionStorage.setItem('queryurl', joinedurl);
                this.$router.push('/mainresult');

            }

        },
        quickmode() {
            const self = this;
            const advmode = document.querySelector("button#advmode");
            const quickmode = document.querySelector("button#quickmode");

            self.isquick = true;

            quickmode.classList.add('disabled');
            advmode.classList.remove('disabled');

        },

        advmode() {
            //const alertcontainer =  document.querySelector('section#msg');
            const self = this;
            self.isfirst = false;
            self.islast = false;
            self.isdob = false;
            self.isnib = false;

            const advmode = document.querySelector("button#advmode");
            const quickmode = document.querySelector("button#quickmode");

            self.isquick = false;

            quickmode.classList.remove('disabled');
            advmode.classList.add('disabled');

            /* alertcontainer.classList.remove('alert-danger');
             alertcontainer.classList.remove('alert-danger');
             alertcontainer.classList.remove('show');
             alertcontainer.classList.add('hide');*/


        },

        switchandler(label) {
            const self = this;
            const firstchecker = document.querySelector("input.firstname");
            const lastchecker = document.querySelector("input.lastname");
            const dobchecker = document.querySelector("input.dob");
            const nibchecker = document.querySelector("input.nib");

            switch (label) {
                case "firstname":
                    if (firstchecker.checked) {
                        self.isfirst = true;
                        self.showsearch = true;
                    }
                    else {

                        self.isfirst = false;
                    }
                case "lastname":
                    if (lastchecker.checked) {
                        self.islast = true;
                        self.showsearch = true;
                    }
                    else {
                        self.islast = false;
                    }
                case "dob":
                    if (dobchecker.checked) {
                        self.isdob = true;
                        self.showsearch = true;
                    }
                    else {
                        self.isdob = false;
                    }
                case "nib":
                    if (nibchecker.checked) {
                        self.showsearch = true;
                        self.isnib = true;
                    }
                    else {
                        self.isnib = false;
                    }
            }
        },

        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    self.csrf_token = data.csrf_token;
                })

        },

        addata() {
            fetch('/api/addata')
                .then((response) => response.json())
                .then((data) => {
                    self.messages = data.message;
                })
        }
    },
    created() {
        //this.getCsrfToken();
        if (sessionStorage.getItem('isauth') == 'true') {
            this.isauth = true;
            this.firstname = sessionStorage.getItem('first_name');
            if (sessionStorage.getItem('role') == "Admin"){
                this.isadmin =  true;
            }
            else{
                this.isadmin = false;
            }
            //this.addata();
        }
    }
}
</script>

<style>
div#QuickSearchForm {
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
    padding: 2em 0 2em 0;
    margin-top: 2em;
    width: 100%;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
}

form#divrow {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: center;
    width: 60%;
}

div#formgrp {
    width: 70%;
}

div#btndiv {
    width: 30%;
}

div#btndiv button {
    width: 100%;
}

div#advbtn {
    margin-top: 1em;
    width: 100%;
}

button {
    font-weight: bold !important;
}

div.inputcombo {
    display: flex;
    flex-flow: column wrap;
    margin-right: 1em;
}

form button {
    margin-top: 0em;
    width: 100%;
}

#btngrp button {
    width: 92%;
    background: #0E086D;
    color: #fff;
}

#btngrp button:hover {
    color: whitesmoke;
}

div.btn-group {
    width: 30%;
}

.btnsignin {
    width: 9rem;
    background: #0E086D;
    color: #fff;
    font-weight: bold;
}

label {
    color: #666;
    font-weight: bold;
}

.hide {
    display: none;
}

.show {
    display: block;
}

.hidecontainer {
    display: none !important;
}

.showgrid {
    display: grid !important;
}

.flexshow {
    display: flex !important;
}



div#advsearch {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
}


div#filters {
    display: flex;
    flex-flow: row wrap;
}

div.form-switch label {
    margin-right: 1em;
}

button a {
    color: #fff !important;
    padding: 0;
    margin: 0;
}


h3 {
    font-weight: bold;
}

section#skiptraceparent {
    width: 70%;
    display: flex;
    flex-flow: column wrap;
    margin: auto;
    align-items: center;
}

section#skiptraceparent div.greetcont{
    display: flex;
    flex-flow: row wrap;
    margin-top: 2em;
    width: 100%;
    justify-content: space-between;
}




div section p {
    color: #666;
}

section.warning {
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
    margin: 4em auto 2em auto;
    width: 90%;
}

section.warning a {
    width: fit-content;
    font-weight: bold;
}

section.resultcontainer {
    display: flex;
    width: 91%;
    margin: 0 auto 2em auto;
    flex-flow: column wrap;
}

section#msg {
    width: 89.5%;
    margin: 0 auto 0 auto;
    text-align: center;
}

div#recorditem {
    display: grid;
    grid-template-columns: repeat(11, 1fr);
    box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
    margin-bottom: 1.5em;
}

div#recorditem img {
    width: 3.5rem;
    margin: 0 auto;
}

div#recorditem div.rowinfo {
    display: flex;
    flex-flow: column wrap;
    color: #666;
}

span {
    color: #666;
}

span.fieldtitle {
    font-weight: bold;
}

.btnsignin {
    background: #0E086D;
    height: 2em !important;
    color: #fff;
}

button#searchagain {
    width: fit-content;
    margin-left: 2em;
}

div#pagination {
    display: grid;
    grid-template-columns: repeat(30, 1fr);
    width: 90%;
    margin: 1em auto 10em auto;
}

div#pagination button {
    width: 1em;
    padding-left: 1em;
    padding-right: 1em;
}



div#singleresult {
    display: gird;
    grid-template-columns: repeat(2, 1fr);
    width: 90% !important;
    margin: 0 auto;
    color: #666;
}

section#singlebanner {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: center;
    margin-top: 2em;
}

section#singlebanner button {
    margin-left: 10em;
}

section#singlebanner img {
    margin-right: 2em;
}

section#singlebanner h2 {
    margin-right: 0.5em;
}

section#infoparent {
    display: flex;
    flex-flow: column wrap;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    align-items: center;
    margin: 2em auto;
    padding: 1em;
}

section.inforow {
    display: flex;
    flex-flow: row wrap;
    width: 70%;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5em;
    border-bottom: solid rgba(99, 99, 99, 0.2) 0.1em;

}

section.inforow span {
    text-align: left;
}
</style>
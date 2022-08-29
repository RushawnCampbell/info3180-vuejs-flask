<template>


<section v-if=isauth id="skiptraceparent">
    
    
    <div  id="QuickSearchForm">
            <form @submit.prevent="search('quick')" v-if=isquick  id="divrow" >
                <div id="formgrp" class="form-group">
                    <h3 for="quicksearch">SKIPTRACE SEARCH QUICK MODE</h3>
                    <input type="text"  v-model="quicksearch" class="form-control" name="quicksearch" id="quicksearch"  placeholder="search anything">
                     <p>You are searching for <b>{{ quicksearch }}</b>  </p>

                </div>
                <div id="btndiv">
                    <button class="btn btn-success"> QUICK SEARCH</button>
                </div>
                
            </form>

            <form @submit.prevent="search('advance')" v-if=!isquick  id="advsearchparent">
                <h3 for="quicksearch">SKIPTRACE SEARCH ADVANCE MODE </h3>
                <span style="color:#666;">Toggle the filters to customize your search.</span><br/><br/>
                <div id="filters"> 

                    <div class="form-check form-switch" id="firstname">
                        <label class="form-check-label" for="flexSwitchCheckDefault">First Name</label>
                        <input  v-on:click ="switchandler('firstname')" class="form-check-input firstname" type="checkbox" id="flexSwitchCheckDefault">
                    </div>

                     <div  class="form-check form-switch" id="lastname">
                        <label class="form-check-label" for="flexSwitchCheckDefault">Last Name</label>
                        <input v-on:click ="switchandler('lastname')" class="form-check-input lastname" type="checkbox" id="flexSwitchCheckDefault">
                    </div>

                     <div  class="form-check form-switch" id="dob">
                         <label class="form-check-label" for="flexSwitchCheckDefault">D.O.B</label>
                        <input v-on:click ="switchandler('dob')" class="form-check-input dob" type="checkbox" id="flexSwitchCheckDefault">
                    </div>

                     <div  class="form-check form-switch" id="nib">
                        <label class="form-check-label" for="flexSwitchCheckDefault">NIB#</label>
                        <input v-on:click ="switchandler('nib')" class="form-check-input nib" type="checkbox" id="flexSwitchCheckDefault">
                    </div>  

                </div>
                <div id="advsearch">
                
                    <div v-if="`${isfirst}` == 'true'" class="inputcombo">
                        <label>First Name</label>
                        <input type="text" id="firstname" name="firstname"/>
                    </div>
                    <div v-if="`${islast}` == 'true'" class="inputcombo">
                        <label>Last Name</label>
                        <input type="text" id="lastname" name="lastname"/>
                    </div>
                    <div v-if="`${isnib}` == 'true'" class="inputcombo">
                        <label>NIB#</label>
                        <input type="text" id="nib" name="nib"/>
                    </div>
                    <div v-if="`${isdob}` == 'true'" class="inputcombo">
                        <label>D.O.B</label>
                        <input type="text"  id="dob" name="dob"/>
                    </div>
                   
                </div> 
                 <div v-if=showsearch id="advbtn">
                    <button  class="btn btn-success"> Search</button>
                </div>

            </form>
           
            
    </div>
    <br/>
    <div id="btngrp" class="btn-group" role="group" aria-label="Button Controls">
        <button id="quickmode" v-on:click="quickmode" type="button" class="btn disabled">QUICK MODE</button>
        <button id="advmode" v-on:click="advmode" type="button" class="btn">ADVANCE MODE</button>
    </div>

</section>

<section class="warning" v-else >
    <h2 class="text-danger"> You must be signed in to access this area.</h2>
    <RouterLink class="btn btnsignin" to="/signin">CLICK HERE TO SIGN IN</RouterLink>
</section>
<section id="msg" class=" form-control alert hide" >
    <span>{{messages}}</span>  <button v-on:click= "searchagain" v-if=isresult to="/search" id="searchagain" class=" btn btn-success"> SEARCH AGAIN</button>
</section>
<section v-if="`${isresult}` == 'true'" class="resultcontainer">

<div id="recorditem" v-for= "rec in records" >
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
       <a  v-on:click="singlehandler(rec)" class=" btn btnsignin">MORE INFO</a>
</div>


</section>
<div  id="pagination">

</div>


<div v-if="`${issingle}` == 'true'" id="singleresult">

    <section id="singlebanner">
        <img id="singleimg" src="../assets/images/apex-logo.png"/>
        <h2 id="firstname"></h2>
        <h2 id="lastname"></h2>
        <button id="backresults" class="btn btnsignin">BACK TO RESULTS</button>  
    </section>

    <section id="infoparent">

        <section class="inforow">
            <span class="infoitem"><b>MIDDLE NAME:</b></span>
            <span class="infoitem" id="inforowmiddle"></span>
        </section>

        <section class="inforow" >
            <span class="infoitem"><b>D.O.B:</b></span>
            <span class="infoitem" id="inforowdob"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>NIB#:</b></span>
            <span class="infoitem" id="inforownib"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>GENDER:</b></span>
            <span class="infoitem" id="inforowgender"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>MARITAL STATUS:</b></span>
            <span class="infoitem" id="inforowmar"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>HOME PH#:</b></span>
            <span class="infoitem" id="inforowhphone"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>CELL PH#:</b></span>
            <span class="infoitem" id="inforowcphone"></span>
        </section>

        <section class="inforow" >
            <span class="infoitem"><b>WORK PH#:</b></span>
            <span class="infoitem" id="inforowwphone"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>STREET ADDRESS:</b></span>
            <span class="infoitem" id="inforowsaddress"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>CITY:</b></span>
            <span class="infoitem" id="inforowcity"></span>
        </section>

        <section class="inforow">
            <span class="infoitem"><b>COUNTRY:</b></span>
            <span class="infoitem"  id="inforowcountry"></span>
        </section>

    </section>

</div>

</template>

<script>
var vanillarecords;
var pagelim;
var joinedurl;
var urlparms = ['/api/advancesearch?'];
var records;

const paginationchecker = setInterval(()=>{

    if(document.contains(document.querySelector("div#pagination button"))){
        let pagebtns = document.querySelectorAll("div#pagination button");
        let resultcontainer = document.querySelector("section.resultcontainer");
        
        pagebtns[0].classList.add("currcolor");

        pagebtns.forEach((btn)=>{
                
                btn.onclick = ()=>{

                    pagebtns.forEach((bt)=>{
                        bt.classList.remove("currcolor");
                        bt.classList.add("regcolor");
                    });

                    btn.classList.add("currcolor");
                    btn.classList.remove("regcolor");

                    resultcontainer.innerHTML = "";
                    let slicedrecords = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));
                   
                    
                    for (let rec=0; rec<slicedrecords.length; rec++){
                            const recorditem = document.createElement("div");
                            recorditem.setAttribute('id', 'recorditem');
                                        
                            const recordimg = document.createElement('img');
                            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
                            recordimg.setAttribute('class', 'recorditem' );

                            const fnamespanlabel = document.createElement('span');
                            fnamespanlabel.setAttribute('class', 'fieldtitle');
                            fnamespanlabel.appendChild(document.createTextNode('First Name'));

                            const lnamespanlabel = document.createElement('span');
                            lnamespanlabel.setAttribute('class', 'fieldtitle');
                            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                            const dobspanlabel = document.createElement('span');
                            dobspanlabel.setAttribute('class', 'fieldtitle');
                            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                            const nibspanlabel = document.createElement('span');
                            nibspanlabel.setAttribute('class', 'fieldtitle');
                            nibspanlabel.appendChild(document.createTextNode('NIB#'));

                            const homepspanlabel = document.createElement('span');
                            homepspanlabel.setAttribute('class', 'fieldtitle');
                            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                            const cellpspanlabel = document.createElement('span');
                            cellpspanlabel.setAttribute('class', 'fieldtitle');
                            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                            const workpspanlabel = document.createElement('span');
                            workpspanlabel.setAttribute('class', 'fieldtitle');
                            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                            const saddressspanlabel = document.createElement('span');
                            saddressspanlabel.setAttribute('class', 'fieldtitle');
                            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                            const cityspanlabel = document.createElement('span');
                            cityspanlabel.setAttribute('class', 'fieldtitle');
                            cityspanlabel.appendChild(document.createTextNode('City'));
                            
                            const fnameinfo = document.createElement('div');
                            fnameinfo.setAttribute('class', 'rowinfo');
                            const fnamespanvalue= document.createElement('span');
                            fnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].first_name));
                            fnameinfo.appendChild(fnamespanlabel);
                            fnameinfo.appendChild(fnamespanvalue);


                            const lnameinfo = document.createElement('div');
                            lnameinfo.setAttribute('class', 'rowinfo');
                            const lnamespanvalue= document.createElement('span');
                            lnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].last_name));
                            lnameinfo.appendChild(lnamespanlabel);
                            lnameinfo.appendChild(lnamespanvalue);


                            const dobinfo = document.createElement('div');
                            dobinfo.setAttribute('class', 'rowinfo');
                            const dobspanvalue= document.createElement('span');
                            dobspanvalue.appendChild(document.createTextNode(slicedrecords[rec].dob));
                            dobinfo.appendChild(dobspanlabel);
                            dobinfo.appendChild(dobspanvalue);


                            const nibinfo = document.createElement('div');
                            nibinfo.setAttribute('class', 'rowinfo');
                            const nibspanvalue= document.createElement('span');
                            nibspanvalue.appendChild(document.createTextNode(slicedrecords[rec].nib));
                            nibinfo.appendChild(nibspanlabel);
                            nibinfo.appendChild(nibspanvalue);


                            const homepinfo = document.createElement('div');
                            homepinfo.setAttribute('class', 'rowinfo');
                            const homepspanvalue= document.createElement('span');
                            homepspanvalue.appendChild(document.createTextNode(slicedrecords[rec].home_phone));
                            homepinfo.appendChild(homepspanlabel);
                            homepinfo.appendChild(homepspanvalue);


                            const cellpinfo = document.createElement('div');
                            cellpinfo.setAttribute('class', 'rowinfo');
                            const cellpspanvalue= document.createElement('span');
                            cellpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].cell_phone));
                            cellpinfo.appendChild(cellpspanlabel);
                            cellpinfo.appendChild(cellpspanvalue);

                            const workpinfo = document.createElement('div');
                            workpinfo.setAttribute('class', 'rowinfo');
                            const workpspanvalue= document.createElement('span');
                            workpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].work_phone));
                            workpinfo.appendChild(workpspanlabel);
                            workpinfo.appendChild(workpspanvalue);



                            const saddressinfo = document.createElement('div');
                            saddressinfo.setAttribute('class', 'rowinfo');
                            const saddressspanvalue= document.createElement('span');
                            saddressspanvalue.appendChild(document.createTextNode(slicedrecords[rec].street_address));
                            saddressinfo.appendChild(saddressspanlabel);
                            saddressinfo.appendChild(saddressspanvalue);


                            const cityinfo = document.createElement('div');
                            cityinfo.setAttribute('class', 'rowinfo');
                            const cityspanvalue= document.createElement('span');
                            cityspanvalue.appendChild(document.createTextNode(slicedrecords[rec].city));
                            cityinfo.appendChild(cityspanlabel);
                            cityinfo.appendChild(cityspanvalue);


                            const moreinfo =document.createElement('a');
                            moreinfo.setAttribute('class', 'btn');
                            moreinfo.classList.add('btnsignin');
                            moreinfo.innerHTML = "MORE INFO";

                            moreinfo.addEventListener("click",function (){
                                sessionStorage.setItem('issingle', true);
                                this.issingle =true;
                                sessionStorage.setItem('isresult', false);
                                this.isresult = false;
                                const msg = document.querySelector("section#msg");
                                msg.classList.add('hide');
                                msg.classList.remove('show');

                                const pagination =  document.querySelector("div#pagination");


                                pagination.classList.remove("showgrid");
                                pagination.classList.add("hidecontainer");

                                let itemchecker =setInterval(()=>{
                                    if(document.contains(document.querySelector('h2#firstname'))){
                        
                                        document.querySelector('h2#firstname').innerHTML ='';
                                        document.querySelector('h2#firstname').appendChild(document.createTextNode(slicedrecords[rec].first_name));

                                        document.querySelector('h2#lastname').innerHTML = '';
                                        document.querySelector('h2#lastname').appendChild(document.createTextNode(slicedrecords[rec].last_name));

                                        document.querySelector('span#inforowmiddle').innerHTML;
                                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(slicedrecords[rec].middle_name));

                                        document.querySelector('span#inforownib').innerHTML ='';
                                        document.querySelector('span#inforownib').appendChild(document.createTextNode(slicedrecords[rec].nib));

                                        document.querySelector('span#inforowdob').innerHTML= '';
                                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(slicedrecords[rec].dob));

                                        document.querySelector('span#inforowgender').innerHTML = '';
                                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(slicedrecords[rec].gender));

                                        document.querySelector('span#inforowmar').innerHTML = '';
                                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(slicedrecords[rec].marital_status));

                                        document.querySelector('span#inforowhphone').innerHTML= '';
                                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(slicedrecords[rec].home_phone));
                                        
                                        document.querySelector('span#inforowcphone').innerHTML = '';
                                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(slicedrecords[rec].cell_phone));

                                        document.querySelector('span#inforowwphone').innerHTML = '';
                                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(slicedrecords[rec].work_phone));

                                        document.querySelector('span#inforowsaddress').innerHTML = '';
                                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(slicedrecords[rec].street_address));

                                        document.querySelector('span#inforowcity').innerHTML ='';
                                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(slicedrecords[rec].city));

                                        document.querySelector('span#inforowcountry').innerHTML = '';
                                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(slicedrecords[rec].country));


                                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                                            sessionStorage.setItem('issingle', false);
                                            this.issingle =false;
                                            sessionStorage.setItem('isresult', true);
                                            this.isresult = true;
                                            msg.classList.remove('hide');
                                            msg.classList.add('show');
                                            pagination.classList.add("showgrid");
                                            pagination.classList.remove("hidecontainer");

                                            let pagebtns = document.querySelectorAll("div#pagination button");

                                            let currid = 0;

                                            let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((b)=>{
                                    if (b.classList.contains('currcolor')){
                                        currid = parseInt(b.getAttribute('id'));
                                    }
                                });

                                records = vanillarecords.slice( (currid * pagelim) - (pagelim), currid * pagelim);


                                for (let rec=0; rec<records.length; rec++){
                            const recorditem = document.createElement("div");
                            recorditem.setAttribute('id', 'recorditem');
                                        
                            const recordimg = document.createElement('img');
                            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
                            recordimg.setAttribute('class', 'recorditem' );

                            const fnamespanlabel = document.createElement('span');
                            fnamespanlabel.setAttribute('class', 'fieldtitle');
                            fnamespanlabel.appendChild(document.createTextNode('First Name'));

                            const lnamespanlabel = document.createElement('span');
                            lnamespanlabel.setAttribute('class', 'fieldtitle');
                            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                            const dobspanlabel = document.createElement('span');
                            dobspanlabel.setAttribute('class', 'fieldtitle');
                            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                            const nibspanlabel = document.createElement('span');
                            nibspanlabel.setAttribute('class', 'fieldtitle');
                            nibspanlabel.appendChild(document.createTextNode('NIB#'));

                            const homepspanlabel = document.createElement('span');
                            homepspanlabel.setAttribute('class', 'fieldtitle');
                            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                            const cellpspanlabel = document.createElement('span');
                            cellpspanlabel.setAttribute('class', 'fieldtitle');
                            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                            const workpspanlabel = document.createElement('span');
                            workpspanlabel.setAttribute('class', 'fieldtitle');
                            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                            const saddressspanlabel = document.createElement('span');
                            saddressspanlabel.setAttribute('class', 'fieldtitle');
                            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                            const cityspanlabel = document.createElement('span');
                            cityspanlabel.setAttribute('class', 'fieldtitle');
                            cityspanlabel.appendChild(document.createTextNode('City'));
                            
                            const fnameinfo = document.createElement('div');
                            fnameinfo.setAttribute('class', 'rowinfo');
                            const fnamespanvalue= document.createElement('span');
                            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
                            fnameinfo.appendChild(fnamespanlabel);
                            fnameinfo.appendChild(fnamespanvalue);


                            const lnameinfo = document.createElement('div');
                            lnameinfo.setAttribute('class', 'rowinfo');
                            const lnamespanvalue= document.createElement('span');
                            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
                            lnameinfo.appendChild(lnamespanlabel);
                            lnameinfo.appendChild(lnamespanvalue);


                            const dobinfo = document.createElement('div');
                            dobinfo.setAttribute('class', 'rowinfo');
                            const dobspanvalue= document.createElement('span');
                            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
                            dobinfo.appendChild(dobspanlabel);
                            dobinfo.appendChild(dobspanvalue);


                            const nibinfo = document.createElement('div');
                            nibinfo.setAttribute('class', 'rowinfo');
                            const nibspanvalue= document.createElement('span');
                            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
                            nibinfo.appendChild(nibspanlabel);
                            nibinfo.appendChild(nibspanvalue);


                            const homepinfo = document.createElement('div');
                            homepinfo.setAttribute('class', 'rowinfo');
                            const homepspanvalue= document.createElement('span');
                            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
                            homepinfo.appendChild(homepspanlabel);
                            homepinfo.appendChild(homepspanvalue);


                            const cellpinfo = document.createElement('div');
                            cellpinfo.setAttribute('class', 'rowinfo');
                            const cellpspanvalue= document.createElement('span');
                            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
                            cellpinfo.appendChild(cellpspanlabel);
                            cellpinfo.appendChild(cellpspanvalue);

                            const workpinfo = document.createElement('div');
                            workpinfo.setAttribute('class', 'rowinfo');
                            const workpspanvalue= document.createElement('span');
                            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
                            workpinfo.appendChild(workpspanlabel);
                            workpinfo.appendChild(workpspanvalue);



                            const saddressinfo = document.createElement('div');
                            saddressinfo.setAttribute('class', 'rowinfo');
                            const saddressspanvalue= document.createElement('span');
                            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
                            saddressinfo.appendChild(saddressspanlabel);
                            saddressinfo.appendChild(saddressspanvalue);


                            const cityinfo = document.createElement('div');
                            cityinfo.setAttribute('class', 'rowinfo');
                            const cityspanvalue= document.createElement('span');
                            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
                            cityinfo.appendChild(cityspanlabel);
                            cityinfo.appendChild(cityspanvalue);


                            const moreinfo =document.createElement('a');
                            moreinfo.setAttribute('class', 'btn');
                            moreinfo.classList.add('btnsignin');
                            moreinfo.innerHTML = "MORE INFO";

                            moreinfo.addEventListener("click",function (){
                                sessionStorage.setItem('issingle', true);
                                this.issingle =true;
                                sessionStorage.setItem('isresult', false);
                                this.isresult = false;
                                const msg = document.querySelector("section#msg");
                                msg.classList.add('hide');
                                msg.classList.remove('show');

                                const pagination =  document.querySelector("div#pagination");


                                pagination.classList.remove("showgrid");
                                pagination.classList.add("hidecontainer");

                                let itemchecker =setInterval(()=>{
                                    if(document.contains(document.querySelector('h2#firstname'))){
                        
                                        document.querySelector('h2#firstname').innerHTML ='';
                                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                                        document.querySelector('h2#lastname').innerHTML = '';
                                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                                        document.querySelector('span#inforowmiddle').innerHTML;
                                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                                        document.querySelector('span#inforownib').innerHTML ='';
                                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                                        document.querySelector('span#inforowdob').innerHTML= '';
                                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                                        document.querySelector('span#inforowgender').innerHTML = '';
                                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                                        document.querySelector('span#inforowmar').innerHTML = '';
                                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                                        document.querySelector('span#inforowhphone').innerHTML= '';
                                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                                        
                                        document.querySelector('span#inforowcphone').innerHTML = '';
                                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                                        document.querySelector('span#inforowwphone').innerHTML = '';
                                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                                        document.querySelector('span#inforowsaddress').innerHTML = '';
                                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                                        document.querySelector('span#inforowcity').innerHTML ='';
                                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                                        document.querySelector('span#inforowcountry').innerHTML = '';
                                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                                            sessionStorage.setItem('issingle', false);
                                            this.issingle =false;
                                            sessionStorage.setItem('isresult', true);
                                            this.isresult = true;
                                            msg.classList.remove('hide');
                                            msg.classList.add('show');
                                            pagination.classList.add("showgrid");
                                            pagination.classList.remove("hidecontainer");

                                            let pagebtns = document.querySelectorAll("div#pagination button");

                                            let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            
            document.querySelector("section.resultcontainer").innerHTML = "";
            let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<records.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");


let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
clearInterval(backchecker);
document.querySelector("section.resultcontainer").innerHTML = "";
pagebtns.forEach((btn)=>{

btn.addEventListener('click',()=>{
document.querySelector("section.resultcontainer").innerHTML = "";
let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
for (let rec=0; rec<records.length; rec++){
const recorditem = document.createElement("div");
recorditem.setAttribute('id', 'recorditem');

const recordimg = document.createElement('img');
recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
recordimg.setAttribute('class', 'recorditem' );

const fnamespanlabel = document.createElement('span');
fnamespanlabel.setAttribute('class', 'fieldtitle');
fnamespanlabel.appendChild(document.createTextNode('First Name'));

const lnamespanlabel = document.createElement('span');
lnamespanlabel.setAttribute('class', 'fieldtitle');
lnamespanlabel.appendChild(document.createTextNode('Last Name'));

const dobspanlabel = document.createElement('span');
dobspanlabel.setAttribute('class', 'fieldtitle');
dobspanlabel.appendChild(document.createTextNode('D.O.B'));

const nibspanlabel = document.createElement('span');
nibspanlabel.setAttribute('class', 'fieldtitle');
nibspanlabel.appendChild(document.createTextNode('NIB#'));

const homepspanlabel = document.createElement('span');
homepspanlabel.setAttribute('class', 'fieldtitle');
homepspanlabel.appendChild(document.createTextNode('Home Phone'));

const cellpspanlabel = document.createElement('span');
cellpspanlabel.setAttribute('class', 'fieldtitle');
cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

const workpspanlabel = document.createElement('span');
workpspanlabel.setAttribute('class', 'fieldtitle');
workpspanlabel.appendChild(document.createTextNode('Work Phone'));

const saddressspanlabel = document.createElement('span');
saddressspanlabel.setAttribute('class', 'fieldtitle');
saddressspanlabel.appendChild(document.createTextNode('Street Address'));

const cityspanlabel = document.createElement('span');
cityspanlabel.setAttribute('class', 'fieldtitle');
cityspanlabel.appendChild(document.createTextNode('City'));

const fnameinfo = document.createElement('div');
fnameinfo.setAttribute('class', 'rowinfo');
const fnamespanvalue= document.createElement('span');
fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
fnameinfo.appendChild(fnamespanlabel);
fnameinfo.appendChild(fnamespanvalue);


const lnameinfo = document.createElement('div');
lnameinfo.setAttribute('class', 'rowinfo');
const lnamespanvalue= document.createElement('span');
lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
lnameinfo.appendChild(lnamespanlabel);
lnameinfo.appendChild(lnamespanvalue);


const dobinfo = document.createElement('div');
dobinfo.setAttribute('class', 'rowinfo');
const dobspanvalue= document.createElement('span');
dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
dobinfo.appendChild(dobspanlabel);
dobinfo.appendChild(dobspanvalue);


const nibinfo = document.createElement('div');
nibinfo.setAttribute('class', 'rowinfo');
const nibspanvalue= document.createElement('span');
nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
nibinfo.appendChild(nibspanlabel);
nibinfo.appendChild(nibspanvalue);


const homepinfo = document.createElement('div');
homepinfo.setAttribute('class', 'rowinfo');
const homepspanvalue= document.createElement('span');
homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
homepinfo.appendChild(homepspanlabel);
homepinfo.appendChild(homepspanvalue);


const cellpinfo = document.createElement('div');
cellpinfo.setAttribute('class', 'rowinfo');
const cellpspanvalue= document.createElement('span');
cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
cellpinfo.appendChild(cellpspanlabel);
cellpinfo.appendChild(cellpspanvalue);

const workpinfo = document.createElement('div');
workpinfo.setAttribute('class', 'rowinfo');
const workpspanvalue= document.createElement('span');
workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
workpinfo.appendChild(workpspanlabel);
workpinfo.appendChild(workpspanvalue);



const saddressinfo = document.createElement('div');
saddressinfo.setAttribute('class', 'rowinfo');
const saddressspanvalue= document.createElement('span');
saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
saddressinfo.appendChild(saddressspanlabel);
saddressinfo.appendChild(saddressspanvalue);


const cityinfo = document.createElement('div');
cityinfo.setAttribute('class', 'rowinfo');
const cityspanvalue= document.createElement('span');
cityspanvalue.appendChild(document.createTextNode(records[rec].city));
cityinfo.appendChild(cityspanlabel);
cityinfo.appendChild(cityspanvalue);


const moreinfo =document.createElement('a');
moreinfo.setAttribute('class', 'btn');
moreinfo.classList.add('btnsignin');
moreinfo.innerHTML = "MORE INFO";

moreinfo.addEventListener("click",function (){
sessionStorage.setItem('issingle', true);
this.issingle =true;
sessionStorage.setItem('isresult', false);
this.isresult = false;
const msg = document.querySelector("section#msg");
msg.classList.add('hide');
msg.classList.remove('show');

const pagination =  document.querySelector("div#pagination");


pagination.classList.remove("showgrid");
pagination.classList.add("hidecontainer");

let itemchecker =setInterval(()=>{
if(document.contains(document.querySelector('h2#firstname'))){

document.querySelector('h2#firstname').innerHTML ='';
document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

document.querySelector('h2#lastname').innerHTML = '';
document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

document.querySelector('span#inforowmiddle').innerHTML;
document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

document.querySelector('span#inforownib').innerHTML ='';
document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

document.querySelector('span#inforowdob').innerHTML= '';
document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

document.querySelector('span#inforowgender').innerHTML = '';
document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

document.querySelector('span#inforowmar').innerHTML = '';
document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

document.querySelector('span#inforowhphone').innerHTML= '';
document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));

document.querySelector('span#inforowcphone').innerHTML = '';
document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

document.querySelector('span#inforowwphone').innerHTML = '';
document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

document.querySelector('span#inforowsaddress').innerHTML = '';
document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

document.querySelector('span#inforowcity').innerHTML ='';
document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

document.querySelector('span#inforowcountry').innerHTML = '';
document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


document.querySelector("button#backresults").addEventListener('click', ()=>{
sessionStorage.setItem('issingle', false);
this.issingle =false;
sessionStorage.setItem('isresult', true);
this.isresult = true;
msg.classList.remove('hide');
msg.classList.add('show');
pagination.classList.add("showgrid");
pagination.classList.remove("hidecontainer");

let pagebtns = document.querySelectorAll("div#pagination button");

});

clearInterval(itemchecker);
}

}, 1);

});


recorditem.appendChild(recordimg);
recorditem.appendChild(fnameinfo);
recorditem.appendChild(lnameinfo);
recorditem.appendChild(dobinfo);
recorditem.appendChild(nibinfo);
recorditem.appendChild(homepinfo);
recorditem.appendChild(cellpinfo);
recorditem.appendChild(workpinfo);
recorditem.appendChild(saddressinfo);
recorditem.appendChild(cityinfo);
recorditem.appendChild(moreinfo);

document.querySelector("section.resultcontainer").appendChild(recorditem);


}

});


});

}

},0);
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
    
        
});

}

},0);
                                        
                                        });

                                        clearInterval(itemchecker);
                                    }

                                }, 0);
                                
                            });


                            recorditem.appendChild(recordimg);
                            recorditem.appendChild(fnameinfo);
                            recorditem.appendChild(lnameinfo);
                            recorditem.appendChild(dobinfo);
                            recorditem.appendChild(nibinfo);
                            recorditem.appendChild(homepinfo);
                            recorditem.appendChild(cellpinfo);
                            recorditem.appendChild(workpinfo);
                            recorditem.appendChild(saddressinfo);
                            recorditem.appendChild(cityinfo);
                            recorditem.appendChild(moreinfo);

                           document.querySelector("section.resultcontainer").appendChild(recorditem);


                    }                          
    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            
            document.querySelector("section.resultcontainer").innerHTML = "";
            let slicedrecords = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<slicedrecords.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(slicedrecords[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(slicedrecords[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(slicedrecords[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(slicedrecords[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(slicedrecords[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(slicedrecords[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(slicedrecords[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(slicedrecords[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(slicedrecords[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(slicedrecords[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(slicedrecords[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(slicedrecords[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(slicedrecords[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(slicedrecords[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(slicedrecords[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(slicedrecords[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(slicedrecords[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(slicedrecords[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");

                            let currid = 0;


let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
clearInterval(backchecker);
document.querySelector("section.resultcontainer").innerHTML = "";
pagebtns.forEach((b)=>{
                                    if (b.classList.contains('currcolor')){
                                        currid = parseInt(b.getAttribute('id'));
                                    }
                                });

                                records = vanillarecords.slice( (currid * pagelim) - (pagelim), currid * pagelim);

for (let rec=0; rec<records.length; rec++){
                            const recorditem = document.createElement("div");
                            recorditem.setAttribute('id', 'recorditem');
                                        
                            const recordimg = document.createElement('img');
                            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
                            recordimg.setAttribute('class', 'recorditem' );

                            const fnamespanlabel = document.createElement('span');
                            fnamespanlabel.setAttribute('class', 'fieldtitle');
                            fnamespanlabel.appendChild(document.createTextNode('First Name'));

                            const lnamespanlabel = document.createElement('span');
                            lnamespanlabel.setAttribute('class', 'fieldtitle');
                            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                            const dobspanlabel = document.createElement('span');
                            dobspanlabel.setAttribute('class', 'fieldtitle');
                            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                            const nibspanlabel = document.createElement('span');
                            nibspanlabel.setAttribute('class', 'fieldtitle');
                            nibspanlabel.appendChild(document.createTextNode('NIB#'));

                            const homepspanlabel = document.createElement('span');
                            homepspanlabel.setAttribute('class', 'fieldtitle');
                            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                            const cellpspanlabel = document.createElement('span');
                            cellpspanlabel.setAttribute('class', 'fieldtitle');
                            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                            const workpspanlabel = document.createElement('span');
                            workpspanlabel.setAttribute('class', 'fieldtitle');
                            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                            const saddressspanlabel = document.createElement('span');
                            saddressspanlabel.setAttribute('class', 'fieldtitle');
                            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                            const cityspanlabel = document.createElement('span');
                            cityspanlabel.setAttribute('class', 'fieldtitle');
                            cityspanlabel.appendChild(document.createTextNode('City'));
                            
                            const fnameinfo = document.createElement('div');
                            fnameinfo.setAttribute('class', 'rowinfo');
                            const fnamespanvalue= document.createElement('span');
                            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
                            fnameinfo.appendChild(fnamespanlabel);
                            fnameinfo.appendChild(fnamespanvalue);


                            const lnameinfo = document.createElement('div');
                            lnameinfo.setAttribute('class', 'rowinfo');
                            const lnamespanvalue= document.createElement('span');
                            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
                            lnameinfo.appendChild(lnamespanlabel);
                            lnameinfo.appendChild(lnamespanvalue);


                            const dobinfo = document.createElement('div');
                            dobinfo.setAttribute('class', 'rowinfo');
                            const dobspanvalue= document.createElement('span');
                            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
                            dobinfo.appendChild(dobspanlabel);
                            dobinfo.appendChild(dobspanvalue);


                            const nibinfo = document.createElement('div');
                            nibinfo.setAttribute('class', 'rowinfo');
                            const nibspanvalue= document.createElement('span');
                            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
                            nibinfo.appendChild(nibspanlabel);
                            nibinfo.appendChild(nibspanvalue);


                            const homepinfo = document.createElement('div');
                            homepinfo.setAttribute('class', 'rowinfo');
                            const homepspanvalue= document.createElement('span');
                            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
                            homepinfo.appendChild(homepspanlabel);
                            homepinfo.appendChild(homepspanvalue);


                            const cellpinfo = document.createElement('div');
                            cellpinfo.setAttribute('class', 'rowinfo');
                            const cellpspanvalue= document.createElement('span');
                            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
                            cellpinfo.appendChild(cellpspanlabel);
                            cellpinfo.appendChild(cellpspanvalue);

                            const workpinfo = document.createElement('div');
                            workpinfo.setAttribute('class', 'rowinfo');
                            const workpspanvalue= document.createElement('span');
                            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
                            workpinfo.appendChild(workpspanlabel);
                            workpinfo.appendChild(workpspanvalue);



                            const saddressinfo = document.createElement('div');
                            saddressinfo.setAttribute('class', 'rowinfo');
                            const saddressspanvalue= document.createElement('span');
                            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
                            saddressinfo.appendChild(saddressspanlabel);
                            saddressinfo.appendChild(saddressspanvalue);


                            const cityinfo = document.createElement('div');
                            cityinfo.setAttribute('class', 'rowinfo');
                            const cityspanvalue= document.createElement('span');
                            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
                            cityinfo.appendChild(cityspanlabel);
                            cityinfo.appendChild(cityspanvalue);


                            const moreinfo =document.createElement('a');
                            moreinfo.setAttribute('class', 'btn');
                            moreinfo.classList.add('btnsignin');
                            moreinfo.innerHTML = "MORE INFO";

                            moreinfo.addEventListener("click",function (){
                                sessionStorage.setItem('issingle', true);
                                this.issingle =true;
                                sessionStorage.setItem('isresult', false);
                                this.isresult = false;
                                const msg = document.querySelector("section#msg");
                                msg.classList.add('hide');
                                msg.classList.remove('show');

                                const pagination =  document.querySelector("div#pagination");


                                pagination.classList.remove("showgrid");
                                pagination.classList.add("hidecontainer");

                                let itemchecker =setInterval(()=>{
                                    if(document.contains(document.querySelector('h2#firstname'))){
                        
                                        document.querySelector('h2#firstname').innerHTML ='';
                                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                                        document.querySelector('h2#lastname').innerHTML = '';
                                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                                        document.querySelector('span#inforowmiddle').innerHTML;
                                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                                        document.querySelector('span#inforownib').innerHTML ='';
                                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                                        document.querySelector('span#inforowdob').innerHTML= '';
                                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                                        document.querySelector('span#inforowgender').innerHTML = '';
                                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                                        document.querySelector('span#inforowmar').innerHTML = '';
                                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                                        document.querySelector('span#inforowhphone').innerHTML= '';
                                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                                        
                                        document.querySelector('span#inforowcphone').innerHTML = '';
                                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                                        document.querySelector('span#inforowwphone').innerHTML = '';
                                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                                        document.querySelector('span#inforowsaddress').innerHTML = '';
                                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                                        document.querySelector('span#inforowcity').innerHTML ='';
                                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                                        document.querySelector('span#inforowcountry').innerHTML = '';
                                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                                            sessionStorage.setItem('issingle', false);
                                            this.issingle =false;
                                            sessionStorage.setItem('isresult', true);
                                            this.isresult = true;
                                            msg.classList.remove('hide');
                                            msg.classList.add('show');
                                            pagination.classList.add("showgrid");
                                            pagination.classList.remove("hidecontainer");

                                            let pagebtns = document.querySelectorAll("div#pagination button");

                                            let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            
            document.querySelector("section.resultcontainer").innerHTML = "";
            let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<records.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");


let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
clearInterval(backchecker);
document.querySelector("section.resultcontainer").innerHTML = "";
pagebtns.forEach((btn)=>{

btn.addEventListener('click',()=>{
document.querySelector("section.resultcontainer").innerHTML = "";
let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
for (let rec=0; rec<records.length; rec++){
const recorditem = document.createElement("div");
recorditem.setAttribute('id', 'recorditem');

const recordimg = document.createElement('img');
recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
recordimg.setAttribute('class', 'recorditem' );

const fnamespanlabel = document.createElement('span');
fnamespanlabel.setAttribute('class', 'fieldtitle');
fnamespanlabel.appendChild(document.createTextNode('First Name'));

const lnamespanlabel = document.createElement('span');
lnamespanlabel.setAttribute('class', 'fieldtitle');
lnamespanlabel.appendChild(document.createTextNode('Last Name'));

const dobspanlabel = document.createElement('span');
dobspanlabel.setAttribute('class', 'fieldtitle');
dobspanlabel.appendChild(document.createTextNode('D.O.B'));

const nibspanlabel = document.createElement('span');
nibspanlabel.setAttribute('class', 'fieldtitle');
nibspanlabel.appendChild(document.createTextNode('NIB#'));

const homepspanlabel = document.createElement('span');
homepspanlabel.setAttribute('class', 'fieldtitle');
homepspanlabel.appendChild(document.createTextNode('Home Phone'));

const cellpspanlabel = document.createElement('span');
cellpspanlabel.setAttribute('class', 'fieldtitle');
cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

const workpspanlabel = document.createElement('span');
workpspanlabel.setAttribute('class', 'fieldtitle');
workpspanlabel.appendChild(document.createTextNode('Work Phone'));

const saddressspanlabel = document.createElement('span');
saddressspanlabel.setAttribute('class', 'fieldtitle');
saddressspanlabel.appendChild(document.createTextNode('Street Address'));

const cityspanlabel = document.createElement('span');
cityspanlabel.setAttribute('class', 'fieldtitle');
cityspanlabel.appendChild(document.createTextNode('City'));

const fnameinfo = document.createElement('div');
fnameinfo.setAttribute('class', 'rowinfo');
const fnamespanvalue= document.createElement('span');
fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
fnameinfo.appendChild(fnamespanlabel);
fnameinfo.appendChild(fnamespanvalue);


const lnameinfo = document.createElement('div');
lnameinfo.setAttribute('class', 'rowinfo');
const lnamespanvalue= document.createElement('span');
lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
lnameinfo.appendChild(lnamespanlabel);
lnameinfo.appendChild(lnamespanvalue);


const dobinfo = document.createElement('div');
dobinfo.setAttribute('class', 'rowinfo');
const dobspanvalue= document.createElement('span');
dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
dobinfo.appendChild(dobspanlabel);
dobinfo.appendChild(dobspanvalue);


const nibinfo = document.createElement('div');
nibinfo.setAttribute('class', 'rowinfo');
const nibspanvalue= document.createElement('span');
nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
nibinfo.appendChild(nibspanlabel);
nibinfo.appendChild(nibspanvalue);


const homepinfo = document.createElement('div');
homepinfo.setAttribute('class', 'rowinfo');
const homepspanvalue= document.createElement('span');
homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
homepinfo.appendChild(homepspanlabel);
homepinfo.appendChild(homepspanvalue);


const cellpinfo = document.createElement('div');
cellpinfo.setAttribute('class', 'rowinfo');
const cellpspanvalue= document.createElement('span');
cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
cellpinfo.appendChild(cellpspanlabel);
cellpinfo.appendChild(cellpspanvalue);

const workpinfo = document.createElement('div');
workpinfo.setAttribute('class', 'rowinfo');
const workpspanvalue= document.createElement('span');
workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
workpinfo.appendChild(workpspanlabel);
workpinfo.appendChild(workpspanvalue);



const saddressinfo = document.createElement('div');
saddressinfo.setAttribute('class', 'rowinfo');
const saddressspanvalue= document.createElement('span');
saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
saddressinfo.appendChild(saddressspanlabel);
saddressinfo.appendChild(saddressspanvalue);


const cityinfo = document.createElement('div');
cityinfo.setAttribute('class', 'rowinfo');
const cityspanvalue= document.createElement('span');
cityspanvalue.appendChild(document.createTextNode(records[rec].city));
cityinfo.appendChild(cityspanlabel);
cityinfo.appendChild(cityspanvalue);


const moreinfo =document.createElement('a');
moreinfo.setAttribute('class', 'btn');
moreinfo.classList.add('btnsignin');
moreinfo.innerHTML = "MORE INFO";

moreinfo.addEventListener("click",function (){
sessionStorage.setItem('issingle', true);
this.issingle =true;
sessionStorage.setItem('isresult', false);
this.isresult = false;
const msg = document.querySelector("section#msg");
msg.classList.add('hide');
msg.classList.remove('show');

const pagination =  document.querySelector("div#pagination");


pagination.classList.remove("showgrid");
pagination.classList.add("hidecontainer");

let itemchecker =setInterval(()=>{
if(document.contains(document.querySelector('h2#firstname'))){

document.querySelector('h2#firstname').innerHTML ='';
document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

document.querySelector('h2#lastname').innerHTML = '';
document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

document.querySelector('span#inforowmiddle').innerHTML;
document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

document.querySelector('span#inforownib').innerHTML ='';
document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

document.querySelector('span#inforowdob').innerHTML= '';
document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

document.querySelector('span#inforowgender').innerHTML = '';
document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

document.querySelector('span#inforowmar').innerHTML = '';
document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

document.querySelector('span#inforowhphone').innerHTML= '';
document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));

document.querySelector('span#inforowcphone').innerHTML = '';
document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

document.querySelector('span#inforowwphone').innerHTML = '';
document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

document.querySelector('span#inforowsaddress').innerHTML = '';
document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

document.querySelector('span#inforowcity').innerHTML ='';
document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

document.querySelector('span#inforowcountry').innerHTML = '';
document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


document.querySelector("button#backresults").addEventListener('click', ()=>{
sessionStorage.setItem('issingle', false);
this.issingle =false;
sessionStorage.setItem('isresult', true);
this.isresult = true;
msg.classList.remove('hide');
msg.classList.add('show');
pagination.classList.add("showgrid");
pagination.classList.remove("hidecontainer");

let pagebtns = document.querySelectorAll("div#pagination button");

});

clearInterval(itemchecker);
}

}, 1);

});


recorditem.appendChild(recordimg);
recorditem.appendChild(fnameinfo);
recorditem.appendChild(lnameinfo);
recorditem.appendChild(dobinfo);
recorditem.appendChild(nibinfo);
recorditem.appendChild(homepinfo);
recorditem.appendChild(cellpinfo);
recorditem.appendChild(workpinfo);
recorditem.appendChild(saddressinfo);
recorditem.appendChild(cityinfo);
recorditem.appendChild(moreinfo);

document.querySelector("section.resultcontainer").appendChild(recorditem);


}

});


});

}

},0);
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
    
        
});

}

},0);
                                        
                                        });

                                        clearInterval(itemchecker);
                                    }

                                }, 0);
                                
                            });


                            recorditem.appendChild(recordimg);
                            recorditem.appendChild(fnameinfo);
                            recorditem.appendChild(lnameinfo);
                            recorditem.appendChild(dobinfo);
                            recorditem.appendChild(nibinfo);
                            recorditem.appendChild(homepinfo);
                            recorditem.appendChild(cellpinfo);
                            recorditem.appendChild(workpinfo);
                            recorditem.appendChild(saddressinfo);
                            recorditem.appendChild(cityinfo);
                            recorditem.appendChild(moreinfo);

                           document.querySelector("section.resultcontainer").appendChild(recorditem);


                    }
pagebtns.forEach((btn)=>{
btn.addEventListener('click',()=>{
document.querySelector("section.resultcontainer").innerHTML = "";
let slicedrecords = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
for (let rec=0; rec<slicedrecords.length; rec++){
const recorditem = document.createElement("div");
recorditem.setAttribute('id', 'recorditem');

const recordimg = document.createElement('img');
recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
recordimg.setAttribute('class', 'recorditem' );

const fnamespanlabel = document.createElement('span');
fnamespanlabel.setAttribute('class', 'fieldtitle');
fnamespanlabel.appendChild(document.createTextNode('First Name'));

const lnamespanlabel = document.createElement('span');
lnamespanlabel.setAttribute('class', 'fieldtitle');
lnamespanlabel.appendChild(document.createTextNode('Last Name'));

const dobspanlabel = document.createElement('span');
dobspanlabel.setAttribute('class', 'fieldtitle');
dobspanlabel.appendChild(document.createTextNode('D.O.B'));

const nibspanlabel = document.createElement('span');
nibspanlabel.setAttribute('class', 'fieldtitle');
nibspanlabel.appendChild(document.createTextNode('NIB#'));

const homepspanlabel = document.createElement('span');
homepspanlabel.setAttribute('class', 'fieldtitle');
homepspanlabel.appendChild(document.createTextNode('Home Phone'));

const cellpspanlabel = document.createElement('span');
cellpspanlabel.setAttribute('class', 'fieldtitle');
cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

const workpspanlabel = document.createElement('span');
workpspanlabel.setAttribute('class', 'fieldtitle');
workpspanlabel.appendChild(document.createTextNode('Work Phone'));

const saddressspanlabel = document.createElement('span');
saddressspanlabel.setAttribute('class', 'fieldtitle');
saddressspanlabel.appendChild(document.createTextNode('Street Address'));

const cityspanlabel = document.createElement('span');
cityspanlabel.setAttribute('class', 'fieldtitle');
cityspanlabel.appendChild(document.createTextNode('City'));

const fnameinfo = document.createElement('div');
fnameinfo.setAttribute('class', 'rowinfo');
const fnamespanvalue= document.createElement('span');
fnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].first_name));
fnameinfo.appendChild(fnamespanlabel);
fnameinfo.appendChild(fnamespanvalue);


const lnameinfo = document.createElement('div');
lnameinfo.setAttribute('class', 'rowinfo');
const lnamespanvalue= document.createElement('span');
lnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].last_name));
lnameinfo.appendChild(lnamespanlabel);
lnameinfo.appendChild(lnamespanvalue);


const dobinfo = document.createElement('div');
dobinfo.setAttribute('class', 'rowinfo');
const dobspanvalue= document.createElement('span');
dobspanvalue.appendChild(document.createTextNode(slicedrecords[rec].dob));
dobinfo.appendChild(dobspanlabel);
dobinfo.appendChild(dobspanvalue);


const nibinfo = document.createElement('div');
nibinfo.setAttribute('class', 'rowinfo');
const nibspanvalue= document.createElement('span');
nibspanvalue.appendChild(document.createTextNode(slicedrecords[rec].nib));
nibinfo.appendChild(nibspanlabel);
nibinfo.appendChild(nibspanvalue);


const homepinfo = document.createElement('div');
homepinfo.setAttribute('class', 'rowinfo');
const homepspanvalue= document.createElement('span');
homepspanvalue.appendChild(document.createTextNode(slicedrecords[rec].home_phone));
homepinfo.appendChild(homepspanlabel);
homepinfo.appendChild(homepspanvalue);


const cellpinfo = document.createElement('div');
cellpinfo.setAttribute('class', 'rowinfo');
const cellpspanvalue= document.createElement('span');
cellpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].cell_phone));
cellpinfo.appendChild(cellpspanlabel);
cellpinfo.appendChild(cellpspanvalue);

const workpinfo = document.createElement('div');
workpinfo.setAttribute('class', 'rowinfo');
const workpspanvalue= document.createElement('span');
workpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].work_phone));
workpinfo.appendChild(workpspanlabel);
workpinfo.appendChild(workpspanvalue);



const saddressinfo = document.createElement('div');
saddressinfo.setAttribute('class', 'rowinfo');
const saddressspanvalue= document.createElement('span');
saddressspanvalue.appendChild(document.createTextNode(slicedrecords[rec].street_address));
saddressinfo.appendChild(saddressspanlabel);
saddressinfo.appendChild(saddressspanvalue);


const cityinfo = document.createElement('div');
cityinfo.setAttribute('class', 'rowinfo');
const cityspanvalue= document.createElement('span');
cityspanvalue.appendChild(document.createTextNode(slicedrecords[rec].city));
cityinfo.appendChild(cityspanlabel);
cityinfo.appendChild(cityspanvalue);


const moreinfo =document.createElement('a');
moreinfo.setAttribute('class', 'btn');
moreinfo.classList.add('btnsignin');
moreinfo.innerHTML = "MORE INFO";

moreinfo.addEventListener("click",function (){
sessionStorage.setItem('issingle', true);
this.issingle =true;
sessionStorage.setItem('isresult', false);
this.isresult = false;
const msg = document.querySelector("section#msg");
msg.classList.add('hide');
msg.classList.remove('show');

const pagination =  document.querySelector("div#pagination");


pagination.classList.remove("showgrid");
pagination.classList.add("hidecontainer");

let itemchecker =setInterval(()=>{
if(document.contains(document.querySelector('h2#firstname'))){

document.querySelector('h2#firstname').innerHTML ='';
document.querySelector('h2#firstname').appendChild(document.createTextNode(slicedrecords[rec].first_name));

document.querySelector('h2#lastname').innerHTML = '';
document.querySelector('h2#lastname').appendChild(document.createTextNode(slicedrecords[rec].last_name));

document.querySelector('span#inforowmiddle').innerHTML;
document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(slicedrecords[rec].middle_name));

document.querySelector('span#inforownib').innerHTML ='';
document.querySelector('span#inforownib').appendChild(document.createTextNode(slicedrecords[rec].nib));

document.querySelector('span#inforowdob').innerHTML= '';
document.querySelector('span#inforowdob').appendChild(document.createTextNode(slicedrecords[rec].dob));

document.querySelector('span#inforowgender').innerHTML = '';
document.querySelector('span#inforowgender').appendChild(document.createTextNode(slicedrecords[rec].gender));

document.querySelector('span#inforowmar').innerHTML = '';
document.querySelector('span#inforowmar').appendChild(document.createTextNode(slicedrecords[rec].marital_status));

document.querySelector('span#inforowhphone').innerHTML= '';
document.querySelector('span#inforowhphone').appendChild(document.createTextNode(slicedrecords[rec].home_phone));

document.querySelector('span#inforowcphone').innerHTML = '';
document.querySelector('span#inforowcphone').appendChild(document.createTextNode(slicedrecords[rec].cell_phone));

document.querySelector('span#inforowwphone').innerHTML = '';
document.querySelector('span#inforowwphone').appendChild(document.createTextNode(slicedrecords[rec].work_phone));

document.querySelector('span#inforowsaddress').innerHTML = '';
document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(slicedrecords[rec].street_address));

document.querySelector('span#inforowcity').innerHTML ='';
document.querySelector('span#inforowcity').appendChild(document.createTextNode(slicedrecords[rec].city));

document.querySelector('span#inforowcountry').innerHTML = '';
document.querySelector('span#inforowcountry').appendChild(document.createTextNode(slicedrecords[rec].country));


document.querySelector("button#backresults").addEventListener('click', ()=>{
sessionStorage.setItem('issingle', false);
this.issingle =false;
sessionStorage.setItem('isresult', true);
this.isresult = true;
msg.classList.remove('hide');
msg.classList.add('show');
pagination.classList.add("showgrid");
pagination.classList.remove("hidecontainer");

let pagebtns = document.querySelectorAll("div#pagination button");

});

clearInterval(itemchecker);
}

}, 1);

});


recorditem.appendChild(recordimg);
recorditem.appendChild(fnameinfo);
recorditem.appendChild(lnameinfo);
recorditem.appendChild(dobinfo);
recorditem.appendChild(nibinfo);
recorditem.appendChild(homepinfo);
recorditem.appendChild(cellpinfo);
recorditem.appendChild(workpinfo);
recorditem.appendChild(saddressinfo);
recorditem.appendChild(cityinfo);
recorditem.appendChild(moreinfo);

document.querySelector("section.resultcontainer").appendChild(recorditem);


}

});


});

}

},0);
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
    
        
});

}

},0);
                                        
                                        });

                                        clearInterval(itemchecker);
                                    }

                                }, 0);
                                
                            });


                            recorditem.appendChild(recordimg);
                            recorditem.appendChild(fnameinfo);
                            recorditem.appendChild(lnameinfo);
                            recorditem.appendChild(dobinfo);
                            recorditem.appendChild(nibinfo);
                            recorditem.appendChild(homepinfo);
                            recorditem.appendChild(cellpinfo);
                            recorditem.appendChild(workpinfo);
                            recorditem.appendChild(saddressinfo);
                            recorditem.appendChild(cityinfo);
                            recorditem.appendChild(moreinfo);

                            resultcontainer.appendChild(recorditem);


                    }
                    
                }
   
            
        });
        clearInterval(paginationchecker);

    }

},0);



export default {
    data() {
        return {
            messages: '',
            csrf_token: '',
            quicksearch: '',
            records: [],
            isquick: true,
            isfirst: false,
            firstname: '',
            islast: false,
            isdob: false,
            isnib: false,
            isauth: false,
            isresult: false,
            issingle: false,
            showsearch: false
        };
    },
    methods: {

        search(searchtype){
            const alertcontainer =  document.querySelector('section#msg');
            const searchcontainer =  document.querySelector("section#skiptraceparent");
            const quicksearch = document.querySelector('input#quicksearch');
            const pagination = document.querySelector('div#pagination');
            const self = this;
            const pagelimit = 10;
            pagelim = pagelimit;
            let pagebtn;
            let text;
            let datalen = 0;
            let totalpages = 0;
            let leftovers = 0;
            let stat = 0;
        
            if (searchtype == "quick"){
                
                fetch('/api/quicksearch?quicksearchquery='+self.quicksearch, {
                    method: 'GET',
                    headers: {
                        'Accept': 'application/json',
                        'Authorization': `Bearer ${sessionStorage.getItem('token')}`
                    }
                })
                .then((response)=>{
                    stat =  response.status
                    self.quicksearch = "";
                    return response.json();
                 })
                .then((data)=>{
                    if (stat == 200){
                        self.messages = `${data.length} RECORDS FOUND`;
                        sessionStorage.setItem('isresult', true);
                        self.isresult = true;
                        datalen = data.length;
                        totalpages = Math.floor(datalen / pagelimit);
                        leftovers = datalen % pagelimit;

                        for (let n = 1; n <= totalpages; n++){
                            pagebtn = document.createElement("button");
                            text = document.createTextNode(n);
                            pagebtn.appendChild(text);
                            pagebtn.setAttribute("id", `${n}`);
                            pagebtn.setAttribute("class", "btnsignin");
                            pagination.appendChild(pagebtn);

                        }

                        if(leftovers > 0){
                            pagebtn = document.createElement("button");
                            text = document.createTextNode(totalpages+1);
                            pagebtn.appendChild(text);
                            pagebtn.setAttribute("id", `${totalpages+1}`);
                            pagebtn.setAttribute("class", "btnsignin");
                            pagination.appendChild(pagebtn);

                        }

                       vanillarecords = data;
                       let firstrecords = data.slice( (1 * pagelimit) - (pagelimit), 1 * pagelimit);
                       firstrecords.forEach((rec)=>{
                            this.records.push(rec);
                       });

                        quicksearch.value= "";
                        searchcontainer.classList.remove('flexshow');
                        searchcontainer.classList.add('hidecontainer');
                        alertcontainer.classList.add('alert-success');
                        alertcontainer.classList.remove('alert-danger');
                        alertcontainer.classList.remove('hide');
                        alertcontainer.classList.add('show');


                    }
                    else if (stat == 201){
                        self.messages = data.message;
                        quicksearch.value= "";
                        alertcontainer.classList.remove('alert-success');
                        alertcontainer.classList.add('alert-danger');
                        alertcontainer.classList.remove('hide');
                        alertcontainer.classList.add('show');      
                    }
                    else if (stat == 401){
                        self.messages = data.message; 
                        quicksearch.value= "";
                        alertcontainer.classList.remove('alert-success');
                        alertcontainer.classList.add('alert-danger');
                        alertcontainer.classList.remove('hide');
                        alertcontainer.classList.add('show');
                    }
                })
            }
            else if (searchtype == "advance"){
             
                if(this.isfirst){
                    let fname = document.querySelector("div input#firstname").value;
                   
                       for (let i =0; i < urlparms.length; i++){
                            if (urlparms[i].startsWith("&firstname=")){
                                urlparms[i]=`&firstname=${fname}`;
                                break;
                            }
                            else if(urlparms[i].startsWith("firstname=")){
                                urlparms[i]=`firstname=${fname}`;
                                break;
                            }
                            else{
                                if (urlparms.length > 1){
                                    urlparms.push(`&firstname=${fname}`);
                                    break;
                                }
                                else{
                                    urlparms.push(`firstname=${fname}`);
                                    break;
                                }
                            }
                       }
                        joinedurl = urlparms.join('');
                        
                }
                

                if(this.islast){
                    let lname = document.querySelector("div input#lastname").value;
                   
                    for (let i =0; i < urlparms.length; i++){
                            if (urlparms[i].startsWith("&lastname=")){
                                urlparms[i]=`&lastname=${lname}`;
                                break;
                            }
                            else if(urlparms[i].startsWith("lastname=")){
                                urlparms[i]=`lastname=${lname}`;
                                break;
                            }
                            else{
                                if (urlparms.length > 1){
                                    urlparms.push(`&lastname=${lname}`);
                                    break;
                                }
                                else{
                                    urlparms.push(`lastname=${lname}`);
                                    break;
                                }
                            }
                       }
                        joinedurl = urlparms.join('');
                       
                }


                 if(this.isdob){
                    let dob = document.querySelector("div input#dob").value;
                   
                    for (let i =0; i < urlparms.length; i++){
                            if (urlparms[i].startsWith("&dob=")){
                                urlparms[i]=`&dob=${dob}`;
                                break;
                            }
                            else if(urlparms[i].startsWith("dob=")){
                                urlparms[i]=`dob=${dob}`;
                                break;
                            }
                            else{
                                if (urlparms.length > 1){
                                    urlparms.push(`&dob=${dob}`);
                                    break;
                                }
                                else{
                                    urlparms.push(`dob=${dob}`);
                                    break;
                                }
                            }
                       }
                        joinedurl = urlparms.join('');
                       
                }

                if(this.isnib){
                    let nib = document.querySelector("div input#nib").value;
                   
                    for (let i =0; i < urlparms.length; i++){
                            if (urlparms[i].startsWith("&nib=")){
                                urlparms[i]=`&nib=${nib}`;
                                break;
                            }
                            else if(urlparms[i].startsWith("nib=")){
                                urlparms[i]=`nib=${nib}`;
                                break;
                            }
                            else{
                                if (urlparms.length > 1){
                                    urlparms.push(`&nib=${nib}`);
                                    break;
                                }
                                else{
                                    urlparms.push(`nib=${nib}`);
                                    break;
                                }
                            }
                       }
                        joinedurl = urlparms.join('');
                       
                }
                
                 
                fetch(joinedurl, {
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
                        urlparms = ['/api/advancesearch?'];
                        if(data.length  == 1){
                            self.messages= `${data.length} RECORD FOUND`;
                        }
                        else{
                            self.messages= `${data.length} RECORDS FOUND`;
                        }
                        sessionStorage.setItem('isresult', true);
                        self.isresult = true;
                        sessionStorage.setItem('currentrec', '');
                        datalen = data.length;
                        totalpages = Math.floor(datalen / pagelimit);
                        leftovers = datalen % pagelimit;

                        for (let n = 1; n <= totalpages; n++){
                            pagebtn = document.createElement("button");
                            text = document.createTextNode(n);
                            pagebtn.appendChild(text);
                            pagebtn.setAttribute("id", `${n}`);
                            pagebtn.setAttribute("class", "btnsignin");
                            pagination.appendChild(pagebtn);

                        }

                        if(leftovers > 0){
                            pagebtn = document.createElement("button");
                            text = document.createTextNode(totalpages+1);
                            pagebtn.appendChild(text);
                            pagebtn.setAttribute("id", `${totalpages+1}`);
                            pagebtn.setAttribute("class", "btnsignin");
                            pagination.appendChild(pagebtn);

                        }

                       vanillarecords = data;
                       let firstrecords = data.slice( (1 * pagelimit) - (pagelimit), 1 * pagelimit);
                       firstrecords.forEach((rec)=>{
                            this.records.push(rec);
                       });

                        const allinps= document.querySelectorAll('div input');
                            allinps.forEach((inp)=>{
                            inp.value='';
                        });

                        searchcontainer.classList.remove('flexshow');
                        searchcontainer.classList.add('hidecontainer');
                        alertcontainer.classList.add('alert-success');
                        alertcontainer.classList.remove('alert-danger');
                        alertcontainer.classList.remove('hide');
                        alertcontainer.classList.add('show');


                    }
                    else if (stat == 201){
                        urlparms = ['/api/advancesearch?'];
                        sessionStorage.setItem('isresult', false);
                        self.isresult = false;
                        self.messages = data.message;
                        const allinps= document.querySelectorAll('div input');
                            allinps.forEach((inp)=>{
                            inp.value='';
                        });
                        alertcontainer.classList.remove('alert-success');
                        alertcontainer.classList.add('alert-danger');
                        alertcontainer.classList.remove('hide');
                        alertcontainer.classList.add('show');      
                    }
                    else if (stat == 401){
                        urlparms = ['/api/advancesearch?'];
                        sessionStorage.setItem('isresult', false);
                        self.isresult = false;
                        self.messages = data.message; 
                        const allinps= document.querySelectorAll('div input');
                            allinps.forEach((inp)=>{
                            inp.value='';
                        });
                        alertcontainer.classList.remove('alert-success');
                        alertcontainer.classList.add('alert-danger');
                        alertcontainer.classList.remove('hide');
                        alertcontainer.classList.add('show');
                    }

                 })
                

            }
            
        },

        searchagain(){

            vanillarecords = '';
            location.reload();
        },

        quickmode(){
            const self = this;
            const advmode = document.querySelector("button#advmode");
            const quickmode = document.querySelector("button#quickmode");
            
            self.isquick =  true;
    
            quickmode.classList.add('disabled');
            advmode.classList.remove('disabled');

        },

        advmode(){
            const alertcontainer =  document.querySelector('section#msg');
            const self = this;
            self.isfirst = false;
            self.islast = false;
            self.isdob = false;
            self.isnib = false;
            
            const advmode = document.querySelector("button#advmode");
            const quickmode = document.querySelector("button#quickmode");

            self.isquick =  false;
    
            quickmode.classList.remove('disabled');
            advmode.classList.add('disabled');

            alertcontainer.classList.remove('alert-danger');
            alertcontainer.classList.remove('alert-danger');
            alertcontainer.classList.remove('show');
            alertcontainer.classList.add('hide');


        },

        switchandler(label){
            const self= this;
            const firstchecker = document.querySelector("input.firstname");
            const lastchecker = document.querySelector("input.lastname");
            const dobchecker = document.querySelector("input.dob");
            const nibchecker = document.querySelector("input.nib");

            switch(label){
                case "firstname":
                    if (firstchecker.checked){
                        self.isfirst = true;
                        self.showsearch = true;
                    }
                    else{
                        
                        self.isfirst = false;
                    }
                case "lastname":
                    if (lastchecker.checked){
                        self.islast = true;
                        self.showsearch = true;
                    }
                    else{
                        self.islast = false;
                    }
                case "dob":
                    if (dobchecker.checked){
                        self.isdob = true;
                        self.showsearch = true;
                    }
                    else{
                        self.isdob = false;
                    }
                case "nib":
                    if (nibchecker.checked){
                        self.showsearch = true;
                        self.isnib = true;
                    }
                    else{
                        self.isnib = false;
                    }
            }
        },

        singlehandler(rec){

            sessionStorage.setItem('issingle', true);
            this.issingle =true;
            sessionStorage.setItem('isresult', false);
            this.isresult = false;
            const msg = document.querySelector("section#msg");
            msg.classList.add('hide');
            msg.classList.remove('show');

            const pagination =  document.querySelector("div#pagination");
            pagination.classList.remove("showgrid");
            pagination.classList.add("hidecontainer");

            let itemchecker =setInterval(()=>{
                if(document.contains(document.querySelector('h2#firstname'))){
                    
                    document.querySelector('h2#firstname').innerHTML ='';
                    document.querySelector('h2#firstname').appendChild(document.createTextNode(rec.first_name));

                    document.querySelector('h2#lastname').innerHTML = '';
                    document.querySelector('h2#lastname').appendChild(document.createTextNode(rec.last_name));

                    document.querySelector('span#inforowmiddle').innerHTML;
                    document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(rec.middle_name));

                    document.querySelector('span#inforownib').innerHTML ='';
                    document.querySelector('span#inforownib').appendChild(document.createTextNode(rec.nib));

                    document.querySelector('span#inforowdob').innerHTML= '';
                    document.querySelector('span#inforowdob').appendChild(document.createTextNode(rec.dob));

                    document.querySelector('span#inforowgender').innerHTML = '';
                    document.querySelector('span#inforowgender').appendChild(document.createTextNode(rec.gender));

                    document.querySelector('span#inforowmar').innerHTML = '';
                    document.querySelector('span#inforowmar').appendChild(document.createTextNode(rec.marital_status));

                    document.querySelector('span#inforowhphone').innerHTML= '';
                    document.querySelector('span#inforowhphone').appendChild(document.createTextNode(rec.home_phone));
                    
                    document.querySelector('span#inforowcphone').innerHTML = '';
                    document.querySelector('span#inforowcphone').appendChild(document.createTextNode(rec.cell_phone));

                    document.querySelector('span#inforowwphone').innerHTML = '';
                    document.querySelector('span#inforowwphone').appendChild(document.createTextNode(rec.work_phone));

                    document.querySelector('span#inforowsaddress').innerHTML = '';
                    document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(rec.street_address));

                    document.querySelector('span#inforowcity').innerHTML ='';
                    document.querySelector('span#inforowcity').appendChild(document.createTextNode(rec.city));

                    document.querySelector('span#inforowcountry').innerHTML = '';
                    document.querySelector('span#inforowcountry').appendChild(document.createTextNode(rec.country));

                    document.querySelector("button#backresults").addEventListener('click', ()=>{
                        sessionStorage.setItem('issingle', false);
                        this.issingle =false;
                        sessionStorage.setItem('isresult', true);
                        this.isresult = true;
                        msg.classList.remove('hide');
                        msg.classList.add('show');
                        pagination.classList.add("showgrid");
                        pagination.classList.remove("hidecontainer");

                        let pagebtns = document.querySelectorAll("div#pagination button")

                        let currid = 0;

                        let backchecker =  setInterval(()=>{

                            if (document.contains(document.querySelector("section.resultcontainer"))){
                                clearInterval(backchecker);
                                document.querySelector("section.resultcontainer").innerHTML = "";

                                pagebtns.forEach((b)=>{
                                    if (b.classList.contains('currcolor')){
                                        currid = parseInt(b.getAttribute('id'));
                                    }
                                });

                                records = vanillarecords.slice( (currid * pagelim) - (pagelim), currid * pagelim);

                                
                            for (let rec=0; rec<records.length; rec++){
                            const recorditem = document.createElement("div");
                            recorditem.setAttribute('id', 'recorditem');
                                        
                            const recordimg = document.createElement('img');
                            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
                            recordimg.setAttribute('class', 'recorditem' );

                            const fnamespanlabel = document.createElement('span');
                            fnamespanlabel.setAttribute('class', 'fieldtitle');
                            fnamespanlabel.appendChild(document.createTextNode('First Name'));

                            const lnamespanlabel = document.createElement('span');
                            lnamespanlabel.setAttribute('class', 'fieldtitle');
                            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                            const dobspanlabel = document.createElement('span');
                            dobspanlabel.setAttribute('class', 'fieldtitle');
                            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                            const nibspanlabel = document.createElement('span');
                            nibspanlabel.setAttribute('class', 'fieldtitle');
                            nibspanlabel.appendChild(document.createTextNode('NIB#'));

                            const homepspanlabel = document.createElement('span');
                            homepspanlabel.setAttribute('class', 'fieldtitle');
                            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                            const cellpspanlabel = document.createElement('span');
                            cellpspanlabel.setAttribute('class', 'fieldtitle');
                            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                            const workpspanlabel = document.createElement('span');
                            workpspanlabel.setAttribute('class', 'fieldtitle');
                            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                            const saddressspanlabel = document.createElement('span');
                            saddressspanlabel.setAttribute('class', 'fieldtitle');
                            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                            const cityspanlabel = document.createElement('span');
                            cityspanlabel.setAttribute('class', 'fieldtitle');
                            cityspanlabel.appendChild(document.createTextNode('City'));
                            
                            const fnameinfo = document.createElement('div');
                            fnameinfo.setAttribute('class', 'rowinfo');
                            const fnamespanvalue= document.createElement('span');
                            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
                            fnameinfo.appendChild(fnamespanlabel);
                            fnameinfo.appendChild(fnamespanvalue);


                            const lnameinfo = document.createElement('div');
                            lnameinfo.setAttribute('class', 'rowinfo');
                            const lnamespanvalue= document.createElement('span');
                            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
                            lnameinfo.appendChild(lnamespanlabel);
                            lnameinfo.appendChild(lnamespanvalue);


                            const dobinfo = document.createElement('div');
                            dobinfo.setAttribute('class', 'rowinfo');
                            const dobspanvalue= document.createElement('span');
                            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
                            dobinfo.appendChild(dobspanlabel);
                            dobinfo.appendChild(dobspanvalue);


                            const nibinfo = document.createElement('div');
                            nibinfo.setAttribute('class', 'rowinfo');
                            const nibspanvalue= document.createElement('span');
                            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
                            nibinfo.appendChild(nibspanlabel);
                            nibinfo.appendChild(nibspanvalue);


                            const homepinfo = document.createElement('div');
                            homepinfo.setAttribute('class', 'rowinfo');
                            const homepspanvalue= document.createElement('span');
                            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
                            homepinfo.appendChild(homepspanlabel);
                            homepinfo.appendChild(homepspanvalue);


                            const cellpinfo = document.createElement('div');
                            cellpinfo.setAttribute('class', 'rowinfo');
                            const cellpspanvalue= document.createElement('span');
                            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
                            cellpinfo.appendChild(cellpspanlabel);
                            cellpinfo.appendChild(cellpspanvalue);

                            const workpinfo = document.createElement('div');
                            workpinfo.setAttribute('class', 'rowinfo');
                            const workpspanvalue= document.createElement('span');
                            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
                            workpinfo.appendChild(workpspanlabel);
                            workpinfo.appendChild(workpspanvalue);



                            const saddressinfo = document.createElement('div');
                            saddressinfo.setAttribute('class', 'rowinfo');
                            const saddressspanvalue= document.createElement('span');
                            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
                            saddressinfo.appendChild(saddressspanlabel);
                            saddressinfo.appendChild(saddressspanvalue);


                            const cityinfo = document.createElement('div');
                            cityinfo.setAttribute('class', 'rowinfo');
                            const cityspanvalue= document.createElement('span');
                            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
                            cityinfo.appendChild(cityspanlabel);
                            cityinfo.appendChild(cityspanvalue);


                            const moreinfo =document.createElement('a');
                            moreinfo.setAttribute('class', 'btn');
                            moreinfo.classList.add('btnsignin');
                            moreinfo.innerHTML = "MORE INFO";

                            moreinfo.addEventListener("click",function (){
                                sessionStorage.setItem('issingle', true);
                                this.issingle =true;
                                sessionStorage.setItem('isresult', false);
                                this.isresult = false;
                                const msg = document.querySelector("section#msg");
                                msg.classList.add('hide');
                                msg.classList.remove('show');

                                const pagination =  document.querySelector("div#pagination");


                                pagination.classList.remove("showgrid");
                                pagination.classList.add("hidecontainer");

                                let itemchecker =setInterval(()=>{
                                    if(document.contains(document.querySelector('h2#firstname'))){
                        
                                        document.querySelector('h2#firstname').innerHTML ='';
                                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                                        document.querySelector('h2#lastname').innerHTML = '';
                                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                                        document.querySelector('span#inforowmiddle').innerHTML;
                                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                                        document.querySelector('span#inforownib').innerHTML ='';
                                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                                        document.querySelector('span#inforowdob').innerHTML= '';
                                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                                        document.querySelector('span#inforowgender').innerHTML = '';
                                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                                        document.querySelector('span#inforowmar').innerHTML = '';
                                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                                        document.querySelector('span#inforowhphone').innerHTML= '';
                                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                                        
                                        document.querySelector('span#inforowcphone').innerHTML = '';
                                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                                        document.querySelector('span#inforowwphone').innerHTML = '';
                                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                                        document.querySelector('span#inforowsaddress').innerHTML = '';
                                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                                        document.querySelector('span#inforowcity').innerHTML ='';
                                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                                        document.querySelector('span#inforowcountry').innerHTML = '';
                                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                                            sessionStorage.setItem('issingle', false);
                                            this.issingle =false;
                                            sessionStorage.setItem('isresult', true);
                                            this.isresult = true;
                                            msg.classList.remove('hide');
                                            msg.classList.add('show');
                                            pagination.classList.add("showgrid");
                                            pagination.classList.remove("hidecontainer");

                                            let pagebtns = document.querySelectorAll("div#pagination button");

                                            let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            
            document.querySelector("section.resultcontainer").innerHTML = "";
            let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<records.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");


let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
clearInterval(backchecker);
document.querySelector("section.resultcontainer").innerHTML = "";
pagebtns.forEach((btn)=>{

btn.addEventListener('click',()=>{
document.querySelector("section.resultcontainer").innerHTML = "";
let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
for (let rec=0; rec<records.length; rec++){
const recorditem = document.createElement("div");
recorditem.setAttribute('id', 'recorditem');

const recordimg = document.createElement('img');
recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
recordimg.setAttribute('class', 'recorditem' );

const fnamespanlabel = document.createElement('span');
fnamespanlabel.setAttribute('class', 'fieldtitle');
fnamespanlabel.appendChild(document.createTextNode('First Name'));

const lnamespanlabel = document.createElement('span');
lnamespanlabel.setAttribute('class', 'fieldtitle');
lnamespanlabel.appendChild(document.createTextNode('Last Name'));

const dobspanlabel = document.createElement('span');
dobspanlabel.setAttribute('class', 'fieldtitle');
dobspanlabel.appendChild(document.createTextNode('D.O.B'));

const nibspanlabel = document.createElement('span');
nibspanlabel.setAttribute('class', 'fieldtitle');
nibspanlabel.appendChild(document.createTextNode('NIB#'));

const homepspanlabel = document.createElement('span');
homepspanlabel.setAttribute('class', 'fieldtitle');
homepspanlabel.appendChild(document.createTextNode('Home Phone'));

const cellpspanlabel = document.createElement('span');
cellpspanlabel.setAttribute('class', 'fieldtitle');
cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

const workpspanlabel = document.createElement('span');
workpspanlabel.setAttribute('class', 'fieldtitle');
workpspanlabel.appendChild(document.createTextNode('Work Phone'));

const saddressspanlabel = document.createElement('span');
saddressspanlabel.setAttribute('class', 'fieldtitle');
saddressspanlabel.appendChild(document.createTextNode('Street Address'));

const cityspanlabel = document.createElement('span');
cityspanlabel.setAttribute('class', 'fieldtitle');
cityspanlabel.appendChild(document.createTextNode('City'));

const fnameinfo = document.createElement('div');
fnameinfo.setAttribute('class', 'rowinfo');
const fnamespanvalue= document.createElement('span');
fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
fnameinfo.appendChild(fnamespanlabel);
fnameinfo.appendChild(fnamespanvalue);


const lnameinfo = document.createElement('div');
lnameinfo.setAttribute('class', 'rowinfo');
const lnamespanvalue= document.createElement('span');
lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
lnameinfo.appendChild(lnamespanlabel);
lnameinfo.appendChild(lnamespanvalue);


const dobinfo = document.createElement('div');
dobinfo.setAttribute('class', 'rowinfo');
const dobspanvalue= document.createElement('span');
dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
dobinfo.appendChild(dobspanlabel);
dobinfo.appendChild(dobspanvalue);


const nibinfo = document.createElement('div');
nibinfo.setAttribute('class', 'rowinfo');
const nibspanvalue= document.createElement('span');
nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
nibinfo.appendChild(nibspanlabel);
nibinfo.appendChild(nibspanvalue);


const homepinfo = document.createElement('div');
homepinfo.setAttribute('class', 'rowinfo');
const homepspanvalue= document.createElement('span');
homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
homepinfo.appendChild(homepspanlabel);
homepinfo.appendChild(homepspanvalue);


const cellpinfo = document.createElement('div');
cellpinfo.setAttribute('class', 'rowinfo');
const cellpspanvalue= document.createElement('span');
cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
cellpinfo.appendChild(cellpspanlabel);
cellpinfo.appendChild(cellpspanvalue);

const workpinfo = document.createElement('div');
workpinfo.setAttribute('class', 'rowinfo');
const workpspanvalue= document.createElement('span');
workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
workpinfo.appendChild(workpspanlabel);
workpinfo.appendChild(workpspanvalue);



const saddressinfo = document.createElement('div');
saddressinfo.setAttribute('class', 'rowinfo');
const saddressspanvalue= document.createElement('span');
saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
saddressinfo.appendChild(saddressspanlabel);
saddressinfo.appendChild(saddressspanvalue);


const cityinfo = document.createElement('div');
cityinfo.setAttribute('class', 'rowinfo');
const cityspanvalue= document.createElement('span');
cityspanvalue.appendChild(document.createTextNode(records[rec].city));
cityinfo.appendChild(cityspanlabel);
cityinfo.appendChild(cityspanvalue);


const moreinfo =document.createElement('a');
moreinfo.setAttribute('class', 'btn');
moreinfo.classList.add('btnsignin');
moreinfo.innerHTML = "MORE INFO";

moreinfo.addEventListener("click",function (){
sessionStorage.setItem('issingle', true);
this.issingle =true;
sessionStorage.setItem('isresult', false);
this.isresult = false;
const msg = document.querySelector("section#msg");
msg.classList.add('hide');
msg.classList.remove('show');

const pagination =  document.querySelector("div#pagination");


pagination.classList.remove("showgrid");
pagination.classList.add("hidecontainer");

let itemchecker =setInterval(()=>{
if(document.contains(document.querySelector('h2#firstname'))){

document.querySelector('h2#firstname').innerHTML ='';
document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

document.querySelector('h2#lastname').innerHTML = '';
document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

document.querySelector('span#inforowmiddle').innerHTML;
document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

document.querySelector('span#inforownib').innerHTML ='';
document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

document.querySelector('span#inforowdob').innerHTML= '';
document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

document.querySelector('span#inforowgender').innerHTML = '';
document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

document.querySelector('span#inforowmar').innerHTML = '';
document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

document.querySelector('span#inforowhphone').innerHTML= '';
document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));

document.querySelector('span#inforowcphone').innerHTML = '';
document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

document.querySelector('span#inforowwphone').innerHTML = '';
document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

document.querySelector('span#inforowsaddress').innerHTML = '';
document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

document.querySelector('span#inforowcity').innerHTML ='';
document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

document.querySelector('span#inforowcountry').innerHTML = '';
document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


document.querySelector("button#backresults").addEventListener('click', ()=>{
sessionStorage.setItem('issingle', false);
this.issingle =false;
sessionStorage.setItem('isresult', true);
this.isresult = true;
msg.classList.remove('hide');
msg.classList.add('show');
pagination.classList.add("showgrid");
pagination.classList.remove("hidecontainer");

let pagebtns = document.querySelectorAll("div#pagination button");

});

clearInterval(itemchecker);
}

}, 1);

});


recorditem.appendChild(recordimg);
recorditem.appendChild(fnameinfo);
recorditem.appendChild(lnameinfo);
recorditem.appendChild(dobinfo);
recorditem.appendChild(nibinfo);
recorditem.appendChild(homepinfo);
recorditem.appendChild(cellpinfo);
recorditem.appendChild(workpinfo);
recorditem.appendChild(saddressinfo);
recorditem.appendChild(cityinfo);
recorditem.appendChild(moreinfo);

document.querySelector("section.resultcontainer").appendChild(recorditem);


}

});


});

}

},0);
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
    
        
});

}

},0);
                                        
                                        });

                                        clearInterval(itemchecker);
                                    }

                                }, 0);
                                
                            });


                            recorditem.appendChild(recordimg);
                            recorditem.appendChild(fnameinfo);
                            recorditem.appendChild(lnameinfo);
                            recorditem.appendChild(dobinfo);
                            recorditem.appendChild(nibinfo);
                            recorditem.appendChild(homepinfo);
                            recorditem.appendChild(cellpinfo);
                            recorditem.appendChild(workpinfo);
                            recorditem.appendChild(saddressinfo);
                            recorditem.appendChild(cityinfo);
                            recorditem.appendChild(moreinfo);

                           document.querySelector("section.resultcontainer").appendChild(recorditem);


                    }




                                pagebtns.forEach((btn)=>{
                                    btn.addEventListener('click',()=>{
                                        
                                        document.querySelector("section.resultcontainer").innerHTML = "";
                                        let slicedrecords = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
                                        for (let rec=0; rec<slicedrecords.length; rec++){
                                        const recorditem = document.createElement("div");
                                        recorditem.setAttribute('id', 'recorditem');
                                                    
                                        const recordimg = document.createElement('img');
                                        recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
                                        recordimg.setAttribute('class', 'recorditem' );

                                        const fnamespanlabel = document.createElement('span');
                                        fnamespanlabel.setAttribute('class', 'fieldtitle');
                                        fnamespanlabel.appendChild(document.createTextNode('First Name'));

                                        const lnamespanlabel = document.createElement('span');
                                        lnamespanlabel.setAttribute('class', 'fieldtitle');
                                        lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                                        const dobspanlabel = document.createElement('span');
                                        dobspanlabel.setAttribute('class', 'fieldtitle');
                                        dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                                        const nibspanlabel = document.createElement('span');
                                        nibspanlabel.setAttribute('class', 'fieldtitle');
                                        nibspanlabel.appendChild(document.createTextNode('NIB#'));

                                        const homepspanlabel = document.createElement('span');
                                        homepspanlabel.setAttribute('class', 'fieldtitle');
                                        homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                                        const cellpspanlabel = document.createElement('span');
                                        cellpspanlabel.setAttribute('class', 'fieldtitle');
                                        cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                                        const workpspanlabel = document.createElement('span');
                                        workpspanlabel.setAttribute('class', 'fieldtitle');
                                        workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                                        const saddressspanlabel = document.createElement('span');
                                        saddressspanlabel.setAttribute('class', 'fieldtitle');
                                        saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                                        const cityspanlabel = document.createElement('span');
                                        cityspanlabel.setAttribute('class', 'fieldtitle');
                                        cityspanlabel.appendChild(document.createTextNode('City'));
                            
                                        const fnameinfo = document.createElement('div');
                                        fnameinfo.setAttribute('class', 'rowinfo');
                                        const fnamespanvalue= document.createElement('span');
                                        fnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].first_name));
                                        fnameinfo.appendChild(fnamespanlabel);
                                        fnameinfo.appendChild(fnamespanvalue);


                                        const lnameinfo = document.createElement('div');
                                        lnameinfo.setAttribute('class', 'rowinfo');
                                        const lnamespanvalue= document.createElement('span');
                                        lnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].last_name));
                                        lnameinfo.appendChild(lnamespanlabel);
                                        lnameinfo.appendChild(lnamespanvalue);


                                        const dobinfo = document.createElement('div');
                                        dobinfo.setAttribute('class', 'rowinfo');
                                        const dobspanvalue= document.createElement('span');
                                        dobspanvalue.appendChild(document.createTextNode(slicedrecords[rec].dob));
                                        dobinfo.appendChild(dobspanlabel);
                                        dobinfo.appendChild(dobspanvalue);


                                        const nibinfo = document.createElement('div');
                                        nibinfo.setAttribute('class', 'rowinfo');
                                        const nibspanvalue= document.createElement('span');
                                        nibspanvalue.appendChild(document.createTextNode(slicedrecords[rec].nib));
                                        nibinfo.appendChild(nibspanlabel);
                                        nibinfo.appendChild(nibspanvalue);


                                        const homepinfo = document.createElement('div');
                                        homepinfo.setAttribute('class', 'rowinfo');
                                        const homepspanvalue= document.createElement('span');
                                        homepspanvalue.appendChild(document.createTextNode(slicedrecords[rec].home_phone));
                                        homepinfo.appendChild(homepspanlabel);
                                        homepinfo.appendChild(homepspanvalue);


                                        const cellpinfo = document.createElement('div');
                                        cellpinfo.setAttribute('class', 'rowinfo');
                                        const cellpspanvalue= document.createElement('span');
                                        cellpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].cell_phone));
                                        cellpinfo.appendChild(cellpspanlabel);
                                        cellpinfo.appendChild(cellpspanvalue);

                                        const workpinfo = document.createElement('div');
                                        workpinfo.setAttribute('class', 'rowinfo');
                                        const workpspanvalue= document.createElement('span');
                                        workpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].work_phone));
                                        workpinfo.appendChild(workpspanlabel);
                                        workpinfo.appendChild(workpspanvalue);



                                        const saddressinfo = document.createElement('div');
                                        saddressinfo.setAttribute('class', 'rowinfo');
                                        const saddressspanvalue= document.createElement('span');
                                        saddressspanvalue.appendChild(document.createTextNode(slicedrecords[rec].street_address));
                                        saddressinfo.appendChild(saddressspanlabel);
                                        saddressinfo.appendChild(saddressspanvalue);


                                        const cityinfo = document.createElement('div');
                                        cityinfo.setAttribute('class', 'rowinfo');
                                        const cityspanvalue= document.createElement('span');
                                        cityspanvalue.appendChild(document.createTextNode(slicedrecords[rec].city));
                                        cityinfo.appendChild(cityspanlabel);
                                        cityinfo.appendChild(cityspanvalue);


                                        const moreinfo =document.createElement('a');
                                        moreinfo.setAttribute('class', 'btn');
                                        moreinfo.classList.add('btnsignin');
                                        moreinfo.innerHTML = "MORE INFO";

                                        moreinfo.addEventListener("click",function (){
                                            sessionStorage.setItem('issingle', true);
                                            this.issingle =true;
                                            sessionStorage.setItem('isresult', false);
                                            this.isresult = false;
                                            const msg = document.querySelector("section#msg");
                                            msg.classList.add('hide');
                                            msg.classList.remove('show');

                                            const pagination =  document.querySelector("div#pagination");


                                            pagination.classList.remove("showgrid");
                                            pagination.classList.add("hidecontainer");

                                            let itemchecker =setInterval(()=>{
                                                if(document.contains(document.querySelector('h2#firstname'))){
                                    
                                                    document.querySelector('h2#firstname').innerHTML ='';
                                                    document.querySelector('h2#firstname').appendChild(document.createTextNode(slicedrecords[rec].first_name));

                                                    document.querySelector('h2#lastname').innerHTML = '';
                                                    document.querySelector('h2#lastname').appendChild(document.createTextNode(slicedrecords[rec].last_name));

                                                    document.querySelector('span#inforowmiddle').innerHTML;
                                                    document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(slicedrecords[rec].middle_name));

                                                    document.querySelector('span#inforownib').innerHTML ='';
                                                    document.querySelector('span#inforownib').appendChild(document.createTextNode(slicedrecords[rec].nib));

                                                    document.querySelector('span#inforowdob').innerHTML= '';
                                                    document.querySelector('span#inforowdob').appendChild(document.createTextNode(slicedrecords[rec].dob));

                                                    document.querySelector('span#inforowgender').innerHTML = '';
                                                    document.querySelector('span#inforowgender').appendChild(document.createTextNode(slicedrecords[rec].gender));

                                                    document.querySelector('span#inforowmar').innerHTML = '';
                                                    document.querySelector('span#inforowmar').appendChild(document.createTextNode(slicedrecords[rec].marital_status));

                                                    document.querySelector('span#inforowhphone').innerHTML= '';
                                                    document.querySelector('span#inforowhphone').appendChild(document.createTextNode(slicedrecords[rec].home_phone));
                                                    
                                                    document.querySelector('span#inforowcphone').innerHTML = '';
                                                    document.querySelector('span#inforowcphone').appendChild(document.createTextNode(slicedrecords[rec].cell_phone));

                                                    document.querySelector('span#inforowwphone').innerHTML = '';
                                                    document.querySelector('span#inforowwphone').appendChild(document.createTextNode(slicedrecords[rec].work_phone));

                                                    document.querySelector('span#inforowsaddress').innerHTML = '';
                                                    document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(slicedrecords[rec].street_address));

                                                    document.querySelector('span#inforowcity').innerHTML ='';
                                                    document.querySelector('span#inforowcity').appendChild(document.createTextNode(slicedrecords[rec].city));

                                                    document.querySelector('span#inforowcountry').innerHTML = '';
                                                    document.querySelector('span#inforowcountry').appendChild(document.createTextNode(slicedrecords[rec].country));


                                                    document.querySelector("button#backresults").addEventListener('click', ()=>{
                                                        sessionStorage.setItem('issingle', false);
                                                        this.issingle =false;
                                                        sessionStorage.setItem('isresult', true);
                                                        this.isresult = true;
                                                        msg.classList.remove('hide');
                                                        msg.classList.add('show');
                                                        pagination.classList.add("showgrid");
                                                        pagination.classList.remove("hidecontainer");

                                                        let pagebtns = document.querySelectorAll("div#pagination button");

                                                        let currid = 0;


                        let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((b)=>{
                                    if (b.classList.contains('currcolor')){
                                        currid = parseInt(b.getAttribute('id'));
                                    }
                                });

                                records = vanillarecords.slice( (currid * pagelim) - (pagelim), currid * pagelim);

                                for (let rec=0; rec<records.length; rec++){
                            const recorditem = document.createElement("div");
                            recorditem.setAttribute('id', 'recorditem');
                                        
                            const recordimg = document.createElement('img');
                            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
                            recordimg.setAttribute('class', 'recorditem' );

                            const fnamespanlabel = document.createElement('span');
                            fnamespanlabel.setAttribute('class', 'fieldtitle');
                            fnamespanlabel.appendChild(document.createTextNode('First Name'));

                            const lnamespanlabel = document.createElement('span');
                            lnamespanlabel.setAttribute('class', 'fieldtitle');
                            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                            const dobspanlabel = document.createElement('span');
                            dobspanlabel.setAttribute('class', 'fieldtitle');
                            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                            const nibspanlabel = document.createElement('span');
                            nibspanlabel.setAttribute('class', 'fieldtitle');
                            nibspanlabel.appendChild(document.createTextNode('NIB#'));

                            const homepspanlabel = document.createElement('span');
                            homepspanlabel.setAttribute('class', 'fieldtitle');
                            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                            const cellpspanlabel = document.createElement('span');
                            cellpspanlabel.setAttribute('class', 'fieldtitle');
                            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                            const workpspanlabel = document.createElement('span');
                            workpspanlabel.setAttribute('class', 'fieldtitle');
                            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                            const saddressspanlabel = document.createElement('span');
                            saddressspanlabel.setAttribute('class', 'fieldtitle');
                            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                            const cityspanlabel = document.createElement('span');
                            cityspanlabel.setAttribute('class', 'fieldtitle');
                            cityspanlabel.appendChild(document.createTextNode('City'));
                            
                            const fnameinfo = document.createElement('div');
                            fnameinfo.setAttribute('class', 'rowinfo');
                            const fnamespanvalue= document.createElement('span');
                            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
                            fnameinfo.appendChild(fnamespanlabel);
                            fnameinfo.appendChild(fnamespanvalue);


                            const lnameinfo = document.createElement('div');
                            lnameinfo.setAttribute('class', 'rowinfo');
                            const lnamespanvalue= document.createElement('span');
                            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
                            lnameinfo.appendChild(lnamespanlabel);
                            lnameinfo.appendChild(lnamespanvalue);


                            const dobinfo = document.createElement('div');
                            dobinfo.setAttribute('class', 'rowinfo');
                            const dobspanvalue= document.createElement('span');
                            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
                            dobinfo.appendChild(dobspanlabel);
                            dobinfo.appendChild(dobspanvalue);


                            const nibinfo = document.createElement('div');
                            nibinfo.setAttribute('class', 'rowinfo');
                            const nibspanvalue= document.createElement('span');
                            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
                            nibinfo.appendChild(nibspanlabel);
                            nibinfo.appendChild(nibspanvalue);


                            const homepinfo = document.createElement('div');
                            homepinfo.setAttribute('class', 'rowinfo');
                            const homepspanvalue= document.createElement('span');
                            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
                            homepinfo.appendChild(homepspanlabel);
                            homepinfo.appendChild(homepspanvalue);


                            const cellpinfo = document.createElement('div');
                            cellpinfo.setAttribute('class', 'rowinfo');
                            const cellpspanvalue= document.createElement('span');
                            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
                            cellpinfo.appendChild(cellpspanlabel);
                            cellpinfo.appendChild(cellpspanvalue);

                            const workpinfo = document.createElement('div');
                            workpinfo.setAttribute('class', 'rowinfo');
                            const workpspanvalue= document.createElement('span');
                            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
                            workpinfo.appendChild(workpspanlabel);
                            workpinfo.appendChild(workpspanvalue);



                            const saddressinfo = document.createElement('div');
                            saddressinfo.setAttribute('class', 'rowinfo');
                            const saddressspanvalue= document.createElement('span');
                            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
                            saddressinfo.appendChild(saddressspanlabel);
                            saddressinfo.appendChild(saddressspanvalue);


                            const cityinfo = document.createElement('div');
                            cityinfo.setAttribute('class', 'rowinfo');
                            const cityspanvalue= document.createElement('span');
                            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
                            cityinfo.appendChild(cityspanlabel);
                            cityinfo.appendChild(cityspanvalue);


                            const moreinfo =document.createElement('a');
                            moreinfo.setAttribute('class', 'btn');
                            moreinfo.classList.add('btnsignin');
                            moreinfo.innerHTML = "MORE INFO";

                            moreinfo.addEventListener("click",function (){
                                sessionStorage.setItem('issingle', true);
                                this.issingle =true;
                                sessionStorage.setItem('isresult', false);
                                this.isresult = false;
                                const msg = document.querySelector("section#msg");
                                msg.classList.add('hide');
                                msg.classList.remove('show');

                                const pagination =  document.querySelector("div#pagination");


                                pagination.classList.remove("showgrid");
                                pagination.classList.add("hidecontainer");

                                let itemchecker =setInterval(()=>{
                                    if(document.contains(document.querySelector('h2#firstname'))){
                        
                                        document.querySelector('h2#firstname').innerHTML ='';
                                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                                        document.querySelector('h2#lastname').innerHTML = '';
                                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                                        document.querySelector('span#inforowmiddle').innerHTML;
                                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                                        document.querySelector('span#inforownib').innerHTML ='';
                                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                                        document.querySelector('span#inforowdob').innerHTML= '';
                                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                                        document.querySelector('span#inforowgender').innerHTML = '';
                                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                                        document.querySelector('span#inforowmar').innerHTML = '';
                                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                                        document.querySelector('span#inforowhphone').innerHTML= '';
                                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                                        
                                        document.querySelector('span#inforowcphone').innerHTML = '';
                                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                                        document.querySelector('span#inforowwphone').innerHTML = '';
                                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                                        document.querySelector('span#inforowsaddress').innerHTML = '';
                                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                                        document.querySelector('span#inforowcity').innerHTML ='';
                                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                                        document.querySelector('span#inforowcountry').innerHTML = '';
                                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                                            sessionStorage.setItem('issingle', false);
                                            this.issingle =false;
                                            sessionStorage.setItem('isresult', true);
                                            this.isresult = true;
                                            msg.classList.remove('hide');
                                            msg.classList.add('show');
                                            pagination.classList.add("showgrid");
                                            pagination.classList.remove("hidecontainer");

                                            let pagebtns = document.querySelectorAll("div#pagination button");

                                            let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            
            document.querySelector("section.resultcontainer").innerHTML = "";
            let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<records.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");


let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
clearInterval(backchecker);
document.querySelector("section.resultcontainer").innerHTML = "";
pagebtns.forEach((btn)=>{

btn.addEventListener('click',()=>{
document.querySelector("section.resultcontainer").innerHTML = "";
let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
for (let rec=0; rec<records.length; rec++){
const recorditem = document.createElement("div");
recorditem.setAttribute('id', 'recorditem');

const recordimg = document.createElement('img');
recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
recordimg.setAttribute('class', 'recorditem' );

const fnamespanlabel = document.createElement('span');
fnamespanlabel.setAttribute('class', 'fieldtitle');
fnamespanlabel.appendChild(document.createTextNode('First Name'));

const lnamespanlabel = document.createElement('span');
lnamespanlabel.setAttribute('class', 'fieldtitle');
lnamespanlabel.appendChild(document.createTextNode('Last Name'));

const dobspanlabel = document.createElement('span');
dobspanlabel.setAttribute('class', 'fieldtitle');
dobspanlabel.appendChild(document.createTextNode('D.O.B'));

const nibspanlabel = document.createElement('span');
nibspanlabel.setAttribute('class', 'fieldtitle');
nibspanlabel.appendChild(document.createTextNode('NIB#'));

const homepspanlabel = document.createElement('span');
homepspanlabel.setAttribute('class', 'fieldtitle');
homepspanlabel.appendChild(document.createTextNode('Home Phone'));

const cellpspanlabel = document.createElement('span');
cellpspanlabel.setAttribute('class', 'fieldtitle');
cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

const workpspanlabel = document.createElement('span');
workpspanlabel.setAttribute('class', 'fieldtitle');
workpspanlabel.appendChild(document.createTextNode('Work Phone'));

const saddressspanlabel = document.createElement('span');
saddressspanlabel.setAttribute('class', 'fieldtitle');
saddressspanlabel.appendChild(document.createTextNode('Street Address'));

const cityspanlabel = document.createElement('span');
cityspanlabel.setAttribute('class', 'fieldtitle');
cityspanlabel.appendChild(document.createTextNode('City'));

const fnameinfo = document.createElement('div');
fnameinfo.setAttribute('class', 'rowinfo');
const fnamespanvalue= document.createElement('span');
fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
fnameinfo.appendChild(fnamespanlabel);
fnameinfo.appendChild(fnamespanvalue);


const lnameinfo = document.createElement('div');
lnameinfo.setAttribute('class', 'rowinfo');
const lnamespanvalue= document.createElement('span');
lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
lnameinfo.appendChild(lnamespanlabel);
lnameinfo.appendChild(lnamespanvalue);


const dobinfo = document.createElement('div');
dobinfo.setAttribute('class', 'rowinfo');
const dobspanvalue= document.createElement('span');
dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
dobinfo.appendChild(dobspanlabel);
dobinfo.appendChild(dobspanvalue);


const nibinfo = document.createElement('div');
nibinfo.setAttribute('class', 'rowinfo');
const nibspanvalue= document.createElement('span');
nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
nibinfo.appendChild(nibspanlabel);
nibinfo.appendChild(nibspanvalue);


const homepinfo = document.createElement('div');
homepinfo.setAttribute('class', 'rowinfo');
const homepspanvalue= document.createElement('span');
homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
homepinfo.appendChild(homepspanlabel);
homepinfo.appendChild(homepspanvalue);


const cellpinfo = document.createElement('div');
cellpinfo.setAttribute('class', 'rowinfo');
const cellpspanvalue= document.createElement('span');
cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
cellpinfo.appendChild(cellpspanlabel);
cellpinfo.appendChild(cellpspanvalue);

const workpinfo = document.createElement('div');
workpinfo.setAttribute('class', 'rowinfo');
const workpspanvalue= document.createElement('span');
workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
workpinfo.appendChild(workpspanlabel);
workpinfo.appendChild(workpspanvalue);



const saddressinfo = document.createElement('div');
saddressinfo.setAttribute('class', 'rowinfo');
const saddressspanvalue= document.createElement('span');
saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
saddressinfo.appendChild(saddressspanlabel);
saddressinfo.appendChild(saddressspanvalue);


const cityinfo = document.createElement('div');
cityinfo.setAttribute('class', 'rowinfo');
const cityspanvalue= document.createElement('span');
cityspanvalue.appendChild(document.createTextNode(records[rec].city));
cityinfo.appendChild(cityspanlabel);
cityinfo.appendChild(cityspanvalue);


const moreinfo =document.createElement('a');
moreinfo.setAttribute('class', 'btn');
moreinfo.classList.add('btnsignin');
moreinfo.innerHTML = "MORE INFO";

moreinfo.addEventListener("click",function (){
sessionStorage.setItem('issingle', true);
this.issingle =true;
sessionStorage.setItem('isresult', false);
this.isresult = false;
const msg = document.querySelector("section#msg");
msg.classList.add('hide');
msg.classList.remove('show');

const pagination =  document.querySelector("div#pagination");


pagination.classList.remove("showgrid");
pagination.classList.add("hidecontainer");

let itemchecker =setInterval(()=>{
if(document.contains(document.querySelector('h2#firstname'))){

document.querySelector('h2#firstname').innerHTML ='';
document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

document.querySelector('h2#lastname').innerHTML = '';
document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

document.querySelector('span#inforowmiddle').innerHTML;
document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

document.querySelector('span#inforownib').innerHTML ='';
document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

document.querySelector('span#inforowdob').innerHTML= '';
document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

document.querySelector('span#inforowgender').innerHTML = '';
document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

document.querySelector('span#inforowmar').innerHTML = '';
document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

document.querySelector('span#inforowhphone').innerHTML= '';
document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));

document.querySelector('span#inforowcphone').innerHTML = '';
document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

document.querySelector('span#inforowwphone').innerHTML = '';
document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

document.querySelector('span#inforowsaddress').innerHTML = '';
document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

document.querySelector('span#inforowcity').innerHTML ='';
document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

document.querySelector('span#inforowcountry').innerHTML = '';
document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


document.querySelector("button#backresults").addEventListener('click', ()=>{
sessionStorage.setItem('issingle', false);
this.issingle =false;
sessionStorage.setItem('isresult', true);
this.isresult = true;
msg.classList.remove('hide');
msg.classList.add('show');
pagination.classList.add("showgrid");
pagination.classList.remove("hidecontainer");

let pagebtns = document.querySelectorAll("div#pagination button");

});

clearInterval(itemchecker);
}

}, 1);

});


recorditem.appendChild(recordimg);
recorditem.appendChild(fnameinfo);
recorditem.appendChild(lnameinfo);
recorditem.appendChild(dobinfo);
recorditem.appendChild(nibinfo);
recorditem.appendChild(homepinfo);
recorditem.appendChild(cellpinfo);
recorditem.appendChild(workpinfo);
recorditem.appendChild(saddressinfo);
recorditem.appendChild(cityinfo);
recorditem.appendChild(moreinfo);

document.querySelector("section.resultcontainer").appendChild(recorditem);


}

});


});

}

},0);
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
    
        
});

}

},0);
                                        
                                        });

                                        clearInterval(itemchecker);
                                    }

                                }, 0);
                                
                            });


                            recorditem.appendChild(recordimg);
                            recorditem.appendChild(fnameinfo);
                            recorditem.appendChild(lnameinfo);
                            recorditem.appendChild(dobinfo);
                            recorditem.appendChild(nibinfo);
                            recorditem.appendChild(homepinfo);
                            recorditem.appendChild(cellpinfo);
                            recorditem.appendChild(workpinfo);
                            recorditem.appendChild(saddressinfo);
                            recorditem.appendChild(cityinfo);
                            recorditem.appendChild(moreinfo);

                           document.querySelector("section.resultcontainer").appendChild(recorditem);


                    }



    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            document.querySelector("section.resultcontainer").innerHTML = "";
            let slicedrecords = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<slicedrecords.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', '../assets/images/apex-logo.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(slicedrecords[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(slicedrecords[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(slicedrecords[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(slicedrecords[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(slicedrecords[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(slicedrecords[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(slicedrecords[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(slicedrecords[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(slicedrecords[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(slicedrecords[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(slicedrecords[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(slicedrecords[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(slicedrecords[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(slicedrecords[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(slicedrecords[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(slicedrecords[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(slicedrecords[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(slicedrecords[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(slicedrecords[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(slicedrecords[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
      
        
});

}

},0);
                                                    
                                                    });

                                                    clearInterval(itemchecker);
                                                }

                                            }, 0);
                                            
                                        });


                                        recorditem.appendChild(recordimg);
                                        recorditem.appendChild(fnameinfo);
                                        recorditem.appendChild(lnameinfo);
                                        recorditem.appendChild(dobinfo);
                                        recorditem.appendChild(nibinfo);
                                        recorditem.appendChild(homepinfo);
                                        recorditem.appendChild(cellpinfo);
                                        recorditem.appendChild(workpinfo);
                                        recorditem.appendChild(saddressinfo);
                                        recorditem.appendChild(cityinfo);
                                        recorditem.appendChild(moreinfo);

                                        document.querySelector("section.resultcontainer").appendChild(recorditem);


                                }

                                    });
                                  
                                    
                            });
    
                        }

                    },0);

                      
                });

                clearInterval(itemchecker);
            }

        }, 1);
           
    },

        getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    self.csrf_token = data.csrf_token;
                })
            
        },
        addata(){
            fetch('/api/addata', {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                    
                }
            })
            .then((resp)=>resp.json())
            .then((dat)=>{
                console.log(dat.message);
            })
        }
    
    },
    created() {
       this.getCsrfToken();
       sessionStorage.setItem('isresult', false);
       sessionStorage.setItem('issingle', false);

    
       if (sessionStorage.getItem('isauth') == 'true')
       {
            this.isauth = true;  
       }


       let stateupdater =  setInterval(()=>{
            this.isresult = sessionStorage.getItem('isresult');
            this.issingle = sessionStorage.getItem('issingle');
       },0);
       //this.addata();
    }
};
</script>

<style>


div#QuickSearchForm{
    display: flex;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
    padding: 2em 0 2em 0;
    margin-top: 2em;
    width: 100%;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
}

form#divrow{
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: center;
    width: 60%;
}

div#formgrp{
    width: 70%;
}

div#btndiv{
    width: 30%;
}

div#btndiv button{
    width: 100%;
}

div#advbtn{
    margin-top:1em;
    width: 100%;
}

button{
    font-weight: bold !important;
}
div.inputcombo{
    display: flex;
    flex-flow: column wrap;
    margin-right: 1em;
}
form button{
    margin-top: 0em;
    width:100%;
}

#btngrp button{
    width: 92%;
    background: #0E086D;
    color: #fff;
}

#btngrp button:hover{
  color: whitesmoke;
}
div.btn-group{
    width: 30%;
}
.btnsignin{
  width: 9rem;
  background: #0E086D;
  color: #fff;
}
label{
    color: #666;
    font-weight: bold;
}

.hide{
    display:none;
}

.show{
    display: block;
}

.hidecontainer{
    display: none !important;
}

.showgrid{
    display: grid !important;
}
.flexshow{
    display: flex !important;
}

.currcolor{
    background: #fff !important;
    color: #0E086D !important;
}

.regcolor{
    background: #0E086D !important;
    color: #fff !important;
}

div#advsearch{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
}


div#filters{
    display: flex;
    flex-flow: row wrap;
}

div.form-switch label{
margin-right: 1em;
}

button a{
  color: #fff !important;
  padding:0;
  margin: 0;
}


h3{
    font-weight: bold;
}
section#skiptraceparent{
    width: 70%;
    display: flex;
    flex-flow: column wrap;
    margin: auto;
    align-items: center;
}

div section p{
     color: #666;
}

section.warning{
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

section.resultcontainer{
    display: flex;
    width: 91%;
    margin: 0 auto 2em auto;
    flex-flow: column wrap;
}

section#msg{
    width: 89.5%;
    margin: 0 auto 0 auto;
    text-align: center;
}

div#recorditem{
    display: grid;
    grid-template-columns: repeat(11, 1fr);
    box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
    margin-bottom: 1.5em;
}

div#recorditem img{
    width: 3.5rem;
    margin: 0 auto;
}

div#recorditem div.rowinfo{
    display: flex;
    flex-flow: column wrap;
    color: #666;
}

span{
    color: #666;
}
span.fieldtitle{
    font-weight: bold;
}

.btnsignin{
  background: #0E086D;
  height: 2em !important;
  color: #fff;
}

button#searchagain{
    width: fit-content;
    margin-left: 2em;
}

div#pagination{
    display: grid;
    grid-template-columns: repeat(30, 1fr);
    width: 90%;
    margin: 1em auto 10em auto;
}

div#pagination button{
    width: 1em;
    padding-left: 1em;
    padding-right: 1em;
}



div#singleresult{
    display: gird;
    grid-template-columns: repeat(2, 1fr);
    width: 90% !important;
    margin: 0 auto;
    color: #666;
}

section#singlebanner{
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: center;
    margin-top: 2em;
}
section#singlebanner button{
    margin-left: 10em;
}

section#singlebanner img{
    margin-right: 2em;
}

section#singlebanner h2{
    margin-right: 0.5em;
}

section#infoparent{
    display: flex;
    flex-flow: column wrap;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    align-items: center;
    margin: 2em auto;
    padding: 1em;
}

section.inforow{
    display: flex;
    flex-flow: row wrap;
    width: 70%;
    justify-content:space-between;
    align-items: center;
    margin-bottom: 1.5em;
    border-bottom: solid rgba(99, 99, 99, 0.2) 0.1em;

}

section.inforow span{
    text-align: left;
}



</style>




<template>



    



      <table class="table">
        <thead>
          <tr>

            <th>User id</th>
            <th>email</th>




      
      
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >
            <td>{{employee.id}}</td>
            <td>{{employee.email}}</td>


            <td>{{employee.date_added}}</td>

    
    
    
    
      
      

          </tr>
        </tbody>
      </table>
      <table class="table">
    <thead>
      <tr>
        <th>User ID</th>


      </tr>
    </thead>
    <tbody>
      <tr v-for="employee1 in employees1" :key="employee1.id" @dblclick="($data.employee1 = employee1)"  >

        <td id="useridinput" scope="row">{{employee1.id}}</td>




        



      </tr>
    </tbody>
  </table>
    </template>



    <script>
    
    import axios from 'axios'
      export default {
        name: 'App',
      
          data()
          {
            return{
            employee:{},
            employees: [],
            employee1:{},
            employees1: [] }
        },
        async created(){
          await this.getEmployees();
          await this.getEmployees1();
          await this.getcube();
      
        },
        
        methods: {
        submitForm(){
        if (this.employee.id === undefined){
          this.createEmployee();
        } else {
          this.editEmployee();
        }
      },

          async getEmployees(){
            var response = await fetch('http://localhost:8000/emailspage/');
            this.employees = await response.json();
      
          },

        async createEmployee(){
        await this.getEmployees();
         await fetch('http://localhost:8000/bids/',{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.employee)
        });
        await this.getEmployees();
  
      },
      async getEmployees1(){
            var response = await fetch('http://127.0.0.1:8000/profile/');
            this.employees1 = await response.json();
      
          },
      getcube(){    
        

        
        var input = document.getElementById("useridinput").textContent
    const test = String(input);
    var hel=document.getElementById("myInput").value
    document.getElementById("myInput").value=test
    
    
    // document.getElementById("myInput").disabled = true;
    element.dispatchEvent(new Event('myInput'));
    console.log(document.getElementById("myInput"))
    console.log(input)}








        }}
        </script>


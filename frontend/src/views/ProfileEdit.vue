
<template>
    Double click to on table row where username is present to edit or add data to user
    <div id="app">
      <form @submit.prevent="submitForm">
        <div class="form-group row">
            <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="email" v-model="employee.username">
            <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="email" v-model="employee.email">
          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="first name" v-model="employee.first_name">
          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="last name" v-model="employee.last_name">
          <input type="date" class="form-control col-3 mx-2 text-primary" placeholder="dob" v-model="employee.dOB">

          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="address line 1" v-model="employee.addressLine1">
          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="address line 2" v-model="employee.addressLine2">
          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="city" v-model="employee.city">
          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="postcode" v-model="employee.postcode">
          <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="country" v-model="employee.country">

          <button class="btn btn-success">Submit</button>
  
        </div>
      </form>
  
  
  <table class="table">
    <thead>
      <tr>
<th>username</th>
        <th>email</th>
        <th>Name</th>
        <th>last name</th>
<th>dob</th>

        <th>address line 1</th>
        <th>address line 2</th>
        <th>city</th>
        <th>postcode</th>
        <th>country</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >

        <td>{{employee.username}}</td>
        <td>{{employee.email}}</td>
        <td>{{employee.first_name}}</td>
        <td>{{employee.last_name}}</td>
        
        <td>{{employee.dOB}}</td>
        <td>{{employee.addressLine1}}</td>
        <td>{{employee.addressLine2}}</td>
        <td>{{employee.city}}</td>
        <td>{{employee.postcode}}</td>
        <td>{{employee.country}}</td>



 

      </tr>
    </tbody>
  </table>
    </div>
  </template>
  
  <script>
  
  
  export default {
    name: 'App',
  
      data()
      {
        return{
        employee:{},
        employees: [] }
    },
    async created(){
      await this.getEmployees();
  
    },
    methods: {
      submitForm(){
        if (this.employee.id === undefined){
            this.editEmployee();
        } else {
            this.editEmployee();
        }
      },
      async getEmployees(){
        var response = await fetch('http://localhost:8000/profile/');
        this.employees = await response.json();
  
      },
      async createEmployee(){
        await this.getEmployees();
         await fetch('http://localhost:8000/api/employees/',{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.employee)
        });
        await this.getEmployees();
  
      },
      async editEmployee(){
        await this.getEmployees();
         await fetch(`http://localhost:8000/profiledet/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.employee)
        });
        await this.getEmployees();
        this.employee={};
      },
  
      
    }
  
  }
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  
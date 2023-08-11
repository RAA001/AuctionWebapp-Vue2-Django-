
<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="Name" v-model="employee.name">
        <input type="text" class="form-control col-3 mx-2 text-primary" placeholder="Job" v-model="employee.job">
        <p>Sixty or more eanings?</p><input type="checkbox" class="" placeholder="Sixtyormoreearnings" v-model="employee.sixtyormoreearnings" value="accepted" unchecked-value="not_accepted">
        <input type="date" class="form-control col-3 mx-2 text-primary" placeholder="Startdate" v-model="employee.startdate">
        <input type="number" class="form-control col-3 mx-2 text-primary" placeholder="Age" v-model="employee.age">
        <button class="btn btn-success">Submit</button>

      </div>
    </form>


<table class="table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Job</th>
      <th>Sixty or more earnings</th>
      <th>Start Date</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >
      <td scope="row">{{employee.name}}</td>
      <td>{{employee.job}}</td>
      <td>{{employee.sixtyormoreearnings}}</td>
      <td>{{employee.startdate}}</td>
      <td>{{employee.age}}</td>
      <td><button class="btn btn-outline-danger btn-sm-mx-1" @click="deleteEmployee(employee)">x</button></td>
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
        this.createEmployee();
      } else {
        this.editEmployee();
      }
    },
    async getEmployees(){
      var response = await fetch('http://localhost:8000/api/employees/');
      this.employees = await response.json();

    },
    async createEmployee(){
      await this.getEmployees();
       await fetch('http://localhost:8000/api/v1/profile/',{
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
       await fetch(`http://localhost:8000/api/employees/${this.employee.id}/`,{
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.employee)
      });
      await this.getEmployees();
      this.employee={};
    },
    async deleteEmployee(employee){
      await this.getEmployees();
       await fetch(`http://localhost:8000/api/employees/${employee.id}/`,{
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.employee)
      });
      await this.getEmployees();
      

    }
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

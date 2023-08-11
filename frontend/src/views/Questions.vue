
<template>


    <div id="app">
        <h4>Please enter product id & question (Product id is on prouduct details page)</h4>



            
    <form  enctype="multipart/form-data" action="http://localhost:8000/questions123/" method="post">
            <div class="form-group row">
              <input name="title" type="text"  placeholder="Title"  required>
          <input type="number" name="product" placeholder="product id" >
          
          <input id="myInput" type="text"  name="user" readonly/>          
          <input type="text" class="textarea" v name="question" placeholder="question" required>


              <!-- <input type="date" class="form-control col-3 mx-2 text-primary"  v-model="employee.finishdate"> -->
              
    
    
              
    
              <button type="submit" class="btn btn-success">Submit</button>
      
            </div>
          </form>
      
      <!-- <form @submit.prevent="submitForm" >
        <div >
            <input type="text"  placeholder="Title" v-model="employee.title">
          <input type="number"  placeholder="product id" v-model="employee.product">
          
          <input id="myInput" type="number"  />          
          <input type="text" class="textarea" v-model="employee.question">


          <button class="btn btn-success">Submit</button>
  
        </div>
      </form> -->
  
  
  <table class="table">
    <thead>
      <tr>
        <th>Title</th>
        <th>Question ID</th>
        <th>Product ID</th>
        <th>User ID</th>
        <th>Question</th>

      </tr>
    </thead>
    <tbody>
      <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >
        <td scope="row">{{employee.title}}</td>
        <td scope="row">{{employee.id}}</td>
        <td scope="row">{{employee.product}}</td>
        <td id="user">{{employee.user}}</td>
        <td>{{employee.question}}</td>
        <td>{{employee.Bids}}</td>
        



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
    </div>
  </template>



  <script>






    

  
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
        var response = await fetch('http://localhost:8000/questions123/');
        this.employees = await response.json();
  
      },
      async createEmployee(){
        await this.getEmployees();
         await fetch('http://localhost:8000/questions123/',{
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
    
    

    
    
    ,
      
    //   async editEmployee(){
    //     await this.getEmployees();
    //      await fetch(`http://localhost:8000/api/employees/${this.employee.id}/`,{
    //       method: 'put',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify(this.employee)
    //     });
    //     await this.getEmployees();
    //     this.employee={};
    //   },
    //   async deleteEmployee(employee){
    //     await this.getEmployees();
    //      await fetch(`http://localhost:8000/api/employees/${employee.id}/`,{
    //       method: 'delete',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify(this.employee)
    //     });
    //     await this.getEmployees();
        
  
    //   }
    // }
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
  

 
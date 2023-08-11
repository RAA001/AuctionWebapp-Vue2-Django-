



<template>
<h1> Only jpeg images should be added to product images </h1>
<h1>Only products you've added will be shown on this page</h1>
    <h1>Enter the category numbers. Category 1 = Pc. Category 2 = Mobiles</h1>
    <h1>Email added to product will be email, auction winner will see to contact you on on the product detail page</h1>
    
    <form  enctype="multipart/form-data" action="http://localhost:8000/products/" method="post">
            <div class="form-group row">
              <input id="myInput" type="text"  name="user" readonly/>    
              <input name="category" id="category" type="text" class="form-control col-3 mx-2 text-primary" placeholder="category" required>
              <input name="name" id="name" type="text" class="form-control col-3 mx-2 text-primary" placeholder="name" required>
              <input name="slug" id="slug" type="text" class="form-control col-3 mx-2 text-primary" placeholder="slug" required>
              <input name="description" id="description" type="text" class="form-control col-3 mx-2 text-primary" placeholder="description" required >
              <input name="price" id="price" type="number" class="form-control col-3 mx-2 text-primary" placeholder="price" required>
              <input name="image" type="file" accept="image/*" id="imageInput" >
              <input name="email" id="email" type="email" class="form-control col-3 mx-2 text-primary" placeholder="contact email" required>
              <input name="date_finish" id="date_finish" type="date" class="form-control col-3 mx-2 text-primary" placeholder="date_finish" required >

              <!-- <input type="date" class="form-control col-3 mx-2 text-primary"  v-model="employee.finishdate"> -->
              
    
    
              
    
              <button type="submit" class="btn btn-success">Submit</button>
      
            </div>
          </form>
      
          
      
      <table class="table">
        <thead>
          <tr>
            <th>category</th>
            <th>name</th>
            <th>slug</th>
            <th>description</th>
            <th>price</th>

            <th>email</th>
            <th>image</th>
            <th>date added</th>
            <th>date auction is to finish</th>
      
      
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >
    
    
            <td v-if="(employee.category==1)">Pc</td>
            <td v-else>Mobiles</td>

            <td>{{employee.name}}</td>
            <td>{{employee.slug}}</td>
            <td>{{employee.description}}</td>
            <td>{{employee.price}}</td>
            <td>{{employee.email}}</td>
            <td><img v-bind:src="employee.get_thumbnail"/></td>
            <td>{{employee.date_added}}</td>
            <td>{{employee.date_finish}}</td>
    
    
    
      
    
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
        //   submitForm(){
        //     if (this.employee.id === undefined){
        //       this.createImage();
        //     } else {
        //     //   this.editEmployee();
        //     }
        //   },
          async getEmployees(){
            var response = await fetch('http://localhost:8000/products/');
            this.employees = await response.json();
      
          },
          async createImage(){
            await this.getEmployees();


            const categoryInput=document.querySelector('#category')
            const nameInput=document.querySelector('#name')
            const slugInput=document.querySelector('#slug')
            const descriptionInput=document.querySelector('#description')
            const priceInput=document.querySelector('#price')
            const imageInput=document.querySelector('#imageInput')


            let category=categoryInput
            let name=nameInput
            let slug=slugInput
            let description=descriptionInput
            let price=priceInput
            let image=imageInput.files[0]

            const formData= new FormData()

            formData.append("category",category)
            formData.append("name",name)
            formData.append("slug",slug)
            formData.append("description",description)
            formData.append("price",price)
            formData.append("image",image)


        //     await fetch('http://localhost:8000/api/v1/products/',{
        //   method: 'post',
        //   headers: {
        //     'Content-Type': 'application/json'
        //   },
        //   body: formData
        // });

            // var response =await fetch('http://localhost:8000/api/v1/products/',{
            //     method:'POST',
            //     headers:{'Content-Type':'application/json'},
            //     body: formData

            // }).then(response=>response.json()).catch(error=>{console.error(error)})









        },      async getEmployees1(){
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
    console.log(input)
    let currentDate=new Date()
        currentDate=currentDate.toISOString();
        var input1 = document.getElementById("date_finish")
        input1=input1.toISOString()
        console.log(input1)
        console.log(currentDate)
        if (currentDate>input1){
          alert("This product cannot be listed as date has been passed")
        }
}
    
      }}
        </script>


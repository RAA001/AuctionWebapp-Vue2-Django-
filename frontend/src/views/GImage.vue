



<template>



    
    <form  enctype="multipart/form-data" action="http://localhost:8000/profile/" method="post">
            <div class="form-group row">
              <input id="myInput" type="text"  name="user" readonly/>      


              <input name="image" id="fileInput" ref="fileInput" type="file" accept="image/*" @input="pickFile">



              
    
    
              
    
              <button type="submit" class="btn btn-success">Submit</button>
      
            </div>
          </form>



      
      <table class="table">
        <thead>
          <tr>
            <th>image</th>
      
      
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >
    
    



            <td><img v-bind:src="employee.get_image"/></td>
  
    
    
    
      
      

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
            previewImage: null,
            employee:{},
            employees: [],
            employee1:{},
            employees1: []
           }
        },
        async created(){
          await this.getEmployees();
          await this.getEmployees1();
          await this.getcube();

      
        },
        
        methods: {
          submitForm(){
            if (this.employee.id === undefined){
              this.addImage();
            } else {
            //   this.editEmployee();
            }
          },
          async getEmployees(){
            var response = await fetch('http://localhost:8000/profile/');
            this.employees = await response.json();
      
          },
          async addImage(){
            let formData = new FormData()
            formData.append('image')
            console.log(formData)
         let response = await fetch('http://localhost:8000/profile/',{
          method: 'post',
          body: formData
        });
        await this.getEmployees();
  
      },
          selectImage () {
    this.$refs.fileInput.click()
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
    console.log(input)},

pickFile () {
  let input = this.$refs.fileInput
  let file = input.files
  if (file && file[0]) {
    let reader = new FileReader
    reader.onload = e => {
      this.previewImage = e.target.result
    }
    reader.readAsDataURL(file[0])
    this.$emit('input', file[0])
  }
  
 








        }}}
        </script>
<style>
.imagePreviewWrapper {
    width: 250px;
    height: 250px;
    display: block;
    cursor: pointer;
    margin: 0 auto 30px;
    background-size: cover;
    background-position: center center;
}
</style>
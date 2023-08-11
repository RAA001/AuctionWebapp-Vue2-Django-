<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
              <a href="http://127.0.0.1:8000">Login</a>
                <h1 class="title">My account</h1>
            </div>
            <table class="table">
        <thead>
          <tr>
            <th>User id</th>
            <th>username</th>
            <th>first_name</th>
            <th>last_name</th>
            <th>image</th>

      
      
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.id" @dblclick="$data.employee = employee"  >
    
    


            <td>{{employee.id}}</td>
            <td>{{employee.username}}</td>
            <td>{{employee.first_name}}</td>
            <td>{{employee.last_name}}</td>
            <td>{{employee.image}}</td>
            
    
    
    
      
      

          </tr>
        </tbody>
      </table>

            <div class="column is-12">
              <a href="http://127.0.0.1:8000/logout/">Logout</a>
            </div>
            <router-link to="/ProfileEdit" class="button is-light">Edit Profile</router-link>
            <router-link to="/GImage" class="button is-light">Edit/Add Image</router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'



export default {
    name: 'MyAccount',
    data(){
        return{
    employee:{},
    employees: [] }
    },
    async created(){
          await this.getEmployees();
      

  },
    methods: {

        async getEmployees(){
            var response = await fetch('http://127.0.0.1:8000/profile/');
            this.employees = await response.json();
      
          },
    }
}
</script>


<template>


    <div class="page-product">
        <div class="columns is-multiline"> 
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image"/>
                </figure>
                <h1 class="title">product name:{{product.name}}</h1>
                <p>product description:<strong>{{product.description}}</strong></p>
                <p>Product id:<strong>{{product.id}}</strong></p>
                <p>Product user id:<strong>{{product.user}}</strong></p>
                <p>Product contact email:<strong>{{product.email}}</strong></p>
                

            </div>
            <div class="column is-3">
                <h2 class="subtitle">Information about the product:</h2>
                <p><strong>Starting price:</strong>£{{product.price}}</p>
                <h1><strong>Finish auction date:</strong>{{product.date_finish}}</h1>
                <div class="field has-addons mt-6">
                    <div class="control">

                    </div>
                    <div class="control">

                    </div>
                </div>
            </div>
        </div>
    </div>

</template>



<script>
import axios from 'axios'

export default{
    name: 'Product',
    data(){
        return{
            product:{},

            employee1:{},
        employees1: []

        }
    },
    mounted(){
        this.getProduct();
        this.getEmployees1();
    },
    methods:{
        async getProduct(){
            this.$store.commit('setIsLoading',true)

            const category_slug=this.$route.params.category_slug
            const product_slug=this.$route.params.product_slug

            await axios
                .get(`products/${category_slug}/${product_slug}/`)
                .then(response=>{
                    this.product=response.data

                    document.title=this.product.name + ' | Techzonezz'
                     
                })
                .catch(error=>{
                console.log(error)})
                this.$store.commit('setIsLoading',false)
        },      async getEmployees1(){
            var response = await fetch('http://127.0.0.1:8000/profile/');
            this.employees1 = await response.json();
      
          },

    }
}
</script>
<template>

  
  <div class="home">
    <section class="hero is-medium is-light mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Techzonezz
        </p>
        <p class="subtitle">
          The best tech auction online
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">All products</h2>
      </div>

      <ProductBox  v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product"/>
</div>
</div>
</template>




<script>
import axios from 'axios'
import ProductBox from'@/components/ProductsBox.vue'

export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts:[]
      
  }},
  components: {
    ProductBox
    
  },
  mounted(){
    this.getallproducts()
    document.title = 'Home | Techzonezz'
  }, 
  methods:{
    async getallproducts(){
      this.$store.commit('setIsLoading',true)
      await axios
      .get('l-products/')
      .then (response=>{
        this.latestProducts=response.data
      })
      .catch(error=>{
        console.log(error)
      })
      this.$store.commit('setIsLoading',false)
    }
  }
}
</script>
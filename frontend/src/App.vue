<template>
  <div id="wrapper">
<nav class="navbar is-light">
<div class="navbar-brand">

  <router-link to="/" class="navbar-item"><strong>Techzonezz</strong></router-link>
  <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
    <span aria-hidden="true"></span>
    <span aria-hidden="true"></span>
    <span aria-hidden="true"></span>
  </a>
</div>

<div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
  <div class="navbar-start">
    <div class="navbar-item">
      <form method="get" action="/search">
        <div class="field has-addons">
          <div class="control">
            <input type="text" class="input" placeholder="What are you looking for?" name="query">
          </div>
          <div class="control">
            <button class="button is-success">
              <span class="icon">
                <i class="fas fa-search"></i>
              </span>
            </button>


          </div>
        </div>
      </form>
    </div>

  </div>
  <div class="navbar-end">
  <router-link to="/Pc" class="navbar-item">Pc</router-link>
  <router-link to="/Mobiles" class="navbar-item">Mobiles</router-link>
  <router-link to="/AddProduct" class="navbar-item">AddProduct</router-link>
  <router-link to="/Questions" class="navbar-item">Questions</router-link>
  <router-link to="/Answers" class="navbar-item">Answers</router-link>
  <router-link to="/Bids" class="navbar-item">Bids</router-link>
  <router-link to="/my-account" class="button is-dark">My account</router-link>
  <router-link to="/emailpage" class="navbar-item">emails page</router-link>
  <div class="navbar-item">
    <div class="buttons">

      








    </div>
  </div>
</div>
</div>
  </nav>
  <div class="is-loading-bar has-text-cenetered" v-bind:class="{'is-loading': $store.state.isLoading}">
  <div class="lds-dual-ring"></div>
  </div>
  <section class="section">
  <router-view/>
  </section>
  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2022</p>
  </footer>
</div>
</template>
<script>
import axios from 'axios'

export default{
  data() {
    return{
      showMobileMenu:false,


    }
  },
}
</script>

<style lang="scss">

.lds-dual-ring{
  display: inline-block;
  width:80px;
  height:80px;
}
.lds-dual-ring:after{
  content:"";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50px;
  border:6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>

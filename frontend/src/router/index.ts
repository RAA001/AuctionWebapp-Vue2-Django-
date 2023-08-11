import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'

import MyAccount from '../views/MyAccount.vue'


import GImage from '../views/GImage.vue'
import store from '@/store'
import AddProduct from '../views/AddProduct.vue'
import Questions from '../views/Questions.vue'
import Answers from '../views/Answers.vue'
import Bids from '../views/Bids.vue'
import emailpage from '../views/emailpage.vue'
import ProfileEdit from '../views/ProfileEdit.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/:category_slug/:product_slug',
    name:'Product',
    component:Product


  },
  {
    path: '/AddProduct',
    name: 'AddProduct',
    component: AddProduct
  },
  {
    path: '/Bids',
    name: 'Bids',
    component: Bids
  },
  {
    path: '/Answers',
    name: 'Answers',
    component: Answers
  },
  {
    path: '/Questions',
    name: 'Questions',
    component: Questions
  },
  {
    path: '/emailpage',
    name: 'emailpage',
    component: emailpage
  },
  {
  path:'/:category_slug',
  name:'Category',
  component:Category},
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/GImage',
    name: 'GImage',
    component: GImage
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
  },
  {
    path: '/ProfileEdit',
    name: 'ProfileEdit',
    component: ProfileEdit,
  },




]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})
router.beforeEach((to,from,next)=>{
if(to.matched.some(record => record.meta.requireLogin)&&!store.state.isAuthenticated)  {
  next({name:'LogIn', query:{to: to.path}});
}
else{
  next()
}
})

export default router

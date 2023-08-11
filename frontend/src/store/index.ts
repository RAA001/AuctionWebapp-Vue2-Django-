import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{

    },

  },
  getters: {
  },
  mutations: {
      setIsLoading(state,status){
        state.isLoading=status
      },


  },
  actions: {
  },
  modules: {
  }
})

import Vue from 'vue'
import Router from 'vue-router'
import UserComponent from '@/components/UserComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserComponent',
      component: UserComponent
    }
  ]
})

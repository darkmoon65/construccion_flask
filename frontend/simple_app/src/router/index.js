import Vue from 'vue'
import Router from 'vue-router'
import DataComponent from '@/components/DataComponent'
import UserComponent from '@/components/UserComponent'
import componentePrueba from '@/components/componentePrueba'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: UserComponent
    },
    {
      path: '/data',
      component: DataComponent
    },
    {
      path: '/prueba',
      component: componentePrueba
    }
  ]
})

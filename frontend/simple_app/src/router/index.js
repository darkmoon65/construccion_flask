import Vue from 'vue'
import Router from 'vue-router'
import DataComponent from '@/components/DataComponent'
// import MethodsComponent from '@/components/MethodsComponent'
// import FormularioComponent from '@/components/FormularioComponent'
import UserComponent from '@/components/UserComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserComponent',
      component: UserComponent
    },
    {
      path: '/data',
      component: DataComponent,
      props: {algo: 'some'}
    }
  ]
})

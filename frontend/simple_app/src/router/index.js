import Vue from 'vue'
import Router from 'vue-router'
import UserComponent from '@/components/UserComponent'
import HomeComponent from '@/components/HomeComponent'
import HorarioComponent from '@/components/HorarioComponent'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: HomeComponent
    },
    {
      path: '/usuarios',
      component: UserComponent
    },
    {
      path: '/justificaciones',
      component: UserComponent
    },
    {
      path: '/horarios',
      component: HorarioComponent
    },
    {
      path: '/asistencias',
      component: UserComponent
    }
  ]
})

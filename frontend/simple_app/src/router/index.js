import Vue from 'vue'
import Router from 'vue-router'
import UserComponent from '@/components/UserComponent'
import HomeComponent from '@/components/HomeComponent'
import AlumnoComponent from '@/components/AlumnoComponent'
import HorarioComponent from '@/components/HorarioComponent'
import AsistenciaComponent from '@/components/AsistenciaComponent'
import LoginComponent from '@/components/LoginComponent'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: HomeComponent,
      meta: {requireAuth: true, administrador: true, alumno: true, profesor: true}
    },
    {
      path: '/usuarios',
      component: UserComponent,
      meta: {requireAuth: true, administrador: true}
    },
    {
      name: 'justificaciones',
      path: '/justificaciones',
      component: UserComponent,
      meta: {requireAuth: true, administrador: true}
    },
    {
      path: '/horarios',
      component: HorarioComponent,
      meta: {requireAuth: true, administrador: true}
    },
    {
      path: '/asistencias',
      component: AsistenciaComponent,
      meta: {requireAuth: true, administrador: true, alumno: true}
    },
    {
      path: '/alumnos',
      component: AlumnoComponent,
      meta: {requireAuth: true, administrador: true}
    },
    {
      path: '/login',
      component: LoginComponent,
      name: 'Login'
    }
  ]
})

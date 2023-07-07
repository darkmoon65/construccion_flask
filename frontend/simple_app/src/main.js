// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueResource)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    const token = localStorage.getItem('token')
    const typeUser = localStorage.getItem('typeUser')
    console.log('just')
    if (!token) {
      next({ name: 'Login' })
    } else {
      if (typeUser === 'administrador' && to.matched.some(record => record.meta.administrador)) {
        console.log('some')
        next()
      } else if (typeUser === 'alumno' && to.matched.some(record => record.meta.alumno)) {
        next()
      } else if (typeUser === 'profesor' && to.matched.some(record => record.meta.profesor)) {
        next()
      } else {
        console.log('aaa')
        next({name: 'justificaciones'})
      }
    }
  } else {
    next()
  }
})
new Vue({
  router,
  components: { App },
  template: '<App/>'
}).$mount('#app')

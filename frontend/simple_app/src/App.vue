<template>
  <div id="app">
    <UserComponent/>
    <formComponent/>

  </div>
</template>

<script>
// import SimpleComponent from './components/SimpleComponent'
// import DataComponent from './components/DataComponent'
// import MethodsComponent from './components/MethodsComponent'
// import formComponent from './components/formComponent'
import UserComponent from './components/UserComponent'

export default {
  name: 'App',
  components: {
    // SimpleComponent,
    // DataComponent,
    // MethodsComponent,
    UserComponent
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

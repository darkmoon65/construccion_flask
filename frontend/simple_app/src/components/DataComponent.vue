<template>
    <div class='test'>
        <h2>Component Data</h2>
        Var title: {{ title }} <br>
        Object user: {{ user }} <br>
        Attribute: {{ user.firstName }} <br>
        Composed var: {{ fullName }} <br>
        Message from App.vue: {{ msg }} <br>
        Composed varttile: {{ titleLastName }} <br>

        <!-- para poder un html -->
        <div v-html='myHtml'></div>

        <!-- para mostrar el contenido solo si una variable es true -->
        <div v-if='showName'>
            <p>showName == true</p>
        </div>
        <div v-else>
            <p>showName == false</p>
        </div>

        <!-- para mostrar un array -->
        <ul><li v-for='task in tasks' :key= "task.id"> {{ task.title }} </li></ul>
    </div>
    </template>

<script>
export default{
  data () {
    return {
      title: 'Hello Vue.js',
      user: {
        firstName: 'Vicente',
        lastName: 'Machaca'
      },
      myHtml: '<font color="red"  > texto </font> <h1> texto </h1>  ',
      showName: true,
      tasks: [
        {title: 'eat'},
        {title: 'study'}
      ]
    }
  },
  computed: {
    fullName () {
      return this.user.firstName + ' ' + this.user.lastName
    },
    titleLastName () {
      return this.title + ' ' + this.user.lastName
    }
  },

  props: { // se utiliza para recibir datos
    msg: {
      type: String,
      default: 'default'
    }
  }
}
</script>

    <style media="screen">
        .test{background-color: #eeeeee;}
    </style>

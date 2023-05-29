<template>
<div class='test' >
    <div>
        <strong>Name: </strong> {{ user.firstName }} <br>
        <strong>Last Name: </strong> {{ user.lastName }} <br>
        <strong>Age: </strong> {{ user.age }} <br>
        <strong>Tasks: </strong>
        <div>
            <table id="tabla">
                <tr>
                    <th>Titulo</th>
                     <th>Descripcion</th>
                </tr>
                <tr v-for='task in tasks' :key="task.id">
                    <td > {{ task.title }}  </td>
                    <td > {{task.description}} </td>

                </tr>
            </table>
        </div>
    </div>
    <div>
        <img src="../assets/perfil.png">
    </div>
</div>
</template>

<script>
export default{
  data () {
    return {
      user: {
        firstName: 'Cesar',
        lastName: 'Santillana',
        age: 30
      },
      tasks: [
        {title: 'eat', description: 'description 1'},
        {title: 'study', description: 'description 1'}
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
    },
    algo: {
      type: String,
      default: 'default'
    }
  }
}
</script>

<style media="screen">
    .test{background-color: black;
        background: rgb(231, 174, 174); color: black;  padding:60px;
        display: flex;
        width: 300px;
    }
    table, th, td{
        border: 1px solid black;
        border-collapse: collapse;
    }
    img {
        width: 100px;
        height: 100px;
    }
</style>

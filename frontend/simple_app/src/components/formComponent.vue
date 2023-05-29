<template>
    <div class='test'>
        Object user: {{ user }} <br>
        Attribute: {{ user.firstName,user.lastName, age, task  }} <br>

        FirstName<input type='text' v-model='user.firstName'> <br>
        LastName<input type='text' v-model='user.LastName'> <br>
        age<input type='text' v-model='user.age' > <br>
        task<input type='text' v-model='user.task' v-on:keyup='typing'> <br>

        <!-- este botton llama a un metodo -->
        <button type='button' v-on:click="saludar(user)"> SEND</button><br>

    </div>
    </template>

<script>
export default{
  data () {
    return {
      user: {firstName: 'Pepe',
        LastName: 'Perez',
        age: '20',
        task: 'Study'
      }
    }
  },
  methods: {
    saludar (user) { console.log(user.firstName, user.LastName, user.age, user.task) },
    typing (e) {
      console.log(e.target.value)
      if (e.target.value === 'quit') {
        console.log('exit...')
      }
    },
    typingEnter (e) { console.log('Tarea realizada') }
  }

}
</script>

    <style>
        .test{background-color: #06ceba; font-weight: bold; line-height: 1.5em}
    </style>

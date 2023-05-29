<template>
<div class='test'>
    Object user: {{ user }} <br>
    First Name: <input class="form-control" type='text' v-model='user.firstName'> <br>
    Last Name:<input class="form-control" type='text' v-model='user.lastName'> <br>
    Age: <input class="form-control" type='text' v-model='user.age'> <br>
    Task: <input class="form-control" type='text' v-model='user.task' v-on:keyup='typing'> <br>
    <div class="divi">
        <button type='button' v-on:click="imprimir(user)" class="btn btn-warning"> Send </button><br>
    </div>
</div>
</template>

<script>
export default{
  data () {
    return {
      user: {firstName: 'Cesar',
        lastName: 'Santillana',
        age: 20,
        task: 'study'}
    }
  },
  methods: {
    imprimir (user) { console.log(user.firstName, user.lastName, user.age, user.task) },
    typing (e) {
      console.log(e.target.value)
      if (e.target.value === 'quit') {
        console.log('exit...')
      }
    },
    typingEnter (e) { console.log('ENTER') }
  }
}
</script>

<style>
    .test{background-color: #eeeeee;}
    .divi{display: flex; justify-content: center;}
</style>

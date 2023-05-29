<template>
    <div class='users'>
        <h2>Users</h2>
        <ul>
            <li v-for='user in users' :key="user.id">
                {{user.name}} - {{ user.email }}
                <button v-on:click='deleteUser(user)'>x</button>
            </li>
        </ul>

        <div class="row">
          <form class="col s12">
            <div class="row">
              <div class="input-field col s6">
                <input  id="first_name" type="text" class="validate">
                <label for="first_name">Nombres</label>
              </div>

              <div class="input-field col s6">
                <input id="last_name" type="text" class="validate">
                <label for="last_name">Apellidos</label>
              </div>
            </div>

            <div class="input-field col s4">
                <input id="last_name" type="text" class="validate">
                <label for="last_name">DNI</label>
              </div>
            <div class="input-field col s4">
                <input id="email" type="email" class="validate">
                <label for="email">Correo electrónico</label>
            </div>
            <div class="row">
              <div class="input-field col s4">
                <input id="password" type="password" class="validate">
                <label for="password">Contraseña</label>
              </div>
            </div>
            <div class="row">

            </div>
            <button class="btn waves-effect green" type="submit" name="action">
                 Agregar <i class="large material-icons">person_add</i>
            </button>
          </form>

        </div>

          <table class="striped">
        <thead>
          <tr>
              <th>Nombre</th>
              <th>DNI</th>
              <th>Item Price</th>
              <th>
              <button class="btn waves-effect waves-light" type="submit" name="action">
                 <i class="large material-icons">remove_red_eye</i>
              </button>

              <button class="btn waves-effect green" type="submit" name="action">
                 Actualizar <i class="large material-icons">system_update_alt</i>
              </button>

              <button class="btn waves-effect red" type="submit" name="action">
                 <i class="large material-icons">delete</i>
              </button>
              </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>Alvin</td>
            <td>Eclair</td>
            <td>$0.87</td>
          </tr>
          <tr>
            <td>Alan</td>
            <td>Jellybean</td>
            <td>$3.76</td>
          </tr>
          <tr>
            <td>Jonathan</td>
            <td>Lollipop</td>
            <td>$7.00</td>
          </tr>
        </tbody>
      </table>

      </div>
    </template>

<script>
export default{
  // con esto podemos crear variables que puedan usarse en el html(template)
  data () { // variables
    return {
      /* users: [ // lo ideal seria recibir esto de un endpoint
        {
          name: 'vicente',
          email: 'vicente.machaca.a@gmail.com',
          contacted: false
        },
        {
          name: 'miguel',
          email: 'miguel@gmail.com',
          contacted: false
        }
      ], */
      users: [],
      newUser: {}
    }
  },
  methods: {
    addUser (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      console.log('user added')
      this.users.push(this.newUser)
      this.newUser = {}
    },
    deleteUser (user) {
      this.users.splice(this.users.indexOf(user), 1)
      console.log('deleteUser')
    }
  },
  created () { // este metodo se lalma cuando se cra el componente
    // con esto hacemos una peticion a un server
    this.$http.get('https://jsonplaceholder.typicode.com/users')
      .then(res => {
        this.users = res.body
      })
  }

}
</script>

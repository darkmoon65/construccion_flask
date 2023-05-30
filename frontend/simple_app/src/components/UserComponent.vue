<template>
    <div class='users'>
      <nav>
        <div class="nav-wrapper">
          <a href="#" class="brand-logo">Usuarios</a>
          <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="sass.html"><i class="material-icons">search</i></a></li>
          </ul>
        </div>
      </nav>
        <div class="row">
          <form v-on:submit='addUsers' class="col s12">
            <div class="row">
              <div class="input-field col s6">
                <input v-model='newUser.nombre' id="first_name" type="text" class="validate">
                <label for="first_name">Nombres y Apellidos</label>
              </div>

              <div class="input-field col s4">
                <input v-model='newUser.dni' id="last_name" type="text" class="validate">
                <label for="last_name">DNI</label>
              </div>
            </div>
            <div class="row">
              <div class="input-field col s4">
                <input v-model='newUser.password' id="password" type="password" class="validate">
                <label for="password">Contraseña</label>
              </div>
              <div class="input-field col s4">
                <input v-on:change="onFileChange" id="foto" type="file" class="validate">
                <label for="foto">Foto</label>
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
          </tr>
        </thead>

        <tbody>
          <tr v-for='user in users' :key="user.id">
            <td>{{user.nombre_usuario}} </td>
            <td>{{user.dni_usuario}} </td>
            <td>{{user.ruta_foto}} </td>
            <td>
              <button class="btn waves-effect waves-light" type="submit" name="action">
                 <i class="large material-icons">remove_red_eye</i>
              </button>

              <a class="waves-effect waves-light btn modal-trigger" data-target="#editarModal"  data-toggle="modal"
              v-on:click="onFileChange2(user.usuario_id)" >Actualizar
                <i class="large material-icons">system_update_alt</i>
              </a>
              <button v-on:click='deleteUsers(user.usuario_id)' class="btn waves-effect red" name="action">
                 <i class="large material-icons">delete</i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div id="editarModal" class="modal">
        <div class="modal-dialog">
            <div class="modal-content">
              <div class="row">
          <form v-on:submit='updateUsers' class="col s12">
            <div class="row">
              <div class="input-field col s6">
                <input v-model='newUser.nombre' id="first_name" type="text" class="validate">
                <label for="first_name">Nombres y Apellidos</label>
              </div>

              <div class="input-field col s4">
                <input v-model='newUser.dni' id="last_name" type="text" class="validate">
                <label for="last_name">DNI</label>
              </div>
            </div>
            <div class="row">
              <div class="input-field col s4">
                <input v-model='newUser.password' id="password" type="password" class="validate">
                <label for="password">Contraseña</label>
              </div>
              <div class="input-field col s4">
                <input v-on:change="onFileChange" id="foto" type="file" class="validate">
                <label for="foto">Foto</label>
              </div>
            </div>
            <div class="row">

            </div>
            <button class="btn waves-effect green" type="submit" name="action">
                 Actualizar <i class="large material-icons">person_add</i>
            </button>
          </form>

        </div>
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>

            </div>
        </div>
      </div>
    </div>
    </template>

<script>
import axios from 'axios'
export default{
  data () {
    return {
      users: [],
      newUser: {},
      postURL: 'http://127.0.0.1:5000'

    }
  },
  methods: {
    onFileChange (e) {
      var files = e.target.files[0]
      this.newUser.foto = files
    },
    onFileChange2 (id) {
      this.newUser.usuario_id = id
      console.log(id)
    },
    addUsers (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      var formData = new FormData()
      formData.append('foto', this.newUser.foto)
      formData.append('nombre', this.newUser.nombre)
      formData.append('dni', this.newUser.dni)
      formData.append('password', this.newUser.password)

      axios.post(this.postURL + '/usuario_create', formData, { configRequest })
        .then(res => {
          this.users.push(res.data)
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })

      this.newUser = {}
    },
    updateUsers (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      var formData = new FormData()
      formData.append('foto', this.newUser.foto)
      formData.append('nombre', this.newUser.nombre)
      formData.append('dni', this.newUser.dni)
      formData.append('password', this.newUser.password)
      formData.append('usuario_id', this.newUser.usuario_id)
      axios.post(this.postURL + '/update_usuario', formData, { configRequest })
        .then(res => {
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })

      this.newUser = {}
    },
    deleteUsers (userId) {
      var configRequest = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
      axios.post(this.postURL + '/usuario_delete', {usuario_id: userId}, { configRequest })
        .then(res => {
          this.users.splice(this.users.indexOf(userId), 1)
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created () {
    axios.get(this.postURL + '/usuarios').then((res) => {
      console.log(res)
      this.users = res.data
    })
      .catch((error) => {
        console.log(error)
      })
  }

}
</script>

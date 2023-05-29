<template>
<div>
    <div class='tasks'>
    </div>
    <div class="container">
        <div class="row">
            <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#crearModal">
                    Crear
            </button>
            <table class="table">
                 <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nombre</th>
                    <th scope="col">Dni</th>
                    <th scope="col">Foto</th>
                    <th scope="col">Opciones</th>
                    </tr>
                </thead>
                <tbody>
                        <tr v-for='user in users' :key='user.id'>
                            <td> # </td>
                            <td> {{user.nombre_usuario}} </td>
                            <td> {{user.dni_usuario}} </td>
                            <td> <img v-bind:src="postURL+ '/' + user.ruta_foto"  alt="" style="width: 80px"> </td>
                            <td>
                                <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#editarModal">
                                    Editar
                                </button>
                            </td>
                            <td>
                                <button v-on:click='deleteUser(user.usuario_id)' class="btn btn-danger">Eliminar</button>
                            </td>
                        </tr>
                </tbody>
            </table>
        </div>

<!-- Modal -->
        <div class="modal fade" id="crearModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Crear </h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                 <form v-on:submit='addUsers'>
                    <div class="input-group mb-3">
                    <label>Nombre</label>
                    <input type="text" v-model='newUser.nombre' class="form-control" placeholder="Nombre" >
                </div>
                <div class="input-group mb-3">
                    <label>Dni</label>
                    <input type="text" v-model='newUser.dni' class="form-control" placeholder="Dni">
                </div>
                <div class="input-group mb-3">
                    <label>Foto</label>
                    <input type="file" v-on:change="onFileChange" class="form-control" placeholder="Foto">
                </div>
                <div class="input-group mb-3">
                    <label>Password</label>
                    <input type="password" v-model='newUser.password' class="form-control" placeholder="Password">
                </div>
                <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
            </div>
            </div>
        </div>
        </div>

         <div class="modal fade" id="editarModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Editar </h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                 <form v-on:submit='updateUsers'>
                    <div class="input-group mb-3">
                    <label>Nombre</label>
                    <input type="text" v-model='newUser.nombre' class="form-control" placeholder="Nombre"  >
                </div>
                <div class="input-group mb-3">
                    <label>Dni</label>
                    <input type="text" v-model='newUser.dni' class="form-control" placeholder="Dni">
                </div>
                <div class="input-group mb-3">
                    <label>Foto</label>
                    <input type="file" v-on:change="onFileChange" class="form-control" placeholder="Foto">
                </div>
                <div class="input-group mb-3">
                    <label>Password</label>
                    <input type="password" v-model='newUser.password' class="form-control" placeholder="Password">
                </div>
                <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                </form>

            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
            </div>
            </div>
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

    updateUsers (e) {
    // with axios

      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      console.log(this.newUser)
      var formData = new FormData()
      formData.append('foto', this.newUser.foto)
      formData.append('nombre', this.newUser.nombre)
      formData.append('dni', this.newUser.dni)
      formData.append('password', this.newUser.password)

      axios.post(this.postURL + '/update_usuario', {formData}, {configRequest}).then((res) => {
        console.log(res.data)
        this.users = res.data
      })
        .catch((error) => {
          console.log(error)
        })
    },
    onFileChange (e) {
      var files = e.target.files[0]
      this.newUser.foto = files
    },
    addUsers (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      console.log(this.newUser)
      var formData = new FormData()
      formData.append('foto', this.newUser.foto)
      formData.append('nombre', this.newUser.nombre)
      formData.append('dni', this.newUser.dni)
      formData.append('password', this.newUser.password)

      axios.post(this.postURL + '/usuario_create', formData, { configRequest })
        .then(res => {
          this.users.push(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteUser (user) {
      var configRequest = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
      console.log(user)
      axios.post(this.postURL + '/usuario_delete', {usuario_id: user}, { configRequest })
        .then(res => {
          this.users.splice(this.users.indexOf(user), 1)
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created () {
    // with axios
    axios.get(this.postURL + '/usuarios').then((res) => {
      console.log(res.data)
      this.users = res.data
    })
      .catch((error) => {
        console.log(error)
      })
  }

}
</script>

    <style>
        .tasks{
            background-color: #cccccc;
        }
    </style>

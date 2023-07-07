<template>
<div>
    <div class="container">
        <div class="row">
          <div style="margin: 10px">
            <b-button size="sm" @click="crearModal($event.target)" class="mr-2 btn btn-success">
                Crear usuario
            </b-button>
          </div>
            <b-table id="my-table" :items="users" :per-page="perPage" :current-page="currentPage" :fields="fields">
                <template #cell(opciones)="row">
                    <b-button @click="editarModal(row.item, $event.target)" class="btn btn-primary">
                      Editar
                    </b-button>
                    <button v-on:click='deleteUser(row.item)' class="btn btn-danger">Eliminar</button>
                </template>
            </b-table>
              <div class="overflow-auto">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="my-table"
                ></b-pagination>

                <p class="mt-3">Pagina actual: {{ currentPage }}</p>
              </div>
        </div>

<!-- Modales -->
      <b-modal :id="createModal.id" :title="'Crear usuarios'" ok-only >
          <div class="modal-content">
            <div class="modal-body">
                 <form v-on:submit='addUsers'>
                      <div class="row p-2">
                          <div class="col-3">
                         <label>Nombre</label>
                      </div>
                      <div class="col-9">
                        <input type="text" v-model='nuevoUsuario.nombre' class="form-control" placeholder="Nombre" >
                      </div>
                      </div>
                  <div class="row p-2">
                          <div class="col-3">
                         <label> DNI</label>
                      </div>
                      <div class="col-9">
                        <input type="text" v-model='nuevoUsuario.dni' class="form-control" placeholder="Ingrese Dni">
                      </div>
                      </div>

                  <div class="row p-2">

                          <div class="col-3">
                            <label>Foto</label>
                      </div>
                      <div class="col-9">
                        <input type="file" v-on:change="onFileChange" class="form-control" placeholder="Foto">
                      </div>
                      </div>

                  <div class="row p-2">
                          <div class="col-3">
                          <label>Password</label>
                      </div>
                      <div class="col-9">
                        <input type="password" v-model='nuevoUsuario.password' class="form-control" >
                      </div>
                      </div>
                  <div style="align-items:center; justify-content: center ; display:flex" class="p-4">
                    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                  </div>
                </form>

            </div>
          </div>
      </b-modal>
      <b-modal :id="updateModal.id" :title="'Actualizar'" ok-only >
          <div class="modal-content">
            <div class="modal-body">
                               <form v-on:submit='updateUsers'>
                      <div class="row p-2">
                          <div class="col-3">
                         <label>Nombre</label>
                      </div>
                      <div class="col-9">
                        <input type="text" v-model='updateUser.nombre' class="form-control" placeholder="Nombre"  >
                      </div>
                      </div>
                  <div class="row p-2">
                          <div class="col-3">
                         <label> DNI</label>
                      </div>
                      <div class="col-9">
                        <input type="text" v-model='updateUser.dni' class="form-control" placeholder="Dni">
                      </div>
                      </div>

                  <div class="row p-2">

                          <div class="col-3">
                            <label>Foto</label>
                      </div>
                      <div class="col-9">
                        <input type="file" v-on:change="onFileChange" class="form-control" placeholder="Foto">
                      </div>
                      </div>
                  <div class="row p-2" style="align-items:center; justify-content: center ; display:flex">
                     <img v-bind:src="updateUser.foto_ruta" width="100" height="100">
                  </div>
                  <div class="row p-2">
                          <div class="col-3">
                          <label>Password</label>
                      </div>
                      <div class="col-9">
                          <input type="password" v-model='updateUser.password' class="form-control" placeholder="Password">
                      </div>
                      </div>
                  <div style="align-items:center; justify-content: center ; display:flex" class="p-4">
                    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                  </div>
                </form>
            </div>
            </div>
      </b-modal>
    </div>
</div>

</template>

<script>
import axios from 'axios'
import Vue from 'vue'
export default{
  data () {
    return {
      fields: ['usuario_id', 'dni_usuario', 'nombre_usuario', 'opciones'],
      perPage: 5,
      currentPage: 1,
      users: [],
      updateUser: {},
      nuevoUsuario: {},
      postURL: 'http://127.0.0.1:5000',
      updateModal: {
        id: 'update-modal',
        title: '',
        content: ''
      },
      createModal: {
        id: 'create-modal',
        title: '',
        content: ''
      }

    }
  },
  computed: {
    rows () {
      return this.users.length
    }
  },
  methods: {
    makeToast (variant = null, message) {
      this.$bvToast.toast(`${message}`, {
        title: `${variant || 'default'}`,
        variant: variant,
        autoHideDelay: 3000,
        solid: true
      })
    },
    updateUsers (e) {
      e.preventDefault()
      if (this.updateUser.dni.length !== 8) {
        console.log('no es 8 digitos')
        this.makeToast('danger', 'EL dni debe ser de 8 digitos')
        return
      }
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      let formUpdate = new FormData()
      formUpdate.append('foto', this.updateUser.foto)
      formUpdate.append('nombre', this.updateUser.nombre)
      formUpdate.append('dni', this.updateUser.dni)
      formUpdate.append('password', this.updateUser.password)
      formUpdate.append('usuario_id', this.updateUser.usuario_id)
      axios.post(this.postURL + '/update_usuario', formUpdate, {configRequest}).then((res) => {
        this.makeToast('success', 'Usuario actualizado')
        this.updateUser = {}
        this.refresh()
        this.$root.$emit('bv::hide::modal', this.updateModal.id)
      })
        .catch(() => {
          this.makeToast('danger', 'Hubo un error en el backend')
        })
    },
    onFileChange (e) {
      var files = e.target.files[0]
      this.nuevoUsuario.foto = files
      this.updateUser.foto = files
      Vue.set(this.updateUser, 'foto_ruta', window.URL.createObjectURL(files))
    },
    addUsers (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      if (this.nuevoUsuario.dni.length !== 8) {
        console.log('no es 8 digitos')
        this.makeToast('danger', 'EL dni debe ser de 8 digitos')
        return
      }
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      var formData = new FormData()
      formData.append('foto', this.nuevoUsuario.foto)
      formData.append('nombre', this.nuevoUsuario.nombre)
      formData.append('dni', this.nuevoUsuario.dni)
      formData.append('password', this.nuevoUsuario.password)

      axios.post(this.postURL + '/usuario_create', formData, { configRequest })
        .then(res => {
          this.makeToast('success', 'Usuario creado')
          this.nuevoUsuario = {}
          this.refresh()
          this.$root.$emit('bv::hide::modal', this.createModal.id)
        })
        .catch((error) => {
          console.log(error)
          this.makeToast('danger', 'Hubo un error en el backend')
        })
    },
    deleteUser (user) {
      var configRequest = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
      axios.post(this.postURL + '/usuario_delete', {usuario_id: user.usuario_id}, { configRequest })
        .then(res => {
          this.users.splice(this.users.indexOf(user), 1)
          console.log(res.data)
          this.makeToast('success', 'Usuario eliminado')
        })
        .catch((error) => {
          console.log(error)
          this.makeToast('danger', 'Hubo un error en el backend')
        })
    },
    editarModal (item, button) {
      Vue.set(this.updateUser, 'dni', item.dni_usuario)
      Vue.set(this.updateUser, 'nombre', item.nombre_usuario)
      Vue.set(this.updateUser, 'foto_ruta', 'http://localhost:5000/' + item.ruta_foto)
      Vue.set(this.updateUser, 'usuario_id', item.usuario_id)

      this.$root.$emit('bv::show::modal', this.updateModal.id, button)
    },
    crearModal (button) {
      this.$root.$emit('bv::show::modal', this.createModal.id, button)
    },
    refresh () {
    // with axios
      axios.get(this.postURL + '/usuarios').then((res) => {
        console.log(res.data)
        this.users = res.data
      })
        .catch((error) => {
          console.log(error)
        })
    }

  },
  created () {
    // with axios
    const config = {
      headers: {
        'Authorization': 'Bearer ' + localStorage.getItem('token')
      }
    }
    axios.get(this.postURL + '/usuarios', config).then((res) => {
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

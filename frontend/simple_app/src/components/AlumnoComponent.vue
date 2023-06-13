<template>
<div>
    <div class="container">
        <div class="row">
          <div style="margin: 10px">
            <b-button size="sm" @click="crearModal($event.target)" class="mr-2 btn btn-success">
                Crear Alumno
            </b-button>
          </div>
            <b-table id="my-table" :items="alumnos" :per-page="perPage" :current-page="currentPage" :fields="fields">
                <template #cell(opciones)="row">
                    <b-button @click="editarModal(row.item, $event.target)" class="btn btn-primary">
                      Editar Alumno
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
      <b-modal :id="createModal.id" :title="'Crear'" ok-only >
          <div class="modal-content">
            <div class="modal-body">
                 <form v-on:submit='addAlumno'>
                    <div class="input-group mb-3">
                        <select v-model="usuario_seleccionado" >
                             <option v-for="user in users" :key="user.id" v-bind:value="user">
                                {{ user.nombre_usuario }}
                            </option>
                        </select>
                        <span>Seleccionado: {{ usuario_seleccionado.usuario_id }}</span>
                        <span>Nombre: {{ usuario_seleccionado.nombre_usuario }}</span>
                        <span>Dni: {{ usuario_seleccionado.dni_usuario }}</span>
                    </div>
                    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                </form>
            </div>
          </div>
      </b-modal>
      <b-modal :id="updateModal.id" :title="'Actualizar'" ok-only >
          <div class="modal-content">
            <div class="modal-body">
                 <form v-on:submit='updateAlumnos'>
                    <select v-model="usuario_seleccionado" >
                        <option v-for="user in users" :key="user.id" v-bind:value="user">
                            {{ user.nombre_usuario }}
                        </option>
                    </select>
                    <div class="input-group mb-3">
                        <span>Nombre: {{ updateAlumno.nombre }}</span>
                    </div>
                    <div class="input-group mb-3">
                        <span>Dni: {{ updateAlumno.dni }}</span>
                    </div>
                    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
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
      fields: ['alumno_id', 'nombre_alumno', 'alumno_dni', 'opciones'],
      perPage: 2,
      currentPage: 1,
      users: [],
      alumnos: [],
      updateAlumno: {},
      nuevoAlumno: {},
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
      },
      usuario_seleccionado: ''

    }
  },
  computed: {
    rows () {
      return this.alumnos.length
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
    updateAlumnos (e) {
      e.preventDefault()
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
      this.nuevoAlumno.foto = files
      this.updateUser.foto = files
      Vue.set(this.updateUser, 'foto_ruta', window.URL.createObjectURL(files))
    },
    addAlumno (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      var configRequest = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
      let data = {'usuario_id': this.usuario_seleccionado.usuario_id}
      axios.post(this.postURL + '/alumno_create', data, { configRequest })
        .then(res => {
          this.makeToast('success', 'Alumno creado')
          this.usuario_seleccionado = {}
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
          this.alumnos.splice(this.alumnos.indexOf(user), 1)
          console.log(res.data)
          this.makeToast('success', 'Usuario eliminado')
        })
        .catch((error) => {
          console.log(error)
          this.makeToast('danger', 'Hubo un error en el backend')
        })
    },
    editarModal (item, button) {
      Vue.set(this.updateAlumno, 'dni', item.alumno_dni)
      Vue.set(this.updateAlumno, 'nombre', item.nombre_alumno)
      // Vue.set(this.updateAlumno, 'foto_ruta', 'http://localhost:5000/' + item.ruta_foto)
      Vue.set(this.updateAlumno, 'alumno_id', item.alumno_id)

      this.$root.$emit('bv::show::modal', this.updateModal.id, button)
    },
    crearModal (button) {
      axios.get(this.postURL + '/usuarios').then((res) => {
        console.log(res.data)
        this.users = res.data
      })
        .catch((error) => {
          console.log(error)
        })
      this.$root.$emit('bv::show::modal', this.createModal.id, button)
    },
    refresh () {
    // with axios
      axios.get(this.postURL + '/alumnos').then((res) => {
        console.log(res.data)
        this.alumnos = res.data
      })
        .catch((error) => {
          console.log(error)
        })
    }

  },
  created () {
    // with axios
    axios.get(this.postURL + '/alumnos').then((res) => {
      console.log(res.data)
      this.alumnos = res.data
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

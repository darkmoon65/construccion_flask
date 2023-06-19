<template>
    <div>
    <div class="container">
    <div class="row">
    <div style="margin: 10px">
    <b-button size="sm" @click="crearModal($event.target)" class="mr-2 btn btn-success">
        Crear
    </b-button>
    </div>
    <b-table id="my-table" :items="horario" :per-page="perPage" :current-page="currentPage" :fields="fields">
    <template #cell(opciones)="row">
    <b-button @click="editarModal(row.item, $event.target)" class="btn btn-primary">
        Editar
    </b-button>
    <button v-on:click='deleteHorario(row.item)' class="btn btn-danger">Eliminar</button>
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
    <form v-on:submit='addHorarios'>
    <div class="input-group mb-3">
    <label>Fecha de Inicio </label>
    <input type="text" v-model='nuevoUsuario.nombre' class="form-control" placeholder="Nombre" >
    </div>
    <div class="input-group mb-3">
    <label> DNI</label>
    <input type="text" v-model='nuevoUsuario.dni' class="form-control" placeholder="Ingrese Dni">
    </div>
    <div class="input-group mb-3">
    <label>Foto</label>
    <input type="file" v-on:change="onFileChange" class="form-control" placeholder="Foto">
    </div>
    <div class="input-group mb-3">
    <label>Password</label>
    <input type="password" v-model='nuevoUsuario.password' class="form-control" >
    </div>
    <button type="submit" class="btn btn-primary">Guardar Cambios</button>
    </form>

    </div>
    </div>
    </b-modal>
    <b-modal :id="updateModal.id" :title="'Actualizar'" ok-only >
    <div class="modal-content">
    <div class="modal-body">
    <form v-on:submit='updateHorarios'>
    <div class="input-group mb-3">
    <label>Nombre</label>
    <input type="text" v-model='updateHorario.nombre' class="form-control" placeholder="Nombre" >
    </div>
    <div class="input-group mb-3">
    <label>Dni</label>
    <input type="text" v-model='updateHorario.dni' class="form-control" placeholder="Dni">
    </div>
    <div class="input-group mb-3">
    <label>Foto</label>
    <input type="file" v-on:change="onFileChange" class="form-control" placeholder="Foto">
    </div>
    <div class="input-group mb-3">
    <label>Password</label>
    <input type="password" v-model='updateHorario.password' class="form-control" placeholder="Password">
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
export default{
  data () {
    return {
      fields: ['usuario_id', 'dni_usuario', 'nombre_usuario', 'opciones'],
      perPage: 5,
      currentPage: 1,
      horarios: [],
      updateHorario: {},
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
      return this.horarios.length
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
    updateHorarios (e) {
      e.preventDefault()
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      let formUpdate = new FormData()
      formUpdate.append('foto', this.updateHorario.foto)
      formUpdate.append('nombre', this.updateHorario.nombre)
      formUpdate.append('dni', this.updateHorario.dni)
      formUpdate.append('password', this.updateHorario.password)
      formUpdate.append('usuario_id', this.updateHorario.usuario_id)
      axios.post(this.postURL + '/update_usuario', formUpdate, {configRequest}).then((res) => {
        this.makeToast('success', 'Usuario actualizado')
        this.updateHorario = {}
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
      this.updateHorario.foto = files
    },
    addHorario (e) {
      e.preventDefault() // cancela el comportamiento por defecto, en este caso evitar que se vuelva a cargar la pagina luego del submit
      var configRequest = {
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'
      }
      var formData = new FormData()
      formData.append('foto', this.nuevoUsuario.foto)
      formData.append('nombre', this.nuevoUsuario.nombre)
      formData.append('dni', this.nuevoUsuario.dni)
      formData.append('password', this.nuevoUsuario.password)

      axios.post(this.postURL + '/horario_create', formData, { configRequest })
        .then(res => {
          this.makeToast('success', 'Horario creado')
          this.nuevoHorario = {}
          this.refresh()
          this.$root.$emit('bv::hide::modal', this.createModal.id)
        })
        .catch((error) => {
          console.log(error)
          this.makeToast('danger', 'Hubo un error en el backend')
        })
    },
    deleteHorario (horario) {
      var configRequest = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
      axios.post(this.postURL + '/delete_horario', {horario_id: horario.horario_id}, { configRequest })
        .then(res => {
          this.horarios.splice(this.horarios.indexOf(horario), 1)
          console.log(res.data)
          this.makeToast('success', 'Horario eliminado')
        })
        .catch((error) => {
          console.log(error)
          this.makeToast('danger', 'Hubo un error en el backend')
        })
    },
    editarModal (item, button) {
      this.updateHorario.horario_id = item.horario_id
      this.$root.$emit('bv::show::modal', this.updateModal.id, button)
    },
    crearModal (button) {
      this.$root.$emit('bv::show::modal', this.createModal.id, button)
    },
    refresh () {
    // with axios
      axios.get(this.postURL + '/horario').then((res) => {
        console.log(res.data)
        this.horario = res.data
      })
        .catch((error) => {
          console.log(error)
        })
    }

  },
  created () {
    // with axios
    axios.get(this.postURL + '/horario').then((res) => {
      console.log(res.data)
      this.horario = res.data
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

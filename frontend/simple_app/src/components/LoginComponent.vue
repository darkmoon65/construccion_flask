<template>
    <div class='simple_component'>
        <div class='logo'>
            <b-avatar src="https://placekitten.com/300/300" size="8rem"></b-avatar>
        </div>
        <div class="inputs">
        <div class="mt-2" style="font-weight: 600; align-content:center;">Ingresa tu correo:</div>
            <b-form-input v-model="dni" type="email" debounce="500"></b-form-input>
            <div class="mt-2" style="font-weight: 600">Ingresa tu contraseña:</div>
            <b-form-input v-model="password" type="password" debounce="500"></b-form-input>
        </div >
        <div class="send">
            <br>
            <b-button variant="primary" v-on:click="login()">Login</b-button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default{
  data () {
    return {
      dni: '',
      password: '',
      postURL: 'http://127.0.0.1:5000'
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
    login () {
      var configRequest = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
      axios.post(this.postURL + '/login', {dni: this.dni, password: this.password}, { configRequest })
        .then(res => {
          console.log(res.data)
          localStorage.setItem('token', res.data.token)
          localStorage.setItem('typeUser', 'administrador')
          this.$router.push('/')
        })
        .catch((error) => {
          console.log(error)
          this.makeToast('danger', 'Usuario o contraseña no validos')
        })
    }
  }
}
</script>

    <style>
        .simple_component{
            display: flex;
            align-items: center;
            justify-content: center;
            padding-left: 43%;
            padding-top: 6%;
        }
        .logo{
            padding-left: 11%;
        }
        .send{
            padding-left: 16%;
        }
        .inputs{
            width: 300px;
        }
    </style>

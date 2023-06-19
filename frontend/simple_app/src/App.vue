<template>
  <div id="app">
    <nav class="navbar navbar-dark bg-dark fixed-top">
        <button id="openNav" class="btn btn-dark" v-on:click='change()'>
            <span class="navbar-toggler-icon"></span>
        </button>
    </nav>
  <div>
    <div id="menuId" style="display:none ;z-index: 999;position: fixed; background-color: #111827; color: white; height: 93%; top: 7%; overflow-y: auto;" >
        <div class="sidebar-sticky pt-3">
            <ul class="nav flex-column">
                    <li class="nav-item p-2">
                        <div class="text-center">
                            <img src="./assets/perfil.png" style="height:70px; border-radius: 40px;" />
                            <label class="nav-link">Usuario 1</label>
                        </div>

                        <hr />
                    </li>

                    <li class="nav-item">
                        <router-link to='/' class="nav-link">
                            <div class="row align-items-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">home</i>
                                <span class="col-md-9">Inicio </span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to='/justificaciones' class="nav-link">
                            <div class="row align-items-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">sort</i>
                                <span class="col-md-9">Justificacion</span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item">
                       <router-link to='/horarios' class="nav-link">
                            <div class="row align-items-md-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">timer</i>
                                <span class="col-md-9">Horario</span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item">
                      <router-link to='/asistencias' class="nav-link">
                            <div class="row align-items-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">equalizer</i>
                                <span class="col-md-9">Asistencia</span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to='/usuarios' class="nav-link">
                            <div class="row align-items-md-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">group</i>
                                <span class="col-md-10">Usuarios</span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to='/alumnos' class="nav-link">
                            <div class="row align-items-md-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">group</i>
                                <span class="col-md-10">Alumnos</span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">
                            <div class="row align-items-center">
                                <i class="Tiny material-icons col-md-2" aria-hidden="true">exit_to_app</i>
                                <span class="col-md-9">Salir</span>
                            </div>
                        </a>
                    </li>

            </ul>
        </div>
    </div>
    <router-view id="main" style="margin-left: 0%; display: block ; margin-top: 5%; overflow-y: auto;"/>
  </div>

  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      estado: true
    }
  },

  methods: {
    change () {
      if (this.estado === true) {
        document.getElementById('main').style.marginLeft = '20%'
        document.getElementById('main').style.marginTop = '5%'
        document.getElementById('main').style.width = '100%'
        document.getElementById('menuId').style.width = '20%'
        document.getElementById('menuId').style.display = 'block'
        this.estado = false
      } else {
        document.getElementById('main').style.marginLeft = '0%'
        document.getElementById('main').style.width = '100%'
        document.getElementById('menuId').style.display = 'none'
        this.estado = true
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#itemsEstado {
            display:flex;
            align-items: center;
            justify-content: center;
        }
        #leyenda{
            background-color: rgb(250, 255, 236);
            border-radius: 10px;
        }
        #menuId::-webkit-scrollbar {
            width: 8px;
            height: 100%;
        }

        #menuId::-webkit-scrollbar-thumb {
            background: rgb(61, 61, 61);
            border-radius: 4px;
        }

        #menuId::-webkit-scrollbar-thumb:hover {
            background: #1b1a1a;
            box-shadow: 0 0 2px 1px rgba(0, 0, 0, 0.2);
        }

        #menuId::-webkit-scrollbar-thumb:active {
            background-color: #1b1136;
        }

        a:hover {
            background-color: #ffffff25;
            color: white;
            opacity: 1;
        }
        a{
            color: white;
            opacity: 0.8;
        }
        body {
            background: #f1f5f9;
        }

        #cal {

            margin:50px auto;
            font: 13px/1.5 "Helvetica Neue", Helvatica, Arial, san-serif;
            display:table;
        }

        #cal table {
            background:#fff;
            border-collapse:collapse;
        }
        #cal td {
            color:#2b2b2b;
            width:30px;
            height:30px;
            line-height:30px;
            text-align:center;
            border:1px solid #e6e6e6;
            cursor:default;
        }
        #cal #days td {
            height:26px;
            line-height: 26px;
            font-size:90%;
            color:#9e9e9e;
        }
        #cal #days td:not(:last-child) {
            border-right:1px solid #fff;
        }
        #cal #cal-frame .nil{
            background:#fa6161;
        }
        #cal #cal-frame .hecho{
            background:#ffb25a;
        }
        #cal #cal-frame .actual{
            background:#60ff38;
        }
        #cal #cal-frame .semana{
            width: 90px;
        }
        #cal #days .nilSemana{
            width: 90px;
            border-top: 0px;
            border-left: 0px;
            border-right: 1px solid #e6e6e6;
        }
</style>

<template>
    <div class='simple_component'>
        <div class='logo'>
            <b-avatar src="https://placekitten.com/300/300" size="8rem"></b-avatar>
        </div>
        <div class="inputs">
        <div class="mt-2" style="font-weight: 600; align-content:center;">Ingresa tu correo:</div>
            <b-form-input v-model="value" type="email" debounce="500"></b-form-input>
            <div class="mt-2" style="font-weight: 600">Ingresa tu contraseña:</div>
            <b-form-input v-model="value" type="password" debounce="500"></b-form-input>
        </div >
        <div class="send">
            <br>
            <b-button variant="primary">Login</b-button>
        </div>
    </div>
</template>

<script>
export default{
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

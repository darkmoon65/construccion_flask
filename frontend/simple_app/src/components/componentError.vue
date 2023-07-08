<template>
    <div class='error_component'>
        <div class="message">
            UPS, no tienes acceso
        </div>
        <div ref="animationError" class="lottie-error"></div>
    </div>
</template>

<script>
import lottie from 'lottie-web'

export default{

  mounted () {
    lottie.loadAnimation({
      container: this.$refs.animationError,
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'https://assets9.lottiefiles.com/packages/lf20_fl0aRz.json' // Ruta a tu archivo JSON de animación
    })
  }
}
</script>

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Belanosima:wght@600&display=swap');
        .simple_component{
            display: flex;
            align-items: center;
            justify-content: center;
            padding-left: 43%;
            padding-top: 6%;
        }
        .message {
            font-family: 'Belanosima', sans-serif;
            font-weight: 600;
            font-size: 36px;
            margin-bottom: 20px;
            align-items: center;
        }

        .lottie-error{
            align-items: center;
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

<template>
    <div class='error_component'>
        <div class="message">
            UPS, no tienes accesos.
        </div>
        <div ref="animationContainer" class="lottie-welcome"></div>
    </div>
</template>

<script>
import lottie from 'lottie-web'

export default{

  mounted () {
    lottie.loadAnimation({
      container: this.$refs.animationContainer,
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'https://assets6.lottiefiles.com/private_files/lf30_TBKozE.json' // Ruta a tu archivo JSON de animación
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

        .lottie-welcome{
            align-items: center;
        }
        .error_component {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .message {
            font-weight: bold;
            font-size: 36px;
            margin-bottom: 20px;
            font-family: 'Belanosima', sans-serif;
        }
        .send{
            padding-left: 16%;
        }
        .inputs{
            width: 300px;
        }
    </style>

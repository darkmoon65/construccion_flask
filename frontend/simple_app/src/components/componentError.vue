<template>
    <div class='simple_component'>
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
        .simple_component{
            display: flex;
            align-items: center;
            justify-content: center;
            padding-left: 43%;
            padding-top: 6%;
        }

        .lottie-error{
            width: 300px;
            height: 300px;
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

<template>
  <div id="app" class="uk-container uk-container-center uk-text-center uk-margin-large-top">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <a href="https://t.me/vodiybozor">Telegram</a>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'VodiyBozor'
    }
  }
}
</script>

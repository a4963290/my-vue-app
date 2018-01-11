<template>
<div class="container-fluid app">
  <my-menu></my-menu>
  <router-view></router-view>
</div>
</template>

<script>
  import MyMenu from './components/MyMenu.vue'
	export default {
		data() {
      return {
        msg: 'Hello Vue!'
      }
		},
    components:{
      MyMenu
    }
	}
</script>

<style>
body {
  margin-top: 15px;
}
.jumbotron h1, h2 {
  color: #FF5A5F;
}
.app,
.app__body {
  padding-right: 0;
  padding-left: 0;
}
.app {
  width: 940px;
}
.app .app__navbar {
  background: #fff;
  border: 0;
}
</style>

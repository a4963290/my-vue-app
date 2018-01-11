<template>
  <div class="container-fluid">
    <div class="jumbotron">
      <button v-on:click="conn">conn</button>
      <button v-on:click="disconn">disconn</button>
    </div>
    <p v-for="item in msg">
      {{item}}
    </p>
  </div>
</template>
<script>
  import io from 'socket.io-client'
  export default {
    data() {
      return {
        socket:null,
        msg:['Hello Vue!']
      }
		},
    methods:{
      conn:function (event) {
        var self = this;
        if(this.socket!=null){
          this.socket.emit('disconnect_request')
        }
        this.socket = io.connect('http://127.0.0.1:8080/test');
        this.socket.on('connect',function () {
          self.socket.emit('my_event', {data: 'I\'m connected!'});
        });
        this.socket.on('my_response', function(msg) {
          self.msg.push('Received #'+msg.count+':'+ msg.data)
        });
      },
      disconn:function () {
        if(this.socket!=null){
          this.socket.emit('disconnect_request')
        }
      }
    }
  }
</script>


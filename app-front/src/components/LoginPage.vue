<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label>Username:</label>
          <input type="text" v-model="username">
        </div>
        <div>
          <label>Password:</label>
          <input type="password" v-model="password">
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        axios.post('http://localhost:7000/login', {
          username: this.username,
          password: this.password,
        }).then(response => {
          localStorage.setItem('access_token', response.data.access_token);
          console.log(response.data.access_token)
          this.$router.push('/home');
        }).catch(error => {
          console.error(error);
        });
      },
    },
  };
  </script>
  
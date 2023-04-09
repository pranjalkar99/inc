<template>

  <nav class="navbar navbar-expand-lg navbar-light bg-dark mb-3">
  <div class="container">
    <div class="logo">
      <img src = "../assets/icons8-helo-48.png" alt=""/>

    <router-link class="navbar-brand" v-if="!accessToken" to="/" ><span class="text-white">Zwitter</span></router-link>
    <router-link class="navbar-brand" v-if="accessToken" to="/home"><span class="text-white">Zwitter</span></router-link>
    </div>
    <div v-if="!accessToken" class="startup nav navbar-nav flex-row float-right">
      <v-btn class="sign-in-btn btn btn-outline-secondary" color="primary"  @click="$router.push('/')" ><span class="text-white">LogIn</span></v-btn>
      <v-btn class="log-in-btn btn btn-outline-primary" color="secondary" @click="$router.push('/signup')" ><span class="text-white">Sign Up</span></v-btn>
    </div>
    
    
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" v-if="accessToken" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <router-link v-if="accessToken" class="nav-link active btn btn-secondary btn-lg active mx-1" aria-current="page" to="/profile">Profile</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link btn btn-info mx-1" aria-current="page" to="/followers">Followers</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link btn btn-warning btn-lg active mx-1" to="/create">Create Post</router-link>
        </li>
        <li class="nav-item">

            <button class="nav-link btn btn-outline-danger mx-2" @click="logout"><span class="text-white">Logout</span></button>
        </li>
        
       
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search to connect.." aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

</template>

<style>
.sign-in-btn {
  margin-right: 8px;
  font-size: 14px;
}

.log-in-btn {
  margin-left: 8px;
  font-size: 14px;
}
</style>

<script>
export default {
  data() {
    return {
      accessToken: null
    }
  },
  mounted() {
    this.accessToken = localStorage.getItem('access_token')
  },
  beforeCreate() {
    this.accessToken = localStorage.getItem('access_token')
  },
  beforeMount(){
    this.accessToken = localStorage.getItem('access_token');
  },
  methods:{
    logout() {
      localStorage.removeItem("access_token");
      this.$router.push("/");
    }
  }

  }

</script>
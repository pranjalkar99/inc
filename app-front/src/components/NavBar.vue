<template>

  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container">
    <img src = "app-front\public\dog-solid.svg" alt="My Happy SVG"/>
    <router-link class="navbar-brand" to="/">Zwitter</router-link>
    
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <router-link class="nav-link active" aria-current="page" to="/profile">Profile</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link active" aria-current="page" to="/followers">Followers</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/create">Create Link</router-link>
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
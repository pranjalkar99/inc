<template>
  <div id="app">
    <Navbar />
    <!-- <MainPage/> -->
    <!-- <ListFollowers/> -->
    <router-view />

  </div>
</template>

<script>
import Navbar from "./components/NavBar.vue";
// import MainPage from "./components/MainPage.vue";
// import ListFollowers from "./components/ListFollowers.vue";

export default {
  name: "App",
  components: {
    Navbar,
    // MainPage,
    // ListFollowers,
  },
};
</script>



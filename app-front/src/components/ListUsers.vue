<template>

    <div class="container">
      <input v-model="searchTerm" class="float-end" type="text" placeholder="Search for more users..." />
      <br>
      <h5 style="text-align: center;">List All Users</h5>
      <div v-for="user in users[0]" :key="user.id" class="user-card">
        <img src="../assets/icons8-helo-48.png" alt="User Avatar" />
        <h3>{{ user.username }}</h3>
        <p>{{ user.id  }}</p>
        <!-- <p>{{ user.handle_id }}</p> -->
        <button class="float-end mx-3" @click="followUser(user.id)">Follow</button>
      </div>
    </div>

</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      searchTerm: "",
      users: []
    };
  },
  mounted() {
    const token = localStorage.getItem("access_token");
    if (token) {
      axios
        .get("http://localhost:7000/list-all-users", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((response) => {
          this.users = response.data;
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  methods: {
    unfollowUser(id) {
      this.users = this.users.filter((user) => user.id !== id);
    },
    followUser(followed_id) {
        console.log("this is working")
        axios.get(`http://localhost:7000/link-follower/${this.users[1]}/${followed_id}`).then((response) => {
            console.log(response)
            
        }).catch((error) => {
            console.log(error)
        })
    }
  },
};
</script>

<style>

.user-card {
  display: flex;
   width: 50rem;
  /* margin-left: 10rem;  */
  align-items: center;
  max-width: 93.5rem;
    margin: 0 auto;
    padding: 0 2rem;

  /* padding: 16px; */
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 16px;
}
.container{
    max-width: 93.5rem;
    margin: 0 auto;
    padding: 0 2rem;
}

.user-card img {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  margin-right: 16px;
}

.user-card h2 {
  margin: 0;
}
</style>
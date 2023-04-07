<template>

    <div class="container">
      <input v-model="searchTerm" class="float-end" type="text" placeholder="Search for more users..." />
      <br>
      <h5 style="text-align: center;">Users you follow</h5>
      <div v-for="user in filteredUsers" :key="user.id" class="user-card">
        <img :src="user.image" alt="User Avatar" />
        <h3>{{ user.handle }}</h3>
        <button class="float-end" @click="unfollowUser(user.id)">Unfollow</button>
        <p>Follows you</p>
      </div>
    </div>

</template>

<script>
export default {
  data() {
    return {
      searchTerm: "",
      users: [
        {
          id: 1,
          handle: "user1",
          image: "https://randomuser.me/api/portraits/men/1.jpg",
        },
        {
          id: 2,
          handle: "user2",
          image: "https://randomuser.me/api/portraits/women/2.jpg",
        },
        {
          id: 3,
          handle: "user3",
          image: "https://randomuser.me/api/portraits/men/3.jpg",
        },
        {
          id: 4,
          handle: "user4",
          image: "https://randomuser.me/api/portraits/women/4.jpg",
        },
        {
          id: 5,
          handle: "user5",
          image: "https://randomuser.me/api/portraits/men/5.jpg",
        },
      ],
    };
  },
  computed: {
    filteredUsers() {
      return this.users.filter((user) =>
        user.handle.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    },
  },
  methods: {
    unfollowUser(id) {
      this.users = this.users.filter((user) => user.id !== id);
    },
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
<template>
  <div class="create-post">
    <label for="title" class="create-post__label">Title:</label>
    <input id="title" class="create-post__input" v-model="title" />

    <label for="body" class="create-post__label">body:</label>
    <textarea id="body" class="create-post__input" v-model="body"></textarea>

    <!-- <label for="image-upload" class="create-post__label"
      >Image/File Upload:</label
    > -->
    <div class="create-post__file-upload">
      <input type="file" id="image-upload" @change="handleImageUpload" />
      <span class="create-post__file-upload-label">{{
        image ? image.name : "Choose File"
      }}</span>
    </div>

    <button class="create-post__button" @click="createPost">Post</button>
  </div>
  <!-- <div
    class="alert alert-warning alert-dismissisable fade show mt-4"
    v-if="error"
    role="alert"
  >
    <strong>{{ error }}</strong>
  </div> -->
</template>
  
 





  <script>
import axios from "axios";

export default {
  
  data() {
    return {
      title: "",
      body: "",
      image: null,
      error: null,
      accessToken: null
    };
  },
  mounted() {
    this.accessToken = localStorage.getItem('access_token')
  },
  methods: {
    handleImageUpload(event) {
      this.image = event.target.files[0];
    },
    createPost() {
  if (!this.title || !this.body) {
    this.error = "Please fill up all fields.";
  } else {
    const formData = {
      title: this.title,
      body: this.body,
    };
    const token=localStorage.getItem("access_token");
    axios.put("http://localhost:7000/add_article", formData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((resp) => {
      console.log(resp);
      this.$router.push({
        name: "home",
      });
    })
    .catch((error) => {
      console.log(error);
    });
  }

  // Reset the form after submitting the data
  this.title = "";
  this.body = "";
}
,
  },
};
</script>
  
<style scoped>
.create-post {
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin: auto;
  padding: 24px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.create-post__label {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 8px;
}

.create-post__input {
  height: 40px;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 16px;
}

.create-post__file-upload {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.create-post__file-upload-label {
  margin-left: 16px;
  font-size: 16px;
}

.create-post__button {
  height: 40px;
  padding: 8px 16px;
  font-size: 16px;
  font-weight: bold;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
<!-- <template>
    <div>
      <label for="title">Title:</label>
      <input id="title" v-model="title" />
  
      <label for="body">body:</label>
      <textarea id="body" v-model="body"></textarea>
  
      <label for="image-upload">Image/File Upload:</label>
      <input type="file" id="image-upload" @change="handleImageUpload" />
  
      <button @click="createPost">Post</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        title: "",
        body: "",
        image: null,
      };
    },
    methods: {
      handleImageUpload(event) {
        this.image = event.target.files[0];
      },
      createPost() {
        // Here you can send the data to your backend API to create a new post
        console.log("Creating post...", {
          title: this.title,
          body: this.body,
          image: this.image,
        });
  
        // Reset the form after submitting the data
        this.title = "";
        this.body = "";
        this.image = null;
      },
    },
  };
  </script>
   -->
-Formatted HTML-
 
<template>
  
   <div class="container">
      <nav aria-label="breadcrumb" class="main-breadcrumb">
         <ol class="breadcrumb">
            <li class="breadcrumb-item">
               <router-link to="/">Home</router-link>
            </li>
            <li class="breadcrumb-item active" aria-current="page">User Profile</li>
         </ol>
      </nav>
      <div class="row" style="height: 80vh">
         <div class="col-md-2">
            <div class="card">
               <div class="card-body">
                  <div class="d-flex flex-column align-items-center text-center">
                    
                     <img
                        :src="
                        user.image_link
                        ? user.image_link
                        : 'https://bootdey.com/img/Content/avatar/avatar7.png'
                        "
                        alt="No Photo Available"
                        class="rounded-circle"
                        width="150"
                        />
                     <input
                        type="file"
                        @change="handleFileUpload"
                        ref="fileInput"
                        style="display: none"
                        />
                     <button
                        class="btn btn-primary mt-3"
                        @click="$refs.fileInput.click()"
                        >
                     Upload Image
                     </button>
                  </div>
                  <p class="card-title d-flex justify-content-center">
                     @{{ user.handle }}
                  </p>
                  <h4 class="card-text">{{ user.fullname || "Empty" }}</h4>
               </div>
            </div>
            <div class="my-2 py-2"></div>
            <div class="card">
               <div class="card-body">
                  <div
                     class="d-flex flex-column align-items-center text-center"
                     >
                     <i class="fas fa-user-friends"></i>
                     <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"  viewBox="0 0 640 512"><!-- Font Awesome Pro 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) --><path d="M192 256c61.9 0 112-50.1 112-112S253.9 32 192 32 80 82.1 80 144s50.1 112 112 112zm76.8 32h-8.3c-20.8 10-43.9 16-68.5 16s-47.6-6-68.5-16h-8.3C51.6 288 0 339.6 0 403.2V432c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48v-28.8c0-63.6-51.6-115.2-115.2-115.2zM480 256c53 0 96-43 96-96s-43-96-96-96-96 43-96 96 43 96 96 96zm48 32h-3.8c-13.9 4.8-28.6 8-44.2 8s-30.3-3.2-44.2-8H432c-20.4 0-39.2 5.9-55.7 15.4 24.4 26.3 39.7 61.2 39.7 99.8v38.4c0 2.2-.5 4.3-.6 6.4H592c26.5 0 48-21.5 48-48 0-61.9-50.1-112-112-112z"/></svg>
            <span>Number of followers: 100</span>
            <svg xmlns="http://www.w3.org/2000/svg"  width="40" height="40"  viewBox="0 0 640 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M96 128a128 128 0 1 1 256 0A128 128 0 1 1 96 128zM0 482.3C0 383.8 79.8 304 178.3 304h91.4C368.2 304 448 383.8 448 482.3c0 16.4-13.3 29.7-29.7 29.7H29.7C13.3 512 0 498.7 0 482.3zM504 312V248H440c-13.3 0-24-10.7-24-24s10.7-24 24-24h64V136c0-13.3 10.7-24 24-24s24 10.7 24 24v64h64c13.3 0 24 10.7 24 24s-10.7 24-24 24H552v64c0 13.3-10.7 24-24 24s-24-10.7-24-24z"/></svg>
            <span>Number of users followed by: 50</span>
                  </div>
               </div>
            </div>
         </div>
         <div class="col-md-8">
         <div class="card">
            <div class="card-body">
               <h5 class="card-title">Bio</h5>
               <ul class="list-group list-group-flush">
                  <li
                     class="list-group-item py-4 d-flex justify-content-center px-1"
                     >
                     About:
                     <textarea
                        class="form-control mx-2"
                        :placeholder="user.bio ? user.bio : 'Empty'"
                        ></textarea>
                  </li>
                  <li class="list-group-item" :disabled="!editing">
                     Username: {{ user.username || "Empty" }}
                  </li>
                  <li class="list-group-item">
                     Date of Birth:
                     <VueDatePicker
                        v-model="dob"
                        :disabled="!editing"
                        :placeholder="user.dob ? user.dob : 'Empty'"
                        ></VueDatePicker>
                  </li>
                  <li class="list-group-item">
                     User Number:
                     <input
                        type="text"
                        class="form-control"
                        :placeholder="user.number ? user.number : 'Empty'"
                        name="username"
                        disabled
                        aria-label="number"
                        aria-describedby="basic-addon1"
                        />
                  </li>
                  <li class="list-group-item">
                     Phone Number:
                     <input
                        type="text"
                        name="number"
                        class="form-control"
                        :placeholder="user.phoneNumber ? user.phoneNumber : 'Empty'"
                        :disabled="!editing"
                        aria-label="number"
                        aria-describedby="basic-addon1"
                        />
                  </li>
                  <!-- Add more profile details here -->
               </ul>
               <button
                  class="btn btn-primary mt-3 float-right"
                  @click="updateProfile()"
                  >
               Edit
               </button>
               <button
                  class="btn btn-success mt-3 mx-2 float-right"
                  :disabled="!editing"
                  @click="updatePostProfile()"
                  >
               Update
               </button>
            </div>
         </div>
      </div>
      </div>
      
   </div>
   
  
</template>


<script>
import axios from "axios";
import VueDatePicker from "@vuepic/vue-datepicker";

export default {
  components: { VueDatePicker },
  data() {
    return {
      user: {
        photo: '',
      },
      fileData: null,
      editing: false,
      file: null,
      imageUrl: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.user.photo = reader.result;
      };
      const dpData = new FormData();
      dpData.append("file",   file);
      const token = localStorage.getItem("access_token");
      axios
        .put("http://localhost:7000/update-dp", dpData, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.user = response.data;
          this.editing = false;
        })
        .catch((error) => {
          console.log(error);
        });

    },
    updateProfile() {
      // Add code to update user profile here
      this.editing = true;
    },
    updatePostProfile() {
      // Add code to update user profile here
      this.editing = false;
      const formData = new FormData();
      formData.append("bio", document.querySelector("#bio").value);
      formData.append("dob", document.querySelector("#dob").value);
      formData.append("username", document.querySelector("#username").value);
      formData.append("phoneNumber", document.querySelector("#number").value);
      formData.append("file", this.file);
      const token = localStorage.getItem("access_token");
      axios
        .put("http://localhost:7000/update-profile", formData, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.user = response.data;
          this.editing = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    const token = localStorage.getItem("access_token");
    if (token) {
      axios
        .get("http://localhost:7000/get_profile", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((response) => {
          this.user = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
};
</script>

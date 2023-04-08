<template>
  <div class="signin">
    <h1>Sign Up</h1>
    <form @submit.prevent="signup">
      <div class="form-field">
        <label>Full Name:</label>
        <input type="text" v-model="fullname" />
      </div>
      <div class="form-field">
        <label>Username:</label>
        <input type="text" v-model="username" />
      </div>
      <div class="form-field">
        <label>Password:</label>
        <input type="password" v-model="password" />
        <span class="password-toggle" @click="togglePasswordVisibility">{{
          showPassword ? "Hide" : "Show"
        }}</span>
      </div>
      <div class="form-field">
        <label>Re-enter Password:</label>
        <input type="password" v-model="password2" />
        <span class="password-toggle" @click="togglePasswordVisibility2">{{
          showPassword2 ? "Hide" : "Show"
        }}</span>
      </div>
      <div class="form-field  my-4  py-1"><label>Date of Birth:</label>
        <VueDatePicker v-model="dob"></VueDatePicker>
      </div>
      
        
      
      <div class="submit my-4">
      <v-btn
        class="signin-btn"
        color="primary"
        :disabled="!valid"
        @click="submitForm"
        >Sign Up</v-btn
      ></div>
    </form>
  </div>
</template>
  
  <script>
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import axios from "axios";

export default {
  components: { VueDatePicker },
  data() {
    return {
        
      fullname: "",
      username: "",
      password: "",
      password2: "",
      dob: "",
      image: null,
      showPassword: false,
      showPassword2: false,
      valid: false,
      errors: {
        username: "",
      },
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    
    submitForm() {
      axios
        .post("http://localhost:7000/register", {
          username: this.username,
          password: this.password,
          fullname: this.fullname,
          date_of_birth: this.date_of_birth,
    
        })
        .then((response) => {
          localStorage.setItem("access_token", response.data.access_token);
          console.log(response.data.access_token);
          this.$router.push("/home");
        })
        .catch((error) => {
          console.error(error);
        });
    },
    togglePasswordVisibility2() {
      this.showPassword2 = !this.showPassword2;
    },
    
  },
};
</script>
  
  <style>
.signin {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

.form-field {
  margin: 10px 0;
}

label {
  font-size: 1.1rem;
  margin-right: 10px;
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  border: none;
  border-radius: 5px;
  box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
  font-size: 1.1rem;
  width: 300px;
}

input[type="file"] {
  padding: 10px;
}

.signin-btn {
  padding: 10px 30px;
  margin-top: 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.2rem;
  font-weight: bold;
  cursor: pointer;
}

.password-toggle {
  margin-left: 10px;
  color: #4caf50;
  font-size: 0.9rem;
  cursor: pointer;
}
</style>
  
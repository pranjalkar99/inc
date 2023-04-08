<template>
    <div class="signin">
      <h1>Sign Up</h1>
      <v-form v-model="valid" ref="form">
        <v-text-field v-model="fullname" :rules="[rules.required]" label="Full Name"></v-text-field>
        <v-text-field v-model="username" :rules="[rules.required, rules.usernameExists]" :error-messages="errors.username" label="Username"></v-text-field>
        <v-text-field v-model="password" :rules="[rules.required]" :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'" :type="showPassword ? 'text' : 'password'" @click:append="showPassword = !showPassword" label="Password"></v-text-field>
        <v-text-field v-model="password2" :rules="[rules.required, rules.passwordMatch]" :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'" :type="showPassword2 ? 'text' : 'password'" @click:append="showPassword2 = !showPassword2" label="Re-enter Password"></v-text-field>
        <v-date-picker v-model="dob" :rules="[rules.required]" label="Date of Birth"></v-date-picker>
        <v-file-input v-model="image" :rules="[rules.image]" label="Upload Image"></v-file-input>
        <v-btn class="signin-btn" color="primary" :disabled="!valid" @click="submitForm">Sign Up</v-btn>
      </v-form>
    </div>
  </template>
  
  <style>
  .signin {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .signin-btn {
    margin-top: 20px;
    width: 100%;
  }
  </style>
  
  <script>
  import axios from "axios";
export default {
  data() {
    return {
      fullname: '',
      username: '',
      password: '',
      password2: '',
      dob: '',
      image: null,
      showPassword: false,
      showPassword2: false,
      valid: false,
      errors: {
        username: ''
      }
    }
  },
  methods: {
    async checkUsernameExists() {
      try {
        const response = await axios.get(`/api/check-username-exists?username=${this.username}`);
        this.errors.username = response.data.exists ? 'This username is already taken' : '';
      } catch (error) {
        console.log(error);
        this.errors.username = 'Error checking username, please try again';
      }
    },
    async submitForm() {
      // Upload image if selected
      let image_url = '';
      if (this.image) {
        const formData = new FormData();
        formData.append('image', this.image);
        try {
          const response = await axios.post('/api/upload-image', formData);
          image_url = response.data.image_url;
        } catch (error) {
          console.log(error);
        }
      }

      // Submit form data
      try {
        const response = await axios.post('/api/signup', {
          fullname: this.fullname,
          username: this.username,
          password: this.password,
          dob: this.dob,
          image_url: image_url
        });
        console.log(response)
        // Redirect to home page or show success message
        this.$router.push('/');
        alert('Sign up successful!');
      } catch (error) {
        console.log(error);
        alert('Error signing up, please try again');
      }
    }
  },
  watch: {
    username: function() {
      this.checkUsernameExists();
    }
  },
  created() {
    this.$validator.localize('en', this.customMessages);
  },
  computed: {
    customMessages() {
      return {
        required: 'This field is required',
        email: 'Please enter a valid email address',
        passwordMatch: 'Passwords do not match',
        image: 'Please select a valid image file',
        usernameExists: this.errors.username
      }
    },
    rules() {
      return {
        required: (value) => !!value || 'This field is required',
        email: (value) => {
          if (!value) return true;
          const pattern = /^[\w-.]+@([\w-]+\.)+[\w-]{2,}$/;
          return pattern.test(value) || 'Please enter a valid email address';
        },
        passwordMatch: (value) => {
          if (value === this.password) return true;
          return 'Passwords do not match';
        },
        image: (value) => {
          if (!value) return true;
          const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
          return allowedTypes.includes(value.type) || 'Please select a valid image file';
        },
        usernameExists: async (value) => {
          if (!value) return true;
          try {
            const response = await axios.get(`/api/check-username-exists?username=${value}`);
            return !response.data.exists;
          } catch (error) {
            console.log(error);
            return false;
          }
        }
      }
    }
  }
}
</script>

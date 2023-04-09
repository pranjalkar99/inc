<!-- eslint-disable vue/no-duplicate-attributes -->
<!-- <template>
  <div class="signin">
    <div class="form-field">
      <label>Full Name:</label>
      <input type="text" v-model="fullname" required />
      <div v-if="$v.fullname.$error">
        <span v-if="!$v.fullname.required">Full name is required</span>
      </div>
    </div>
    <div class="form-field">
      <label>Username:</label>
      <input type="text" v-model="username" required />
      <div v-if="$v.username.$error">
        <span v-if="!$v.username.required">Username is required</span>
      </div>
    </div>
    <div class="form-field">
      <label>Password:</label>
      <input
        type="password"
        v-model="password"
        :type="showPassword ? 'text' : 'password'"
        required
        :minlength="8"
      />
      <span
        class="password-toggle"
        @click="togglePasswordVisibility"
        >{{ showPassword ? "Hide" : "Show" }}</span
      >
      <div v-if="$v.password.$error">
        <span v-if="!$v.password.required">Password is required</span>
        <span v-if="!$v.password.minLength">
          Password must be at least 8 characters long
        </span>
      </div>
    </div>
    <div class="form-field">
      <label>Confirm Password:</label>
      <input
        type="password"
        v-model="password2"
        :type="showPassword2 ? 'text' : 'password'"
        required
        :minlength="8"
        v-validate="{ sameAsPassword: password }"
      />
      <span
        class="password-toggle"
        @click="togglePasswordVisibility2"
        >{{ showPassword2 ? "Hide" : "Show" }}</span
      >
      <div v-if="$v.password2.$error">
        <span v-if="!$v.password2.required">Confirm password is required</span>
        <span v-if="!$v.password2.minLength">
          Confirm password must be at least 8 characters long
        </span>
        <span v-if="!$v.password2.sameAsPassword">
          Confirm password must match the password
        </span>
      </div>
    </div>
    <div class="form-field">
      <label>Date of Birth:</label>
      <vue-date-picker v-model="dob" required />
      <div v-if="$v.dob.$error">
        <span v-if="!$v.dob.required">Date of birth is required</span>
      </div>
    </div>
    <div class="form-field">
      <label>Profile Picture:</label>
      <input type="file" v-model="image" />
    </div>
    <button class="signin-btn" @click="submitForm">Sign Up</button>
  </div>
</template> -->

<template>
  <div class="signin">
    <h1>Sign Up</h1>
    <div class="form-field">
      <label for="fullname">Full Name:</label>
      <input type="text" id="fullname" v-model="fullname">
    </div>
    <div class="form-field">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username">
      <span v-if="errors.username" class="error">{{ errors.username }}</span>
    </div>
    <div class="form-field">
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password">
      <span class="password-toggle" v-on:click="togglePasswordVisibility">
        {{ showPassword ? 'Hide' : 'Show' }}
      </span>
    </div>
    <div class="form-field">
      <label for="password2">Confirm Password:</label>
      <input type="password" id="password2" v-model="password2">
      <span class="password-toggle" v-on:click="togglePasswordVisibility2">
        {{ showPassword2 ? 'Hide' : 'Show' }}
      </span>
    </div>
    <div class="form-field">
      <label for="dob">Date of Birth:</label>
      <vue-date-picker id="dob" v-model="dob"></vue-date-picker>
    </div>
    <div class="form-field">
      <label for="image">Profile Picture:</label>
      <input type="file" id="image" v-on:change="onFileChange">
    </div>
    <button class="signin-btn" v-on:click="submitForm">Sign Up</button>
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
      const formData = new FormData();
      formData.append("username", this.username);
      formData.append("password", this.password);
      formData.append("fullname", this.fullname);
      formData.append("date_of_birth", this.dob);
      formData.append("image", this.image);
    
      axios
        .post("http://localhost:7000/register", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
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
    
    onFileChange(event) {
      this.image = event.target.files[0];
    },
    
    togglePasswordVisibility2() {
      this.showPassword2 = !this.showPassword2;
    },
  },
};
</script>

<!-- <script>
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
        fullname: "",
        username: "",
        password: "",
        password2: "",
        dob: "",
        image: "",
      },
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    submitForm() {
      if (this.validateForm()) {
        const formData = new FormData();
        formData.append("fullname", this.fullname);
        formData.append("username", this.username);
        formData.append("password", this.password);
        formData.append("date_of_birth", this.dob);
        formData.append("image", this.image);

        axios
          .post("http://localhost:7000/register", formData)
          .then((response) => {
            localStorage.setItem("access_token", response.data.access_token);
            console.log(response.data.access_token);
            this.$router.push("/home");
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    togglePasswordVisibility2() {
      this.showPassword2 = !this.showPassword2;
    },
    validateForm() {
      let isValid = true;
      if (!this.fullname.trim()) {
        this.errors.fullname = "Full Name is required";
        isValid = false;
      } else {
        this.errors.fullname = "";
      }
      if (!this.username.trim()) {
        this.errors.username = "Username is required";
        isValid = false;
      } else {
        this.errors.username = "";
      }
      if (!this.password.trim()) {
        this.errors.password = "Password is required";
        isValid = false;
      } else if (this.password.trim().length < 8) {
        this.errors.password = "Password must be at least 8 characters long";
        isValid = false;
      } else {
        this.errors.password = "";
      }
      if (!this.password2.trim()) {
        this.errors.password2 = "Confirm Password is required";
        isValid = false;
      } else if (this.password.trim() !== this.password2.trim()) {
        this.errors.password2 = "Passwords do not match";
        isValid = false;
      } else {
        this.errors.password2 = "";
      }
      if (!this.dob) {
        this.errors.dob = "Date of Birth is required";
        isValid = false;
      } else {
        this.errors.dob = "";
      }
      if (this.image && !this.isValidImageFile(this.image)) {
        this.errors.image = "Invalid Image File";
        isValid = false;
      } else {
        this.errors.image = "";
      }
      return isValid;
    },
    isValidImageFile(file) {
      const allowedExtensions = ["jpg", "jpeg", "png"];
      const extension = file.name.split(".").pop().toLowerCase();
      return allowedExtensions.includes(extension);
    },
  },
};
</script>
   -->
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
  
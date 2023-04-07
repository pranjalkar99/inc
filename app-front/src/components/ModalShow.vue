<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">
        <div class="modal-header">
          <h3>Edit Profile</h3>
          <br>
          <button class="modal-default-button" @click="$emit('close')">
            X Cancel
          </button>
        </div>
        <div class="modal-body">
          <form>
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="name" />
       
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" />
            <button type="submit">Save</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      required: true,
    },
    user: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      name: this.user.name,
      email: this.user.email,
    };
  },
  methods: {
    saveChanges() {
      // Save changes to user profile
      this.$emit('save', {
        name: this.name,
        email: this.email,
      });
    },
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}
</style>

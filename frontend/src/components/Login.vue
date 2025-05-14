<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <form v-on:submit.prevent="setLogin" class="bg-white p-8 rounded-lg shadow-lg w-full max-w-sm">
      <h2 class="text-2xl font-semibold text-center mb-6">Login</h2>
      
      <div class="mb-4">
        <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
        <input
          id="username"
          type="text"
          v-model="username"
          required
          class="mt-1 p-3 w-full border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
        />
      </div>
      
      <div class="mb-6">
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input
          id="password"
          type="password"
          v-model="password"
          required
          class="mt-1 p-3 w-full border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
        />
      </div>
      
      <button
        type="submit"
        class="w-full py-3 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
      >
        Login
      </button>
    </form>
  </div>
  
  <p class="text-center mt-6 text-gray-700">{{ username }}</p>
  <p class="text-center text-gray-700">{{ password }}</p>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    setLogin() {
      axios
        .post('http://localhost:5000/api/login', {
          username: this.username,
          password: this.password,
        },{
          withCredentials: true
        })
        .then((response) => {
          console.log('Übertragung erfolgreich', response.data);

          this.$router.push('/dashboard');
        })
        .catch((error) => {
          console.error('Login fehlgeschlagen:', error.response?.data || error.message);
        });
    },
  },
};
</script>


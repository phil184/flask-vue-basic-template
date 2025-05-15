<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Sidebar -->
    <div class="w-64 bg-indigo-700 text-white p-6 space-y-8">
      <h2 class="text-2xl font-semibold text-center">{{ username }}</h2>
      
      <!-- Navigation Links -->
      <nav>
        <ul class="space-y-4">
          <li>
            <a href="#" class="block px-4 py-2 rounded-md text-gray-200 hover:bg-indigo-600">
              Dashboard
            </a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 rounded-md text-gray-200 hover:bg-indigo-600">
              Users
            </a>
          </li>
        </ul>
      </nav>
    </div>
    
    <!-- Main Content -->
    <div class="flex-1 p-8">
      <!-- Header -->
      <header class="flex items-center justify-between mb-8">
        <h1 class="text-3xl font-semibold text-gray-800">Dashboard</h1>
        <div class="flex items-center space-x-4">
          <button class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700" @click="logout">Logout</button>
        </div>
      </header>
      
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <!-- Card 1 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Card 1</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">9999</p>
        </div>
        
        <!-- Card 2 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Card 2</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">9999</p>
        </div>

        <!-- Card 3 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Card 3</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">9999</p>
        </div>

        <!-- Card 4 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Card 4</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">9999</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
    };
  },

  created() {
    axios.get('http://localhost:5000/api/auth', { withCredentials: true })
      .then((res) => {
        this.username = res.data.username;
        console.log("Angemeldet als:", this.username);
      })
      .catch((err) => {
        console.error('Nicht authentifiziert:', err);
        this.$router.push('/login');
      });
  },

  methods: {
    logout() {
      const path = 'http://localhost:5000/api/logout';
      axios.get(path, { withCredentials: true })
        .then((res) => {
          console.log("Logout", res.data)
          this.$router.push('/login');
        })
        .catch((error) => {

          console.error(error);
        });
    },
    
  },

    

     
};
</script>


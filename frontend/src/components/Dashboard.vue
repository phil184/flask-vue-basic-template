<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Sidebar -->
    <div class="w-64 bg-indigo-700 text-white p-6 space-y-8">
      <h2 class="text-2xl font-semibold text-center">Admin</h2>
      
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
          <li>
            <a href="#" class="block px-4 py-2 rounded-md text-gray-200 hover:bg-indigo-600">
              Settings
            </a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 rounded-md text-gray-200 hover:bg-indigo-600">
              Reports
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
          <div class="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center">
            <span class="text-gray-700 font-semibold">A</span>
          </div>
        </div>
      </header>
      
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <!-- Card 1 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Total Users</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">1,250</p>
        </div>
        
        <!-- Card 2 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">New Orders</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">450</p>
        </div>

        <!-- Card 3 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Revenue</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">$12,500</p>
        </div>

        <!-- Card 4 -->
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <h3 class="text-xl font-semibold text-gray-700">Pending Tasks</h3>
          <p class="text-3xl font-bold text-indigo-600 mt-2">35</p>
        </div>
      </div>
      
      <!-- Recent Activity -->
      <div class="bg-white p-6 rounded-lg shadow-lg mt-8">
        <h2 class="text-2xl font-semibold text-gray-800 mb-6">Recent Activity</h2>
        
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <div class="text-gray-600">John Doe commented on your post</div>
            <span class="text-sm text-gray-400">2 hours ago</span>
          </div>
          <div class="flex items-center justify-between">
            <div class="text-gray-600">Alice created a new order</div>
            <span class="text-sm text-gray-400">4 hours ago</span>
          </div>
          <div class="flex items-center justify-between">
            <div class="text-gray-600">David updated his profile</div>
            <span class="text-sm text-gray-400">6 hours ago</span>
          </div>
          <div class="flex items-center justify-between">
            <div class="text-gray-600">Mark added a new product</div>
            <span class="text-sm text-gray-400">1 day ago</span>
          </div>
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
      
    };
  },
  mounted() {
    axios
      .get('http://localhost:5000/api/dashboard', { withCredentials: true })
      .then((res) => {
        console.log("Welcome!", res.data);
      })
      .catch((err) => {
        console.error('Err:', err.response?.data || err.message);
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


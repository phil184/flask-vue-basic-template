import { createRouter, createWebHistory } from 'vue-router'
import ApiTest from '../components/ApiTest.vue'
import Login from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'
import axios from 'axios';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ApiTest',
      component: ApiTest,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,

    },

    {
    path: '/dashboard',
    component: Dashboard,
    beforeEnter: async () => {
      try {
        const res = await axios.get('http://localhost:5000/api/auth', {
          withCredentials: true,
        });

        if (res.status === 200) {
          return true; 
        } else {
          return { path: '/login' };
        }
      } catch (err) {
        return { path: '/login' };
      }
    }
  },
      
  ]
})

export default router
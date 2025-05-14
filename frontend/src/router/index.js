import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Login from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,

    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,

    },
      
  ]
})

export default router
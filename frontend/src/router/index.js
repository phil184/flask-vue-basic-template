import { createRouter, createWebHistory } from 'vue-router'
import ApiTest from '../components/ApiTest.vue'
import Login from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'

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
      name: 'dashboard',
      component: Dashboard,

    },
      
  ]
})

export default router
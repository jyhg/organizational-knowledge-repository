import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/chat',
    },
    {
      path: '/chat',
      name: 'chat',
      component: () => import('../views/ChatView.vue'),
    },
    {
      path: '/docs',
      name: 'docs',
      component: () => import('../views/DocsManage.vue'),
    },
    {
      path: '/eval',
      name: 'eval',
      component: () => import('../views/EvalDashboard.vue'),
    },
  ],
})

export default router

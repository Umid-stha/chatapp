import Vue from 'vue'
import Router from 'vue-router'
import Chat from '@/components/Chat'
import Auth from '@/components/UserAuth'


Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/chats',
      name: 'Chat',
      component: Chat
    },
    {
      path:'/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path:'/chats/:uri?',
      name: 'Chat',
      component: Chat
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next()
  }
  else {
    next('/auth')
  }
})

export default router
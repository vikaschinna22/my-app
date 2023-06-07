import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'
import PersonImagesPage from "@/pages/PersonImagesPage.vue"
import AlbumsCreate from'@/pages/createA.vue'
import AlbumImagesPage from'@/pages/AlbumImagesPage.vue';
import SearchPage from '@/pages/SearchPage'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/search',
    name: 'search',
    component: SearchPage
  },
  {
    path:'/person/:pid',
    name:"person",
    component:PersonImagesPage
  }
  ,
  {
    path:'/AlbumCreate',
    name:"album",
    component:AlbumsCreate

  },
  {
    path:'/Album/:aid',
    name:'albumname',
    component:AlbumImagesPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

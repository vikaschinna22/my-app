import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '@/components/HelloWorld.vue'
import PersonImages from "@/components/PeopleComp/PersonImages.vue"
import AlbumsCreate from'@/components/AlbumComponenets/createA.vue'
import AlbumView from'@/components/AlbumComponenets/AlbumView.vue';
const routes = [
  {
    path: '/',
    name: 'home',
    component: HelloWorld
  },
  {
    path: '/search',
    name: 'search',
    component: () => import( '../views/SearchView.vue')
  },
  {
    path:'/person/:pid',
    name:"person",
    component:PersonImages
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
    component:AlbumView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

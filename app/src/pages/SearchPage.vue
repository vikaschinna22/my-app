<template>
  <div class="about" >
    <PeopleMenu :imgs="clusters"/>
    <AlbumMenu :albumname="albumname"/>
  </div>
</template>
<script>
import PeopleMenu from '@/components/PeopleMenu.vue';
import AlbumMenu from '@/components/AlbumMenu.vue'
import { usePhotoStore } from '@/store/PhotoStore';
import { storeToRefs } from 'pinia';

export default{
  setup(){
    const photoStore = usePhotoStore()
    return {photoStore}
  },
  data(){
    const {clusters,albumname}=storeToRefs(this.photoStore)
    return {
      clusters,
      albumname
    }
  },
  components:{
    PeopleMenu,
    AlbumMenu
  }
}
</script>
<style scoped>
.about{
  margin-top: 50px;
}
</style>
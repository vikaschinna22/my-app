<template>
  <div class="gallery" >
    <ImageComponent :Imgsrc="s" v-for="s,i in allphotos" v-bind:key="i"  />
    
  </div>
</template>

<script>

import ImageComponent from '@/components/ImageComponent.vue'
import {usePhotoStore} from '@/store/PhotoStore.js'
import { storeToRefs } from 'pinia'
export default {
  
  name: 'HelloWorld',
  emits: ['updateImgs'],
  components:{
    ImageComponent
  },
  setup(){
    const usephotostore=usePhotoStore()
    return {
      usephotostore
    }
  },
  data(){
    const {allphotos,getAllPhotos}=storeToRefs(this.usephotostore)
    const {updatePhotos}=this.usephotostore
    return {
      allphotos,
      getAllPhotos,
      updatePhotos
    }
  },
  computed:{
    getimgs(){
      return this.allphotos
    }
  },
  async mounted(){
    console.log('hii')
    await this.updatePhotos()
    // console.log(this.data)
  },
  
}
</script>


<style scoped>
/* .gallery-Image{
  text-align: center;
  vertical-align: center;
  width: 30%;
  margin: 5px;
   height: fit-content; 
   float:inline-start 
 }  */

 .gallery{
    display:block;
    /* float: left; */
    display: flex;
    /* flex-direction:column; */
    flex-wrap:wrap;
    gap:20px;
    /* width:250px; */
    /* padding: 5px; */
    /* flex-direction: row */
 }
 /* .c1{
  display: flex;
  flex-direction: column;
 }
 .c2{
  flex-direction: column;
 }
 .c3{
  flex-direction: column;
 } */
</style>

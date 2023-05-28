<template>
    <div class="gallery">
    <div v-for="(link, i) in albumname[myfunc]" :key="i">
       
        <img :src="'http://localhost:5000/images/'+link" />
        
    </div>
    </div>
</template>
<script>
//import router from '@/router'
import {storeToRefs} from 'pinia'
import { usePhotoStore } from '@/store/PhotoStore';
//import axios from 'axios';
//import ImageComponent from '@/components/ImageComponent.vue';
export default {
    /* view the album here /album/i */ 
  
    setup()
    {
        const photostore=usePhotoStore()
        return{
            photostore
        }
    },
    data()
    {
        const {albumname}=storeToRefs(this.photostore)
        return{
            albumname,
            
        }
    },
    computed:{
        myfunc()
        {
            const route = this.$route.path.split("/").filter(r => r != '')
            const f_id = route.at(-1)
            return f_id
        }
    }
    
}
</script>
<style scoped>
.gallery{
    
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    flex-wrap:wrap;
    gap:20px;  
    justify-content:space-evenly;
    
 }
 img{
 
  object-fit:cover;
  
  width:250px;
  height:100%;
  text-align: center;
  
  
}
</style>
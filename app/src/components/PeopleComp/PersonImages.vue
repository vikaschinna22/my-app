<template>
    <div>
        <img :src="link" v-for="link,i in getPersonImages" :key="i">
    </div>
</template>
<script>  
import router from '@/router'
import { usePhotoStore } from '@/store/PhotoStore'
import { storeToRefs } from 'pinia'
export default{
    setup(){
        const photoStore=usePhotoStore()
        return {photoStore}
    },
    data(){
        const {clusterImages} = storeToRefs(this.photoStore)
        return{
            clu_imgs:clusterImages
        }
    },
    computed:{
        getPersonImages(){
            const route=this.$route.path.split("/").filter(r=> r!='')
            const f_id = route.at(-1)
            // console.log(f_id)
            // console.log(this.clu_imgs[f_id]
            if(!(f_id  in this.clu_imgs ))
                router.replace('/search')
            return this.clu_imgs[f_id]
        }
    }    
}
</script>
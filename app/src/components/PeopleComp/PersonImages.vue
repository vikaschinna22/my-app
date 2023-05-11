<template>
    <div>
        <img :src="link" v-for="link,i in getPersonImages" :key="i">

    </div>
</template>
<script>  
import { usePhotoStore } from '@/store/PhotoStore'
export default{
    setup(){
        const usephotostore=usePhotoStore()
        return {usephotostore}
    },
    data(){
        return{
            clu_imgs:this.usephotostore.clusterImages
        }
    },
    computed:{
        getPersonImages(){
            const route=this.$route.path.split("/").filter(r=> r!='')
            const f_id = route.at(-1)
            // console.log(f_id)
            // console.log(this.clu_imgs[f_id])
            return this.clu_imgs[f_id]
        }
    }    
}
</script>
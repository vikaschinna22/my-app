<template>
    <div class="NavWrapper" v-if='!fullScreenImg'>
        <div class="NavContainer">
            <img src="@/assets/back.png" alt='back' class='Navicons' @click="$router.go(-1)" />
        </div>
    </div>
    <div class="gallery">
        <div class="gal-Container">
            <div v-for="link,i in getPersonImages" :key="i" @click="handleClick">
                <img :src="link"  class="gal-img">
            </div>
        </div>
    </div>
    <FullScreenImage v-if='fullScreenImg' :photos='getPersonImages' :Imgidx="Imgidx" :close="handleFullScreenClose"/>
</template>
<script>  
import router from '@/router'
import { usePhotoStore } from '@/store/PhotoStore'
import { storeToRefs } from 'pinia'
import FullScreenImage from '@/components/FullScreenImage.vue'

export default{
    setup() {
        const photoStore = usePhotoStore();
        return { photoStore };
    },
    data() {
        const { clusterImages } = storeToRefs(this.photoStore);
        return {
            clu_imgs: clusterImages,
            fullScreenImg:false,
            Imgidx:-1
        };
    },
    computed: {
        getPersonImages() {
            const route = this.$route.path.split("/").filter(r => r != "");
            const f_id = route.at(-1);
            // console.log(f_id)
            // console.log(this.clu_imgs[f_id]
            if (!(f_id in this.clu_imgs))
                router.replace("/search");
            return this.clu_imgs[f_id];
        },
        
    },
    methods:{
        handleClick(e){
            this.fullScreenImg=true;
            const k= Object.entries(this.getPersonImages).find(item => item[1]===e.target.src)
            console.log(typeof k)
            this.Imgidx =  parseInt(k)   
        },
        handleFullScreenClose(){
            this.fullScreenImg = false
            this.Imgidx=-1
        },
    },
    components: { FullScreenImage }
}
</script>

<style scoped>
.Navicons{
  height: 30px;
  width: 30px;
  object-fit: cover;
 
}
.Navicons:hover{
    -ms-transform: scale(1.5); 
    -webkit-transform: scale(1.5); 
    transform: scale(1.5); 
}

.NavWrapper{
  position: fixed;
  top: 0%;
  width: 100%;
  height: 50px;
  z-index: 2;
}

.NavContainer{
  background-color: white;
  padding: 10px;
  z-index: 3;
  display: flex;
  align-items: center;
}
.gal-img{
  object-fit:fill;
  width:250px;
  height:300px;
  text-align: center;
  padding:15px;
}
.gal-Container{
    position: relative;
    display: flex;
    justify-content: left;
    flex-wrap: wrap;
 }

 
</style>
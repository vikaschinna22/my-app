<template>

    <div class="NavWrapper">
        <div class="NavContainer">
            <img src="@/assets/back.png" alt='back' class='Navicons' @click="$router.go(-1)" />
        </div>
    </div>
    <div class="gallery">
    <div v-for="(link, i) in albumname[myfunc]" :key="i">
        <img :src="'http://localhost:5000/images/'+link" @click="handleClick" />
    </div>
    </div> 
    <FullScreenImage v-if='fullScreenImg'  :photos='photos' :Imgidx="Imgidx" :close="handleFullScreenClose"/>
</template>
<script>



//import router from '@/router'
import {storeToRefs} from 'pinia'
import { usePhotoStore } from '@/store/PhotoStore';
import router from '@/router';
import FullScreenImage from '@/components/FullScreenImage.vue';
//import axios from 'axios';
//import ImageComponent from '@/components/ImageComponent.vue';
export default {
    /* view the album here /album/i */
    beforeMount() {
        const route = this.$route.path.split("/").filter(r => r != "");
        const f_id = route.at(-1);
        if (!this.albumname[f_id])
            router.push("/search");
    },
    setup() {
        const photostore = usePhotoStore();
        return {
            photostore
        };
    },
    data() {
        const { albumname } = storeToRefs(this.photostore);
        return {
            albumname,
            fullScreenImg:false,
            Imgidx:-1,
            photos:[],
        };
    },
    computed: {
        myfunc() {
            const route = this.$route.path.split("/").filter(r => r != "");
            const f_id = route.at(-1);
            return f_id;
        }
    },
    methods:{
        handleClick(e){
            // console.log(e)
            this.fullScreenImg=true;
            // console.log(this.fullScreenImg)
            // this.allphotos = this.albumname[this.myfunc].slice()
            this.photos = this.albumname[this.myfunc].map(item=>{
                // console.log(item)
                return 'http://localhost:5000/images/' + item
            })
            // console.log(this.allphotos)
            const k= Object.entries(this.photos).find((item)=>  item[1]===e.target.src)
            // console.log(k)
            this.Imgidx = parseInt(k[0])
            
        },
        handleFullScreenClose(){
            this.fullScreenImg = false
            this.photos=[]
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
  /* margin: 0 10px ; */
}
.Navicons:hover{
    -ms-transform: scale(1.5); /* IE 9 */
    -webkit-transform: scale(1.5); /* Safari 3-8 */
    transform: scale(1.5); 
}

.NavWrapper{
  position: fixed;
  top: 0%;
  width: 100%;
  height: 50px;
  z-index: 1;
}

.NavContainer{
  background-color: white;
  padding: 10px;
  z-index: 3;
  display: flex;
  align-items: center;
  /* justify-content: space-between; */
}



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
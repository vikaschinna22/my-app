<template>
    <div v-if="show" class="delNavWrapper">
        <div class="delContainer">
            <img src="@/assets/delete.png" alt="delete" class="delicons" @click="handleDel">
            <img src="@/assets/back.png" alt='back' class='delicons' @click="handleDelBack" />
        </div>
      </div>
    <div class="NavWrapper">
        <div class="NavContainer">
            <img src="@/assets/back.png" alt='back' class='Navicons' @click="$router.go(-1)" />
        </div>
    </div>
    <div class="gallery">
    <div v-for="(link, i) in albumname[myfunc]" :key="i">
        <div class="gal-wrapper">
            <div class="gal-Container">
                <label class="lbl" :for="'chk' + i" @click="handleLabel">
                    <img :src="'http://localhost:5000/images/'+link" class="gal-img" @click="handleImgClick"/>
                </label>
                <input type="checkbox" :id="'chk'+i" :key="i" v-model="selimg" :value="link" :class="[chkboxshow ? 'selectImages' : 'selectImageshover']"/>
            </div>
        </div>
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
import axios from 'axios';
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
        const {updatePhotos} =this.photostore;
        const { albumname } = storeToRefs(this.photostore);
        return {
            show:false,
            albumname,
            fullScreenImg:false,
            Imgidx:-1,
            selimg:[],
            chkboxshow:false,
            photos:[],
            updatePhotos
        };
    },
    watch:{
        selimg(newselimg)
        {
            if(newselimg.length>0){this.chkboxshow=true
                this.show=true;
            }
            else{ this.chkboxshow=false
                this.show=false;
            }
        }
    },
    computed: {
        myfunc() {
            const route = this.$route.path.split("/").filter(r => r != "");
            const f_id = route.at(-1);
            return f_id;
        }
    },
    methods:{
        handleDelBack()
        {
            this.selimg=[]
            this.show=false
        },
        async handleDel()
        {
        
            const data={
                imgs:this.selimg,
                id:this.myfunc
            }
            console.log(data)
            await axios.post('http://localhost:5000/delalb/',data).then(res=>{
                res
                this.selimg=[]
                this.updatePhotos()
                this.show=false
            }).catch(err=>{
                console.log(err)
            })
        },
        handleLabel(e)
        {
            if (e.target.nodeName === 'IMG' && this.selimg.length <= 0)
                e.preventDefault();
        },
        handleImgClick(e){
            // console.log(e)
            if(this.selimg.length>0)return;
            this.fullScreenImg=true;
            this.show=false;
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
            //this.show=true;
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
.gal-img{
  object-fit:fill;
  width:250px;
  height:300px;
  text-align: center;
}
.NavContainer{
  background-color: white;
  padding: 10px;
  z-index: 3;
  display: flex;
  align-items: center;
  /* justify-content: space-between; */
}

.gal-Container{
    position: relative;
 }
.delicons{
  height: 30px;
  width: 30px;
  object-fit: cover;
  margin: 0 20px;
}
.delicons:hover{
  -ms-transform: scale(1.5); /* IE 9 */
  -webkit-transform: scale(1.5); /* Safari 3-8 */
  transform: scale(1.5); 
}
.gallery{
    position:relative;
    
    margin-top: 10px;
    display: flex;
    flex-direction: row;
    flex-wrap:wrap;
    gap:20px;  
    justify-content:space-evenly;
    
 }
 
.delNavWrapper{
  position: fixed;
  top: 0%;
  width: 100%;
  height: 50px;
  z-index: 2;
  
}
.delContainer{
  background-color: white;
  opacity: 0.95;
  padding: 10px;
  z-index: 3;
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  justify-content: space-between;
}
.selectImages{
  width: 20px;
  height: 25px;
  position: absolute; 
  bottom: 90%; 
  right: 0px; 
  visibility: visible;
 }
 .selectImageshover{
  width: 20px;
  height: 25px;
  position: absolute; 
  bottom: 90%; 
  right: 0px; 
   visibility: hidden;
 }
 .selectImageshover:hover,.selectImages:focus{
   visibility: visible;
 }
 .gal-Container{
    position: relative;
 }
</style>
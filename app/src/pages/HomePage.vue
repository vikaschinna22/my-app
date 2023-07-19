<template>
  <div v-if="show" class="delNavWrapper">
    <div class="delContainer">
      <img src="@/assets/back.png" alt='back' class='delicons' @click="handleDelBack" />
      <img src="@/assets/delete.png" alt="delete" class="delicons" @click="handleDel">
    </div>
  </div>

  <div class="gallery" >
    <div v-for="s,i in allphotos" :key="i" >
      <div class="gal-wrapper">
        <div class="gal-Container">
          <label class="lbl" :for="'chk'+i" @click="handleLabel">
            <img :src="s" alt="" class="gal-img" @click=" handleImgClick">
          </label>
          <input type="checkbox" :key="i" :id="'chk'+i" v-model="selectImages" :value="s" :class="[chkboxshow?'selectImages':'selectImageshover']"
            />
        </div>
      </div>
    </div>
    <FullScreenImage v-if='fullScreenImg' :photos='allphotos' :Imgidx="fullScreenImgidx" :close="handleFullScreenClose"/>
  </div>
</template>

<script>

import {usePhotoStore} from '@/store/PhotoStore.js'
import axios from 'axios'
import { storeToRefs } from 'pinia'
import FullScreenImage from '@/components/FullScreenImage.vue'
export default {
  
  name: 'HomePage',
  components:{
    FullScreenImage
  },
  setup(){
    const photostore=usePhotoStore()
    return { photostore}
  },
  
  data(){
    const {allphotos,getAllPhotos}=storeToRefs(this.photostore)
    return {
      allphotos,
      getAllPhotos,
      selectImages:[],
      chkboxshow:false,
      fullScreenImg:false,
      fullScreenImgidx:-1
    }
  },
  watch:{
    selectImages(newselectImages){
      if(newselectImages.length>=1)this.chkboxshow=true;
      else this.chkboxshow=false;
    }
  },
  computed:{
    getimgs(){
      return this.allphotos
    },
    show(){
      return this.selectImages.length >=1
    }
  
  },
  methods:{
    handleLabel(e){
      if(e.target.nodeName === 'IMG' && this.selectImages.length<=0) 
        e.preventDefault();
      // console.log(e.target.nodeName) 
    },
    handleImgClick(e){
      if(this.selectImages.length >=1)return;
      // console.log(e.target.nodeName)
      this.fullScreenImg=true;
      // this.curImg=e.target.src
      const k= Object.entries(this.allphotos).find((item)=>  item[1]===e.target.src)
      this.fullScreenImgidx = parseInt(k[0])
      // console.log(typeof k)
      // console.log(typeof this.photostore.allphotos)
    },
    handleDelBack(){
      // console.log(this.selectImages)
      this.selectImages = []
    },
    handleDel(){
      const Ids= this.selectImages.map((item)=>{
        const ele = item.split('/')
        // console.log(ele)
        return ele.at(-1)
      })
      const data={
        Images:Ids
      }
      axios.post('http://localhost:5000/deleteImages/',data).then(res=>{
        console.log(res)
        this.updatePhotos()
        this.handleDelBack()
      }).catch(err=>{
        console.log(err)
      })
      
    },
    handleFullScreenClose(){
      this.fullScreenImg = false
      this.fullScreenImgidx=-1
    },
  },
  
}
</script>


<style scoped>
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
  align-items: center;
  justify-content: space-between;
}

.gal-img{
  object-fit:fill;
  width:250px;
  height:300px;
  text-align: center;
}

 .gallery{
    margin-top: 50px;
    display: flex;
    flex-wrap:wrap;
    gap:20px;  
    justify-content:space-evenly;
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

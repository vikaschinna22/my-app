<template>
  <div :class="[chkboxshow ?'galleryPage' : '']">
  </div>
  <div v-if="show" class="delNavWrapper">
    <div class="delContainer">
      <img src='./back.png' alt='back' class='delicons' @click="handleDelBack" />
      <img src="./delete.png" alt="delete" class="delicons" @click="handleDel">
    </div>
  </div>
  <div class="gallery" >
    <div v-for="s,i in allphotos" :key="i" >
      <div class="wrapper">
        <div class="Container">
          <label class="lbl" :for="'chk'+i" @click="handleLabel">
            <ImageComponent :Imgsrc="s" @click="handleImgClick" />
          </label>
          <input type="checkbox" :key="i" :id="'chk'+i" v-model="selectImages" :value="s" :class="[chkboxshow?'selectImages':'selectImageshover']"
            />
        </div>
      </div>
    </div>
    <div v-if="fullScreenImg" class="fullImg" > 
      <div class="closeBtn"><img src="./back-white.png" @click="handleClose"  class="fclosebtn"></div>
      <div class="fullImgContainer">
        <div class="fullLeft ">
          <img src ='./left-arrow.png' alt='left' @click="handleLeft" class="arrow"> 
        </div>
        <div class="fullCenter">
          <img :src="curImg"/>
        </div>
        <div class="fullRight ">
            <img src="./right-arrow.png" alt="right" @click="handleRight" class="arrow">
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import ImageComponent from '@/components/ImageComponent.vue'
import {usePhotoStore} from '@/store/PhotoStore.js'
import axios from 'axios'
import { storeToRefs } from 'pinia'

export default {
  
  name: 'HelloWorld',
  emits: ['updateImgs'],
  components:{
    ImageComponent
  },
  setup(){
    const photostore=usePhotoStore()
    return {
      photostore
    }
  },
  
  data(){
    const {allphotos,getAllPhotos}=storeToRefs(this.photostore)
    const {updatePhotos}=this.photostore
    return {
      allphotos,
      getAllPhotos,
      updatePhotos,
      selectImages:[],
      chkboxshow:false,
      fullScreenImg:false,
      curImg:null,
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
  async mounted(){
    // console.log('hii')
    await this.updatePhotos()
    // console.log(this.data)
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
      this.curImg=e.target.src
      const k= Object.entries(this.allphotos).find((item)=>  item[1]===e.target.src)
      this.fullScreenImgidx = k[0]
      // console.log(typeof this.photostore.allphotos)
    },
    handleClose(){
      this.fullScreenImg=false
      this.curImg=null
      this.fullScreenImgidx=-1
    },
    handleRight(){
      // console.log(this.allphotos.length)
      this.fullScreenImgidx = (this.fullScreenImgidx + 1)%this.allphotos.length
      this.curImg = this.allphotos[this.fullScreenImgidx]
    },
    handleLeft(){
      this.fullScreenImgidx = (this.fullScreenImgidx - 1+ this.allphotos.length)%this.allphotos.length
      this.curImg = this.allphotos[this.fullScreenImgidx]
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
/* .galleryPage{
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  transform: translateY(-10%);
} */
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

/* .gallery-Image{
  text-align: center;
  vertical-align: center;
  width: 30%;
  margin: 5px;
   height: fit-content; 
   float:inline-start 
 }  */

 .gallery{
    /* display:block; */
    /* float: left; */
    margin-top: 10px;
    display: flex;
    /* flex-direction:column; */
    flex-wrap:wrap;
    gap:20px;  
    justify-content:space-evenly;
    /* width:250px; */
    /* padding: 5px; */
    /* flex-direction: row */
 }

.selectImages{
  width: 20px;
  height: 25px;
  position: absolute; 
  bottom: 90%; 
  right: 0px; 
  visibility: visible;
  /* float: left; */
 }
 .selectImageshover{
  width: 20px;
  height: 25px;
  position: absolute; 
  bottom: 90%; 
  right: 0px; 
   visibility: hidden;
 }
 .selectImageshover:hover{
   visibility: visible;
 }
 .Container{
    position: relative;
    /* width: 100px; */
    /* height: 100px; */
    /* float: left; */
    /* margin-left: 10px;  */
 }
 /* .wrapper{
   width: 250px;
   height: 250px;
   over
 } */
 .fullImg{
    position: fixed;
    z-index: 1;
    left: 50%;
    top: 50%;
    width: 100vw;
    height: 100vh;
    transform: translate(-50%, -50%);
    background-color: rgba(0, 0, 0, 0.9 );
    
 }
 .fullImgContainer{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    height: 100%;

 }
 .closeBtn{
  /* background-color: rgba(0, 0, 0, 0.5); */
  /* padding: 20px; */
   display: flex;
    flex-direction: row;
   justify-content: left;
  width: 100%;
  height: 10%;
  border-radius: 10px;
  /* display: none; */
  /* right: 30px; */
 }
/* .closeBtn:hover{
  background-color: rgba(0, 0, 0, 0.5);
} */
 .fclosebtn{
  /* float:left; */
  border-radius: 50%;
  margin: auto 0;
  left: 30px;
  position: relative;
  height: 30px;
  width: 30px;
 }
 .fclosebtn:hover{
  -ms-transform: scale(1.5); /* IE 9 */
  -webkit-transform: scale(1.5); /* Safari 3-8 */
  transform: scale(1.5); 
 }
 .arrow {
    width: 30px;
    height: 50px;
 }
 .arrow:hover{
  -ms-transform: scale(1.5); /* IE 9 */
  -webkit-transform: scale(1.5); /* Safari 3-8 */
  transform: scale(1.5); 
 }
 .fullRight,.fullLeft{
    height: 100%;
    align-items: center;
    display: flex;
    width: 70px;
    justify-content: center;
 }
</style>

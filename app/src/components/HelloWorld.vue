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
      //console.log(this.allphotos)
      return this.allphotos
    }
  },
  async mounted(){
    console.log('hii')
    await this.updatePhotos()
    //console.log(this.allphotos)
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

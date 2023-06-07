<template>
    <!-- <div v-if="fullScreenImg" class="fullImg" >  -->
    <div class="fullImg">
        <div class="closeBtn"><img src="@/assets/back-white.png" @click="handleClose"  class="fclosebtn"></div>
        <div class="fullImgContainer">
            <div class="fullLeft ">
            <img src ='@/assets/left-arrow.png' alt='left' @click="handleLeft" class="arrow"> 
            </div>
            <div class="fullCenter">
            <img :src="curImg"/>
            </div>
            <div class="fullRight ">
                <img src="@/assets/right-arrow.png" alt="right" @click="handleRight" class="arrow">
            </div>
        </div>
    </div>
    <!-- </div> -->
  </template>
  
  <script>
  

  
  export default {
    beforeMount(){
        this.curImg = this.photos[this.idx]
    },
    props:['photos','Imgidx','close'],
    data(){
        return{
            curImg:'',
            idx:this.Imgidx
        }
    },
    methods:{
      handleClose(){
        this.curImg=null
        this.idx=-1
        this.close()
      },
      handleRight(){
        // console.log(this.idx)
        this.idx = ( this.idx + 1 ) % this.photos.length
        this.curImg = this.photos[this.idx]
      },
      handleLeft(){
        this.idx = (this.idx - 1 + this.photos.length)%this.photos.length
        this.curImg = this.photos[this.idx]
      }
    },
  }
  </script>
  
  
  <style scoped>
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
     display: flex;
      flex-direction: row;
     justify-content: left;
    width: 100%;
    height: 10%;
    border-radius: 10px;
   
   }
   .fclosebtn{
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
  
<template>
  <div>
    <nav class=".nav">
      <span class = 'nav-item' @click="$router.push('/')">Gallery</span>
       <span class = 'nav-item' @click="$router.push('/search')">Search</span>
      <!-- <router-link class = 'nav-item' to="/">Gallery</router-link> 
      <router-link class = 'nav-item' to="/search">Search</router-link> -->
      <!-- accept=".jpg, .jpeg, .png" -->
      <input
      class = 'nav-item'
        ref="images" 
        type="file"
        id="image_uploads"
        name="image_uploads"
        
        @change="upload"
        hidden
        multiple 
      />
      <span class = 'nav-item' @click="getImages">Add</span>
    </nav>
    <div></div>
    <router-view/>
  </div>
  
</template>

<script>
import axios from 'axios';
import { usePhotoStore } from './store/PhotoStore.js';

export default{ 
  setup(){
    const usephotostore=usePhotoStore()
    return {
      usephotostore
    }
  },
  data(){
    const {updatePhotos} = this.usephotostore
    return {updatePhotos};
  },
  async mounted(){
    // console.log('hii')
    await this.updatePhotos()
    // console.log(this.data)
  }, 
  methods:{
      async getImages(){
        let imgupload = this.$refs.images;
        await imgupload.click()
      },
      async upload(){
        const formData=new FormData()
        let imgupload = this.$refs.images;
        for(let i=0;i<imgupload.files.length;i++){
            const f= imgupload.files[i];
            // console.log(f)
            formData.append('files',f)
        }
        console.log(formData)
        try{
          await axios.post('http://localhost:5000/imageupload/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            },
          })
          this.$refs.images.value=null;
        }catch(err){
          console.log(err)
        }
        await this.usephotostore.updatePhotos()
        // this.$forceUpdate()
      },
    
  }
}

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* background-color: lightgrey; */
  /* height: 100vh; */
  /* width: 100; */
}
</style>
<style scoped>

nav {
  padding-top: 10px;
  width: 100%;
  top:0;
  display: flex;
  position: fixed;
  z-index: 1;
   align-items: center;
   padding: 5px;
   /* justify-content:right; */
   background-color: rgba(211, 211, 211, 0.7);
}
.nav-item{
  font-weight: bold;
  text-decoration: none;
  color:#000000;
  /* border:1px solid #aba9a9; */
  margin-left: 15px;
  padding:5px 10px;
  transition:0s ease;

    font-weight: bold;
    font-size:large;
    color: #2c3e50;
  }
  .nav-item:hover{
    background-color: rgb(153, 151, 151);
    border-radius: 10px;
  color:#000;
  border-radius: 2px;
}


/* nav a.router-link-exact-active {
  color: #42b983;
} */
</style>

<template>
  <div>
    <nav>
      <router-link to="/">Gallery</router-link> |
      <router-link to="/search">Search</router-link>
      <!-- accept=".jpg, .jpeg, .png" -->
      <input
      ref="images" 
      type="file"
      id="image_uploads"
      name="image_uploads"
      
      @change="upload"
      hidden
      multiple />
      <button @click="getImages">add</button>
    </nav>
    <div></div>
    <router-view/>
  </div>
  
</template>

<script>
import axios from 'axios';
import { usePhotoStore } from './store/PhotoStore.js';
export default{  
  data(){
    const usephotostore=usePhotoStore()
    return {usephotostore,renderc:true};
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
  /* background-color: #ccc; */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

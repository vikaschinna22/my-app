<template>
<div class ="field" id="searchform">
    <form @submit="process">
      <input type="text" v-model="name1" @change="name2" id="searchterm" required>
      <button id="search">create</button>
    </form>
</div>
<div class="container">
    <div v-for="s,i in allphotos" :key="i">
        <div class="wrapper">
            <input type="checkbox" :key="i" :id="'chk' + i" v-model="selImg" :value="s">
            <label class="lbl" :for="'chk'+i">
                <ImageComponent :Imgsrc="s" />
            </label>
        </div>
    </div>
</div>

</template>
<script>
import { usePhotoStore } from '@/store/PhotoStore';
import { storeToRefs } from 'pinia';
import ImageComponent from '@/components/ImageComponent.vue'
import axios from 'axios';
import router from '@/router';
export default{
    components:{
        ImageComponent
    },
    setup() {
        const photostore = usePhotoStore()
        return {
            photostore
        }
    },
    data()
    {
        const { allphotos, getAllPhotos } = storeToRefs(this.photostore)
        return{
            allphotos,
            getAllPhotos,
            selImg:[],
            name1:"",
            quantity:false,
        }
    },
    methods:{
         name2() {
            let temp = this.name1.replaceAll(' ', '')
            if (temp.length == 0)
                this.quantity = false;
            else if(this.selImg.length>0)
                this.quantity=true;

        },
        async process(e){
            e.preventDefault()
            let temp=this.name1.replaceAll(' ', '')
            if(temp.length == 0)
                return;
            if(this.selImg==null || this.selImg.length==0)
                return;
            console.log(this.name1)
            const Ids = this.selImg.map((item) => {
                const ele = item.split('/')
                // console.log(ele)
                return ele.at(-1)
            })
            console.log(Ids)
            const data={
                title:this.name1,
                Img:Ids
            }
            await axios.post('http://localhost:5000/createAlbum/',data)
            router.push('/search')
        }
    }
}
</script>
<style scoped>
input[type="checkbox"] {
  display: none;
}

label {
  border: 1px solid #fff;
  padding: 10px;
  display: block;
  position: relative;
  margin: 10px;
  cursor: pointer;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

label::before {
  background-color: white;
  color: white;
  content: " ";
  display: block;
  border-radius: 50%;
  border: 1px solid grey;
  position: relative;
  top: -5px;
  left: -5px;
  width: 25px;
  height: 25px;
  text-align: center;
  line-height: 28px;
  transition-duration: 0.4s;
  transform: scale(0);
}

label img {
  height: 100px;
  width: 100px;
  transition-duration: 0.2s;
  transform-origin: 50% 50%;
}

:checked+label {
  border-color: #ddd;
}

:checked+label::before {
  content: "✓";
  background-color: grey;
  transform: scale(1);
}

:checked+label img {
  transform: scale(0.9);
  box-shadow: 0 0 5px #333;
  z-index: -1;
}
.container {
    display: flex;
    flex-direction: row;
    /*display: flex;
     flex-direction:column; */
    flex-wrap:wrap;
    
    justify-content:space-evenly;
}

.field {
  display:flex;
  /*position:realtive;*/
  /*margin:5em auto;*/
    padding-left: 25em;
  width:500px;
  flex-direction:row;
  /* -moz-box-shadow:    0px 0px 2px 0px rgba(0,0,0,0.2);
  -webkit-box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.2);
  box-shadow:         0px 0px 2px 0px rgba(0,0,0,0.2); */
}

.field>input[type=text],
.field>button {
  display:block;
  font:1.2em 'Open sans';
}

.field>input[type=text] {
  flex:1;
  padding:0.6em;
  border:0.2em solid #819090;
  border-left: none;
  border-top: none;
}

.field>button {
  padding:0.6em 0.8em;
  background-color: #819090;
  color: #fff;
  border:none;
}
</style>
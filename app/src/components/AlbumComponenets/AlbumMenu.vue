<template>
    <div class="menu" >
        <h3>Albums</h3>
        <div class="menu" v-if="Object.keys(albumname).length > 0">
        <div v-for="(s,v,i) in albumname" :key=i>
            <button class="roundit"  @click="redirect(v)" :key="i"><h2>o</h2></button>
        </div>
        </div>
        <div class="menu roundit-c">
            <div class="item" @click="handleClick"><h1>+</h1></div>
        </div>
    </div>
</template>
<script>
import router from '@/router'
import { usePhotoStore } from '@/store/PhotoStore';
import { storeToRefs } from 'pinia';
export default{
    setup()
    {
        const photostore=new usePhotoStore()
        return{
            photostore
        }
    },
    data(){
        const {albumname}=storeToRefs(this.photostore)
        return {
            albumname,
            show:false,
        }
    },
    
    methods:{
        handleClick(){
            this.show=true;
            console.log(this.albumname)
            console.log(this.show)
            router.push('/AlbumCreate')
        },
        redirect(i)
        {
            console.log(this.albumname[i])
            router.push('Album/'+i)
        }
    }
}
</script>
<style scoped>
.All {
    position: absolute;
    z-index: 1;
    left: 50%;
    top: 50%;
    background-color: white;
    color: red;
    width: 100vw;
    height: 90vh;
    transform: translate(-50%, -50%);
}
.menu{
    display: flex;
    overflow: auto;
    white-space: nowrap;
    scrollbar-width: none;
    flex-direction: row;
}
.item{
    height: 100px;
    width: 70px;
    padding:10px;
    background-color: gray;
    color: black;
    opacity: 0.7;

}
.menu::-webkit-scrollbar{
    display: none;
}
button {
  background-color: #6d52c4;
  border: none;
  color: white;
  padding: 22px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  margin-right: 12px;
}
.roundit{
    border-radius: 50%;
}
.roundit-c{
    border-radius: 48%;
}
</style>
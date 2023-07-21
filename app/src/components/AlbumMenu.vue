<template>
    <div >
        <h3>Albums</h3>
        <div class="menu" >
            <div class="roundit-c">
                <div class="item-create" @click="handleClick"><span><img src=@/assets/plus.png style="max-width: 100%;"/></span></div>
            </div>
            <div v-for="(s,v,i) in albumname" :key="i" class="item"  >
                <img :src="'http://localhost:5000/images/'+s.at(-1)" class="item-img"
                @click="redirect(v)" :key="i"  alt="">
                <p>{{ v }}</p>
            </div>
        </div>
        
    </div>
</template>
<script>
import router from '@/router'

export default{
    props:['albumname'],

    methods:{
        handleClick(){
            router.push('/AlbumCreate')
        },
        redirect(i){
            console.log(i)
            router.push('Album/'+i)
        }
    }
}
</script>
<style scoped>
h3{
    text-align: left;
}
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
.item p{
    text-align:center ;
    color:rgba(0, 0, 0, 0.911);
    font-weight: bold;
    padding: 0px;
    margin: 0;
    margin-right: 20px;
}
.item-create{
    margin-right: 20px;
    height: 170px;
    width: 170px;
    border-radius: 15px;
    /* background-color:white; */
    color: black;
    opacity: 0.7;

    

}

.item-img{
    margin-right: 20px;
    height: 170px;
    width: 170px;
    border-radius: 15px;

    -moz-box-shadow: 10px 10px 5px #ccc;
  -webkit-box-shadow: 10px 10px 5px #ccc;
  box-shadow: 10px 10px 5px #ccc;
  -moz-border-radius:25px;
  -webkit-border-radius:25px;
  border-radius:25px
}
.item-img:hover{
    transform:scale(1.1);
    transition:0.3s ease-in-out;
}
/* img{
    height: inherit;
    width: 100%;
    object-fit: fill;
} */
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
    border-radius: 10px;
}
.roundit-c{
    border-radius: 10px;
} 

</style>
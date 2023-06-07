<template>
    <div v-if="pshow">
        <h3>People</h3>
        <div class="menu">
            <div v-for="item,i in imgs" :key="i">
                <img class="menu-img" :src="item.link"  @click="imgClick(item.p_id)">
            </div>
        </div>
    </div>
</template>
<script>
import router from '@/router';
export default{
    props:['imgs'],
    computed:{
        pshow(){
            return this.imgs.length >0 ?true:false;
        }
    },
    methods:{
        imgClick(e){
            console.log(e)
            router.push('/person/'+e)
        }
    }
}
</script>

<style scoped>
.menu{
    display: flex;
    overflow: auto;
    white-space: nowrap;
    scrollbar-width: none;
}
h3{
    text-align: justify;
}
.menu::-webkit-scrollbar{
    display: none;
}
.menu-img{
    margin-right: 20px;
    height: 150px;
    width: 150px;
    border-radius: 50%;
}
</style>
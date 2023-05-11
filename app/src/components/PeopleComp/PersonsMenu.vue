<template>
    <div v-if="pshow">
        <h3>People</h3>
        <div class="menu">
            <PeopleComponet v-for="item,i in imgs" :key="i" :img_link = "item['link']" :p_id="item['p_id']"/>
        </div>
    </div>
</template>
<script>
import { usePhotoStore } from '@/store/PhotoStore';
import PeopleComponet from '@/components/PeopleComp/PeopleComponet.vue';
export default{
    setup(){
        const photostore = usePhotoStore()
        return {
            photostore
        }
    },data(){
        return{
            imgs:this.photostore.clusters
        }
    },
    computed:{
        pshow(){
            // console.log(this.imgs)
            return this.imgs.length >0 ?true:false;
        }
    },
    components:{
        PeopleComponet
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
</style>
<template>
    <div>
        <img :src="img_link" alt="" @click="imgClick">
    </div>
</template>
<script>
import router from '@/router';

export default{
    props:['img_link','p_id'],
    methods:{
        imgClick(){
            console.log(this.p_id)
            router.push('/person/'+this.p_id)
        }
    }
}
</script>
<style scoped>
img{
    margin-right: 20px;
    height: 150px;
    width: 150px;
    border-radius: 50%;
}
</style>
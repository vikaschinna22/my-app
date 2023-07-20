<template>
    <div class="ImageComponent" >
        <img :src='Imgsrc' alt="">
    </div>
</template>

<script>
export default{
    props:['Imgsrc']
}
</script>

<style scoped>
.ImageComponent{
    height: 300px;
}

img{
  object-fit:fill;
  width:250px;
  height:100%;
  text-align: center;
}
</style>
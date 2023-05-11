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
    /* padding:5px; */
    /* width:35vh; */
    /* display: flex; */
    /* flex-wrap: wrap; */
    height: 300px;
    /* border-radius: 7%; */
    /* display: flex; */
    /* flex-wrap: wrap; */
    /* flex-direction:row; */
    /* margin-top: 10px; */
    /* justify-content:center; */
    /* object-fit: contain; */
  /* margin-top: 10px;
  padding: 5px;
  height: auto;
  width: 30%; */
}

img{
  /* border-radius: 7%; */
  object-fit:cover;
  /* display:inline-block; */
  /* object-position:unset; */
  /* object-fit:cover; */
  width:250px;
  height:100%;
  text-align: center;
  
  /* display: flex; */
  /* object-fit: contain;
   max-width: 100%;
   max-height: 100%;
   width: auto;
   height: auto; */
}
</style>
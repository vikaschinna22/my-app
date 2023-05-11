<template>
  <div class="about">
    <PersonsMenu/>
    <AlbumMenu/>
  </div>
</template>
<script>
  import PersonsMenu from '@/components/PeopleComp/PersonsMenu.vue';
  import AlbumMenu from '@/components/AlbumComponenets/AlbumMenu.vue'
  export default{
    components:{
      PersonsMenu,
      AlbumMenu
    }
  }
</script>
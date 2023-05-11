<template>
    <div >
        <h3>Albums</h3>
        <!-- <div v-if="show" class="All">
            <button><h2></h2></button>
        </div> -->
        <div class="menu" >
            <div class="item" @click="handleClick"><h1>+</h1></div>
        </div>
    </div>
</template>
<script>
export default{
    data(){
        return {
            show:false
        }
    },
    methods:{
        handleClick(){
            this.show=true;
            console.log(this.show)
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
    flex-direction: row;
    overflow-x: auto;
}
.item{
    height: 100px;
    width: 70px;
    background-color: gray;
    color: black;
    opacity: 0.7;
}

</style>
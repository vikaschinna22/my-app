import { defineStore} from "pinia";
import axios from 'axios'

export const usePhotoStore=defineStore('PhotoStore',{
    state:()=>({
        allphotos:[],
        clusters:[],
        clusterImages:{}
    }),
    getters:{
        getAllPhotos:(state)=> state.allphotos,
    },
    actions:{
        async updatePhotos(){
            console.log('update photo')
            try{
                const res= await axios.get("http://localhost:5000/")
                // console.log(typeof res.data.imgs)
                this.allphotos=res.data.imgs
                this.clusters=res.data.clusters
                this.clusterImages=res.data.clusterImages
            }catch(err){
                console.log(err)
            }
        }
    }

})
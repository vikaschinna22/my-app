import { defineStore} from "pinia";
import axios from 'axios'

export const usePhotoStore=defineStore('PhotoStore',{
    state:()=>({
        allphotos:[],
        clusters:[],
        clusterImages:{},
        albumname:{},

    }),
    getters:{
        getAllPhotos:(state)=> state.allphotos,
    },
    actions:{
        async updatePhotos(){
            try{
                const res= await axios.get("http://localhost:5000/")
                // console.log(res.data)
                this.allphotos=res.data.imgs
                this.clusters=res.data.clusters
                this.clusterImages=res.data.clusterImages
                const res1=await axios.get("http://localhost:5000/getalb/")
                this.albumname=res1.data.var
                console.log(this.albumname)
            }catch(err){
                console.log(err)
            }
        }
    }

})
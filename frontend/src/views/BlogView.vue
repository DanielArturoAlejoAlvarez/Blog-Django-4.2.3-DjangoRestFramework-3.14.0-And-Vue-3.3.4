<template>
  <div class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8">
    <div class="absolute inset-0">
      <div class="bg-white h-1/3 sm:h-2/3" />
    </div>
    <div class="relative max-w-7xl mx-auto">
      <div class="text-center">
        <div class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
          <HelloWorld msg="Discover with me the most incredible posts" />
        </div>
      </div>
      <div class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">
        <div v-for="posts in APIData" :key="posts.id" class="flex flex-col rounded-lg shadow-lg overflow-hidden">
        
            <router-link to="#">
                <img :src="base + posts.thumbnail" />
                <div class="p-4">
                  <p class="text-3xl text-red-600 font-bold mb-3">{{posts.title}}</p>
                  <p class="text-gray-700 font-medium">{{posts.content}}</p>
                </div>
            </router-link>
        
        </div>
      </div>
    </div>

  </div>
</template>


<script>

import HelloWorld from '@/components/HelloWorld.vue'
import {getAPI} from '../assets/js/api.js'

export default {
    
    name: 'BlogView',
    components: {
      HelloWorld
    },
    data(){
      return {
        APIData: [],
        base: getAPI.defaults.baseURL,
      }
    },
    created(){
      getAPI.get('/blog/posts/')
        .then(res=>{
          console.log('Post API has received data')
          this.APIData = res.data
        })
        .catch(err=>{
          console.log(err)
        })
    }
}
</script>

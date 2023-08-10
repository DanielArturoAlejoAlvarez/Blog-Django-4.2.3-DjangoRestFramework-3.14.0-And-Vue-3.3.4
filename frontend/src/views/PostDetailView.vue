<template>
    <div class="relative py-16  overflow-hidden">

    <div class="relative px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl text-lg mx-auto shadow-md p-2">
        <div class="flex bg-red-700 text-white text-xl"><img class="mr-2" width="28" src="../assets//img/time-and-calendar.png"/>{{this.post.published}}</div>
        <img :src="base + this.post.thumbnail" />
        
        <h1>
          <span class="mt-2 block text-3xl text-center leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">{{this.post.title}}</span>
        </h1>
        <p class="mt-8 text-2xl font-bold text-gray-700 leading-8">{{this.post.excerpt}}</p>
      
        <div class="mt-6 prose prose-indigo prose-lg text-gray-500 mx-auto">
          {{this.post.content}}
        </div>
      
      </div>
      
    </div>
  </div>
</template>

<script>

import HelloWorld from '@/components/HelloWorld.vue'
import {getAPI} from '../assets/js/api.js'

export default {
    
    name: 'PostDetailView',
    components: {
      HelloWorld
    },
    data(){
      return {
        post: {},
        base: getAPI.defaults.baseURL
      }
    },
    created(){
      
      getAPI.get(`/blog/posts/${this.$route.params.slug}`)
        .then(res=>{
          console.log('Post API has received data')
          this.post = res.data
        })
        .catch(err=>{
          console.log(err)
        })
    }
}
</script>

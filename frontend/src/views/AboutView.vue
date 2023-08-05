<template>
  <div class="p-10 mt-6">
    <HelloWorld msg="This is an about page"/>
  </div>
</template>

<script>
  import HelloWorld from '@/components/HelloWorld.vue';
  export default {
    name: 'AboutView',
    components: {
      HelloWorld
    }
  }
</script>

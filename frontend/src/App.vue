<template>
  <NavBar msg="JOIN"/> 
  <router-view/>
</template>

<script>
import NavBar from '@/components/navigation/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>


<style lang="scss">

</style>

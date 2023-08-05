  <template>
    <div class="font-sans antialiased" id="app">
        <nav class="flex items-center justify-between flex-wrap bg-gray-800 text-gray-300 p-6">
            <div class="flex items-center flex-no-shrink text-white mr-6">
            <img class="mr-4" src="../../assets/MEDIASOFT.png" width="80" />
            <span class="font-semibold text-xl tracking-tight"></span>
            </div>
            <div class="block sm:hidden">
            <button @click="toggle" class="flex items-center px-3 py-2 border rounded text-teal-lighter border-teal-light hover:text-white hover:border-white">
                <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
            </button>
            </div>
            <div :class="open ? 'block': 'hidden'" class="w-full flex-grow sm:flex sm:items-center sm:w-auto">
            <div class="text-sm sm:flex-grow">
                <router-link to="/" class="no-underline block mt-4 sm:inline-block sm:mt-0 text-lg text-gray-300 hover:text-white mr-4">
                Home
                </router-link>
                <router-link to="/about" class="no-underline block mt-4 sm:inline-block sm:mt-0 text-lg  text-gray-300 hover:text-white mr-4">
                About
                </router-link>
                <router-link to="/blog" class="no-underline block mt-4 sm:inline-block sm:mt-0 text-lg text-gray-300 hover:text-white mr-4">
                Blog
                </router-link>
            </div>
            <div>
                <a href="#" class="no-underline inline-block text-lg px-6 py-4 leading-none border rounded font-bold text-white border-white hover:border-transparent transition ease-in-out duration-300 hover:text-gray-300 bg-red-700 hover:bg-red-900 mt-4 sm:mt-0">{{msg}}</a>
            </div>
            </div>
        </nav>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NavBar',
    props: {
      msg: String
    },
    data() {
        return {
            open: false,
         }
    },
    methods: {
        toggle() {
            this.open = !this.open
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
  
  </style>
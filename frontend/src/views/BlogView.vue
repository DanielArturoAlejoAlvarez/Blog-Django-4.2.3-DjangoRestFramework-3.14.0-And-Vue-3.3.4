<template>
    <div class="blog">
        <HelloWorld msg="Our Blog App" />
    </div>
</template>

<script>

import HelloWorld from '@/components/HelloWorld.vue';

export default {
    name: 'BlogView',
    components: {
        HelloWorld
    }
}
</script>

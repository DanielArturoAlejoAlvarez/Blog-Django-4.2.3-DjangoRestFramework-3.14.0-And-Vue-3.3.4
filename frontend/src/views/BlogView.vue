<template>
    <div class="p-10 mt-6">
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

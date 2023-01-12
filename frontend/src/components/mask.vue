<template>
  <div class="mask"></div>
</template>

<script>
export default {
  name: "Mask"
}
</script>

<style scoped>

.mask {
  position: fixed;
  z-index: 9;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
}

</style>
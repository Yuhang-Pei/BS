<template>
  <div @click="changeStatus" class="switch" :class="switchStatus?'switchOn':'switchOff'">
    <div class="circle"></div>
  </div>
</template>

<script>
export default {
  name: "Switch",
  props: {
    switchStatus: {
      default: false
    }
  }
}
</script>

<style scoped>

.switch {
  position: relative;
  width: 42px;
  height: 20px;
  border-radius: 19px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.circle {
  position: absolute;
  top: 2px;
  width: 16px;
  height: 16px;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.25);
  transition: all 0.3s;
}

.switchOn {
  background-color: rgb(55, 204, 61);
}

.switchOn .circle {
  left: 24px;
}

.switchOn:hover {
  background-color: rgb(111, 218, 115);
}

.switchOff {
  background-color: rgb(200, 200, 200);
}

.switchOff .circle {
  left: 2px;
}

.switchOff:hover {
  background-color: rgb(175, 175, 175);
}

</style>
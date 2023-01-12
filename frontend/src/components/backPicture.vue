<template>
<!--  <div id="background"></div>-->
  <img :src="background">
</template>

<script>
import {global_data} from "@/store";
import p1 from '@/assets/backPicture/backPicture1.jpg'
import p2 from '@/assets/backPicture/backPicture2.jpg'
import p3 from '@/assets/backPicture/backPicture3.jpg'
import p4 from '@/assets/backPicture/backPicture4.jpg'
import p5 from '@/assets/backPicture/backPicture5.jpg'
import p6 from '@/assets/backPicture/backPicture6.jpg'

export default {
  name: "backPicture",
  data() {
    if (global_data.current_scenario.background_picture === 0)
      return {
        background: p1
      }
    if (global_data.current_scenario.background_picture === 1)
      return {
        background: p2
      }
    if (global_data.current_scenario.background_picture === 2)
      return {
        background: p3
      }
    if (global_data.current_scenario.background_picture === 3)
      return {
        background: p4
      }
    if (global_data.current_scenario.background_picture === 4)
      return {
        background: p5
      }
    if (global_data.current_scenario.background_picture === 5)
      return {
        background: p6
      }
  },
}
</script>

<style scoped>

#background {
  position: fixed;
  float: top;
  left: 0;
  top: 0;
  z-index: -10;
  width: 100%;
  height: 100%;
  background-size: cover;
}

img {
  position: fixed;
  float: top;
  left: 0;
  top: 0;
  z-index: -10;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

</style>
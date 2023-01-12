<template>
  <div id="staticsContainer" :class="{notAllClose: openCount!==0, allClose: openCount===0}">
    <img class="icon" src="@/assets/furnitureIcon/light.svg">
    <h1>灯具</h1>
    <h2 v-show="openCount !== 0">{{openCount}} 打开</h2>
    <h2 v-show="openCount === 0">全部关闭</h2>
  </div>
</template>

<script>
import {global_data, isObjectEmpty} from "@/store";

export default {
  name: "lightStatics",
  data() {
    return {
      openCount: 0
    }
  },
  created() {
    if (isObjectEmpty(global_data.light_list)) {
      this.$http.post('light/get_all_lights', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.light_list = res.data.light_list;
            this.getOpenCount();
          });
    }
    else
      this.getOpenCount();
  },
  methods: {
    getOpenCount() {
      for (let light in global_data.light_list)
        if (global_data.light_list[light].light_state)
          this.openCount += 1;
    }
  }
}
</script>

<style scoped>

#staticsContainer {
  display: inline-block;
  position: relative;
  height: 60px;
  width: 150px;
  border-radius: 35px;
  margin-right: 12px;
  margin-bottom: 12px;
  transition: all 0.3s;
  backdrop-filter: blur(15px);
}

.notAllClose {
  background-color: rgba(255, 255, 255, 0.8);
}

.allClose {
  background-color: rgba(56, 56, 56, 0.5);
}

.icon {
  position: absolute;
  left: 12px;
  top: 14px;
  width: 30px;
}

h1 {
  position: absolute;
  left: 50px;
  top: 9px;
  font-size: 18px;
}

.notAllClose h1 {
  color: rgb(5, 5, 5);
}

.allClose h1 {
  color: rgb(255, 255, 255);
}

h2 {
  position: absolute;
  left: 50px;
  top: 34px;
  font-size: 14px;
  font-weight: 500;
}

.notAllClose h2 {
  color: rgb(147, 143, 137);
}

.allClose h2 {
  color: rgb(220, 215, 205);
}

</style>
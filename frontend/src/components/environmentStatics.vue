<template>
  <div id="staticsContainer" :class="{openMain: open, closeMain: !open}">
    <img class="icon" src="@/assets/furnitureIcon/environment.svg">
    <h1>环境</h1>
    <h2 id="environmentValue">{{temperature}}℃ &nbsp{{humidity}}%</h2>
  </div>
</template>

<script>
import {global_data, isObjectEmpty} from "@/store";

export default {
  name: "environmentStatics",
  data() {
    return {
      temperature: '-',
      humidity: '-',
      open: false
    }
  },
  created() {
    if (isObjectEmpty(global_data.sensor_list)) {
      this.$http.post('sensor/get_all_sensors', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.sensor_list = res.data.sensor_list;
            for (let sensor_id in global_data.sensor_list) {
              if (global_data.sensor_list[sensor_id].is_main && global_data.sensor_list[sensor_id].sensor_state) {
                this.temperature = global_data.sensor_list[sensor_id].temperature;
                this.humidity = global_data.sensor_list[sensor_id].humidity;
                this.open = true;
                return;
              }
            }
          });
    }
    else {
      for (let sensor_id in global_data.sensor_list) {
        if (global_data.sensor_list[sensor_id].is_main && global_data.sensor_list[sensor_id].sensor_state) {
          this.temperature = global_data.sensor_list[sensor_id].temperature;
          this.humidity = global_data.sensor_list[sensor_id].humidity;
          this.open = true;
          return;
        }
      }
    }
  }
}
</script>

<style scoped>

#staticsContainer {
  display: inline-block;
  position: relative;
  height: 60px;
  width: 200px;
  border-radius: 35px;
  margin-right: 12px;
  margin-bottom: 12px;
  transition: all 0.3s;
  backdrop-filter: blur(15px);
}

.openMain {
  background-color: rgba(255, 255, 255, 0.8);
}

.closeMain {
  background-color: rgba(56, 56, 56, 0.5);
}

.icon {
  position: absolute;
  left: 11px;
  top: 15px;
  width: 32px;
}

h1 {
  position: absolute;
  left: 50px;
  top: 9px;
  font-size: 18px;
}

.openMain h1 {
  color: rgb(5, 5, 5);
}

.closeMain h1 {
  color: rgb(255, 255, 255);
}

h2 {
  position: absolute;
  left: 50px;
  top: 34px;
  font-size: 14px;
  font-weight: 500;
}

.openMain h2 {
  color: rgb(147, 143, 137);
}

.closeMain h2 {
  color: rgb(220, 215, 205);
}

</style>
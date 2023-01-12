<template>
  <div class="categorySensor">
    <h1>传感器</h1>
    <div v-if="format === 'info'" id="addIcon" @click="newSensor">
      <img class="newDevice" src="@/assets/utility/add1.svg">
    </div>
    <sensor-button v-if="format === 'button'"
                   v-for="(sensor, sensor_id) in sensor_list"
                   :sensor-id="sensor_id"
                   :sensor-name="sensor.device_name"
                   :sensor-status="sensor.sensor_state"
                   :sensor-temperature="sensor.temperature"
                   :sensor-humidity="sensor.humidity"
                   :is-main="sensor_id == current_main"
                   :sensor-room="sensor.room_name"
                   :key="sensor_change[sensor_id]"
                   @getCurrentMainSensor="getCurrentMainSensor">
    </sensor-button>

    <sensor-info v-if="format === 'info'"
                 v-for="(sensor, sensor_id) in sensor_list"
                 :ref="sensor_id"
                 :sensor-id="sensor_id"
                 :sensor-name="sensor.device_name"
                 :sensor-status="sensor.sensor_state"
                 :sensor-temperature="sensor.temperature"
                 :sensor-humidity="sensor.humidity"
                 :is-main="sensor_id == current_main"
                 :sensor-room="sensor.room_name"
                 @getCurrentMainSensor="getCurrentMainSensor">
    </sensor-info>
  </div>
</template>

<script>
import sensorButton from "@/components/sensorButton";
import SensorInfo from "@/components/sensorInfo";
import {global_data, isObjectEmpty} from "@/store";

export default {
  name: "categorySensor",
  components: {SensorInfo, sensorButton},
  props: {
    format: {
      required: true
    }
  },
  data() {
    return {
      sensor_list: {},
      current_main: -1,
      sensor_change: {}
    }
  },
  created() {
    if (isObjectEmpty(global_data.sensor_list)) {
      this.$http.post('sensor/get_all_sensors', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.sensor_list = global_data.sensor_list = res.data.sensor_list;
            for (let sensor_id in this.sensor_list) {
              this.sensor_change[sensor_id] = 0;
              if (this.sensor_list[sensor_id].is_main == true)
                this.current_main = sensor_id;
            }
            this.$emit('finishLoading', 2);
          });
    }
    else {
      this.sensor_list = global_data.sensor_list;
      for (let sensor_id in this.sensor_list) {
        this.sensor_change[sensor_id] = 0;
        if (this.sensor_list[sensor_id].is_main == true)
          this.current_main = sensor_id;
      }
      this.$emit('finishLoading', 2);
    }
  },
  methods: {
    getCurrentMainSensor(new_main_sensor) {
      if (new_main_sensor) {  // if the new main sensor exists
        if (this.current_main != -1) {  // the previous main sensor existed
          this.sensor_list[this.current_main].is_main = false;
          if (this.format === 'button')
            this.sensor_change[this.current_main] += 1;
          else
            this.$refs[this.current_main][0].passiveChangeMain()
        }
        this.sensor_list[new_main_sensor].is_main = true;
        this.current_main = new_main_sensor;
      }
      else {  // if the new main sensor does not exist, namely the previous main sensor is canceled
        this.sensor_list[this.current_main].is_main = false;
        this.current_main = -1;
      }
    },
    newSensor() {
      let room_id = Object.keys(global_data.room_list)[0];
      this.$http.post('/sensor/add_sensor', {
        'room_id': room_id
      }).then((res) => {
        let sensor_id = res.data.sensor_id;
        global_data.sensor_list[sensor_id] = {
          'sensor_state': false,
          'temperature':  null,
          'humidity':     null,
          'is_main':      false,
          'sensor_icon':  0,
          'device_name':  '传感器',
          'device_model': '',
          'device_x':     null,
          'device_y':     null,
          'room_id':      room_id,
          'room_name':    global_data.room_list[room_id],
          'scenario_id':  this.$cookies.get('scenario_id')
        };
        this.$router.push({
          path: '/sensorDetail',
          query: {
            id: sensor_id
          }
        })
      });
    }
  }
}
</script>

<style scoped>

.categorySensor {
  position: relative;
  margin-bottom: 31px;
}

.categorySensor h1 {
  color: white;
  font-size: 20px;
  margin-left: 5px;
  margin-bottom: 14px;
}

#addIcon {
  position: absolute;
  top: 0;
  left: 75px;
  cursor: pointer;
}

.newDevice {
  position: absolute;
  top: 2px;
  width: 22px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.newDevice:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

</style>
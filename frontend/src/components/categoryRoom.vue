<template>
  <div id="categoryRoom">
    <h1>{{room_name}}</h1>

    <light-button v-for="(light, light_id) in global_data.light_list"
                  v-show="type === 'light' && light.room_name == room_name"
                  :light-id="light_id"
                  :light-name="light.device_name"
                  :light-status="light.light_state"
                  :light-room="room_name"
                  :light-luminance="light.luminance">
    </light-button>

    <lock-button v-for="(lock, lock_id) in global_data.lock_list"
                 v-show="type === 'lock' && lock.room_name == room_name"
                 :lock-id="lock_id"
                 :lock-name="lock.device_name"
                 :lock-status="lock.lock_state"
                 :lock-room="lock.room_name">
    </lock-button>

    <sensor-button v-for="(sensor, sensor_id) in global_data.sensor_list"
                   v-show="type === 'sensor' && sensor.room_name == room_name"
                   @click="select(sensor_id)"
                   :sensor-id="sensor_id"
                   :sensor-name="sensor.device_name"
                   :sensor-status="sensor.sensor_state"
                   :sensor-temperature="sensor.temperature"
                   :sensor-humidity="sensor.humidity"
                   :is-main="sensor.is_main"
                   :sensor-room="sensor.room_name"
                   :key="sensor_keys[sensor_id]"
                   @deselect="deselect">
    </sensor-button>

    <switch-button v-for="(_switch, switch_id) in global_data.switch_list"
                   v-show="type === 'switch' && _switch.room_name == room_name"
                   :switch-id="switch_id"
                   :switch-name="_switch.device_name"
                   :switch-status="_switch.switch_state"
                   :switch-room="_switch.room_name">
    </switch-button>

  </div>
</template>

<script>
import {global_data} from "@/store";
import LightButton from "@/components/lightButton.vue";
import LockButton from "@/components/lockButton.vue";
import SensorButton from "@/components/sensorButton.vue";
import SwitchButton from "@/components/switchButton.vue";

export default {
  name: "categoryRoom",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {SwitchButton, SensorButton, LockButton, LightButton},
  props: {
    roomId: {
      required: true
    },
    type: {
      required: true,
      type: String
    }
  },
  mounted() {
    for (let i in global_data.sensor_list)
      this.sensor_keys[i] = 0;
    if (this.type === 'sensor') {
      setInterval(() => {
        this.updateSensorKeys();
      }, 2000);
    }
  },
  data() {
    return {
      room_name: global_data.room_list[this.roomId],
      sensor_keys: {},
      selected_sensor: -1
    }
  },
  methods: {
    updateSensorKeys() {
      for (let i in this.sensor_keys) {
        if (i != this.selected_sensor) {
          this.sensor_keys[i] += 1;
        }
      }
    },
    select(sensor_id) {
      if (this.selected_sensor === -1)
        this.selected_sensor = sensor_id;
    },
    deselect() {
      this.selected_sensor = -1;
    }
  }
}
</script>

<style scoped>

h1 {
  color: white;
  font-size: 20px;
  margin-bottom: 14px;
  margin-left: 5px;
}

</style>
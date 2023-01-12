<template>
  <back-picture></back-picture>
  <navigate :current-choice="parseInt(room_id)+8" @changeRoom="changeRoom"></navigate>

  <div class="main">
    <h1>
      {{room_name}}
      <svg @click="roomDetail" id="setting" viewBox="0 0 93 93" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill="white" d="M46.5 28.6328C36.1641 28.6328 27.6328 37.1641 27.6328 47.5C27.6328 57.8359 36.1641 66.3672 46.5 66.3672C56.8359 66.3672 65.3672 57.8359 65.3672 47.5C65.3672 37.1641 56.8359 28.6328 46.5 28.6328ZM46.5 61.4453C38.7891 61.4453 32.5547 55.2109 32.5547 47.5C32.5547 39.7891 38.7891 33.5547 46.5 33.5547C54.2109 33.5547 60.4453 39.7891 60.4453 47.5C60.4453 55.2109 54.2109 61.4453 46.5 61.4453Z"/>
        <path fill="white" d="M81.9375 53.7344C79.8047 52.4219 78.4922 50.125 78.4922 47.5C78.4922 44.875 79.8047 42.7422 81.9375 41.2656C83.414 40.2813 84.0703 38.4766 83.5781 36.6719C82.7578 33.8828 81.6093 31.2578 80.2968 28.7969C79.4765 27.3203 77.6718 26.3359 75.8672 26.8281C73.4062 27.3203 70.9453 26.6641 69.1406 24.8594C67.3359 23.0547 66.6797 20.5938 67.1718 18.1328C67.5 16.4922 66.6797 14.6875 65.2031 13.7031C62.7422 12.2266 59.9531 11.2422 57.3281 10.4219C55.6875 9.92969 53.7187 10.5859 52.7343 12.0625C51.4218 14.1953 49.125 15.5078 46.5 15.5078C43.875 15.5078 41.7422 14.1953 40.2656 12.0625C39.2812 10.5859 37.4765 9.92969 35.6718 10.4219C32.8828 11.2422 30.2578 12.3906 27.7968 13.7031C26.3203 14.5234 25.3359 16.3281 25.8281 18.1328C26.3203 20.5938 25.664 23.2188 23.8593 24.8594C22.0547 26.6641 19.5937 27.3203 17.1328 26.8281C15.4922 26.5 13.6875 27.3203 12.7031 28.7969C11.2265 31.2578 10.2422 34.0469 9.42184 36.6719C8.92966 38.3125 9.58591 40.2813 11.0625 41.2656C13.1953 42.5781 14.5078 44.875 14.5078 47.5C14.5078 50.125 13.1953 52.2578 11.0625 53.7344C9.58591 54.7188 8.92966 56.5234 9.42184 58.3281C10.2422 61.1172 11.3906 63.7422 12.7031 66.2031C13.5234 67.6797 15.3281 68.5 17.1328 68.1719C19.5937 67.6797 22.2187 68.3359 23.8593 70.1406C25.664 71.9453 26.3203 74.4063 25.8281 76.8672C25.5 78.5078 26.3203 80.3125 27.7968 81.2969C30.2578 82.7734 33.0468 83.7578 35.6718 84.5781C37.3125 85.0703 39.2812 84.4141 40.2656 82.9375C41.5781 80.8047 43.875 79.4922 46.5 79.4922C49.125 79.4922 51.2578 80.8047 52.7343 82.9375C53.5547 84.0859 54.8672 84.7422 56.1797 84.7422C56.5078 84.7422 57 84.7422 57.3281 84.5781C60.1172 83.7578 62.7422 82.6094 65.2031 81.2969C66.6797 80.4766 67.664 78.6719 67.1718 76.8672C66.6797 74.4063 67.3359 71.7813 69.1406 70.1406C70.9453 68.3359 73.4062 67.6797 75.8672 68.1719C77.5078 68.5 79.3125 67.6797 80.2968 66.2031C81.7734 63.7422 82.7578 60.9531 83.5781 58.3281C84.0703 56.5234 83.414 54.7188 81.9375 53.7344V53.7344ZM76.1953 63.25C72.2578 62.5938 68.3203 63.9063 65.5312 66.6953C62.7422 69.4844 61.4297 73.4219 62.0859 77.3594C60.2812 78.3438 58.3125 79.1641 56.3437 79.8203C54.0468 76.7031 50.4375 74.7344 46.3359 74.7344C42.3984 74.7344 38.789 76.5391 36.3281 79.8203C34.3593 79.1641 32.3906 78.3438 30.5859 77.3594C31.2422 73.4219 29.9297 69.4844 27.1406 66.6953C24.3515 63.9063 20.414 62.5938 16.4765 63.25C15.4922 61.4453 14.6718 59.4766 14.0156 57.5078C17.1328 55.2109 19.1015 51.6016 19.1015 47.5C19.1015 43.5625 17.2968 39.9531 14.0156 37.4922C14.6718 35.5234 15.4922 33.5547 16.4765 31.75C20.414 32.4063 24.3515 31.0937 27.1406 28.3047C29.9297 25.5156 31.2422 21.5781 30.5859 17.6406C32.3906 16.6563 34.3593 15.8359 36.3281 15.1797C38.625 18.2969 42.2343 20.2656 46.3359 20.2656C50.2734 20.2656 53.8828 18.4609 56.3437 15.1797C58.3125 15.8359 60.2812 16.6563 62.0859 17.6406C61.4297 21.5781 62.7422 25.5156 65.5312 28.3047C68.3203 31.0937 72.2578 32.4063 76.1953 31.75C77.1797 33.5547 78 35.5234 78.6562 37.4922C75.539 39.7891 73.5703 43.3984 73.5703 47.5C73.5703 51.4375 75.375 55.0469 78.6562 57.5078C78 59.4766 77.1797 61.4453 76.1953 63.25Z"/>
      </svg>
    </h1>

    <div v-show="isShowLight()">
      <h2 class="typeTitle">灯具</h2>
      <light-button v-for="(light, light_id) in global_data.light_list"
                    v-show="light.room_name == room_name"
                    :light-id="light_id"
                    :light-name="light.device_name"
                    :light-status="light.light_state"
                    :light-room="room_name"
                    :light-luminance="light.luminance">
      </light-button>
    </div>

    <div v-show="isShowLock()">
      <h2 class="typeTitle">锁</h2>
      <lock-button v-for="(lock, lock_id) in global_data.lock_list"
                   v-show="lock.room_name == room_name"
                   :lock-id="lock_id"
                   :lock-name="lock.device_name"
                   :lock-status="lock.lock_state"
                   :lock-room="lock.room_name">
      </lock-button>
    </div>

    <div v-show="isShowSensor()">
      <h2 class="typeTitle">传感器</h2>
      <sensor-button v-for="(sensor, sensor_id) in global_data.sensor_list"
                     v-show="sensor.room_name == room_name"
                     :sensor-id="sensor_id"
                     :sensor-name="sensor.device_name"
                     :sensor-status="sensor.sensor_state"
                     :sensor-temperature="sensor.temperature"
                     :sensor-humidity="sensor.humidity"
                     :is-main="sensor.is_main"
                     :sensor-room="sensor.room_name">
      </sensor-button>
    </div>

    <div v-show="isShowSwitch()">
      <h2 class="typeTitle">开关</h2>
      <switch-button v-for="(_switch, switch_id) in global_data.switch_list"
                     v-show="_switch.room_name == room_name"
                     :switch-id="switch_id"
                     :switch-name="_switch.device_name"
                     :switch-status="_switch.switch_state"
                     :switch-room="_switch.room_name">
      </switch-button>
    </div>

  </div>
</template>

<script>
import BackPicture from "@/components/backPicture.vue";
import Navigate from "@/components/navigate.vue";
import {global_data, isObjectEmpty} from "@/store";
import LightButton from "@/components/lightButton.vue";
import LockButton from "@/components/lockButton.vue";
import SensorButton from "@/components/sensorButton.vue";
import SwitchButton from "@/components/switchButton.vue";

export default {
  name: "roomView",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {SwitchButton, SensorButton, LockButton, LightButton, Navigate, BackPicture},
  data() {
    return {
      room_id: this.$route.query.id,
      room_name: ''
    }
  },
  created() {
    this.room_name = global_data.room_list[this.room_id];

    if (isObjectEmpty(global_data.light_list)) {
      this.$http.post('light/get_all_lights', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.light_list = res.data.light_list;
          });
    }

    if (isObjectEmpty(global_data.lock_list)) {
      this.$http.post('lock/get_all_locks', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.lock_list = res.data.lock_list;
          });
    }

    if (isObjectEmpty(global_data.sensor_list)) {
      this.$http.post('sensor/get_all_sensors', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.sensor_list = res.data.sensor_list;
          });
    }

    if (isObjectEmpty(global_data.switch_list)) {
      this.$http.post('switch/get_all_switches', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.switch_list = res.data.switch_list;
          });
    }
  },
  methods: {
    changeRoom(new_room_id) {
      this.room_id = new_room_id;
      this.room_name = global_data.room_list[this.room_id];
    },
    isShowLight() {
      for (let light in global_data.light_list)
        if (global_data.light_list[light].room_id == this.room_id)
          return true;
      return false;
    },
    isShowLock() {
      for (let lock in global_data.lock_list)
        if (global_data.lock_list[lock].room_id == this.room_id)
          return true;
      return false;
    },
    isShowSensor() {
      for (let sensor in global_data.sensor_list)
        if (global_data.sensor_list[sensor].room_id == this.room_id)
          return true;
      return false;
    },
    isShowSwitch() {
      for (let _switch in global_data.switch_list)
        if (global_data.switch_list[_switch].room_id == this.room_id)
          return true;
      return false;
    },
    roomDetail() {
      this.$router.push({
        path: '/roomDetail',
        query: {
          id: this.room_id
        }
      })
    }
  }
}
</script>

<style scoped>

.main {
  margin-left: 215px;
  padding: 30px 0 0 30px;
}

h1 {
  color: white;
  font-size: 26px;
  margin-left: 5px;
  margin-bottom: 22px;
}

h2 {
  color: white;
  font-size: 20px;
  margin-bottom: 14px;
  margin-left: 5px;
}

.tail {
  height: 160px;
  background-color: transparent;
}

#setting {
  float: right;
  width: 32px;
  transform: translateX(-20px);
  cursor: pointer;
}

</style>
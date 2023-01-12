<template>
  <Mask v-show="roomFocus" :class="{high: roomFocus}" @click="loseRoomFocus"></Mask>
  <div class="sensorInfo" :class="{sensorInfoOn:status, sensorInfoOff:!status, high: roomFocus}">
    <device-icon class="sensorIcon" type="sensor" :state="status" :index="sensor_icon"></device-icon>
<!--    <img class="sensorIcon" :src="require(status?'@/assets/furnitureIcon/sensor-on.svg':'@/assets/furnitureIcon/sensor-off.svg')">-->
    <h1>{{sensorName}}</h1>
    <svg @click="sensorDetail" class="moreButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <path d="M390.948571 897.462857a53.028571 53.028571 0 0 1-38.765714-16.091428 54.491429 54.491429 0 0 1 0-77.531429l288.914286-288.914286-288.914286-288.914285a54.491429 54.491429 0 0 1 0-77.531429 55.222857 55.222857 0 0 1 77.531429 0l365.714285 365.714286-365.714285 365.714285a54.125714 54.125714 0 0 1-38.765715 17.554286z"></path>
    </svg>

    <div class="sensorInfoRoomLine">
      <h3 id="sensorInfoRoomCaption">房间</h3>
      <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
      <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="sensorId"></room-list>
    </div>
    <div class="sensorInfoSwitchLine">
      <h3 id="sensorInfoSwitchCaption">开关</h3>
      <Switch class="sensorInfoSwitch" @click="changeSensorStatus" :switch-status="status"></Switch>
    </div>
    <div class="sensorInfoMainLine">
      <h3 id="sensorInfoSwitchCaption">主传感器</h3>
      <Switch class="sensorInfoSwitch" @click="changeMain" :switch-status="main"></Switch>
    </div>
    <div class="sensorInfoEnvironmentLine">
      <h3>环境</h3>
      <div class="environment">
        <div class="environmentTemperature">
          <div class="temperatureValue">{{temperature}}</div><div class="temperatureUnit">℃</div>
          <div class="sensorSubCaption">{{temperature==='-'?'':(temperature<10?'寒冷':(temperature>30?'炎热':(temperature<20?'凉爽':'温暖')))}}</div>
        </div>
        <div class="environmentHumidity">
          <div class="humidityValue">{{humidity}}</div><div class="humidityUnit">%</div>
          <div class="sensorSubCaption">{{humidity==='-'?'':(humidity<40?'干燥':(humidity>75?'潮湿':'舒适'))}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Switch from "@/components/switch";
import Mask from "@/components/mask.vue";
import {global_data} from "@/store";
import RoomList from "@/components/roomList.vue";
import DeviceIcon from "@/components/deviceIcon.vue";
export default {
  name: "sensorInfo",
  components: {DeviceIcon, Switch, Mask, RoomList},
  props: {
    "sensorId": {
      required: true
    },
    "sensorName": {
      required: true
    },
    "sensorStatus": {
      default: false
    },
    "sensorTemperature": {
      default: '-'
    },
    "sensorHumidity": {
      default: '-'
    },
    "sensorRoom": {
      required: true
    },
    "isMain": {
      default: false
    }
  },
  data() {
    return {
      status: this.sensorStatus,
      main: this.isMain,
      temperature: this.sensorTemperature,
      humidity: this.sensorHumidity,
      room_name: global_data.sensor_list[this.sensorId].room_name,
      room_id: global_data.sensor_list[this.sensorId].room_id,
      roomFocus: false,
      sensor_icon: global_data.sensor_list[this.sensorId].sensor_icon,
    }
  },
  mounted() {
    if (this.temperature === null)
      this.temperature = '-';
    if (this.humidity === null)
      this.humidity = '-';
  },
  methods: {
    changeSensorStatus() {
      this.$http.post('/sensor/change_sensor_state', {
        'sensor_id': this.sensorId,
        'sensor_state': this.status
      }).then((res) => {
        global_data.sensor_list[this.sensorId].temperature = this.temperature = (res.data.temperature === null) ? '-' : res.data.temperature;
        global_data.sensor_list[this.sensorId].humidity = this.humidity = (res.data.humidity === null) ? '-' : res.data.humidity;
      })

      global_data.sensor_list[this.sensorId].sensor_state = this.status = !this.status;
    },
    changeMain() {
      this.$http.post('/sensor/change_main_sensor', {
        'sensor_id': this.sensorId,
        'is_main': this.main,
        'scenario_id': this.$cookies.get('scenario_id')
      }).then((res) => {
        this.$emit('getCurrentMainSensor', res.data.current_main_sensor)
      })

      global_data.sensor_list[this.sensorId].is_main = this.main = !this.main;
    },
    sensorDetail() {
      this.$router.push({
        path: "/sensorDetail",
        query: {
          id: this.sensorId
        }
      });
    },
    passiveChangeMain() {
      this.main = false;
    },
    getRoomFocus() {
      this.roomFocus = true;
    },
    loseRoomFocus() {
      this.roomFocus = false;
    },
    changeRoom(new_room_id) {
      let new_room_name = global_data.room_list[new_room_id];
      global_data.sensor_list[this.sensorId].room_id = this.room_id = new_room_id;
      global_data.sensor_list[this.sensorId].room_name = this.room_name = new_room_name;
    }
  }
}
</script>

<style scoped>

/*Universal properties of sensor*/

.sensorInfo {
  display: inline-block;
  position: relative;
  margin-top: 0;
  margin-right: 12px;
  margin-bottom: 10px;
  width: 245px;
  height: 260px;
  border-radius: 13px;
  backdrop-filter: blur(15px);
  transition: all 0.3s;
}

.sensorIcon {
  position: absolute;
  left: 12px;
  top: 10px;
  width: 35px;
  height: 35px;
}

.sensorInfo h1 {
  position: absolute;
  left: 60px;
  top: 14px;
  font-size: 20px;
  font-weight: bolder;
}

.environment {
  position: absolute;
  text-align: center;
  color: rgb(29, 176, 239);
  left: 0;
  right: 0;
  margin: 10px auto 0;
}

.environmentTemperature, .environmentHumidity {
  display: inline-block;
  margin: 0 10px 0;
}

.environmentTemperature .temperatureValue,
.environmentTemperature .temperatureUnit,
.environmentHumidity .humidityValue,
.environmentHumidity .humidityUnit {
  display: inline;
}

.temperatureValue, .humidityValue {
  font-size: 40px;
}

.temperatureUnit, .humidityUnit {
  font-size: 25px;
}

.sensorSubCaption {
  color: rgb(147, 143, 137);
  font-size: 12px;
}

/*Properties of "on" sensor*/

.sensorInfoOn {
  background-color: rgba(255, 255, 255, 0.8);
}

.sensorInfoOn h1, .sensorInfoOff h3 {
  color: rgb(5, 5, 5);
}

.sensorInfoOn:hover {
  background-color: rgba(255, 255, 255, 0.95);
}

.sensorInfoRoomLine, .sensorInfoSwitchLine, .sensorInfoMainLine, .sensorInfoEnvironmentLine {
  position: relative;
  top: 65px;
  margin: 0 15px;
  height: 30px;
}

.roomValue {
  position: absolute;
  right: 0;
  top: 0;
  cursor: pointer;
  transition: color 0.3s;
}

.sensorInfoOn .roomValue {
  color: rgb(80, 80, 80);
}

.sensorInfoOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.sensorInfoOff .roomValue {
  color: rgb(220, 215, 205);
}

.sensorInfoOff .roomValue:hover {
  color: white;
}

.sensorInfoSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.sensorInfo h3 {
  font-size: 14px;
  font-weight: 500;
}

.moreButton {
  position: absolute;
  width: 22px;
  height: auto;
  right: 12px;
  top: 16px;
  fill: rgba(200, 200, 200, 0.95);
  cursor: pointer;
  transition: fill 0.3s;
}

.moreButton:hover {
  fill: rgb(29, 176, 239);
}

/*Properties of "off" sensor*/

.sensorInfoOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.sensorInfoOff h1, .sensorInfoOff h3 {
  color: rgb(255, 255, 255);
}

.sensorInfoOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

.high {
  z-index: 100;
}

</style>
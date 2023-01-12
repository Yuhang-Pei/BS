<template>
  <div class="sensorButtonWrapper" @mousedown="onDrag">
    <div @click="selectSensorButton" class="sensorButton" :class="{sensorButtonSelected:selected, sensorButtonTransition:transition, sensorButtonOn:status, sensorButtonOff:!status}">
      <!--  Original button elements  -->
      <device-icon class="sensorIcon" type="sensor" :state="status" :index="sensor_icon"></device-icon>
<!--      <img class="sensorIcon" :src="require(status?'@/assets/furnitureIcon/sensor-on.svg':'@/assets/furnitureIcon/sensor-off.svg')">-->
      <!--  Extended button elements  -->
      <h1 class="fade" :class="{'hide':transition||!selected}">{{sensorName}}</h1>
      <h2 class="fade" :class="{'hide':transition||!selected}">{{(sensorRoom) + ' | ' + (status?'Open':'Close')}}</h2>
      <svg class="fade closeButton" :class="{'hide':transition||!selected}" @click="deselectSensorButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <path :fill="status?'rgba(210, 210, 210, 0.95)':'rgba(200, 200, 200, 0.95)'" d="M512 64c-247.00852 0-448 200.960516-448 448S264.960516 960 512 960c247.00852 0 448-200.960516 448-448S759.039484 64 512 64zM694.752211 649.984034c12.480043 12.54369 12.447359 32.768069-0.063647 45.248112-6.239161 6.208198-14.399785 9.34412-22.591372 9.34412-8.224271 0-16.415858-3.135923-22.65674-9.407768l-137.60043-138.016718-138.047682 136.576912c-6.239161 6.14455-14.368821 9.247789-22.496761 9.247789-8.255235 0-16.479505-3.168606-22.751351-9.504099-12.416396-12.576374-12.320065-32.800753 0.25631-45.248112l137.887703-136.384249-137.376804-137.824056c-12.480043-12.512727-12.447359-32.768069 0.063647-45.248112 12.512727-12.512727 32.735385-12.447359 45.248112 0.063647l137.567746 137.984034 138.047682-136.575192c12.54369-12.447359 32.831716-12.320065 45.248112 0.25631 12.447359 12.576374 12.320065 32.831716-0.25631 45.248112L557.344443 512.127295 694.752211 649.984034z"></path>
      </svg>
      <div class="fade sensorButtonRoomLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>房间</h3>
        <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
        <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="sensorId"></room-list>
      </div>
      <div class="fade sensorButtonSwitchLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>开关</h3>
        <Switch class="sensorButtonSwitch" @click="changeSensorStatus" :switch-status="status"></Switch>
      </div>
      <div class="fade sensorButtonMainLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>主传感器</h3>
        <Switch class="sensorButtonSwitch" @click="changeMain" :switch-status="main"></Switch>
      </div>
      <div class="fade sensorButtonEnvironmentLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
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
  </div>
  <Mask :class="{'hide':!selected}" @click="deselectSensorButton"></Mask>
</template>

<script>
import Switch from "@/components/switch";
import Mask from "@/components/mask";
import {global_data} from "@/store";
import RoomList from "@/components/roomList.vue";
import DeviceIcon from "@/components/deviceIcon.vue";

export default {
  name: "sensorInteractionIcon",
  components: {DeviceIcon, RoomList, Mask, Switch},
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
    "sensorRoom": {
      required: true
    },
    "sensorTemperature": {
      default: '-'
    },
    "sensorHumidity": {
      default: '-'
    },
    "isMain": {
      default: false
    },
    "canvasWidth": {
      required: true
    },
    "canvasHeight": {
      required: true
    },
    "canvasEdit": {
      default: false
    },
    "sensorX": {
      required: true
    },
    "sensorY": {
      required: true
    }
  },
  data() {
    return {
      status: this.sensorStatus,
      temperature: (this.sensorTemperature == null ? '-' : this.sensorTemperature),
      humidity: (this.sensorHumidity == null ? '-' : this.sensorHumidity),
      main: this.isMain,
      selected: false,
      transition: false,
      edit: this.canvasEdit,
      X: this.sensorX + 'px',
      Y: this.sensorY + 'px',

      room_name: global_data.sensor_list[this.sensorId].room_name,
      room_id: global_data.sensor_list[this.sensorId].room_id,
      roomFocus: false,
      sensor_icon: global_data.sensor_list[this.sensorId].sensor_icon,
    }
  },
  methods: {
    selectSensorButton() {
      if (!this.edit && !this.selected) {
        this.z_index = 10;
        this.selected = true;
      }
    },
    deselectSensorButton() {
      this.transition = true;
      this.roomFocus = false;
      setTimeout(() => {
        this.transition = false;
        this.selected = false;
      }, 300);
    },
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
    onDrag(e) {
      e.preventDefault();
      if (this.edit) {
        let icon = e.currentTarget;
        const x = e.clientX - icon.offsetLeft;
        const y = e.clientY - icon.offsetTop;
        const maxWidth = this.canvasWidth - 40;
        const maxHeight = this.canvasHeight - 40;
        let left, top;

        document.onmousemove = (event) => {
          left = event.clientX - x;
          top = event.clientY - y;

          if (left < 0)
            left = 0;
          else if (left > maxWidth)
            left = maxWidth;
          if (top < 0)
            top = 0;
          else if (top > maxHeight)
            top = maxHeight;

          icon.style.left = left + 'px';
          icon.style.top = top + 'px';
        }

        document.onmouseup = () => {
          icon.style.cursor = 'default';
          document.onmousemove = null;
          document.onmouseup = null;
          this.X = left + 'px';
          this.Y = top + 'px';

          global_data.sensor_list[this.sensorId].device_x = left;
          global_data.sensor_list[this.sensorId].device_y = top;
          this.$emit('changePosition', 1, this.sensorId, left, top);
        }
      }
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

.sensorButtonWrapper {
  position: absolute;
  left: v-bind(X);
  top: v-bind(Y);
  margin-top: 0;
  width: 40px;
  height: 40px;
}

.sensorButton {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  backdrop-filter: blur(15px);
  cursor: pointer;
  transition-property: background-color, height, width, border-radius;
  transition-duration: 0.3s;
}

.sensorIcon {
  position: absolute;
  left: 0;
  top: 0;
  width: 40px;
  height: 40px;
  transition: all 0.3s;
}

.sensorButton h1 {
  position: absolute;
  left: 65px;
  top: 8px;
  width: 120px;
  font-size: 17px;
  font-weight: bolder;
}

.sensorButton h2 {
  position: absolute;
  left: 65px;
  top: 31px;
  font-size: 13px;
  font-weight: 500;
}

/*Properties of "on" button*/

.sensorButtonOn {
  background-color: rgb(255, 255, 255);
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.05);
}

.sensorButtonOn h1, .sensorButtonOff h3 {
  color: rgb(5, 5, 5);
}

.sensorButtonOn h2 {
  color: rgb(147, 143, 137);
}

.sensorButtonOn:hover {
  cursor: pointer;
}

/*Properties of "off" button*/

.sensorButtonOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.sensorButtonOff h1, .sensorButtonOff h3 {
  color: rgb(255, 255, 255);
}

.sensorButtonOff h2 {
  color: rgb(220, 215, 205);
}

.sensorButtonOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

/*Properties of selected button*/

.sensorButtonSelected {
  z-index: 10;
  width: 245px;
  height: 260px;
  border-radius: 13px;
  cursor: default !important;
}

.sensorButtonSelected .sensorIcon {
  position: absolute;
  left: 12px;
  top: 7px;
  width: 40px;
  height: 40px;
}

.sensorButtonRoomLine, .sensorButtonSwitchLine, .sensorButtonMainLine, .sensorButtonEnvironmentLine {
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

.sensorButtonOn .roomValue {
  color: rgb(80, 80, 80);
}

.sensorButtonOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.sensorButtonOff .roomValue {
  color: rgb(220, 215, 205);
}

.sensorButtonOff .roomValue:hover {
  color: white;
}

.sensorButtonSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.sensorButton h3 {
  font-size: 14px;
  font-weight: 500;
}

.environment {
  position: absolute;
  text-align: center;
  color: rgb(29, 176, 239);
  left: 0;
  right: 0;
  width: 215px;
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

.closeButton {
  position: absolute;
  width: 30px;
  height: auto;
  right: 15px;
  top: 12px;
  cursor: pointer;
}

/*Properties of animation*/

.sensorButtonTransition {
  z-index: 10;
  height: 40px;
  width: 40px;
  border-radius: 20px;
}

.sensorButtonTransition .sensorIcon {
  z-index: 10;
  top: 0;
  left: 0;
}

.fade {
  transition: all 0.3s;
}

.hide {
  opacity: 0;
  pointer-events: none;
}

.translateY {
  transform: translateY(-30px);
}

</style>
<template>
  <Mask v-show="roomFocus" :class="{high: roomFocus}" @click="loseRoomFocus"></Mask>
  <div class="lightInfo" :class="{lightInfoOn:status, lightInfoOff:!status, high: roomFocus}">
    <device-icon class="lightIcon" type="light" :state="status" :index="light_icon"></device-icon>
<!--    <img class="lightIcon" :src="require(status?'@/assets/furnitureIcon/light-on.svg':'@/assets/furnitureIcon/light-off.svg')">-->
    <h1>{{lightName}}</h1>
    <svg @click="lightDetail" class="moreButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <path d="M390.948571 897.462857a53.028571 53.028571 0 0 1-38.765714-16.091428 54.491429 54.491429 0 0 1 0-77.531429l288.914286-288.914286-288.914286-288.914285a54.491429 54.491429 0 0 1 0-77.531429 55.222857 55.222857 0 0 1 77.531429 0l365.714285 365.714286-365.714285 365.714285a54.125714 54.125714 0 0 1-38.765715 17.554286z"></path>
    </svg>

    <div class="lightInfoRoomLine">
      <h3 id="lightInfoRoomCaption">房间</h3>
      <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
      <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="lightId"></room-list>
    </div>
    <div class="lightInfoSwitchLine">
      <h3 id="lightInfoSwitchCaption">开关</h3>
      <Switch class="lightInfoSwitch" @click="changeLightStatus" :switch-status="status"></Switch>
    </div>
    <div class="lightInfoLuminanceLine">
      <h3 id="lightInfoLuminanceCaption">亮度</h3>
      <light-slider @changeLuminance="changeLuminance" class="lightInfoSlider" :luminance="luminance" :key="status"
                    :slider-front-color="status?'rgb(255, 207, 8)':'rgb(150, 150, 150)'"
                    :slider-back-color="status?'rgba(220, 220, 220, 0.95)':'rgba(200, 200, 200, 0.95)'"></light-slider>
    </div>
  </div>
</template>

<script>
import Switch from "@/components/switch";
import LightSlider from "@/components/lightSlider";
import {global_data} from "@/store";
import RoomList from "@/components/roomList.vue";
import Mask from "@/components/mask.vue";
import DeviceIcon from "@/components/deviceIcon.vue";

export default {
  name: "lightInfo",
  components: {DeviceIcon, Mask, LightSlider, Switch, RoomList},
  props: {
    "lightId": {
      required: true
    },
    "lightName": {
      required: true
    },
    "lightStatus": {
      default: false
    },
    "lightLuminance": {
      default: 0
    },
    "lightRoom": {
      required: true
    }
  },
  data() {
    return {
      status: this.lightStatus,
      luminance: this.lightLuminance,
      room_name: global_data.light_list[this.lightId].room_name,
      room_id: global_data.light_list[this.lightId].room_id,
      light_icon: global_data.light_list[this.lightId].light_icon,
      roomFocus: false
    }
  },
  methods: {
    changeLightStatus() {
      this.$http.post('/light/change_light_state', {
        'light_id': this.lightId,
        'light_state': this.status
      });

      this.status = !this.status;
      global_data.light_list[this.lightId].light_state = this.status;
    },
    changeLuminance(new_luminance) {
      this.$http.post('/light/change_light_luminance', {
        'light_id': this.lightId,
        'luminance': new_luminance
      });

      this.luminance = global_data.light_list[this.lightId].luminance = new_luminance;
    },
    lightDetail() {
      this.$router.push({
        path: "/lightDetail",
        query: {
          id: this.lightId
        }
      });
    },
    getRoomFocus() {
      this.roomFocus = true;
    },
    loseRoomFocus() {
      this.roomFocus = false;
    },
    changeRoom(new_room_id) {
      let new_room_name = global_data.room_list[new_room_id];
      global_data.light_list[this.lightId].room_id = this.room_id = new_room_id;
      global_data.light_list[this.lightId].room_name = this.room_name = new_room_name;
    }
  }
}
</script>

<style scoped>

/*Universal properties of light*/

.lightInfo {
  display: inline-block;
  position: relative;
  margin-top: 0;
  margin-right: 12px;
  margin-bottom: 10px;
  width: 245px;
  height: 195px;
  border-radius: 13px;
  backdrop-filter: blur(15px);
  transition: all 0.3s;
}

.lightIcon {
  position: absolute;
  left: 12px;
  top: 10px;
  width: 35px;
  height: 35px;
}

.lightInfo h1 {
  position: absolute;
  left: 60px;
  top: 14px;
  font-size: 20px;
  font-weight: bolder;
}

.lightInfo h2 {
  position: absolute;
  left: 65px;
  top: 31px;
  font-size: 13px;
  font-weight: 500;
}

/*Properties of "on" light*/

.lightInfoOn {
  background-color: rgba(255, 255, 255, 0.8);
}

.lightInfoOn h1, .lightInfoOff h3 {
  color: rgb(5, 5, 5);
}

.lightInfoOn h2 {
  color: rgb(147, 143, 137);
}

.lightInfoOn:hover {
  background-color: rgba(255, 255, 255, 0.95);
}

.lightInfoRoomLine, .lightInfoSwitchLine  {
  position: relative;
  top: 68px;
  margin: 0 15px;
  height: 30px;
}

.roomValue {
  position: absolute;
  right: 0;
  top: -1px;
  cursor: pointer;
  transition: color 0.3s;
}

.lightInfoOn .roomValue {
  color: rgb(80, 80, 80);
}

.lightInfoOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.lightInfoOff .roomValue {
  color: rgb(220, 215, 205);
}

.lightInfoOff .roomValue:hover {
  color: white;
}

.lightInfoLuminanceLine {
  position: relative;
  top: 68px;
  margin: 0 15px;
  height: 52px;
}

.lightInfoSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.lightInfoSlider {
  position: absolute;
  bottom: 0;
}

.lightInfo h3 {
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
  fill: rgb(255, 207, 8);
}

/*Properties of "off" light*/

.lightInfoOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.lightInfoOff h1, .lightInfoOff h3 {
  color: rgb(255, 255, 255);
}

.lightInfoOff h2 {
  color: rgb(220, 215, 205);
}

.lightInfoOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

.high {
  z-index: 100;
}

</style>
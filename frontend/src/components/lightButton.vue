<template>
  <div class="lightButtonWrapper">
    <div @click="selectLightButton" class="lightButton" :class="{lightButtonSelected:selected, lightButtonTransition:transition, lightButtonOn:status, lightButtonOff:!status}">
      <!--  Original button elements  -->
      <device-icon class="lightIcon" type="light" :state="status" :index="light_icon"></device-icon>
<!--      <img class="lightIcon" :src="require(status?('@/assets/furnitureIcon/light-on.svg'):'@/assets/furnitureIcon/light-off.svg')">-->
      <h1>{{lightName}}</h1>
      <h2>{{(room_name) + ' | ' + (status?'On':'Off')}}</h2>
      <!--  Extended button elements  -->
      <svg class="fade closeButton" :class="{'hide':transition||!selected}" @click="deselectLightButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <path fill="rgba(200, 200, 200, 0.95)" d="M512 64c-247.00852 0-448 200.960516-448 448S264.960516 960 512 960c247.00852 0 448-200.960516 448-448S759.039484 64 512 64zM694.752211 649.984034c12.480043 12.54369 12.447359 32.768069-0.063647 45.248112-6.239161 6.208198-14.399785 9.34412-22.591372 9.34412-8.224271 0-16.415858-3.135923-22.65674-9.407768l-137.60043-138.016718-138.047682 136.576912c-6.239161 6.14455-14.368821 9.247789-22.496761 9.247789-8.255235 0-16.479505-3.168606-22.751351-9.504099-12.416396-12.576374-12.320065-32.800753 0.25631-45.248112l137.887703-136.384249-137.376804-137.824056c-12.480043-12.512727-12.447359-32.768069 0.063647-45.248112 12.512727-12.512727 32.735385-12.447359 45.248112 0.063647l137.567746 137.984034 138.047682-136.575192c12.54369-12.447359 32.831716-12.320065 45.248112 0.25631 12.447359 12.576374 12.320065 32.831716-0.25631 45.248112L557.344443 512.127295 694.752211 649.984034z"></path>
      </svg>
      <div class="fade lightButtonRoomLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3 class="fade">房间</h3>
        <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
        <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="lightId"></room-list>
      </div>
      <div class="fade lightButtonSwitchLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>开关</h3>
        <Switch class="lightButtonSwitch" @click="changeLightStatus" :switch-status="status"></Switch>
      </div>
      <div class="fade lightButtonLuminanceLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>亮度</h3>
        <light-slider @changeLuminance="changeLuminance" class="lightButtonSlider" :luminance="luminance" :key="status"
                      :slider-front-color="status?'rgb(255, 207, 8)':'rgb(150, 150, 150)'"
                      :slider-back-color="status?'rgba(220, 220, 220, 0.95)':'rgba(200, 200, 200, 0.95)'"></light-slider>
      </div>
    </div>
    <Mask :class="{'hide':!selected}" @click="deselectLightButton"></Mask>
  </div>
</template>

<script>
import Switch from "@/components/switch";
import Mask from "@/components/mask";
import LightSlider from "@/components/lightSlider";
import {global_data} from "@/store";
import RoomList from "@/components/roomList.vue";
import DeviceIcon from "@/components/deviceIcon.vue";

export default {
  name: "lightButton",
  components: {DeviceIcon, RoomList, LightSlider, Mask, Switch},
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
    "lightSelected": {
      default: false
    },
    "lightRoom": {
      required: true
    }
  },
  data() {
    return {
      status: this.lightStatus,
      luminance: this.lightLuminance,
      selected: this.lightSelected,
      room_name: global_data.light_list[this.lightId].room_name,
      room_id: global_data.light_list[this.lightId].room_id,

      transition: false,
      roomFocus: false,

      light_icon: global_data.light_list[this.lightId].light_icon,
    }
  },
  methods: {
    selectLightButton() {
      if (this.selected === false) {
        this.z_index = 10;
        this.selected = true;
      }
    },
    deselectLightButton() {
      this.transition = true;
      setTimeout(() => {
        this.transition = false;
        this.selected = false;
        this.roomFocus = false;
      }, 300);
    },
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

.lightButtonWrapper {
  display: inline-block;
  position: relative;
  margin-top: 0;
  margin-right: 12px;
  margin-bottom: 10px;
  width: 245px;
  height: 55px;
}

.lightButton {
  position: relative;
  width: 245px;
  height: 55px;
  border-radius: 13px;
  backdrop-filter: blur(15px);
  cursor: pointer;
  transition-property: background-color, height;
  transition-duration: 0.3s;
}

.lightIcon {
  position: absolute;
  left: 12px;
  top: 7px;
  width: 40px;
  height: 40px;
}

.lightButton h1 {
  position: absolute;
  left: 65px;
  top: 8px;
  font-size: 17px;
  font-weight: bolder;
}

.lightButton h2 {
  position: absolute;
  left: 65px;
  top: 31px;
  font-size: 13px;
  font-weight: 500;
}

/*Properties of "on" button*/

.lightButtonOn {
  background-color: rgba(255, 255, 255, 0.8);
}

.lightButtonOn h1, .lightButtonOff h3 {
  color: rgb(5, 5, 5);
}

.lightButtonOn h2 {
  color: rgb(147, 143, 137);
}

.lightButtonOn:hover {
  background-color: rgba(255, 255, 255, 0.95);
  cursor: pointer;
}

/*Properties of "off" button*/

.lightButtonOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.lightButtonOff h1, .lightButtonOff h3 {
  color: rgb(255, 255, 255);
}

.lightButtonOff h2 {
  color: rgb(220, 215, 205);
}

.lightButtonOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

/*Properties of selected button*/

.lightButtonSelected {
  z-index: 10;
  height: 195px;
  cursor: default !important;
}

.lightButtonSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.lightButtonSlider {
  position: absolute;
  bottom: 0;
}

.lightButton h3 {
  position: absolute;
  font-size: 14px;
  font-weight: 500;
}

.lightButtonRoomLine, .lightButtonSwitchLine {
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

.lightButtonOn .roomValue {
  color: rgb(80, 80, 80);
}

.lightButtonOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.lightButtonOff .roomValue {
  color: rgb(220, 215, 205);
}

.lightButtonOff .roomValue:hover {
  color: white;
}

.lightButtonLuminanceLine {
  position: relative;
  top: 68px;
  margin: 0 15px;
  height: 52px;
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

.lightButtonTransition {
  z-index: 10;
  height: 55px;
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
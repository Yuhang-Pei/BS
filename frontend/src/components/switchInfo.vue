<template>
  <Mask v-show="roomFocus" :class="{high: roomFocus}" @click="loseRoomFocus"></Mask>
  <div class="switchInfo" :class="{switchInfoOn:status, switchInfoOff:!status, high: roomFocus}">
    <device-icon class="switchIcon" type="switch" :state="status" :index="switch_icon"></device-icon>
<!--    <img class="switchIcon" :src="require(status?'@/assets/furnitureIcon/switch-on.svg':'@/assets/furnitureIcon/switch-off.svg')">-->
    <h1>{{switchName}}</h1>
    <svg @click="switchDetail" class="moreButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <path d="M390.948571 897.462857a53.028571 53.028571 0 0 1-38.765714-16.091428 54.491429 54.491429 0 0 1 0-77.531429l288.914286-288.914286-288.914286-288.914285a54.491429 54.491429 0 0 1 0-77.531429 55.222857 55.222857 0 0 1 77.531429 0l365.714285 365.714286-365.714285 365.714285a54.125714 54.125714 0 0 1-38.765715 17.554286z"></path>
    </svg>

    <div class="switchInfoRoomLine">
      <h3 id="switchInfoRoomCaption">房间</h3>
      <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
      <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="switchId"></room-list>
    </div>
    <div class="switchInfoSwitchLine">
      <h3 id="switchInfoSwitchCaption">开关</h3>
      <Switch class="switchInfoSwitch" @click="changeSwitchStatus" :switch-status="status"></Switch>
    </div>
  </div>
</template>

<script>
import Switch from "@/components/switch";
import {global_data} from "@/store";
import Mask from "@/components/mask.vue";
import RoomList from "@/components/roomList.vue";
import DeviceIcon from "@/components/deviceIcon.vue";
export default {
  name: "switchInfo",
  components: {DeviceIcon, RoomList, Mask, Switch},
  props: {
    "switchId": {
      required: true
    },
    "switchName": {
      required: true
    },
    "switchStatus": {
      default: false
    },
    "switchRoom": {
      required: true
    }
  },
  data() {
    return {
      status: this.switchStatus,
      room_name: global_data.switch_list[this.switchId].room_name,
      room_id: global_data.switch_list[this.switchId].room_id,
      roomFocus: false,
      switch_icon: global_data.switch_list[this.switchId].switch_icon,
    }
  },
  methods: {
    changeSwitchStatus() {
      this.$http.post('/switch/change_switch_state', {
        'switch_id': this.switchId,
        'switch_state': this.status
      });

      this.status = !this.status;
      global_data.switch_list[this.switchId].switch_state = this.status;
    },
    switchDetail() {
      this.$router.push({
        path: "/switchDetail",
        query: {
          id: this.switchId
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
      global_data.switch_list[this.switchId].room_id = this.room_id = new_room_id;
      global_data.switch_list[this.switchId].room_name = this.room_name = new_room_name;
    }
  }
}
</script>

<style scoped>

/*Universal properties of switch*/

.switchInfo {
  display: inline-block;
  position: relative;
  margin-top: 0;
  margin-right: 12px;
  margin-bottom: 10px;
  width: 245px;
  height: 125px;
  border-radius: 13px;
  backdrop-filter: blur(15px);
  transition: all 0.3s;
}

.switchIcon {
  position: absolute;
  left: 12px;
  top: 10px;
  width: 35px;
  height: 35px;
}

.switchInfo h1 {
  position: absolute;
  left: 60px;
  top: 14px;
  font-size: 20px;
  font-weight: bolder;
}

.switchInfo h2 {
  position: absolute;
  left: 65px;
  top: 31px;
  font-size: 13px;
  font-weight: 500;
}

/*Properties of "on" switch*/

.switchInfoOn {
  background-color: rgba(255, 255, 255, 0.8);
}

.switchInfoOn h1, .switchInfoOff h3 {
  color: rgb(5, 5, 5);
}

.switchInfoOn h2 {
  color: rgb(147, 143, 137);
}

.switchInfoOn:hover {
  background-color: rgba(255, 255, 255, 0.95);
}

.switchInfoRoomLine, .switchInfoSwitchLine  {
  position: relative;
  top: 63px;
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

.switchInfoOn .roomValue {
  color: rgb(80, 80, 80);
}

.switchInfoOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.switchInfoOff .roomValue {
  color: rgb(220, 215, 205);
}

.switchInfoOff .roomValue:hover {
  color: white;
}

.switchInfoSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.switchInfo h3 {
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
  fill: rgb(55, 204, 61);
}

/*Properties of "off" switch*/

.switchInfoOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.switchInfoOff h1, .switchInfoOff h3 {
  color: rgb(255, 255, 255);
}

.switchInfoOff h2 {
  color: rgb(220, 215, 205);
}

.switchInfoOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

.high {
  z-index: 100;
}

</style>
<template>
  <Mask v-show="roomFocus" :class="{high: roomFocus}" @click="loseRoomFocus"></Mask>
  <div class="lockInfo" :class="{lockInfoOn:status, lockInfoOff:!status, high: roomFocus}">
    <device-icon class="lockIcon" type="lock" :state="status" :index="lock_icon"></device-icon>
<!--    <img class="lockIcon" :src="require(status?'@/assets/furnitureIcon/lock-on.svg':'@/assets/furnitureIcon/lock-off.svg')">-->
    <h1>{{lockName}}</h1>
    <svg @click="lockDetail" class="moreButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <path d="M390.948571 897.462857a53.028571 53.028571 0 0 1-38.765714-16.091428 54.491429 54.491429 0 0 1 0-77.531429l288.914286-288.914286-288.914286-288.914285a54.491429 54.491429 0 0 1 0-77.531429 55.222857 55.222857 0 0 1 77.531429 0l365.714285 365.714286-365.714285 365.714285a54.125714 54.125714 0 0 1-38.765715 17.554286z"></path>
    </svg>

    <div class="lockInfoRoomLine">
      <h3 id="lockInfoRoomCaption">房间</h3>
      <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
      <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="lockId"></room-list>
    </div>
    <div class="lockInfoSwitchLine">
      <h3 id="lockInfoSwitchCaption">开关</h3>
      <Switch class="lockInfoSwitch" @click="changeLockStatus" :switch-status="status"></Switch>
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
  name: "lockInfo",
  components: {DeviceIcon, Mask, Switch, RoomList},
  props: {
    "lockId": {
      required: true
    },
    "lockName": {
      required: true
    },
    "lockStatus": {
      default: false
    },
    "lockRoom": {
      required: true
    }
  },
  data() {
    return {
      status: this.lockStatus,
      room_name: global_data.lock_list[this.lockId].room_name,
      room_id: global_data.lock_list[this.lockId].room_id,
      roomFocus: false,
      lock_icon: global_data.lock_list[this.lockId].lock_icon,
    }
  },
  methods: {
    changeLockStatus() {
      this.$http.post('/lock/change_lock_state', {
        'lock_id': this.lockId,
        'lock_state': this.status
      });

      this.status = !this.status;
      global_data.lock_list[this.lockId].lock_state = this.status;
    },
    lockDetail() {
      this.$router.push({
        path: "/lockDetail",
        query: {
          id: this.lockId
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
      global_data.lock_list[this.lockId].room_id = this.room_id = new_room_id;
      global_data.lock_list[this.lockId].room_name = this.room_name = new_room_name;
    }
  }
}
</script>

<style scoped>

/*Universal properties of lock*/

.lockInfo {
  z-index: 18;
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

.lockIcon {
  position: absolute;
  left: 12px;
  top: 10px;
  width: 35px;
  height: 35px;
}

.lockInfo h1 {
  position: absolute;
  left: 60px;
  top: 14px;
  font-size: 20px;
  font-weight: bolder;
}

.lockInfo h2 {
  position: absolute;
  left: 65px;
  top: 31px;
  font-size: 13px;
  font-weight: 500;
}

/*Properties of "on" lock*/

.lockInfoOn {
  background-color: rgba(255, 255, 255, 0.8);
}

.lockInfoOn h1, .lockInfoOff h3 {
  color: rgb(5, 5, 5);
}

.lockInfoOn h2 {
  color: rgb(147, 143, 137);
}

.lockInfoOn:hover {
  background-color: rgba(255, 255, 255, 0.95);
}

.lockInfoRoomLine, .lockInfoSwitchLine  {
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

.lockInfoOn .roomValue {
  color: rgb(80, 80, 80);
}

.lockInfoOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.lockInfoOff .roomValue {
  color: rgb(220, 215, 205);
}

.lockInfoOff .roomValue:hover {
  color: white;
}

.lockInfoSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.lockInfo h3 {
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
  fill: rgb(107, 231, 230);
}

/*Properties of "off" lock*/

.lockInfoOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.lockInfoOff h1, .lockInfoOff h3 {
  color: rgb(255, 255, 255);
}

.lockInfoOff h2 {
  color: rgb(220, 215, 205);
}

.lockInfoOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

.high {
  z-index: 100;
}

</style>
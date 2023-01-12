<template>
  <div class="switchButtonWrapper" @mousedown="onDrag">
    <div @click="selectSwitchButton" class="switchButton" :class="{switchButtonSelected:selected, switchButtonTransition:transition, switchButtonOn:status, switchButtonOff:!status}">
      <!--  Original button elements  -->
      <device-icon class="switchIcon" type="switch" :state="status" :index="switch_icon"></device-icon>
<!--      <img class="switchIcon" :src="require(status?'@/assets/furnitureIcon/switch-on.svg':'@/assets/furnitureIcon/switch-off.svg')">-->
      <!--  Extended button elements  -->
      <h1 class="fade" :class="{'hide':transition||!selected}">{{switchName}}</h1>
      <h2 class="fade" :class="{'hide':transition||!selected}">{{(switchRoom) + ' | ' + (status?'Open':'Close')}}</h2>
      <svg class="fade closeButton" :class="{'hide':transition||!selected}" @click="deselectSwitchButton" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <path :fill="status?'rgba(210, 210, 210, 0.95)':'rgba(200, 200, 200, 0.95)'" d="M512 64c-247.00852 0-448 200.960516-448 448S264.960516 960 512 960c247.00852 0 448-200.960516 448-448S759.039484 64 512 64zM694.752211 649.984034c12.480043 12.54369 12.447359 32.768069-0.063647 45.248112-6.239161 6.208198-14.399785 9.34412-22.591372 9.34412-8.224271 0-16.415858-3.135923-22.65674-9.407768l-137.60043-138.016718-138.047682 136.576912c-6.239161 6.14455-14.368821 9.247789-22.496761 9.247789-8.255235 0-16.479505-3.168606-22.751351-9.504099-12.416396-12.576374-12.320065-32.800753 0.25631-45.248112l137.887703-136.384249-137.376804-137.824056c-12.480043-12.512727-12.447359-32.768069 0.063647-45.248112 12.512727-12.512727 32.735385-12.447359 45.248112 0.063647l137.567746 137.984034 138.047682-136.575192c12.54369-12.447359 32.831716-12.320065 45.248112 0.25631 12.447359 12.576374 12.320065 32.831716-0.25631 45.248112L557.344443 512.127295 694.752211 649.984034z"></path>
      </svg>
      <div class="fade switchButtonRoomLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>房间</h3>
        <h3 class="roomValue" @click="getRoomFocus">{{room_name}}</h3>
        <room-list id="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus" :room-id="room_id" :device-id="switchId"></room-list>
      </div>
      <div class="fade switchButtonSwitchLine" :class="{'hide':transition||!selected, 'translateY':transition||!selected}">
        <h3>开关</h3>
        <Switch class="switchButtonSwitch" @click="changeSwitchStatus" :switch-status="status"></Switch>
      </div>
    </div>
  </div>
  <Mask :class="{'hide':!selected}" @click="deselectSwitchButton"></Mask>
</template>

<script>
import Switch from "@/components/switch";
import Mask from "@/components/mask";
import {global_data} from "@/store";
import RoomList from "@/components/roomList.vue";
import DeviceIcon from "@/components/deviceIcon.vue";

export default {
  name: "switchInteractionIcon",
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
    "switchX": {
      required: true
    },
    "switchY": {
      required: true
    }
  },
  data() {
    return {
      status: this.switchStatus,
      selected: false,
      transition: false,
      edit: this.canvasEdit,
      X: this.switchX + 'px',
      Y: this.switchY + 'px',

      room_name: global_data.switch_list[this.switchId].room_name,
      room_id: global_data.switch_list[this.switchId].room_id,
      roomFocus: false,
      switch_icon: global_data.switch_list[this.switchId].switch_icon,
    }
  },
  methods: {
    selectSwitchButton() {
      if (!this.edit && !this.selected) {
        this.z_index = 10;
        this.selected = true;
      }
    },
    deselectSwitchButton() {
      this.transition = true;
      this.roomFocus = false;
      setTimeout(() => {
        this.transition = false;
        this.selected = false;
      }, 300);
    },
    changeSwitchStatus() {
      this.$http.post('/switch/chagne_switch_state', {
        'switch_id': this.switchId,
        'switch_state': this.status
      });

      this.status = !this.status;
      global_data.switch_list[this.switchId].switch_state = this.status;
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

          global_data.switch_list[this.switchId].device_x = left;
          global_data.switch_list[this.switchId].device_y = top;
          this.$emit('changePosition', 3, this.switchId, left, top);
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
      global_data.switch_list[this.switchId].room_id = this.room_id = new_room_id;
      global_data.switch_list[this.switchId].room_name = this.room_name = new_room_name;
    }
  }
}
</script>

<style scoped>

/*Universal properties of switch*/

.switchButtonWrapper {
  position: absolute;
  left: v-bind(X);
  top: v-bind(Y);
  margin-top: 0;
  width: 40px;
  height: 40px;
}

.switchButton {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  backdrop-filter: blur(15px);
  cursor: pointer;
  transition-property: background-color, height, width, border-radius;
  transition-duration: 0.3s;
}

.switchIcon {
  position: absolute;
  left: 0;
  top: 0;
  width: 40px;
  height: 40px;
  transition: all 0.3s;
}

.switchButton h1 {
  position: absolute;
  left: 65px;
  top: 8px;
  width: 120px;
  font-size: 17px;
  font-weight: bolder;
}

.switchButton h2 {
  position: absolute;
  left: 65px;
  top: 31px;
  font-size: 13px;
  font-weight: 500;
}

/*Properties of "on" button*/

.switchButtonOn {
  background-color: rgb(255, 255, 255);
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.05);
}

.switchButtonOn h1, .switchButtonOff h3 {
  color: rgb(5, 5, 5);
}

.switchButtonOn h2 {
  color: rgb(147, 143, 137);
}

.switchButtonOn:hover {
  cursor: pointer;
}

/*Properties of "off" button*/

.switchButtonOff {
  background-color: rgba(56, 56, 56, 0.5);
}

.switchButtonOff h1, .switchButtonOff h3 {
  color: rgb(255, 255, 255);
}

.switchButtonOff h2 {
  color: rgb(220, 215, 205);
}

.switchButtonOff:hover {
  background-color: rgba(45, 45, 45, 0.6);
}

/*Properties of selected button*/

.switchButtonSelected {
  z-index: 10;
  width: 245px;
  height: 125px;
  border-radius: 13px;
  cursor: default !important;
}

.switchButtonSelected .switchIcon {
  position: absolute;
  left: 12px;
  top: 7px;
  width: 40px;
  height: 40px;
}

.switchButtonRoomLine, .switchButtonSwitchLine {
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

.switchButtonOn .roomValue {
  color: rgb(80, 80, 80);
}

.switchButtonOn .roomValue:hover {
  color: rgb(5, 5, 5);
}

.switchButtonOff .roomValue {
  color: rgb(220, 215, 205);
}

.switchButtonOff .roomValue:hover {
  color: white;
}

.switchButtonSwitch {
  position: absolute;
  right: 0;
  top: -1px;
}

.switchButton h3 {
  font-size: 14px;
  font-weight: 500;
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

.switchButtonTransition {
  z-index: 10;
  height: 40px;
  width: 40px;
  border-radius: 20px;
}

.switchButtonTransition .switchIcon {
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
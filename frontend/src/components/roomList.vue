<template>
  <div id="roomListContainer">
    <h3 id="roomListHeader">房间列表</h3>
    <ul>
      <li class="roomItem" v-for="(room_name, index) in room_list" @click="changeRoom(index)">
        {{room_name}}
        <img v-show="(room_id == index) && !loading" class="currentRoomIcon" src="@/assets/utility/right.svg">
        <loading class="loadingIcon" v-show="(room_id == index) && loading" height="18px" length="5px" size="12px" width="1.5px"></loading>
      </li>
    </ul>
  </div>
  <Mask @click="loseRoomFocus"></Mask>
</template>

<script>
import {global_data} from "@/store";
import Mask from "@/components/mask.vue";
import Loading from "@/components/loading.vue";

export default {
  name: "roomList",
  components: {Loading, Mask},
  props: {
    deviceId: {
      required: true
    },
    roomId: {
      required: true
    },
    right: {
      default: '0'
    },
    top: {
      default: '25px'
    }
  },
  data() {
    return {
      room_list: global_data.room_list,
      room_id: this.roomId,

      loading: false
    }
  },
  methods: {
    loseRoomFocus() {
      this.$emit('loseRoomFocus');
    },
    changeRoom(new_room_id) {
      this.loading = true;
      if (new_room_id != this.room_id) {
        this.$http.post('/device/change_device_room', {
          'device_id': this.deviceId,
          'room_id': new_room_id
        }).then((res) => {
          this.room_id = new_room_id;
          this.loading = false;
          this.$emit('changeRoom', new_room_id);
        });
      }
    }
  }
}
</script>

<style scoped>

#roomListContainer {
  position: absolute;
  right: v-bind(right);
  top: v-bind(top);
  width: 160px;
  padding: 0;
  z-index: 20;
  border-radius: 10px;
  background-color: rgb(255, 255, 255, 0.9);
  backdrop-filter: blur(25px);
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.08);
}

#roomListHeader {
  padding: 0 15px;
  font-size: 17px;
  line-height: 45px;
}

.roomItem {
  position: relative;
  padding: 0 15px;
  line-height: 35px;
  border-top: 1px solid rgb(220, 220, 220);
  font-size: 15px;
  transition: background-color 0.3s;
}

.roomItem:last-child {
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

.roomItem:hover {
  background-color: rgba(200, 200, 200, 0.3);
  cursor: pointer;
}

.currentRoomIcon {
  position: absolute;
  right: 12px;
  top: 6px;
  fill: white;
  width: 24px;
}

.loadingIcon {
  position: absolute;
  right: 60px;
  top: 8px;
}

</style>
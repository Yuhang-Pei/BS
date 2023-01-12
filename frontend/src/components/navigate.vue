<template>
  <nav class="navigate">
    <img class="logo" src="@/assets/utility/logo.svg">

    <ul id="navigateMainChoice">
      <nav-choice nav-choice-name="家庭概览" nav-choice-icon-file-name="home" :nav-choice-status="current_choice === 0" nav-choice-link="/home"></nav-choice>
      <nav-choice nav-choice-name="设备管理" nav-choice-icon-file-name="appliance" :nav-choice-status="current_choice === 1" nav-choice-link="/appliance"></nav-choice>
      <nav-choice nav-choice-name="布局图" nav-choice-icon-file-name="layout" :nav-choice-status="current_choice === 2" nav-choice-icon-size="24px" nav-choice-link="/layout"></nav-choice>
      <nav-choice nav-choice-name="设置" nav-choice-icon-file-name="setting" :nav-choice-status="current_choice === 3" nav-choice-icon-size="24px" nav-choice-link="/setting"></nav-choice>
    </ul>
    <h2 id="navigateFurniture">家具</h2>
    <ul id="navigateFurnitureChoice">
      <nav-choice nav-choice-name="灯具" nav-choice-icon-file-name="light" :nav-choice-status="current_choice === 4" nav-choice-link="/light"></nav-choice>
      <nav-choice nav-choice-name="锁" nav-choice-icon-file-name="lock" :nav-choice-status="current_choice === 5" nav-choice-link="/lock"></nav-choice>
      <nav-choice nav-choice-name="传感器" nav-choice-icon-file-name="sensor" :nav-choice-status="current_choice === 6" nav-choice-link="/sensor"></nav-choice>
      <nav-choice nav-choice-name="开关" nav-choice-icon-file-name="switch" :nav-choice-status="current_choice === 7" nav-choice-link="/switch"></nav-choice>
    </ul>
    <h2 id="navigateRoom">房间<img class="newRoom" src="@/assets/utility/add1.svg" @click="newRoom"></h2>

    <ul id="navigateRoomChoice">
      <nav-choice v-for="(room, room_id) in room_list"
                  :nav-choice-name="room"
                  nav-choice-icon-file-name="room"
                  :nav-choice-status="current_choice === parseInt(room_id) + 8"
                  :room-id="room_id"
                  @changeRoom="changeRoom">
      </nav-choice>
    </ul>
  </nav>
</template>

<script>
import NavChoice from "@/components/navChoice";
import {global_data, isObjectEmpty} from "@/store";
import roomList from "@/components/roomList.vue";

export default {
  name: "navigate",
  components: {NavChoice},
  props: {
    currentChoice: {
      required: true
    }
  },
  data() {
    return {
      room_list: {},
      current_choice: this.currentChoice
    }
  },
  created() {
    if (isObjectEmpty(global_data.room_list)) {
      this.$http.post('/room/get_all_rooms', {
        scenario_id: this.$cookies.get('scenario_id')
      }).then((res) => {
        global_data.room_list = this.room_list = res.data.room_list;
      });
    }
    else {
      this.room_list = global_data.room_list;
    }
  },
  methods: {
    changeRoom(new_choice) {
      this.current_choice = new_choice;
      this.$emit('changeRoom', new_choice - 8);
    },
    newRoom() {
      this.$http.post('/room/add_room', {
        scenario_id: this.$cookies.get('scenario_id')
      }).then((res) => {
        let new_room_id = res.data.room_id;
        global_data.room_list[new_room_id] = '房间';
        this.$router.push({
          path: '/roomDetail',
          query: {
            id: new_room_id
          }
        })
      })
    }
  }
}
</script>

<style scoped>

.navigate {
  position: fixed;
  width: 175px;
  height: 100%;
  padding: 30px 20px 0;
  background-color: rgba(75, 75, 75, 0.3);
  backdrop-filter: blur(15px);
  text-align: left;
  font-size: 16px;
  color: white;
}

.logo {
  height: 26px;
  margin-left: 8px;
  margin-bottom: 12px;
}

#navigateHead {
  font-size: 26px;
  margin-left: 10px;
  margin-bottom: 22px;
}

#navigateMainChoice, #navigateFurnitureChoice, #navigateRoomChoice {
  margin-top: 15px;
  padding-left: 0;
}

#navigateFurniture, #navigateRoom {
  font-size: 20px;
  margin-left: 10px;
  margin-top: 25px;
}

.newRoom {
  float: right;
  transform: translateY(2px);
  width: 22px;
  border-radius: 5px;
  transition: background-color 0.3s;
  cursor: pointer;
}

.newRoom:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

</style>
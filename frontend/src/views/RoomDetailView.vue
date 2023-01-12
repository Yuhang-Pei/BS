<template>
  <back-picture></back-picture>
  <navigate :current-choice="-1"></navigate>
  <div class="main">
    <back-button back-button-color="rgb(241, 195, 4)"></back-button>
    <h1 id="roomNameTitle" v-text="room_name"></h1>

    <div id="roomNameLine">
      <h2>房间名称</h2>
      <h3 @click="getNameFocus">{{room_name}}</h3>
      <input ref="nameInput" v-show="nameFocus" @focusout="loseNameFocus" type="text" class="textInput" v-model="room_name">
    </div>

    <delete-warning v-if="deleteWarning"
                    @confirmDelete="confirmDelete"
                    @cancelDelete="cancelDelete">
    </delete-warning>

    <div class="roomDeleteLine" @click="onDelete">
      <p class="deleteRoom">删 除 房 间</p>
    </div>
  </div>
</template>

<script>
import BackPicture from "@/components/backPicture.vue";
import Navigate from "@/components/navigate.vue";
import BackButton from "@/components/backButton.vue";
import {global_data} from "@/store";
import DeleteWarning from "@/components/deleteWarning.vue";

export default {
  name: "RoomDetailView",
  components: {DeleteWarning, BackButton, Navigate, BackPicture},
  data() {
    return {
      room_id: this.$route.query.id,
      room_name: '',
      nameFocus: false,
      deleteWarning: false
    }
  },
  created() {
    this.room_name = global_data.room_list[this.room_id];
  },
  methods: {
    getNameFocus() {
      this.nameFocus = true;
      this.$nextTick(() => {
        this.$refs.nameInput.focus();
      })
    },
    loseNameFocus(e) {
      this.nameFocus = false;
      let new_name = e.target.value;
      this.$http.post('/room/change_room_name', {
        room_id: this.room_id,
        room_name: new_name
      }).then((res) => {
        global_data.room_list[this.room_id] = new_name;

        for (let light in global_data.light_list)
          if (global_data.light_list[light].room_id == this.room_id)
            global_data.light_list[light].room_name = new_name;

        for (let lock in global_data.lock_list)
          if (global_data.lock_list[lock].room_id == this.room_id)
            global_data.lock_list[lock].room_name = new_name;

        for (let sensor in global_data.sensor_list)
          if (global_data.sensor_list[sensor].room_id == this.room_id)
            global_data.sensor_list[sensor].room_name = new_name;

        for (let _switch in global_data.switch_list)
          if (global_data.switch_list[_switch].room_id == this.room_id)
            global_data.switch_list[_switch].room_name = new_name;
      })
    },
    onDelete() {
      this.deleteWarning = true;
    },
    confirmDelete() {
      const that = this;
      this.$http.post('/room/delete_room', {
        'room_id': this.room_id
      }).then((res) => {
        console.log(global_data)
        for (let light in global_data.light_list)
          if (global_data.light_list[light].room_id == this.room_id)
            delete global_data.light_list[light];

        for (let lock in global_data.lock_list) {
          console.log(global_data.lock_list[lock].room_id, this.room_id)
          if (global_data.lock_list[lock].room_id == this.room_id)
            delete global_data.lock_list[lock];
        }

        for (let sensor in global_data.sensor_list)
          if (global_data.sensor_list[sensor].room_id == this.room_id)
            delete global_data.sensor_list[sensor];

        for (let _switch in global_data.switch_list)
          if (global_data.switch_list[_switch].room_id == this.room_id)
            delete global_data.switch_list[_switch];

        delete global_data.room_list[this.room_id];

        console.log(global_data)

        that.$router.go(-2);
      })
      this.deleteWarning = false;
    },
    cancelDelete() {
      this.deleteWarning = false;
    }
  }
}
</script>

<style scoped>

.main {
  position: fixed;
  margin-left: 215px;
  padding: 30px 0 0 30px;
  width: calc(100% - 245px);
  height: 100%;
  background-color: rgb(243, 242, 248);
  overflow-y: scroll;
}

h2 {
  position: absolute;
  left: 20px;
  top: 14px;
  font-size: 18px;
  color: rgb(5, 5, 5);
  font-weight: bold;
}

h3 {
  position: absolute;
  right: 20px;
  top: 14px;
  text-align: right;
  min-width: 50px;
  min-height: 20px;
  font-size: 18px;
  font-weight: normal;
  color: rgb(147, 143, 137);
  transition: color 0.3s;
  cursor: pointer;
}

h3:hover {
  color: rgb(80, 80, 80);
}

#roomNameTitle {
  margin: 20px auto;
  height: 40px;
  text-align: center;
}

#roomNameLine {
  position: relative;
  top: 20px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.textInput {
  position: absolute;
  right: 18px;
  top: 14px;
  text-align: right;
  min-width: 50px;
  min-height: 20px;
  font-size: 18px;
  font-weight: normal;
  color: rgb(80, 80, 80);
  border: none;
  outline: none;
  text-align: right;
  caret-color: rgb(255, 207, 8);
}

.roomDeleteLine {
  position: relative;
  top: 40px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.deleteRoom {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: red;
  cursor: pointer;
}

</style>
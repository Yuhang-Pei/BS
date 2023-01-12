<template>
  <back-picture></back-picture>
  <navigate v-if="!global_data.is_mobile" :current-choice="1"></navigate>
  <mobile-nav v-if="global_data.is_mobile" :cur-choice="1"></mobile-nav>

  <div :class="global_data.is_mobile?'m_main':'main'">
    <back-button back-button-color="rgb(241, 195, 4)"></back-button>

    <div id="loadingContainer" v-show="loading">
      <loading id="loadingAnimation" height="70px" length="16px" size="70px"></loading>
    </div>

    <delete-warning v-if="deleteWarning"
                    @confirmDelete="confirmDelete"
                    @cancelDelete="cancelDelete">
    </delete-warning>

    <div v-show="!loading">
      <div class="lightIconLine">
        <device-icon @click="getIconFocus" class="lightIcon" type="light" :state="true" :index="light_icon" :key="light_icon"></device-icon>
<!--        <img class="lightIcon" :src="'@/assets/furnitureIcon/light-on.svg'">-->
        <icon-list @changeIcon="changeIcon" @loseIconFocus="loseIconFocus" v-if="iconFocus" type="light" :device-id="id" :icon-id="light_icon"></icon-list>
        <h1 class="lightIconName">{{name}}</h1>
      </div>

      <div class="lightNameLine">
        <h2>家具名称</h2>
        <h3 @click="getNameFocus">{{name}}</h3>
        <input ref="nameInput" v-show="nameFocus" @focusout="loseNameFocus" type="text" class="textInput" v-model="name">
      </div>

      <div class="lightRoomLine">
        <h2>房间</h2>
        <h3 @click="getRoomFocus">{{room}}</h3>
        <room-list class="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus"
                   :room-id="room_id" :device-id="id" right="15px" top="42px"></room-list>
      </div>

      <div class="lightModelLine">
        <h2>型号</h2>
        <h3 @click="getModelFocus">{{model}}</h3>
        <input ref="modelInput" v-show="modelFocus" @focusout="loseModelFocus" type="text" class="textInput" v-model="model">
      </div>

      <div class="division"></div>

      <div class="lightSwitchLine">
        <h2>开关</h2>
        <Switch @click="changeStatus" class="lightSwitch" :switch-status="status"></Switch>
      </div>
      <div class="lightLuminanceLine">
        <h2>亮度</h2>
        <light-slider @changeLuminance="changeLuminance" :luminance="luminance" :key="status" class="lightLuminanceSlider" :slider-width="global_data.is_mobile?300:400" slider-height="40" slider-border-radius="12"
                      :slider-front-color="status?'rgb(255, 207, 8)':'rgb(150, 150, 150)'"
                      :slider-back-color="status?'rgba(220, 220, 220, 0.95)':'rgba(200, 200, 200, 0.95)'"></light-slider>
      </div>

      <div class="division"></div>

      <div class="lightDeleteLine" @click="onDelete">
        <p class="deleteLight">删 除 灯 具</p>
      </div>

      <div class="tail"></div>
    </div>
  </div>
</template>

<script>
import Navigate from "@/components/navigate";
import BackPicture from "@/components/backPicture";
import BackButton from "@/components/backButton";
import Switch from "@/components/switch";
import LightSlider from "@/components/lightSlider";
import {global_data, isObjectEmpty} from "@/store";
import RoomList from "@/components/roomList.vue";
import Loading from "@/components/loading.vue";
import DeviceIcon from "@/components/deviceIcon.vue";
import IconList from "@/components/iconList.vue";
import MobileNav from "@/components/mobileNav.vue";
import DeleteWarning from "@/components/deleteWarning.vue";

export default {
  name: "LightDetailView",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {
    DeleteWarning,
    MobileNav,
    IconList, DeviceIcon, Loading, RoomList, LightSlider, Switch, BackButton, BackPicture, Navigate},
  data() {
    return {
      id: '',
      name: '',
      room: '',
      room_id: '',
      model: '',
      status: false,
      luminance: 0,

      light_icon: 0,
      iconFocus: false,
      nameFocus: false,
      roomFocus: false,
      modelFocus: false,
      loading: true,
      deleteWarning: false
    }
  },
  created() {
    if (isObjectEmpty(global_data.light_list)) {
      this.$http.post('light/get_all_lights', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.light_list = global_data.light_list = res.data.light_list;
            this.init();
          });
    }
    else
      this.init();
  },
  methods: {
    init() {
      this.id = this.$route.query.id;
      this.name = global_data.light_list[this.id].device_name;
      this.room = global_data.light_list[this.id].room_name;
      this.room_id = global_data.light_list[this.id].room_id;
      this.model = global_data.light_list[this.id].device_model;
      this.status = global_data.light_list[this.id].light_state;
      this.luminance = global_data.light_list[this.id].luminance;
      this.light_icon = global_data.light_list[this.id].light_icon;

      this.loading = false;
    },
    getIconFocus() {
      this.iconFocus = true;
    },
    loseIconFocus() {
      this.iconFocus = false;
    },
    changeIcon(new_icon_id) {
      global_data.light_list[this.id].light_icon = this.light_icon = new_icon_id;
    },
    getNameFocus() {
      this.nameFocus = true;
      this.$nextTick(() => {
        this.$refs.nameInput.focus();
      })
    },
    loseNameFocus(e) {
      this.nameFocus = false;
      let new_name = e.target.value;
      global_data.light_list[this.id].device_name = new_name;
      this.$http.post('/device/change_device_name', {
        device_id: this.id,
        device_name: new_name
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
      global_data.light_list[this.id].room_id = this.room_id = new_room_id;
      global_data.light_list[this.id].room_name = this.room = new_room_name;
    },
    getModelFocus() {
      this.modelFocus = true;
      this.$nextTick(() => {
        this.$refs.modelInput.focus();
      })
    },
    loseModelFocus(e) {
      this.modelFocus = false;
      let new_model = e.target.value;
      global_data.light_list[this.id].device_model = new_model;
      this.$http.post('/device/change_device_model', {
        device_id: this.id,
        device_model: new_model
      });
    },
    changeStatus() {
      this.$http.post('/light/change_light_state', {
        'light_id': this.id,
        'light_state': this.status
      });

      this.status = !this.status;
      global_data.light_list[this.id].light_state = this.status;
    },
    changeLuminance(new_luminance) {
      this.$http.post('/light/change_light_luminance', {
        'light_id': this.id,
        'luminance': new_luminance
      });

      this.luminance = global_data.light_list[this.id].luminance = new_luminance;
    },
    onDelete() {
      this.deleteWarning = true;
    },
    confirmDelete() {
      const that = this;
      this.$http.post('/device/delete_device', {
        'device_id': this.id
      }).then((res) => {
        delete global_data.light_list[this.id];
        that.$router.go(-1);
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
  background-color: rgb(243, 242, 248);
  height: 100%;
  overflow-y: scroll;
}

.main::-webkit-scrollbar {
  width: 10px;
  height: 100%;
}

.main::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: rgba(75, 75, 75, 0.3);
}

.main::-webkit-scrollbar-thumb:hover {
  background-color: rgba(75, 75, 75, 0.5);
}

.main::-webkit-scrollbar-track {
  background-color: transparent;
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
  caret-color: rgb(255, 207, 8);
}

.division {
  position: relative;
  top: 80px;
  height: 40px;
}

.lightIconLine {
  position: relative;
  top: 80px;
  width: 97%;
  text-align: center;
  margin-bottom: 40px;
}

.lightNameLine, .lightRoomLine, .lightModelLine, .lightSwitchLine, .lightLuminanceLine, .lightDeleteLine {
  position: relative;
  top: 80px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.lightLuminanceLine {
  height: 120px;
}

.lightIcon {
  height: 85px;
  cursor: pointer;
  border-radius: 45px;
  transition: all 0.3s;
}

.lightIcon:hover {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.lightIconName {
  margin: 12px auto;
  height: 40px;
}

.lightSwitch {
  position: absolute;
  right: 20px;
  top: 14px;
}

.lightLuminanceSlider {
  position: relative;
  top: 50px;
  margin: 0 auto;
}

.deleteLight {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: red;
  cursor: pointer;
}

.tail {
  position: relative;
  top: 90px;
  height: 40px;
  background-color: transparent;
}

#loadingContainer {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 120px;
  height: 120px;
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border-radius: 25px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
}

#loadingAnimation {
  position: relative;
  top: 26px;
  left: 10px;
}

.m_main {
  position: fixed;
  padding: 30px 0 0 0;
  width: 100%;
  height: calc(100% - 95px);
  overflow-y: scroll;
  overflow-x: hidden;
  background-color: rgb(243, 242, 248);
}

.m_main::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: rgba(75, 75, 75, 0.3);
}

.m_main::-webkit-scrollbar-thumb:hover {
  background-color: rgba(75, 75, 75, 0.5);
}

.m_main::-webkit-scrollbar-track {
  background-color: transparent;
}

.m_main .lightIconLine {
  position: relative;
  top: 80px;
  width: 100%;
  text-align: center;
  margin-bottom: 40px;
}

.m_main .lightNameLine,
.m_main .lightRoomLine,
.m_main .lightModelLine,
.m_main .lightSwitchLine,
.m_main .lightLuminanceLine,
.m_main .lightDeleteLine {
  position: relative;
  top: 80px;
  width: 94%;
  margin-top: 10px;
  margin-left: 3%;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

</style>
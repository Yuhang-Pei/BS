<template>
  <back-picture></back-picture>
  <navigate v-if="!global_data.is_mobile" :current-choice="1"></navigate>
  <mobile-nav v-if="global_data.is_mobile" :cur-choice="1"></mobile-nav>

  <div :class="global_data.is_mobile?'m_main':'main'">
    <back-button back-button-color="rgb(29, 176, 239)"></back-button>

    <div id="loadingContainer" v-show="loading">
      <loading id="loadingAnimation" height="70px" length="16px" size="70px"></loading>
    </div>

    <delete-warning v-if="deleteWarning"
                    @confirmDelete="confirmDelete"
                    @cancelDelete="cancelDelete">
    </delete-warning>

    <div v-show="!loading">
      <div class="sensorIconLine">
        <device-icon @click="getIconFocus" class="sensorIcon" type="sensor" :state="true" :index="sensor_icon" :key="sensor_icon"></device-icon>
<!--        <img class="sensorIcon" src="@/assets/furnitureIcon/sensor-on.svg">-->
        <icon-list @changeIcon="changeIcon" @loseIconFocus="loseIconFocus" v-if="iconFocus" type="sensor" :device-id="id" :icon-id="sensor_icon"></icon-list>
        <h1 class="sensorIconName">{{name}}</h1>
      </div>

      <div class="sensorNameLine">
        <h2>家具名称</h2>
        <h3 @click="getNameFocus">{{name}}</h3>
        <input ref="nameInput" v-show="nameFocus" @focusout="loseNameFocus" type="text" class="textInput" v-model="name">
      </div>

      <div class="sensorRoomLine">
        <h2>房间</h2>
        <h3 @click="getRoomFocus">{{room}}</h3>
        <room-list class="roomList" @changeRoom="changeRoom" @loseRoomFocus="loseRoomFocus" v-if="roomFocus"
                   :room-id="room_id" :device-id="id" right="15px" top="42px"></room-list>
      </div>

      <div class="sensorModalLine">
        <h2>型号</h2>
        <h3 @click="getModelFocus">{{model}}</h3>
        <input ref="modelInput" v-show="modelFocus" @focusout="loseModelFocus" type="text" class="textInput" v-model="model">
      </div>

      <div class="division"></div>

      <div class="sensorSwitchLine">
        <h2>开关</h2>
        <Switch @click="changeStatus" class="sensorSwitch" :switch-status="status"></Switch>
      </div>
      <div class="sensorMainLine">
        <h2>主传感器</h2>
        <Switch @click="changeMain" class="sensorSwitch" :switch-status="main"></Switch>
      </div>
      <div class="sensorEnvironmentLine">
        <h2>环境</h2>
        <div class="environment">
          <div class="environmentTemperature">
            <div class="temperatureValue">{{temperature}}</div><div class="temperatureUnit">℃</div>
            <div class="sensorSubCaption">{{(temperature==='-')?'':(temperature<10?'寒冷':(temperature>30?'炎热':(temperature<20?'凉爽':'温暖')))}}</div>
          </div>
          <div class="environmentHumidity">
            <div class="humidityValue">{{humidity}}</div><div class="humidityUnit">%</div>
            <div class="sensorSubCaption">{{humidity==='-'?'':(humidity<40?'干燥':(humidity>75?'潮湿':'舒适'))}}</div>
          </div>
        </div>
      </div>

      <div class="division"></div>

      <div class="sensorDeleteLine" @click="onDelete">
        <p class="deleteSensor">删 除 传 感 器</p>
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
import Loading from "@/components/loading.vue";
import RoomList from "@/components/roomList.vue";
import {global_data, isObjectEmpty} from "@/store";
import DeviceIcon from "@/components/deviceIcon.vue";
import IconList from "@/components/iconList.vue";
import MobileNav from "@/components/mobileNav.vue";
import DeleteWarning from "@/components/deleteWarning.vue";
export default {
  name: "SensorDetailView",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {
    DeleteWarning,
    MobileNav, IconList, DeviceIcon, RoomList, Loading, Switch, BackButton, BackPicture, Navigate},
  data() {
    return {
      id: '',
      name: '',
      room: '',
      room_id: '',
      model: '',
      status: false,
      main: false,
      temperature: 0,
      humidity: 0,

      sensor_icon: 0,
      iconFocus: false,
      nameFocus: false,
      roomFocus: false,
      modelFocus: false,
      loading: true,
      deleteWarning: false
    }
  },
  created() {
    if (isObjectEmpty(global_data.sensor_list)) {
      this.$http.post('sensor/get_all_sensors', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.sensor_list = global_data.sensor_list = res.data.sensor_list;
            this.init();
          });
    }
    else
      this.init();
  },
  methods: {
    init() {
      this.id = this.$route.query.id;
      this.name = global_data.sensor_list[this.id].device_name;
      this.room = global_data.sensor_list[this.id].room_name;
      this.room_id = global_data.sensor_list[this.id].room_id;
      this.model = global_data.sensor_list[this.id].device_model;
      this.status = global_data.sensor_list[this.id].sensor_state;
      this.main = global_data.sensor_list[this.id].is_main;
      this.temperature = global_data.sensor_list[this.id].temperature;
      this.humidity = global_data.sensor_list[this.id].humidity;
      this.sensor_icon = global_data.sensor_list[this.id].sensor_icon;
      if (this.temperature === null)
        this.temperature = '-';
      if (this.humidity === null)
        this.humidity = '-';

      this.loading = false;
    },
    getIconFocus() {
      this.iconFocus = true;
    },
    loseIconFocus() {
      this.iconFocus = false;
    },
    changeIcon(new_icon_id) {
      global_data.sensor_list[this.id].sensor_icon = this.sensor_icon = new_icon_id;
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
      global_data.sensor_list[this.id].device_name = new_name;
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
      global_data.sensor_list[this.id].room_id = this.room_id = new_room_id;
      global_data.sensor_list[this.id].room_name = this.room = new_room_name;
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
      global_data.sensor_list[this.id].device_model = new_model;
      this.$http.post('/device/change_device_model', {
        device_id: this.id,
        device_model: new_model
      });
    },
    changeStatus() {
      this.$http.post('/sensor/change_sensor_state', {
        'sensor_id': this.id,
        'sensor_state': this.status
      }).then((res) => {
        global_data.sensor_list[this.id].temperature = this.temperature = (res.data.temperature === null) ? '-' : res.data.temperature;
        global_data.sensor_list[this.id].humidity = this.humidity = (res.data.humidity === null) ? '-' : res.data.humidity;
      })

      global_data.sensor_list[this.id].sensor_state = this.status = !this.status;
    },
    changeMain() {
      this.$http.post('/sensor/change_main_sensor', {
        'sensor_id': this.id,
        'is_main': this.main,
        'scenario_id': this.$cookies.get('scenario_id')
      });

      global_data.sensor_list[this.id].is_main = this.main = !this.main;
      if (this.main)
        for (let sensor in global_data.sensor_list)
          if (sensor != this.id && global_data.sensor_list[sensor].is_main) {
            global_data.sensor_list[sensor].is_main = false;
            break;
          }
    },
    onDelete() {
      this.deleteWarning = true;
    },
    confirmDelete() {
      const that = this;
      this.$http.post('/device/delete_device', {
        'device_id': this.id
      }).then((res) => {
        delete global_data.sensor_list[this.id];
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
  height: 100%;
  background-color: rgb(243, 242, 248);
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
  font-size: 18px;
  font-weight: normal;
  color: rgb(80, 80, 80);
  border: none;
  outline: none;
  text-align: right;
  caret-color: rgb(29, 176, 239);
}

.division {
  position: relative;
  top: 80px;
  height: 40px;
}

.sensorIconLine {
  position: relative;
  top: 80px;
  width: 97%;
  text-align: center;
  margin-bottom: 40px;
}

.sensorNameLine, .sensorRoomLine, .sensorModalLine, .sensorSwitchLine, .sensorDeleteLine, .sensorEnvironmentLine, .sensorMainLine {
  position: relative;
  top: 80px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.sensorEnvironmentLine {
  height: 150px;
}

.sensorIcon {
  height: 85px;
  cursor: pointer;
  border-radius: 45px;
  transition: all 0.3s;
}

.sensorIcon:hover {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.sensorIconName {
  margin: 12px auto;
  height: 40px;
}

.sensorSwitch {
  position: absolute;
  right: 20px;
  top: 14px;
}

.deleteSensor {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: red;
  cursor: pointer;
}

.environment {
  position: relative;
  top: 50px;
  width: 100%;
  height: 80px;
  text-align: center;
  color: rgb(29, 176, 239)
}

.environmentTemperature, .environmentHumidity {
  display: inline-block;
  margin: 0 8% 0;
}

.environmentTemperature .temperatureValue,
.environmentTemperature .temperatureUnit,
.environmentHumidity .humidityValue,
.environmentHumidity .humidityUnit {
  display: inline;
}

.temperatureValue, .humidityValue {
  font-size: 50px;
}

.temperatureUnit, .humidityUnit {
  font-size: 35px;
}

.sensorSubCaption {
  color: rgb(147, 143, 137);
  font-size: 15px;
}

.tail {
  position: relative;
  top: 90px;
  height: 40px;
  background-color: transparent;
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

.m_main .sensorIconLine {
  position: relative;
  top: 80px;
  width: 100%;
  text-align: center;
  margin-bottom: 40px;
}

.m_main .sensorNameLine,
.m_main .sensorRoomLine,
.m_main .sensorModalLine,
.m_main .sensorMainLine,
.m_main .sensorEnvironmentLine,
.m_main .sensorSwitchLine,
.m_main .sensorDeleteLine {
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
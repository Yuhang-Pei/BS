<template>
  <back-picture></back-picture>
  <navigate :current-choice="2"></navigate>
  <div class="main">
    <h1>布局图</h1>
    <div id="fabricContainer">
      <div id="toolBarContainer">
        <img v-if="layoutPicture === ''" id="noLayout" src="@/assets/layout/nolayout.svg">
        <div id="uploadLayoutDiv" v-if="layoutPicture === ''">
          <p id="uploadText">上 传 布 局 图</p>
          <input type="file" id="uploadLayout" @change="uploadLayout">
        </div>

        <div v-if="layoutPicture !== ''" id="toolBar">
          <div class="toolIconContainer" id="editIcon" @click="changeEditState">
            <svg v-show="!edit && !loading" class="toolIcon" viewBox="0 0 1028 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200.78125" height="200">
              <path fill="rgb(128, 127, 132)" d="M1018.319924 112.117535q4.093748 9.210934 6.652341 21.492179t2.558593 25.585928-5.117186 26.609365-16.374994 25.585928q-12.281245 12.281245-22.003898 21.492179t-16.886712 16.374994q-8.187497 8.187497-15.351557 14.32812l-191.382739-191.382739q12.281245-11.257808 29.167958-27.121083t28.144521-25.074209q14.32812-11.257808 29.679676-15.863275t30.191395-4.093748 28.656239 4.605467 24.050772 9.210934q21.492179 11.257808 47.589826 39.402329t40.425766 58.847634zM221.062416 611.554845q6.140623-6.140623 28.656239-29.167958t56.289041-56.80076l74.710909-74.710909 82.898406-82.898406 220.038979-220.038979 191.382739 192.406177-220.038979 220.038979-81.874969 82.898406q-40.937484 39.914047-73.687472 73.175753t-54.242167 54.753885-25.585928 24.562491q-10.234371 9.210934-23.539054 19.445305t-27.632802 16.374994q-14.32812 7.16406-41.960921 17.398431t-57.824197 19.957024-57.312478 16.886712-40.425766 9.210934q-27.632802 3.070311-36.843736-8.187497t-5.117186-37.867173q2.046874-14.32812 9.722653-41.449203t16.374994-56.289041 16.886712-53.730448 13.304682-33.773425q6.140623-14.32812 13.816401-26.097646t22.003898-26.097646z"></path>
            </svg>
            <svg v-show="edit && !loading" class="toolIcon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
              <path fill="white" d="M689.49333333 370.88h-105.81333333V123.94666667h105.81333333v246.93333333zM971.73333333 265.06666667v599.78666666c0 58.45333333-47.36 105.81333333-105.81333333 105.81333334H160.21333333c-58.45333333 0-105.81333333-47.36-105.81333333-105.81333334V159.14666667c0-58.45333333 47.36-105.81333333 105.81333333-105.81333334h599.78666667c29.22666667 0 46.50666667 21.76 127.46666667 105.6 64.53333333 66.88 84.26666667 76.90666667 84.26666666 106.13333334z m-740.90666666 105.81333333c0 19.41333333 15.78666667 35.30666667 35.30666666 35.30666667h458.66666667c19.41333333 0 35.30666667-15.89333333 35.30666667-35.30666667V123.94666667c0-19.41333333-15.78666667-35.30666667-35.30666667-35.30666667h-458.66666667c-19.41333333 0-35.30666667 15.89333333-35.30666666 35.30666667v246.93333333z m635.09333333 176.42666667c0-19.41333333-15.78666667-35.30666667-35.30666667-35.30666667H195.52c-19.41333333 0-35.30666667 15.89333333-35.30666667 35.30666667v352.85333333c0 19.41333333 15.78666667 35.30666667 35.30666667 35.30666667h635.09333333c19.41333333 0 35.30666667-15.89333333 35.30666667-35.30666667V547.30666667z"></path>
            </svg>
            <loading id="loadingIcon" v-show="loading && edit" height="22px" length="6px" size="14px" width="2px" color="white"></loading>
          </div>

          <div class="toolIconContainer" id="changeIcon">
            <svg class="toolIcon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
              <path fill="rgb(128, 127, 132)" d="M484.096 1015.296c-7.936 7.936-24.064 7.936-32 7.936H76.8c-32 0-47.872-15.872-55.808-39.936V632.064c0-32 15.872-47.872 39.936-55.808h383.232c15.872 0 24.064 0 39.936 7.936 15.872 7.936 15.872 24.064 24.064 39.936v343.296c-0.256 16.128-8.192 32-24.064 47.872zM531.968 440.576c-15.872-7.936-24.064-24.064-24.064-47.872v-335.36c0-24.064 15.872-47.872 39.936-55.808h391.168c24.064 0 39.936 7.936 55.808 32 0 7.936 7.936 15.872 7.936 24.064v335.36c0 24.064-15.872 47.872-39.936 55.808H579.84c-23.808-0.256-39.936-0.256-47.872-8.192zM827.392 552.192c-55.808 55.808-103.68 119.808-151.808 175.616h95.744c-7.936 32-15.872 64-32 95.744-24.064 39.936-64 71.936-111.872 79.872h-1.28v119.808c46.848-5.12 91.648-21.248 129.024-47.872 87.808-64 127.744-143.616 127.744-247.552h95.744c-55.552-63.744-103.424-119.552-151.296-175.616z" ></path>
              <path fill="rgb(128, 127, 132)" d="M626.432 962.816m-60.416 0a60.416 60.416 0 1 0 120.832 0 60.416 60.416 0 1 0-120.832 0Z"></path>
              <path fill="rgb(128, 127, 132)" d="M187.392 471.808c55.808-55.808 103.68-119.808 151.808-175.616H243.456c7.936-32 15.872-64 32-95.744 24.064-39.936 64-71.936 111.872-79.872h1.28V0.512c-46.848 5.12-91.648 21.248-129.024 47.872-87.808 64-127.744 143.616-127.744 247.552H35.84c55.808 64 103.68 119.808 151.552 175.872z"></path>
              <path fill="rgb(128, 127, 132)" d="M388.352 61.184m-60.416 0a60.416 60.416 0 1 0 120.832 0 60.416 60.416 0 1 0-120.832 0Z"></path>
            </svg>
          </div>
        </div>
      </div>

      <div id="canvas" v-if="layoutPicture !== ''">
<!--        <img v-show="layoutPicture !== ''" id="layoutPicture" :src="layoutPicture">-->
<!--        <img id="layoutPicture" src="@/assets/layout/layout.jpg">-->
        <img id="layoutPicture" :src="layoutPicture" alt="@/assets/layout/layout.jpg">

        <light-interaction-icon v-for="(light, light_id) in layout_light_list"
                                :light-id="light_id"
                                :light-name="light.device_name"
                                :light-status="light.light_state"
                                :light-luminance="light.luminance"
                                :light-room="light.room_name"
                                canvas-width="900"
                                canvas-height="635"
                                :canvas-edit="edit"
                                :light-x="light.device_x"
                                :light-y="light.device_y"
                                :key="edit"
                                @changePosition="changePosition">
        </light-interaction-icon>

        <lock-interaction-icon v-for="(lock, lock_id) in layout_lock_list"
                               :lock-id="lock_id"
                               :lock-name="lock.device_name"
                               :lock-status="lock.lock_state"
                               :lock-room="lock.room_name"
                               canvas-width="900"
                               canvas-height="635"
                               :canvas-edit="edit"
                               :lock-x="lock.device_x"
                               :lock-y="lock.device_y"
                               :key="edit"
                               @changePosition="changePosition">
        </lock-interaction-icon>

        <sensor-interaction-icon v-for="(sensor, sensor_id) in layout_sensor_list"
                                 :sensor-id="sensor_id"
                                 :sensor-name="sensor.device_name"
                                 :sensor-status="sensor.sensor_state"
                                 :sensor-temperature="sensor.temperature"
                                 :sensor-humidity="sensor.humidity"
                                 :is-main="sensor_id == current_main"
                                 :sensor-room="sensor.room_name"
                                 canvas-width="900"
                                 canvas-height="635"
                                 :canvas-edit="edit"
                                 :sensor-x="sensor.device_x"
                                 :sensor-y="sensor.device_y"
                                 :key="edit + 100 * sensor_change[sensor_id]"
                                 @changePosition="changePosition"
                                 @getCurrentMainSensor="getCurrentMainSensor">
        </sensor-interaction-icon>

        <switch-interaction-icon v-for="(_switch, switch_id) in layout_switch_list"
                                        :switch-id="switch_id"
                                        :switch-name="_switch.device_name"
                                        :switch-status="_switch.switch_state"
                                        :switch-room="_switch.room_name"
                                        canvas-width="900"
                                        canvas-height="635"
                                        :canvas-edit="edit"
                                        :switch-x="_switch.device_x"
                                        :switch-y="_switch.device_y"
                                        :key="edit"
                                        @changePosition="changePosition">
      </switch-interaction-icon>
      </div>
    </div>

    <ul id="furnitureList" v-if="layoutPicture !== ''" >
      <li v-for="(light, light_id) in light_list" v-show="!light.device_x || !light.device_y" class="furnitureListItem">
        <svg class="addToLayout" :class="{'editing': edit && !loading}"
             @click="addToLayout(0, light_id)" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
          <path d="M509.72826 92.853781c-231.475955 0-419.148265 187.67231-419.148265 419.148265 0 231.470839 187.67231 419.143149 419.148265 419.143149 231.498468 0 419.143149-187.67231 419.143149-419.143149C928.871409 280.526091 741.226728 92.853781 509.72826 92.853781L509.72826 92.853781zM745.847979 538.195615 535.921829 538.195615 535.921829 748.121765c0 14.278191-11.736299 25.846668-26.193569 25.846668-14.474666 0-26.198685-11.568477-26.198685-25.846668L483.529575 538.195615 273.603425 538.195615c-14.278191 0-25.841551-11.736299-25.841551-26.193569 0-14.474666 11.592013-26.198685 25.841551-26.198685l209.92615 0L483.529575 275.849582c0-14.250562 11.724019-25.813922 26.198685-25.813922 14.45727 0 26.193569 11.56336 26.193569 25.813922l0 209.953779 209.92615 0c14.305821 0 25.846668 11.724019 25.846668 26.198685C771.694647 526.459317 760.1538 538.195615 745.847979 538.195615L745.847979 538.195615zM745.847979 538.195615"></path>
        </svg>
        <light-button :light-id="light_id"
                      :light-name="light.device_name"
                      :light-status="light.light_state"
                      :light-room="light.room_name"
                      :light-luminance="light.luminance">
        </light-button>
      </li>

      <li v-for="(lock, lock_id) in lock_list" v-show="!lock.device_x || !lock.device_y" class="furnitureListItem">
        <svg class="addToLayout" :class="{'editing': edit && !loading}"
             @click="addToLayout(1, lock_id)" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
          <path d="M509.72826 92.853781c-231.475955 0-419.148265 187.67231-419.148265 419.148265 0 231.470839 187.67231 419.143149 419.148265 419.143149 231.498468 0 419.143149-187.67231 419.143149-419.143149C928.871409 280.526091 741.226728 92.853781 509.72826 92.853781L509.72826 92.853781zM745.847979 538.195615 535.921829 538.195615 535.921829 748.121765c0 14.278191-11.736299 25.846668-26.193569 25.846668-14.474666 0-26.198685-11.568477-26.198685-25.846668L483.529575 538.195615 273.603425 538.195615c-14.278191 0-25.841551-11.736299-25.841551-26.193569 0-14.474666 11.592013-26.198685 25.841551-26.198685l209.92615 0L483.529575 275.849582c0-14.250562 11.724019-25.813922 26.198685-25.813922 14.45727 0 26.193569 11.56336 26.193569 25.813922l0 209.953779 209.92615 0c14.305821 0 25.846668 11.724019 25.846668 26.198685C771.694647 526.459317 760.1538 538.195615 745.847979 538.195615L745.847979 538.195615zM745.847979 538.195615"></path>
        </svg>
        <lock-button :lock-id="lock_id"
                     :lock-name="lock.device_name"
                     :lock-status="lock.lock_state"
                     :lock-room="lock.room_name">
        </lock-button>
      </li>

      <li v-for="(sensor, sensor_id) in sensor_list" v-show="!sensor.device_x || !sensor.device_y" class="furnitureListItem">
        <svg class="addToLayout" :class="{'editing': edit && !loading}"
             @click="addToLayout(2, sensor_id)" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
          <path d="M509.72826 92.853781c-231.475955 0-419.148265 187.67231-419.148265 419.148265 0 231.470839 187.67231 419.143149 419.148265 419.143149 231.498468 0 419.143149-187.67231 419.143149-419.143149C928.871409 280.526091 741.226728 92.853781 509.72826 92.853781L509.72826 92.853781zM745.847979 538.195615 535.921829 538.195615 535.921829 748.121765c0 14.278191-11.736299 25.846668-26.193569 25.846668-14.474666 0-26.198685-11.568477-26.198685-25.846668L483.529575 538.195615 273.603425 538.195615c-14.278191 0-25.841551-11.736299-25.841551-26.193569 0-14.474666 11.592013-26.198685 25.841551-26.198685l209.92615 0L483.529575 275.849582c0-14.250562 11.724019-25.813922 26.198685-25.813922 14.45727 0 26.193569 11.56336 26.193569 25.813922l0 209.953779 209.92615 0c14.305821 0 25.846668 11.724019 25.846668 26.198685C771.694647 526.459317 760.1538 538.195615 745.847979 538.195615L745.847979 538.195615zM745.847979 538.195615"></path>
        </svg>
        <sensor-button :ref="sensor_id"
                       :sensor-id="sensor_id"
                       :sensor-name="sensor.device_name"
                       :sensor-status="sensor.sensor_state"
                       :sensor-temperature="sensor.temperature"
                       :sensor-humidity="sensor.humidity"
                       :is-main="sensor_id == current_main"
                       :sensor-room="sensor.room_name"
                       :key="sensor_change[sensor_id]"
                       @getCurrentMainSensor="getCurrentMainSensor">
        </sensor-button>
      </li>

      <li v-for="(_switch, switch_id) in switch_list" v-show="!_switch.device_x || !_switch.device_y" class="furnitureListItem">
        <svg class="addToLayout" :class="{'editing': edit && !loading}"
             @click="addToLayout(3, switch_id)" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
          <path d="M509.72826 92.853781c-231.475955 0-419.148265 187.67231-419.148265 419.148265 0 231.470839 187.67231 419.143149 419.148265 419.143149 231.498468 0 419.143149-187.67231 419.143149-419.143149C928.871409 280.526091 741.226728 92.853781 509.72826 92.853781L509.72826 92.853781zM745.847979 538.195615 535.921829 538.195615 535.921829 748.121765c0 14.278191-11.736299 25.846668-26.193569 25.846668-14.474666 0-26.198685-11.568477-26.198685-25.846668L483.529575 538.195615 273.603425 538.195615c-14.278191 0-25.841551-11.736299-25.841551-26.193569 0-14.474666 11.592013-26.198685 25.841551-26.198685l209.92615 0L483.529575 275.849582c0-14.250562 11.724019-25.813922 26.198685-25.813922 14.45727 0 26.193569 11.56336 26.193569 25.813922l0 209.953779 209.92615 0c14.305821 0 25.846668 11.724019 25.846668 26.198685C771.694647 526.459317 760.1538 538.195615 745.847979 538.195615L745.847979 538.195615zM745.847979 538.195615"></path>
        </svg>
        <switch-button :switch-id="switch_id"
                       :switch-name="_switch.device_name"
                       :switch-status="_switch.switch_state"
                       :switch-room="_switch.room_name">
        </switch-button>
      </li>
    </ul>
  </div>
</template>

<script>
import BackPicture from "@/components/backPicture";
import Navigate from "@/components/navigate";
import LightButton from "@/components/lightButton";
import LockButton from "@/components/lockButton";
import SwitchButton from "@/components/switchButton";
import SensorButton from "@/components/sensorButton";
import LightInteractionIcon from "@/components/lightInteractionIcon.vue";
import LockInteractionIcon from "@/components/lockInteractionIcon";
import {global_data, isObjectEmpty} from "@/store";
import SwitchInteractionIcon from "@/components/switchInteractionIcon.vue";
import SensorInteractionIcon from "@/components/sensorInteractionIcon.vue";
import Loading from "@/components/loading.vue";

export default {
  name: "LayoutView",
  components: {
    Loading,
    SensorInteractionIcon,
    SwitchInteractionIcon,
    LightInteractionIcon,
    LockInteractionIcon, SensorButton, SwitchButton, LockButton, LightButton, BackPicture, Navigate},
  data() {
    return {
      light_list: {},
      lock_list: {},
      sensor_list: {},
      switch_list: {},

      layout_light_list: {},
      layout_lock_list: {},
      layout_sensor_list: {},
      layout_switch_list: {},

      current_main: -1,
      sensor_change: {},

      layoutPicture: '',
      edit: false,
      loading: false,
      editBackground: 'rgb(229, 229, 231)'
    }
  },
  created() {
    this.$http.post('scenario/get_layout', {
      'user_id': this.$cookies.get('user_id'),
      'scenario_id': this.$cookies.get('scenario_id')
    }, {
      responseType: 'arraybuffer'
    }).then((res) => {
      if (res.data.byteLength > 500)
        this.layoutPicture = "data:image/jpeg;base64," + this.arrayBufferToBase64(res.data);
      else
        this.layoutPicture = '';
    });

    if (isObjectEmpty(global_data.light_list)) {
      this.$http.post('light/get_all_lights', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.light_list = global_data.light_list = res.data.light_list;
            for (let light_id in this.light_list)
              if (this.light_list[light_id].device_x != null && this.light_list[light_id].device_y != null)
                this.layout_light_list[light_id] = this.light_list[light_id];
          });
    }
    else {
      this.light_list = global_data.light_list;
      for (let light_id in this.light_list)
        if (this.light_list[light_id].device_x != null && this.light_list[light_id].device_y != null)
          this.layout_light_list[light_id] = this.light_list[light_id];
    }

    if (isObjectEmpty(global_data.lock_list)) {
      this.$http.post('lock/get_all_locks', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.lock_list = global_data.lock_list = res.data.lock_list;
            for (let lock_id in this.lock_list)
              if (this.lock_list[lock_id].device_x != null && this.lock_list[lock_id].device_y != null)
                this.layout_lock_list[lock_id] = this.lock_list[lock_id];
          });
    }
    else {
      this.lock_list = global_data.lock_list;
      for (let lock_id in this.lock_list)
        if (this.lock_list[lock_id].device_x != null && this.lock_list[lock_id].device_y != null)
          this.layout_lock_list[lock_id] = this.lock_list[lock_id];
    }

    if (isObjectEmpty(global_data.sensor_list)) {
      this.$http.post('sensor/get_all_sensors', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.sensor_list = global_data.sensor_list = res.data.sensor_list;
            for (let sensor_id in this.sensor_list) {
              this.sensor_change[sensor_id] = 0;
              if (this.sensor_list[sensor_id].is_main == true)
                this.current_main = sensor_id;
            }
            for (let sensor_id in this.sensor_list)
              if (this.sensor_list[sensor_id].device_x != null && this.sensor_list[sensor_id].device_y != null)
                this.layout_sensor_list[sensor_id] = this.sensor_list[sensor_id];
          });
    }
    else {
      this.sensor_list = global_data.sensor_list;
      for (let sensor_id in this.sensor_list) {
        this.sensor_change[sensor_id] = 0;
        if (this.sensor_list[sensor_id].is_main == true)
          this.current_main = sensor_id;
      }
      for (let sensor_id in this.sensor_list)
        if (this.sensor_list[sensor_id].device_x != null && this.sensor_list[sensor_id].device_y != null)
          this.layout_sensor_list[sensor_id] = this.sensor_list[sensor_id];
    }

    if (isObjectEmpty(global_data.switch_list)) {
      this.$http.post('switch/get_all_switches', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.switch_list = global_data.switch_list = res.data.switch_list;
            for (let switch_id in this.switch_list)
              if (this.switch_list[switch_id].device_x != null && this.switch_list[switch_id].device_y != null)
                this.layout_switch_list[switch_id] = this.switch_list[switch_id];
          });
    }
    else {
      this.switch_list = global_data.switch_list;
      for (let switch_id in this.switch_list)
        if (this.switch_list[switch_id].device_x != null && this.switch_list[switch_id].device_y != null)
          this.layout_switch_list[switch_id] = this.switch_list[switch_id];
    }
  },
  methods: {
    arrayBufferToBase64(buffer) {
      let binary = "";
      let bytes = new Uint8Array(buffer);
      let len = bytes.byteLength;
      for (let i = 0; i < len; i++)
        binary += String.fromCharCode(bytes[i]);
      return window.btoa(binary);
    },
    uploadLayout(e) {
      this.layoutPicture = e.target.files[0];
      console.log(this.layoutPicture)
      console.log(typeof(this.layoutPicture))
      const formData = new FormData();
      formData.append('file', this.layoutPicture);
      formData.append('user', this.$cookies.get('user_id'));
      formData.append('scenario', this.$cookies.get('scenario_id'));
      this.$http.post('/scenario/upload_layout', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then((res) => {
        this.layoutPicture = res.data;
      })
    },
    async changeEditState() {
      if (this.edit) {
        this.loading = true;
        await this.$http.post('/light/change_light_position', this.layout_light_list);
        await this.$http.post('/lock/change_lock_position', this.layout_lock_list);
        await this.$http.post('/sensor/change_sensor_position', this.layout_sensor_list);
        await this.$http.post('/switch/change_switch_position', this.layout_switch_list);
        this.editBackground = 'rgb(229, 229, 231)';
        this.edit = false;
        this.loading = false;
      }
      else {
        this.editBackground = 'rgb(255, 207, 8)';
        this.edit = true;
      }
    },
    getCurrentMainSensor(new_main_sensor) {
      if (new_main_sensor) {  // if the new main sensor exists
        if (this.current_main != -1) {  // the previous main sensor existed
          this.sensor_list[this.current_main].is_main = false;
          this.sensor_change[this.current_main] += 1;
        }
        this.sensor_list[new_main_sensor].is_main = true;
        this.current_main = new_main_sensor;
      }
      else {  // if the new main sensor does not exist, namely the previous main sensor is canceled
        this.sensor_list[this.current_main].is_main = false;
        this.current_main = -1;
      }
    },
    addToLayout(device_type, id) {
      switch(device_type) {
        case 0:
          global_data.light_list[id].device_x = this.light_list[id].device_x = 20;
          global_data.light_list[id].device_y = this.light_list[id].device_y = 20;
          this.layout_light_list[id] = this.light_list[id];
          break;
        case 1:
          global_data.lock_list[id].device_x = this.lock_list[id].device_x = 20;
          global_data.lock_list[id].device_y = this.lock_list[id].device_y = 20;
          this.layout_lock_list[id] = this.lock_list[id];
          break;
        case 2:
          global_data.sensor_list[id].device_x = this.sensor_list[id].device_x = 20;
          global_data.sensor_list[id].device_y = this.sensor_list[id].device_y = 20;
          this.layout_sensor_list[id] = this.sensor_list[id];
          break;
        case 3:
          global_data.switch_list[id].device_x = this.switch_list[id].device_x = 20;
          global_data.switch_list[id].device_y = this.switch_list[id].device_y = 20;
          this.layout_switch_list[id] = this.switch_list[id];
          break;
      }
    },
    changePosition(device_type, id, x, y) {
      switch(device_type) {
        case 0:
          this.layout_light_list[id].device_x = x;
          this.layout_light_list[id].device_y = y;
          break;
        case 1:
          this.layout_lock_list[id].device_x = x;
          this.layout_lock_list[id].device_y = y;
          break;
        case 2:
          this.layout_sensor_list[id].device_x = x;
          this.layout_sensor_list[id].device_y = y;
          break;
        case 3:
          this.layout_switch_list[id].device_x = x;
          this.layout_switch_list[id].device_y = y;
          break;
      }
    }
  }
}

</script>

<style scoped>

.main {
  margin-left: 215px;
  padding: 30px 0 0 30px;
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

h1 {
  color: white;
  font-size: 26px;
  margin-left: 5px;
  margin-bottom: 22px;
}

#fabricContainer {
  display: inline-block;
  width: 940px;
  height: 750px;
  background-color: white;
  border-radius: 20px;
}

#toolBarContainer {
  position: relative;
  top: 10px;
  margin: 0 auto;
  width: 95%;
  height: 70px;
}

#toolBar {
  display: inline-block;
  position: relative;
  margin: 0 auto;
  padding: 10px;
  top: 10px;
  background-color: white;
  border-radius: 30px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.toolIconContainer {
  position: relative;
  display: inline-block;
  margin-left: 7px;
  margin-right: 7px;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  transition: all 0.3s;
  cursor: pointer;
}

#editIcon {
  background-color: v-bind(editBackground);
}

#changeIcon {
  background-color: rgb(229, 229, 231);
}

#loadingIcon {
  position: absolute;
  top: 9px;
  left: -29px;
}

.toolIcon {
  position: absolute;
  width: 20px;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
}

#canvas {
  position: relative;
  width: 900px;
  height: 635px;
  top: 25px;
  left: 20px;
}

#layoutPicture {
  position: absolute;
  width: 96%;
  height: 96%;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  margin: 0 auto;
  text-align: center;
  pointer-events: none;
}

#furnitureList {
  position: fixed;
  padding-left: 0;
  display: inline-block;
  margin-left: 10px;
  margin-right: 15px;
  width: 320px;
  height: 750px;
  overflow: scroll;
}

#furnitureList::-webkit-scrollbar {
  width: 10px;
  height: 100%;
}

#furnitureList::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: rgba(75, 75, 75, 0.3);
}

#furnitureList::-webkit-scrollbar-thumb:hover {
  background-color: rgba(75, 75, 75, 0.5);
}

#furnitureList::-webkit-scrollbar-track {
  background-color: transparent;
}

.furnitureListItem {
  width: 100%;
  list-style: none;
}

.addToLayout {
  position: relative;
  vertical-align: top;
  height: 40px;
  width: auto;
  margin-top: 8px;
  margin-right: 10px;
  fill: rgba(200, 200, 200, 0.95);
  opacity: 0;
  cursor: default;
  transition: opacity 0.3s;
}

.editing {
  opacity: 1;
  cursor: pointer;
}

#uploadLayoutDiv {
  position: relative;
  width: 300px;
  height: 50px;
  margin: 0 auto;
  color: white;
  font-size: 24px;
  text-align: center;
  font-weight: 700;
  background-color: rgb(255, 227, 127);
  border-radius: 15px;
  transition: background-color 0.3s;
  cursor: pointer;
}

#noLayout {
  display: block;
  width: 480px;
  margin: 120px auto 70px;
}

#uploadLayoutDiv:hover {
  background-color: rgb(250, 212, 79);
}

#uploadText {
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
}

#uploadLayout {
  height: 50px;
  width: 300px;
  opacity: 0;
  cursor: pointer;
}

</style>
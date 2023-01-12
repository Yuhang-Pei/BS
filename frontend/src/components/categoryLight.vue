<template>
  <div class="categoryLight">
    <h1>灯具</h1>
    <div v-if="format === 'info'" id="addIcon" @click="newLight">
      <img class="newDevice" src="@/assets/utility/add1.svg">
    </div>
    <light-button v-if="format === 'button'"
                  v-for="(light, light_id) in light_list"
                  :light-id="light_id"
                  :light-name="light.device_name"
                  :light-status="light.light_state"
                  :light-room="light.room_name"
                  :light-luminance="light.luminance">
    </light-button>

    <light-info v-if="format === 'info'"
                v-for="(light, light_id) in light_list"
                :light-id="light_id"
                :light-name="light.device_name"
                :light-status="light.light_state"
                :light-room="light.room_name"
                :light-luminance="light.luminance">
    </light-info>
<!--    <light-info light-name="餐厅灯" :light-status="true" light-room="餐厅"></light-info>-->
  </div>
</template>

<script>
import LightButton from "@/components/lightButton";
import Switch from "@/components/switch.vue";
import LightInfo from "@/components/lightInfo";
import {global_data, isObjectEmpty} from "@/store";
export default {
  name: "categoryLight",
  components: {LightInfo, Switch, LightButton},
  props: {
    format: {
      required: true
    }
  },
  data() {
    return {
      light_list: {}
    }
  },
  created() {
    if (isObjectEmpty(global_data.light_list)) {
      this.$http.post('light/get_all_lights', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.light_list = global_data.light_list = res.data.light_list;
            this.$emit('finishLoading', 0);
          });
    }
    else {
      this.light_list = global_data.light_list;
      this.$emit('finishLoading', 0);
    }
  },
  methods: {
    newLight() {
      let room_id = Object.keys(global_data.room_list)[0];
      this.$http.post('/light/add_light', {
        'room_id': room_id
      }).then((res) => {
        console.log(res)
        console.log(global_data)
        let light_id = res.data.light_id;
        global_data.light_list[light_id] = {
          'light_state': false,
          'luminance':   0,
          'light_icon':  0,
          'device_name':  '灯',
          'device_model': '',
          'device_x':     null,
          'device_y':     null,
          'room_id':      room_id,
          'room_name':    global_data.room_list[room_id],
          'scenario_id':  this.$cookies.get('scenario_id')
        };
        this.$router.push({
          path: '/lightDetail',
          query: {
            id: light_id
          }
        })
      });
    }
  }
}
</script>

<style scoped>

.categoryLight {
  position: relative;
  margin-bottom: 31px;
}

.categoryLight h1 {
  color: white;
  font-size: 20px;
  margin-bottom: 14px;
  margin-left: 5px;
}

#addIcon {
  position: absolute;
  top: 0;
  left: 55px;
  cursor: pointer;
}

.newDevice {
  position: absolute;
  top: 2px;
  width: 22px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.newDevice:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

</style>
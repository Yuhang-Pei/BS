<template>
  <div class="categorySwitch">
    <h1>开关</h1>
    <div v-if="format === 'info'" id="addIcon" @click="newSwitch">
      <img class="newDevice" src="@/assets/utility/add1.svg">
    </div>
    <switch-button v-if="format === 'button'"
                   v-for="(_switch, switch_id) in switch_list"
                   :switch-id="switch_id"
                   :switch-name="_switch.device_name"
                   :switch-status="_switch.switch_state"
                   :switch-room="_switch.room_name">
    </switch-button>

    <switch-info v-if="format === 'info'"
                 v-for="(_switch, switch_id) in switch_list"
                 :switch-id="switch_id"
                 :switch-name="_switch.device_name"
                 :switch-status="_switch.switch_state"
                 :switch-room="_switch.room_name">
    </switch-info>
  </div>
</template>

<script>
import switchButton from "@/components/switchButton";
import SwitchInfo from "@/components/switchInfo";
import {global_data, isObjectEmpty} from "@/store";

export default {
  name: "categorySwitch",
  components: {SwitchInfo, switchButton},
  props: {
    format: {
      required: true
    }
  },
  data() {
    return {
      switch_list: {}
    }
  },
  created() {
    if (isObjectEmpty(global_data.switch_list)) {
      this.$http.post('switch/get_all_switches', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.switch_list = global_data.switch_list = res.data.switch_list;
            this.$emit('finishLoading', 3);
          });
    }
    else {
      this.switch_list = global_data.switch_list;
      this.$emit('finishLoading', 3);
    }
  },
  methods: {
    newSwitch() {
      let room_id = Object.keys(global_data.room_list)[0];
      this.$http.post('/switch/add_switch', {
        'room_id': room_id
      }).then((res) => {
        let switch_id = res.data.switch_id;
        global_data.switch_list[switch_id] = {
          'switch_state': false,
          'switch_icon':  0,
          'device_name':  '开关',
          'device_model': '',
          'device_x':     null,
          'device_y':     null,
          'room_id':      room_id,
          'room_name':    global_data.room_list[room_id],
          'scenario_id':  this.$cookies.get('scenario_id')
        };
        this.$router.push({
          path: '/switchDetail',
          query: {
            id: switch_id
          }
        })
      });
    }
  }
}
</script>

<style scoped>

.categorySwitch {
  position: relative;
  margin-bottom: 31px;
}

.categorySwitch h1 {
  color: white;
  font-size: 20px;
  margin-left: 5px;
  margin-bottom: 14px;
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
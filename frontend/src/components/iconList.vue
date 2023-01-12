<template>
  <div id="iconListContainer">
    <device-icon v-for="i in range" @click="changeIcon(i-1)"
                 class="deviceIcon" :class="{'selectedIcon': i-1==icon_id}"
                 :type="type" :state="true" :index="i-1"></device-icon>
  </div>
  <Mask @click="loseIconFocus"></Mask>
</template>

<script>
import DeviceIcon from "@/components/deviceIcon.vue";
import {global_data} from "@/store";
import Mask from "@/components/mask.vue";

export default {
  name: "iconList",
  components: {Mask, DeviceIcon},
  props: {
    type: {
      required: true,
      type: String
    },
    iconId: {
      required: true
    },
    deviceId: {
      required: true
    }
  },
  data() {
    if (this.type === 'light')
      return {
        icon_id: this.iconId,
        range: 5
      }
    else if (this.type === 'lock')
      return {
        icon_id: this.iconId,
        range: 3
      }
    else if (this.type === 'sensor')
      return {
        icon_id: this.iconId,
        range: 2
      }
    else if (this.type === 'switch')
      return {
        icon_id: this.iconId,
        range: 6
      }
  },
  methods: {
    changeIcon(new_icon_id) {
      if (this.icon_id != new_icon_id) {
        this.$http.post('/device/change_device_icon', {
          'device_id': this.deviceId,
          'device_type': this.type,
          'device_icon': new_icon_id
        }).then((res) => {
          this.icon_id = new_icon_id;
          this.$emit('changeIcon', new_icon_id);
        })
      }
    },
    loseIconFocus() {
      this.$emit('loseIconFocus');
    }
  }
}
</script>

<style scoped>

#iconListContainer {
  position: absolute;
  left: 50%;
  transform: translateX(80px);
  top: 0;
  width: 90px;
  height: 145px;
  padding-top: 5px;
  padding-bottom: 4px;
  z-index: 20;
  border-radius: 10px;
  background-color: rgb(255, 255, 255, 0.8);
  backdrop-filter: blur(25px);
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.05);
  overflow-y: scroll;
}

#iconListContainer::-webkit-scrollbar {
  width: 6px;
  height: 100%;
}

#iconListContainer::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background-color: rgba(75, 75, 75, 0.3);
}

#iconListContainer::-webkit-scrollbar-thumb:hover {
  background-color: rgba(75, 75, 75, 0.5);
}

#iconListContainer::-webkit-scrollbar-track {
  background-color: transparent;
}

.deviceIcon {
  height: 60px;
  width: 60px;
  margin-top: 4px;
  margin-bottom: 4px;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s;
}

.selectedIcon {
  box-shadow: 0 0 0 4px rgb(210, 210, 210);
}

</style>
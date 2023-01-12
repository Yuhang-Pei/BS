<template>
  <img :src="state?icon_on:icon_off">
</template>

<script>

import light_on_0 from '@/assets/furnitureIcon/0light-on.svg'
import light_off_0 from '@/assets/furnitureIcon/0light-off.svg'
import light_on_1 from '@/assets/furnitureIcon/1light-on.svg'
import light_off_1 from '@/assets/furnitureIcon/1light-off.svg'
import light_on_2 from '@/assets/furnitureIcon/2light-on.svg'
import light_off_2 from '@/assets/furnitureIcon/2light-off.svg'
import light_on_3 from '@/assets/furnitureIcon/3light-on.svg'
import light_off_3 from '@/assets/furnitureIcon/3light-off.svg'
import light_on_4 from '@/assets/furnitureIcon/4light-on.svg'
import light_off_4 from '@/assets/furnitureIcon/4light-off.svg'

import lock_on_0 from '@/assets/furnitureIcon/0lock-on.svg'
import lock_off_0 from '@/assets/furnitureIcon/0lock-off.svg'
import lock_on_1 from '@/assets/furnitureIcon/1lock-on.svg'
import lock_off_1 from '@/assets/furnitureIcon/1lock-off.svg'
import lock_on_2 from '@/assets/furnitureIcon/2lock-on.svg'
import lock_off_2 from '@/assets/furnitureIcon/2lock-off.svg'

import sensor_on_0 from '@/assets/furnitureIcon/0sensor-on.svg'
import sensor_off_0 from '@/assets/furnitureIcon/0sensor-off.svg'
import sensor_on_1 from '@/assets/furnitureIcon/1sensor-on.svg'
import sensor_off_1 from '@/assets/furnitureIcon/1sensor-off.svg'

import switch_on_0 from '@/assets/furnitureIcon/0switch-on.svg'
import switch_off_0 from '@/assets/furnitureIcon/0switch-off.svg'
import switch_on_1 from '@/assets/furnitureIcon/1switch-on.svg'
import switch_off_1 from '@/assets/furnitureIcon/1switch-off.svg'
import switch_on_2 from '@/assets/furnitureIcon/2switch-on.svg'
import switch_off_2 from '@/assets/furnitureIcon/2switch-off.svg'
import switch_on_3 from '@/assets/furnitureIcon/3switch-on.svg'
import switch_off_3 from '@/assets/furnitureIcon/3switch-off.svg'
import switch_on_4 from '@/assets/furnitureIcon/4switch-on.svg'
import switch_off_4 from '@/assets/furnitureIcon/4switch-off.svg'
import switch_on_5 from '@/assets/furnitureIcon/5switch-on.svg'
import switch_off_5 from '@/assets/furnitureIcon/5switch-off.svg'

export default {
  name: "deviceIcon",
  data() {
    if (this.type === 'light') {
      if (this.index == 1)
        return {
          icon_on: light_on_1,
          icon_off: light_off_1,
        }
      else if (this.index == 2)
        return {
          icon_on: light_on_2,
          icon_off: light_off_2,
        }
      else if (this.index == 3)
        return {
          icon_on: light_on_3,
          icon_off: light_off_3,
        }
      else if (this.index == 4)
        return {
          icon_on: light_on_4,
          icon_off: light_off_4,
        }
      else
        return {
          icon_on: light_on_0,
          icon_off: light_off_0,
        }
    }
    else if (this.type === 'lock') {
      if (this.index == 1)
        return {
          icon_on: lock_on_1,
          icon_off: lock_off_1,
        }
      else if (this.index == 2)
        return {
          icon_on: lock_on_2,
          icon_off: lock_off_2,
        }
      else
        return {
          icon_on: lock_on_0,
          icon_off: lock_off_0,
        }
    }
    else if (this.type === 'sensor') {
      if (this.index == 1)
        return {
          icon_on: sensor_on_1,
          icon_off: sensor_off_1,
        }
      else
        return {
          icon_on: sensor_on_0,
          icon_off: sensor_off_0,
        }
    }
    else if (this.type === 'switch') {
      if (this.index == 1)
        return {
          icon_on: switch_on_1,
          icon_off: switch_off_1,
        }
      else if (this.index == 2)
        return {
          icon_on: switch_on_2,
          icon_off: switch_off_2,
        }
      else if (this.index == 3)
        return {
          icon_on: switch_on_3,
          icon_off: switch_off_3,
        }
      else if (this.index == 4)
        return {
          icon_on: switch_on_4,
          icon_off: switch_off_4,
        }
      else if (this.index == 5)
        return {
          icon_on: switch_on_5,
          icon_off: switch_off_5,
        }
      else
        return {
          icon_on: switch_on_0,
          icon_off: switch_off_0,
        }
    }
  },
  props: {
    edit: {
      default: true
    },
    state: {
      required: true,
      type: Boolean
    },
    type: {
      required: true,
      type: String
    },
    index: {
      default: 0
    }
  }
}
</script>

<style scoped>

</style>
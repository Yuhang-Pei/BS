<template>
  <div class="categoryLock">
    <h1>锁</h1>
    <div v-if="format === 'info'" id="addIcon"  @click="newLock">
      <img class="newDevice" src="@/assets/utility/add1.svg">
    </div>
    <lock-button v-if="format === 'button'"
                 v-for="(lock, lock_id) in lock_list"
                 :lock-id="lock_id"
                 :lock-name="lock.device_name"
                 :lock-status="lock.lock_state"
                 :lock-room="lock.room_name">
    </lock-button>

    <lock-info v-if="format === 'info'"
               v-for="(lock, lock_id) in lock_list"
               :lock-id="lock_id"
               :lock-name="lock.device_name"
               :lock-status="lock.lock_state"
               :lock-room="lock.room_name">
    </lock-info>
  </div>
</template>

<script>
import lockButton from "@/components/lockButton";
import LockInfo from "@/components/lockInfo";
import {global_data, isObjectEmpty} from "@/store";

export default {
  name: "categoryLock",
  components: {LockInfo, lockButton},
  props: {
    format: {
      required: true
    }
  },
  data() {
    return {
      lock_list: {}
    }
  },
  created() {
    if (isObjectEmpty(global_data.lock_list)) {
      this.$http.post('lock/get_all_locks', this.$cookies.get('scenario_id'))
          .then((res) => {
            this.lock_list = global_data.lock_list = res.data.lock_list;
            this.$emit('finishLoading', 1);
          });
    }
    else {
      this.lock_list = global_data.lock_list;
      this.$emit('finishLoading', 1);
    }
  },
  methods: {
    newLock() {
      let room_id = Object.keys(global_data.room_list)[0];
      this.$http.post('/lock/add_lock', {
        'room_id': room_id
      }).then((res) => {
        let lock_id = res.data.lock_id;
        global_data.lock_list[lock_id] = {
          'lock_state': false,
          'lock_icon':  0,
          'device_name':  '锁',
          'device_model': '',
          'device_x':     null,
          'device_y':     null,
          'room_id':      room_id,
          'room_name':    global_data.room_list[room_id],
          'scenario_id':  this.$cookies.get('scenario_id')
        };
        this.$router.push({
          path: '/lockDetail',
          query: {
            id: lock_id
          }
        })
      });
    }
  }
}
</script>

<style scoped>

.categoryLock {
  position: relative;
  margin-bottom: 31px;
}

.categoryLock h1 {
  color: white;
  font-size: 20px;
  margin-left: 5px;
  margin-bottom: 14px;
}

#addIcon {
  position: absolute;
  top: 0;
  left: 35px;
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
<template>
  <back-picture></back-picture>
  <navigate :current-choice="5"></navigate>
  <div class="main">
    <div id="loadingContainer" v-show="loading">
      <loading id="loadingAnimation" height="70px" length="16px" size="70px"></loading>
    </div>

    <h1>灯具</h1>

    <lock-statics :key="statics_key"></lock-statics>

    <category-room class="rooms" v-for="(room, room_id) in room_list" v-show="isShowRoom(room_id)" :room-id="room_id" type="lock"></category-room>

    <div class="tail"></div>
  </div>
</template>

<script>
import {global_data, isObjectEmpty} from "@/store";
import BackPicture from "@/components/backPicture.vue";
import Navigate from "@/components/navigate.vue";
import Loading from "@/components/loading.vue";
import CategoryRoom from "@/components/categoryRoom.vue";
import LockStatics from "@/components/lockStatics.vue";

export default {
  name: "lockView",
  components: {LockStatics, CategoryRoom, Loading, Navigate, BackPicture},
  data() {
    return {
      loading: true,
      room_list: global_data.room_list,
      statics_key: 0
    }
  },
  created() {
    this.loading = true;
    if (isObjectEmpty(global_data.lock_list)) {
      this.$http.post('lock/get_all_locks', this.$cookies.get('scenario_id'))
          .then((res) => {
            global_data.lock_list = res.data.lock_list;
            this.loading = false;
          });
    }
    else
      this.loading = false;
  },
  mounted() {
    setInterval(() => {
      this.updateStatics();
    }, 1000);
  },
  methods: {
    isShowRoom(room_id) {
      for (let lock_id in global_data.lock_list)
        if (global_data.lock_list[lock_id].room_id == room_id)
          return true;
      return false;
    },
    updateStatics() {
      this.statics_key += 1;
    }
  }
}
</script>

<style scoped>

.main {
  margin-left: 215px;
  padding: 30px 0 0 30px;
}

#loadingContainer {
  position: absolute;
  top: 45%;
  left: 45%;
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

h1 {
  color: white;
  font-size: 26px;
  margin-left: 5px;
  margin-bottom: 22px;
}

.tail {
  height: 160px;
  background-color: transparent;
}

.rooms {
  margin-bottom: 31px;
}

</style>
<template>
  <router-view v-if="!loading"/>
</template>

<script>
import {global_data, isObjectEmpty} from "@/store";

export default {
  name: 'App',
  data() {
    return {
      loading: true,
      is_mobile: false,
      scalesNum: 1
    }
  },
  created() {
    if (isObjectEmpty(global_data.current_scenario)) {
      this.$http.post('/scenario/get_scenario', {
        scenario_id: this.$cookies.get('scenario_id')
      }).then((res) => {
        global_data.current_scenario = res.data.scenario;
      })
    }

    if (isObjectEmpty(global_data.room_list)) {
      this.$http.post('/room/get_all_rooms', {
        scenario_id: this.$cookies.get('scenario_id')
      }).then((res) => {
        global_data.room_list = res.data.room_list;
        this.loading = false;
      });
    }
  },
  mounted() {
    window.onload = () => {
      return (
          () => {
            let width = document.body.clientWidth;
            let height = window.screen.availHeight;
            global_data.is_mobile = this.is_mobile = (width / height < 0.78);
          }
      )()
    };
    window.onresize = () => {
      return (
          () => {
            let width = document.body.clientWidth;
            let height = window.screen.availHeight;
            global_data.is_mobile = this.is_mobile = (width / height < 0.78);
          }
      )()
    };
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  margin: 0;
  user-select: none;
}

ul, li {
  list-style: none;
  padding: 0;
  margin: 0;
}

</style>

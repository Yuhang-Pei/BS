<template>
  <div class="home">
    <back-picture></back-picture>
    <navigate v-if="!global_data.is_mobile" :current-choice="0"></navigate>
    <mobile-nav v-if="global_data.is_mobile" :cur-choice="0"></mobile-nav>

    <div v-if="!global_data.is_mobile" class="main">
      <div id="loadingContainer" v-show="loading[0] || loading[1] || loading[2] || loading[3]">
        <loading id="loadingAnimation" height="70px" length="16px" size="70px"></loading>
      </div>
      <h1 id="scenario" v-text="global_data.current_scenario.scenario_name"></h1>
      <environment-statics :key="environment_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></environment-statics>
      <light-statics :key="light_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></light-statics>
      <lock-statics :key="lock_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></lock-statics>
      <sensor-statics :key="sensor_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></sensor-statics>
      <switch-statics :key="switch_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></switch-statics>
      <div style="height: 28px"></div>

      <category-light format="button"  @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-light>
      <category-lock format="button" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-lock>
      <category-sensor format="button" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-sensor>
      <category-switch format="button" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-switch>
      <div class="tail"></div>
    </div>

    <div v-if="global_data.is_mobile" class="m_main">
      <div id="loadingContainer" v-show="loading[0] || loading[1] || loading[2] || loading[3]">
        <loading id="loadingAnimation" height="55px" width="4px" length="14px" size="50px"></loading>
      </div>
      <h1 id="scenario" v-text="global_data.current_scenario.scenario_name"></h1>
      <environment-statics :key="environment_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></environment-statics>
      <light-statics :key="light_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></light-statics>
      <lock-statics :key="lock_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></lock-statics>
      <sensor-statics :key="sensor_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></sensor-statics>
      <switch-statics :key="switch_statics_key" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></switch-statics>
      <div style="height: 28px"></div>

      <category-light format="button"  @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-light>
      <category-lock format="button" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-lock>
      <category-sensor format="button" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-sensor>
      <category-switch format="button" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-switch>
      <div class="tail"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import BackPicture from "@/components/backPicture";
import Navigate from "@/components/navigate";
import CategoryLight from "@/components/categoryLight";
import CategoryLock from "@/components/categoryLock";
import CategorySensor from "@/components/categorySensor";
import CategorySwitch from "@/components/categorySwitch";
import Switch from "@/components/switch";
import Loading from "@/components/loading.vue";
import {global_data} from "@/store";
import LightStatics from "@/components/lightStatics.vue";
import LockStatics from "@/components/lockStatics.vue";
import SensorStatics from "@/components/sensorStatics.vue";
import SwitchStatics from "@/components/switchStatics.vue";
import EnvironmentStatics from "@/components/environmentStatics.vue";
import MobileNav from "@/components/mobileNav.vue";

export default {
  name: 'HomeView',
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {
    MobileNav,
    EnvironmentStatics,
    SwitchStatics,
    SensorStatics,
    LockStatics,
    LightStatics,
    Loading,
    CategorySwitch,
    CategorySensor,
    CategoryLock,
    CategoryLight,
    Navigate,
    BackPicture,
    Switch
  },
  data() {
    return {
      loading: [true, true, true, true],
      light_statics_key: 0,
      lock_statics_key: 0,
      sensor_statics_key: 0,
      switch_statics_key: 0,
      environment_statics_key: 0
    }
  },
  mounted() {
    setInterval(() => {
      this.updateStatics();
    }, 1000);
  },
  methods: {
    finishLoading(index) {
      this.loading[index] = false;
    },
    updateStatics() {
      this.light_statics_key += 1;
      this.lock_statics_key += 1;
      this.sensor_statics_key += 1;
      this.switch_statics_key += 1;
      this.environment_statics_key += 1;
    }
  }
}
</script>

<style>



.main {
  position: fixed;
  margin-left: 215px;
  padding: 30px 0 0 30px;
  width: calc(100% - 245px);
  height: 100%;
  overflow-y: scroll;
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

#scenario {
  color: white;
  font-size: 26px;
  margin-left: 5px;
  margin-bottom: 22px;
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

.tail {
  height: 100px;
  background-color: transparent;
}

/* mobile */

.m_main {
  position: fixed;
  padding: 50px 0 0 30px;
  height: calc(100% - 115px);
  overflow-y: scroll;
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

.m_main #loadingContainer {
  position: fixed;
  top: 45%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 100px;
  height: 100px;
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  border-radius: 25px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
}

.m_main #loadingAnimation {
  top: 25px;
  left: 0px;
}

</style>
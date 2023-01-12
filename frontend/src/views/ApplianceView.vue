<template>
  <div class="appliance">
    <back-picture></back-picture>
    <navigate v-if="!global_data.is_mobile" :current-choice="1"></navigate>
    <mobile-nav v-if="global_data.is_mobile" :cur-choice="1"></mobile-nav>

    <div v-if="!global_data.is_mobile" class="main">
      <div id="loadingContainer" v-show="loading[0] || loading[1] || loading[2] || loading[3]">
        <loading id="loadingAnimation" height="70px" length="16px" size="70px"></loading>
      </div>
      <h1>我的设备</h1>
      <category-light format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-light>
      <category-lock format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-lock>
      <category-sensor format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-sensor>
      <category-switch format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-switch>
      <div class="tail"></div>
    </div>

    <div v-if="global_data.is_mobile" class="m_main">
      <div id="loadingContainer" v-show="loading[0] || loading[1] || loading[2] || loading[3]">
        <loading id="loadingAnimation" height="55px" width="4px" length="14px" size="50px"></loading>
      </div>
      <h1>我的设备</h1>
      <category-light format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-light>
      <category-lock format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-lock>
      <category-sensor format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-sensor>
      <category-switch format="info" @finishLoading="finishLoading" v-show="!loading[0] && !loading[1] && !loading[2] && !loading[3]"></category-switch>
      <div class="tail"></div>
    </div>
  </div>
</template>

<script>
import BackPicture from "@/components/backPicture";
import Navigate from "@/components/navigate";
import CategoryLight from "@/components/categoryLight.vue";
import CategoryLock from "@/components/categoryLock.vue";
import CategorySensor from "@/components/categorySensor.vue";
import CategorySwitch from "@/components/categorySwitch.vue";
import Loading from "@/components/loading.vue";
import MobileNav from "@/components/mobileNav.vue";
import {global_data} from "@/store";

export default {
  name: "ApplianceView",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {MobileNav, Loading, CategorySwitch, CategorySensor, CategoryLock, CategoryLight, Navigate, BackPicture},
  data() {
    return {
      loading: [true, true, true, true]
    }
  },
  methods: {
    finishLoading(index) {
      this.loading[index] = false;
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
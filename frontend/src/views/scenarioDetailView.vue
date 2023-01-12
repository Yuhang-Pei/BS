<template>
  <back-picture></back-picture>
  <navigate v-if="!global_data.is_mobile" :current-choice="3"></navigate>
  <mobile-nav v-if="global_data.is_mobile" :cur-choice="2"></mobile-nav>

  <div :class="global_data.is_mobile?'m_main':'main'">
    <back-button back-button-color="rgb(241, 195, 4)"></back-button>
    <h1 id="scenarioNameTitle" v-text="scenario_name"></h1>

    <div id="scenarioNameLine">
      <h2>场景名称</h2>
      <h3 @click="getNameFocus">{{scenario_name}}</h3>
      <input ref="nameInput" v-show="nameFocus" @focusout="loseNameFocus" type="text" class="textInput" v-model="scenario_name">
    </div>

    <div id="scenarioBackgroundLine">
      <h2>背景</h2>
      <div id="backgroundContainer">
        <div v-for="i in 6" class="backgroundChoice" :class="{currentChoice: background_picture+1===i}" :id="'choice'+i"
             @click="changeBackground(i-1)"></div>
      </div>
    </div>

    <div id="changeScenarioLine">
      <p id="changeScenario" @click="changeScenario">切 换 为 该 场 景</p>
    </div>

    <div id="deleteScenarioLine" @click="deleteScenario">
      <p id="deleteScenario">删 除 场 景</p>
    </div>

    <delete-warning v-if="deleteWarning"
                    @confirmDelete="confirmDelete"
                    @cancelDelete="cancelDelete">
    </delete-warning>

    <div v-if="deleteFail" id="deleteFailContainer">
      <div id="deleteFailSubcontainer">
        <h1 id="deleteFailTitle">无法删除当前选中的场景</h1>
        <div id="cancelDelete">
          <p id="cancel" @click="deleteFail=false">确 定</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BackPicture from "@/components/backPicture.vue";
import Navigate from "@/components/navigate.vue";
import BackButton from "@/components/backButton.vue";
import loading from "@/components/loading.vue";
import {global_data} from "@/store";
import MobileNav from "@/components/mobileNav.vue";
import DeleteWarning from "@/components/deleteWarning.vue";

export default {
  name: "scenarioDetailView",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {DeleteWarning, MobileNav, BackButton, Navigate, BackPicture},
  data() {
    return {
      scenario_id: this.$route.query.id,
      scenario_name: '',
      is_current: this.scenario_id == this.$cookies.get('scenario_id'),
      background_picture: 0,

      loading: true,
      nameFocus: false,
      deleteWarning: false,
      deleteFail: false
    }
  },
  created() {
    this.$http.post('/scenario/get_scenario', {
      scenario_id: this.scenario_id
    }).then((res) => {
      this.scenario_name = res.data.scenario.scenario_name;
      this.background_picture = res.data.scenario.background_picture;
      this.loading = false;
    })
  },
  methods: {
    getNameFocus() {
      this.nameFocus = true;
      this.$nextTick(() => {
        this.$refs.nameInput.focus();
      })
    },
    loseNameFocus(e) {
      this.nameFocus = false;
      let new_name = e.target.value;
      this.$http.post('/scenario/change_scenario_name', {
        scenario_id: this.scenario_id,
        scenario_name: new_name
      }).then((res) => {
        if (this.is_current)
          global_data.current_scenario.scenario_name = new_name;
      })
    },
    changeBackground(background_id) {
      if (background_id !== this.background_picture) {
        this.background_picture = background_id;
        this.$http.post('/scenario/change_background', {
          scenario_id: this.scenario_id,
          background: background_id
        }).then((res) => {
          if (this.scenario_id === this.$cookies.get('scenario_id'))
            global_data.current_scenario.background_picture = background_id;
        })
      }
    },
    async changeScenario() {
      if (this.scenario_id !== this.$cookies.get('scenario_id')) {
        await this.$http.post('/scenario/get_scenario', {
          scenario_id: this.scenario_id
        }).then((res) => {
          global_data.current_scenario = res.data.scenario;
          global_data.room_list = {};
          global_data.light_list = {};
          global_data.lock_list = {};
          global_data.sensor_list = {};
          global_data.switch_list = {};
          this.$cookies.set('scenario_id', this.scenario_id);
          this.$router.push({
            path: '/home'
          });
        })
      }
    },
    deleteScenario() {
      this.deleteWarning = true;
    },
    confirmDelete() {
      const that = this;
      const current_scenario = that.$cookies.get('scenario_id');
      if (current_scenario !== this.scenario_id) {
        this.$http.post('/scenario/delete_scenario', {
          'scenario_id': this.scenario_id
        }).then((res) => {
          that.$router.go(-1);
        })
      }
      else {
        this.deleteFail = true;
      }
      this.deleteWarning = false;
    },
    cancelDelete() {
      this.deleteWarning = false;
    }
  }
}
</script>

<style scoped>

.main {
  position: fixed;
  margin-left: 215px;
  padding: 30px 0 0 30px;
  width: calc(100% - 245px);
  height: 100%;
  background-color: rgb(243, 242, 248);
  overflow-y: scroll;
}

h2 {
  position: absolute;
  left: 20px;
  top: 14px;
  font-size: 18px;
  color: rgb(5, 5, 5);
  font-weight: bold;
}

h3 {
  position: absolute;
  right: 20px;
  top: 14px;
  text-align: right;
  min-width: 50px;
  min-height: 20px;
  font-size: 18px;
  font-weight: normal;
  color: rgb(147, 143, 137);
  transition: color 0.3s;
  cursor: pointer;
}

h3:hover {
  color: rgb(80, 80, 80);
}

#scenarioNameTitle {
  margin: 20px auto;
  height: 40px;
  text-align: center;
}

#scenarioNameLine {
  position: relative;
  top: 20px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

#scenarioBackgroundLine {
  position: relative;
  top: 20px;
  width: 97%;
  height: 240px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.textInput {
  position: absolute;
  right: 18px;
  top: 14px;
  text-align: right;
  min-width: 50px;
  min-height: 20px;
  font-size: 18px;
  font-weight: normal;
  color: rgb(80, 80, 80);
  border: none;
  outline: none;
  text-align: right;
  caret-color: rgb(255, 207, 8);
}

#backgroundContainer {
  position: relative;
  top: 54px;
  left: 20px;
  height: 180px;
  width: calc(100% - 40px);
  overflow-x: auto;
  white-space: nowrap;
}

#backgroundContainer::-webkit-scrollbar {
  display: none;
}

.backgroundChoice {
  display: inline-block;
  width: 258px;
  height: 160px;
  margin-right: 20px;
  background-size: cover;
  border-radius: 10px;
  cursor: pointer;
  border: white 4px solid;
  transition: all 0.3s;
}

.backgroundChoice:last-child {
  margin-right: 0;
}

.currentChoice {
  border: rgb(241, 195, 4) 4px solid;
}

#choice1 {
  background-image: url("@/assets/backPicture/backPicture1.jpg");
}

#choice2 {
  background-image: url("@/assets/backPicture/backPicture2.jpg");
}

#choice3 {
  background-image: url("@/assets/backPicture/backPicture3.jpg");
}

#choice4 {
  background-image: url("@/assets/backPicture/backPicture4.jpg");
}

#choice5 {
  background-image: url("@/assets/backPicture/backPicture5.jpg");
}

#choice6 {
  background-image: url("@/assets/backPicture/backPicture6.jpg");
}

#changeScenarioLine, #deleteScenarioLine {
  position: relative;
  top: 80px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  transition: all 0.3s;
  cursor: pointer;
}

#changeScenario {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: dodgerblue;
}

#deleteScenario {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: red;
}

.m_main {
  position: fixed;
  padding: 30px 0 0 0;
  width: 100%;
  height: calc(100% - 95px);
  overflow-y: scroll;
  overflow-x: hidden;
  background-color: rgb(243, 242, 248);
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

.m_main #scenarioNameLine,
.m_main #scenarioBackgroundLine,
.m_main #changeScenarioLine,
.m_main #deleteScenarioLine {
  position: relative;
  width: 94%;
  margin-top: 10px;
  margin-left: 3%;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.m_main .backgroundChoice {
  width: 150px;
  height: 110px;
  margin-right: 8px;
}

.m_main .backgroundChoice:last-child {
  margin-right: 0;
}

.m_main #scenarioBackgroundLine {
  height: 190px;
}

#deleteFailContainer {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%,-50%);
  height: 120px;
  width: 240px;
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
  border-radius: 15px;
  z-index: 20;
}

#deleteFailSubcontainer {
  position: relative;
  width: 100%;
  height: 100%;
}

#deleteFailTitle {
  position: relative;
  top: 24px;
  text-align: center;
  font-size: 16px;
  color: rgb(5, 5, 5);
  font-weight: 500;
}

#cancelDelete {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 45%;
  border-top: 1px solid rgb(220, 220, 220);
  border-bottom-right-radius: 15px;
  border-bottom-left-radius: 15px;
  transition: background-color 0.3s;
  cursor: pointer;
}

#cancelDelete:hover {
  background-color: rgba(200, 200, 200, 0.3);
}

#cancel {
  position: relative;
  top: 16px;
  font-size: 17px;
  text-align: center;
  color: rgb(100, 100, 100);
}

</style>
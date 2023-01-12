<template>
  <back-picture></back-picture>
  <navigate v-if="!global_data.is_mobile" :current-choice="3"></navigate>
  <mobile-nav v-if="global_data.is_mobile" :cur-choice="2"></mobile-nav>

  <div :class="global_data.is_mobile?'m_main':'main'">
    <back-button back-button-color="rgb(241, 195, 4)"></back-button>
    <div id="personalInfoLine">
      <img id="avatar" src="@/assets/avatar/6.png">
      <h1 id="userName">{{user_name}}</h1>
      <h2 id="userPhone">{{phone}}</h2>
    </div>
<!--    <div id="editUserNameLine" @click="">-->
<!--      <h3>修改用户名</h3>-->
<!--      <img class="moreIcon" src="@/assets/utility/more.svg">-->
<!--      <h4>{{user_name}}</h4>-->
<!--    </div>-->
<!--    <div id="modifyPasswordLine">-->
<!--      <h3>修改手机号</h3>-->
<!--      <img class="moreIcon" src="@/assets/utility/more.svg">-->
<!--    </div>-->

    <h2 id="scenarioListTitle">场景</h2>
    <ul id="scenarioList">
      <li class="scenarioItem" v-for="(scenario_info, scenario_id) in scenario_list">
        <h3>{{scenario_info.scenario_name}}</h3>
        <img v-show="scenario_id === $cookies.get('scenario_id')" class="currentIcon" src="@/assets/utility/right.svg">
        <img class="moreIcon" src="@/assets/utility/more.svg" @click="scenarioDetail(scenario_id)">
      </li>
    </ul>
    <div id="newScenarioLine">
      <p id="newScenario" @click="newScenario">新 增 场 景</p>
    </div>

    <div class="division"></div>

    <div id="logOutLine">
      <p id="logOut" @click="logOut">退 出</p>
    </div>

    <div class="tail"></div>
  </div>
</template>

<script>

import BackPicture from "@/components/backPicture";
import Navigate from "@/components/navigate";
import BackButton from "@/components/backButton";
import MobileNav from "@/components/mobileNav.vue";
import {global_data} from "@/store";

export default {
  name: "SettingView",
  computed: {
    global_data() {
      return global_data
    }
  },
  components: {MobileNav, BackButton, Navigate, BackPicture},
  data() {
    return {
      user_id: this.$cookies.get('user_id'),
      user_name: this.$cookies.get('user_name'),
      phone: this.$cookies.get('phone'),
      scenario_list: {}
    }
  },
  created() {
    this.getScenarioList();
  },
  methods: {
    getScenarioList() {
      this.$http.post('/scenario/get_scenarios', this.user_id)
          .then((res) => {
            this.scenario_list = res.data.scenario_list;
          });
    },
    logOut() {
      let cookies = this.$cookies.keys();
      for (let cookie of cookies)
        this.$cookies.remove(cookie);
      this.$router.push('/');
    },
    scenarioDetail(scenario_id) {
      this.$router.push({
        path: '/scenarioDetail',
        query: {
          id: scenario_id
        }
      })
    },
    newScenario() {
      this.$http.post('/scenario/new_scenario', this.$cookies.get('user_id'))
          .then((res) => {
            this.$router.push({
              path: '/scenarioDetail',
              query: {
                id: res.data.scenario_id
              }
            })
          })
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

h3 {
  position: absolute;
  left: 20px;
  top: 14px;
  font-size: 18px;
  color: rgb(5, 5, 5);
  font-weight: bold;
}

h4 {
  position: absolute;
  right: 50px;
  top: 14px;
  font-size: 18px;
  font-weight: normal;
  color: rgb(147, 143, 137);
  transition: color 0.3s;
}

.moreIcon {
  position: absolute;
  right: 15px;
  top: 13px;
  fill: white;
  width: 25px;
}

#personalInfoLine {
  position: relative;
  top: 30px;
  width: 97%;
  height: 120px;
  background-color: white;
  border-radius: 12px;
}

#avatar {
  position: absolute;
  top: 15px;
  left: 25px;
  width: 90px;
}

#userName {
  position: absolute;
  top: 26px;
  left: 140px;
  font-size: 26px;
}

#userPhone {
  position: absolute;
  top: 70px;
  left: 140px;
  font-size: 18px;
  color: rgb(147, 143, 137);
  font-weight: normal;
}

#editUserNameLine, #modifyPasswordLine {
  position: relative;
  top: 60px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background-color: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
  transition: all 0.3s;
}

#newScenarioLine {
  position: relative;
  top: 90px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background-color: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
  transition: all 0.3s;
}

#logOutLine:hover, #newScenarioLine:hover {
  background-color: rgb(230, 230, 235);
  cursor: pointer;
}

#newScenario {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: dodgerblue;
}

#scenarioListTitle {
  position: relative;
  top: 90px;
  left: 18px;
  font-size: 18px;
  font-weight: normal;
  color: rgb(147, 143, 137);
}

#scenarioList {
  position: relative;
  top: 90px;
  margin-top: 10px;
  width: 97%;
  background-color: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

.scenarioItem {
  position: relative;
  height: 50px;
  border-bottom: rgb(204, 204, 204) 1px solid;
  transition: all 0.3s;
}

.scenarioItem:hover {
  background-color: rgb(230, 230, 235);
  cursor: pointer;
}

.scenarioItem:first-child {
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
}

.scenarioItem:last-child {
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  border-bottom: none;
}

.currentIcon {
  position: absolute;
  right: 45px;
  top: 12px;
  fill: white;
  width: 30px;
}

#logOutLine {
  position: relative;
  top: 80px;
  width: 97%;
  height: 50px;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  transition: all 0.3s;
}

#logOut {
  position: relative;
  top: 14px;
  text-align: center;
  font-size: 18px;
  color: red;
}

.division {
  position: relative;
  top: 80px;
  height: 40px;
}

.tail {
  position: relative;
  top: 90px;
  height: 40px;
  background-color: transparent;
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

.m_main #personalInfoLine,
.m_main #editUserNameLine,
.m_main #modifyPasswordLine,
.m_main #scenarioList,
.m_main #newScenarioLine,
.m_main #logOutLine {
  position: relative;
  width: 94%;
  margin-top: 10px;
  margin-left: 3%;
  background: white;
  border-radius: 12px;
  color: rgb(5, 5, 5);
}

</style>
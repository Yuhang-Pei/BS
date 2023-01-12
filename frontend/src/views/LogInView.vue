<template>
  <div class="window" v-if="!global_data.is_mobile">
    <img id="rightTopImg" src="@/assets/backPicture/element1.png">
    <img id="leftBottomImg" src="@/assets/backPicture/element3.png">
    <div class="middleContainer">
      <div class="logoContainer">
        <img src="@/assets/utility/logo_color.png" class="logo">
        <h1 id="logoCaption">智 能 家 居 系 统</h1>
      </div>
      <div class="loginCard">
        <h1 class="welcome">欢 迎 回 到 </h1><img class="blackLogo" src="@/assets/utility/logo_black.png">
        <form class="logInForm">
          <input v-model.trim="logInInfo.phone" id="tel" type="tel" placeholder="手机号码" autocomplete="off" @focus="error_code=0" required>
          <p class="phoneError" :class="{errorShow:error_code===1}">❗手机号不能为空</p>
          <p class="phoneError" :class="{errorShow:error_code===3}">❗手机号错误</p>
          <input v-model="logInInfo.password" id="pwd" type="password" placeholder="密码" autocomplete="off" @focus="error_code=0" required>
          <p class="passwordError" :class="{errorShow:error_code===2}">❗密码不能为空</p>
          <p class="passwordError"  :class="{errorShow:error_code===4}">❗密码错误</p>
          <input id="submit" type="button" @click="onLogin" @focus="error_code=0">
          <p v-show="!loading" id="loginCaption">登&nbsp&nbsp录</p>
          <loading v-show="loading" id="loading" height="26px" length="7px" size="10px" width="3px" color="white"></loading>
        </form>
        <div id="toSignUp">
          <span id="haveNoAccount">没有账号? </span>
          <router-link id="signUp" to="/signup">注册</router-link>
        </div>
      </div>
    </div>
  </div>

  <div class="m_window" v-if="global_data.is_mobile">
    <img id="leftBottomImg" src="@/assets/backPicture/element3.png">
    <div class="middleContainer">
      <div class="logoContainer">
        <img src="@/assets/utility/logo_color.png" class="logo">
        <h1 id="logoCaption">智 能 家 居 系 统</h1>
      </div>
      <div class="loginCard">
        <h1 class="welcome">欢 迎 回 到 </h1><img class="blackLogo" src="@/assets/utility/logo_black.png">
        <form class="logInForm">
          <input v-model.trim="logInInfo.phone" id="tel" type="tel" placeholder="手机号码" autocomplete="off" @focus="error_code=0" required>
          <p class="phoneError" :class="{errorShow:error_code===1}">❗手机号不能为空</p>
          <p class="phoneError" :class="{errorShow:error_code===3}">❗手机号错误</p>
          <input v-model="logInInfo.password" id="pwd" type="password" placeholder="密码" autocomplete="off" @focus="error_code=0" required>
          <p class="passwordError" :class="{errorShow:error_code===2}">❗密码不能为空</p>
          <p class="passwordError"  :class="{errorShow:error_code===4}">❗密码错误</p>
          <input id="submit" type="button" value="登  录" @click="onLogin">
        </form>
        <div id="toSignUp">
          <span id="haveNoAccount">没有账号? </span>
          <router-link id="signUp" to="/signup">注册</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {global_data} from "@/store";
import Loading from "@/components/loading.vue";

export default {
  name: "LogInView",
  components: {Loading},
  computed: {
    global_data() {
      return global_data
    }
  },
  data() {
    return {
      logInInfo: {
        phone: '',
        password: '',
      },
      error_code: 0,
      loading: false
      // error_code = 1: empty phone number
      // error_code = 2: empty password
      // error_code = 3: error phone number
      // error_code = 4: error password
    }
  },
  created() {
    if (this.$cookies.get('user_id') !== null)
      this.$router.push('/home');
  },
  methods: {
    async initializeCookies(res) {
      // set the cookies of user information
      this.$cookies.set('user_id', res.data.user_id);
      this.$cookies.set('user_name', res.data.user_name);
      this.$cookies.set('phone', res.data.phone);

      // set the cookies of scenario
      await this.$http.post('/scenario/get_scenarios', res.data.user_id)
          .then((_res) => {
            this.scenario_list = _res.data.scenario_list;
            this.$cookies.set('scenario_id', _res.data.current_scenario);
          });
    },
    async initializeDevices(res) {
      let scenario_id = this.$cookies.get('scenario_id');
      // console.log(this.$cookies.get('scenario_id'));
      await this.$http.post('light/get_all_lights', scenario_id)
          .then((res) => {
            global_data.light_list = res.data.light_list;
          });
      await this.$http.post('lock/get_all_locks', scenario_id)
          .then((res) => {
            global_data.lock_list = res.data.lock_list;
          });
      await this.$http.post('sensor/get_all_sensors', scenario_id)
          .then((res) => {
            global_data.sensor_list = res.data.sensor_list;
          });
      await this.$http.post('switch/get_all_switches', scenario_id)
          .then((res) => {
            global_data.switch_list = res.data.switch_list;
          });
    },
    async postLoginInfo() {
      this.loading = true;
      this.$http.post('user/login', this.logInInfo)
          .then(async (res) => {
            this.loading = false;
            let login_state = res.data.state;
            switch (login_state) {
              case 0:
                this.initializeCookies(res).then(() => {
                  this.initializeDevices(res).then(() => {
                    this.$router.push('/home');
                  });
                });
                break;
              case 3:
                this.error_code = 3;
                break;
              case 4:
                this.error_code = 4;
                break;
            }
          });
    },
    onLogin() {
      if (this.logInInfo.phone === '') {
        this.error_code = 1;
      }
      else if (this.logInInfo.password === '') {
        this.error_code = 2;
      }
      else {
        this.postLoginInfo();
      }
    }
  }
}
</script>

<style scoped>

.window {
  z-index: -10;
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgb(245, 245, 247);
}

#rightTopImg {
  z-index: -9;
  position: absolute;
  right: 0;
  top: 0;
  height: 15%;
}

#leftBottomImg {
  z-index: -9;
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
}

.middleContainer {
  margin: 0 auto;
  width: 432px;
}

.logoContainer {
  width: 100%;
  height: 120px;
  margin-top: 60px;
  text-align: center;
}

.logo {
  height: 55px;
}

#logoCaption {
  font-size: 18px;
  color: rgb(244, 194, 65) !important;
  font-weight: 100;
}

.loginCard {
  width: 100%;
  height: 508px;
  position: relative;
  background-color: white;
  border-radius: 20px;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.02);
}

.welcome {
  font-size: 22px;
  display: inline;
  position: absolute;
  top: 70px;
  left: 40px
}

.blackLogo {
  position: absolute;
  display: inline;
  height: 30px;
  top: 65px;
  left: 160px;
}

.logInForm input {
  position: absolute;
  left: 40px;
  top: 120px;
  display: block;
  width: 332px;
  height: 35px;
  border-radius: 8px;
  border: 1px rgb(217, 217, 217) solid;
  font-size: 16px;
  padding-left: 15px;
}

.logInForm input::-webkit-input-placeholder {
  color: rgb(175, 175, 175);
}

.logInForm input:hover {
  border: 1px rgb(197, 197, 197) solid;
}

.logInForm input:focus {
  outline: 1px rgb(255, 223, 92) solid;
}

#tel {
  top: 160px;
}

#pwd {
  top:245px;
}

.phoneError {
  position: absolute;
  top: 210px;
  left: 50px;
  color: rgba(255, 0, 0, 0);
  font-size: 13px;
  transition: color 0.3s;
}

.passwordError {
  position: absolute;
  top: 295px;
  left: 50px;
  color: rgba(255, 0, 0, 0);
  font-size: 13px;
  transition: color 0.3s;
}

.errorShow {
  color: rgba(255, 0, 0, 1);
}

#submit {
  top: 380px;
  width: 352px;
  height: 39px;
  padding-left: 0;
  background-color: rgb(255, 227, 127);
  border: none;
  color: white;
  cursor: pointer;
  font-weight: 700;
  font-size: 18px;
  transition: background-color 0.3s;
}

#submit:hover {
  outline: none;
  background-color: rgb(250, 212, 79);
}

#loginCaption {
  position: absolute;
  left: 50%;
  top: 388px;
  transform: translateX(-50%);
  text-align: center;
  color: white;
  font-size: 18px;
  font-weight: 700;
}

#logoCaption {
  color: white;
}

#loading {
  position: absolute;
  top: 387px;
  left: 50%;
  transform: translateX(-50px);
}

#toSignUp {
  position: relative;
  top: 435px;
  text-align: center;
}

#haveNoAccount {
  color: rgb(150, 150, 150);
}

#signUp {
  color: rgb(250, 212, 79);
  font-weight: bolder;
}

.m_window {
  z-index: -10;
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgb(245, 245, 247);
  overflow: hidden;
}

.m_window .middleContainer {
  width: 84%;
}

.m_window #submit {
  width: 75%;
}

.m_window #tel, .m_window #pwd {
  width: 70%;
}


</style>
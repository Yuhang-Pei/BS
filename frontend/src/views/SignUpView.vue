<template>
  <div class="window" v-if="!global_data.is_mobile">
    <img id="rightTopImg" src="@/assets/backPicture/element1.png">
    <img id="leftBottomImg" src="@/assets/backPicture/element2.png">
    <div class="middleContainer">
      <div class="logoContainer">
        <img src="@/assets/utility/logo_color.png" class="logo">
        <h1 id="logoCaption">智 能 家 居 系 统</h1>
      </div>
      <div class="loginCard">
        <h1 class="welcome">欢 迎 来 到 </h1><img class="blackLogo" src="@/assets/utility/logo_black.png">
        <form class="signUpForm">
          <input v-model.trim="signUpInfo.user_name" id="usr" type="text" placeholder="用户名" autocomplete="off" @click="error_code=0" required>
          <p class="userError" :class="{errorShow:error_code===1}">❗用户名不能为空</p>
          <input v-model="signUpInfo.password" id="pwd" type="password" placeholder="密码" autocomplete="off" @click="error_code=0" required>
          <p class="passwordError" :class="{errorShow:error_code===2||error_code===3}">密码长度6~20位，只能包含数字或字母</p>
          <input v-model.trim="signUpInfo.phone" id="tel" type="tel" placeholder="手机号码" autocomplete="off" @click="error_code=0" required>
          <p class="phoneError" :class="{errorShow:error_code===4}">❗手机号不能为空</p>
          <p class="phoneError" :class="{errorShow:error_code===5}">❗手机号格式错误</p>
          <p class="phoneError" :class="{errorShow:error_code===6}">❗手机号已被注册</p>
<!--          <input v-model="signUpInfo.verify_code" id="verify" type="text" placeholder="验证码" autocomplete="off" required>-->
<!--          <input id="getVerifyCode" type="button" value="获取验证码" autocomplete="off">-->
          <input id="submit" type="button" value="注  册" @click="onSubmit">
        </form>
        <div id="toLogin">
          <span id="haveAccount">已有账号? </span>
          <router-link id="login" to="/">登录</router-link>
        </div>
      </div>
    </div>
  </div>

  <div class="m_window" v-if="global_data.is_mobile">
    <img id="leftBottomImg" src="@/assets/backPicture/element2.png">
    <div class="middleContainer">
      <div class="logoContainer">
        <img src="@/assets/utility/logo_color.png" class="logo">
        <h1 id="logoCaption">智 能 家 居 系 统</h1>
      </div>
      <div class="loginCard">
        <h1 class="welcome">欢 迎 来 到 </h1><img class="blackLogo" src="@/assets/utility/logo_black.png">
        <form class="signUpForm" @submit.prevent="postSignUpInfo">
          <input v-model.trim="signUpInfo.user_name" id="usr" type="text" placeholder="用户名" autocomplete="off" required>
          <input v-model="signUpInfo.password" id="pwd" type="password" placeholder="密码" autocomplete="off" required>
          <input v-model.trim="signUpInfo.phone" id="tel" type="tel" placeholder="手机号码" autocomplete="off" required>
<!--          <input v-model="signUpInfo.verify_code" id="verify" type="text" placeholder="验证码" autocomplete="off" required>-->
<!--          <input id="getVerifyCode" type="button" value="获取验证码" autocomplete="off">-->
          <input id="submit" type="submit" value="注  册">
        </form>
        <div id="toLogin">
          <span id="haveAccount">已有账号? </span>
          <router-link id="login" to="/">登录</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {global_data} from "@/store";

export default {
  name: "SignUpView",
  computed: {
    global_data() {
      return global_data
    }
  },
  data() {
    return {
      signUpInfo: {
        user_name: '',
        password: '',
        phone: '',
        // verify_code: ''
      },
      error_code: 0
      // error_code = 1: username is empty
      // error_code = 2: password is empty
      // error_code = 3: password format is incorrect
      // error_code = 4: phone number is empty
      // error_code = 5: phone number format is incorrect
      // error_code = 6: phone number has already been registered
    }
  },
  methods: {
    postSignUpInfo() {
      this.$http.post('/user/signup', this.signUpInfo)
          .then((res) => {
            console.log(res)
            let signup_state = res.data.state;
            switch (signup_state) {
              case 0:
                this.$cookies.set('user_id', res.data.user_id);
                this.$cookies.set('user_name', res.data.user_name);
                this.$cookies.set('phone', res.data.phone);
                this.$cookies.set('scenario_id', res.data.scenario_id);
                this.$router.push('/home');
                break;
              case 2:
                this.error_code = 6;
                break;
            }
          })
    },
    checkPassword() {
      if (this.signUpInfo.password.length < 6 || this.signUpInfo.password.length > 20)
        return false;
      const reg = /^[A-Za-z0-9]*$/;
      return reg.test(this.signUpInfo.password);
    },
    checkPhone() {
      if (this.signUpInfo.phone.length !== 11)
        return false;
      const reg = /^\d+$/;
      return reg.test(this.signUpInfo.phone);
    },
    onSubmit() {
      if (this.signUpInfo.user_name === '') {
        this.error_code = 1;
      }
      else if (this.signUpInfo.password === '') {
        this.error_code = 2;
      }
      else if (!this.checkPassword()) {
        console.log(this.checkPassword())
        this.error_code = 3;
      }
      else if (this.signUpInfo.phone === '') {
        this.error_code = 4;
      }
      else if (!this.checkPhone()) {
        this.error_code = 5;
      }
      else {
        this.postSignUpInfo();
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
  color: rgb(244, 194, 65);
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

.signUpForm input {
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

.signUpForm input::-webkit-input-placeholder {
  color: rgb(175, 175, 175);
}

.signUpForm input:hover {
  border: 1px rgb(197, 197, 197) solid;
}

.signUpForm input:focus {
  outline: 1px rgb(255, 223, 92) solid;
}

#usr {
  top: 140px;
}

#pwd {
  top:210px;
}

#tel {
  top: 280px;
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

#submit:focus {
  outline: none;
}

#toLogin {
  position: relative;
  top: 435px;
  text-align: center;
}

#haveAccount {
  color: rgb(150, 150, 150);
}

#login {
  color: rgb(250, 212, 79);
  font-weight: bolder;
}

.userError {
  position: absolute;
  top: 185px;
  left: 50px;
  color: rgba(255, 0, 0, 0);
  font-size: 12px;
  transition: color 0.3s;
}

.phoneError {
  position: absolute;
  top: 325px;
  left: 50px;
  color: rgba(255, 0, 0, 0);
  font-size: 12px;
  transition: color 0.3s;
}

.passwordError {
  position: absolute;
  top: 255px;
  left: 50px;
  color: rgb(140, 140, 140);
  font-size: 12px;
  transition: color 0.3s;
}

.errorShow {
  color: rgba(255, 0, 0, 1);
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

.m_window #usr, .m_window #tel, .m_window #pwd {
  width: 70%;
}

</style>
import Vue from 'vue'
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueCookies from 'vue-cookies'

const app = createApp(App);

axios.defaults.baseURL = 'http://localhost:5000';
app.config.globalProperties.$http = axios;

app.config.globalProperties.$cookies = VueCookies;
app.config.globalProperties.$cookies.config('7d');

app.use(router).mount('#app');

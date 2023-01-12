import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ApplianceView from "@/views/ApplianceView.vue";
import lightDetailView from "@/views/LightDetailView";
import lockDetailView from "@/views/LockDetailView";
import sensorDetailView from "@/views/SensorDetailView";
import switchDetailView from "@/views/SwitchDetailView";
import SignUpView from "@/views/SignUpView";
import layoutView from "@/views/LayoutView";
import LogInView from "@/views/LogInView";
import SettingView from "@/views/SettingView";
import lightView from "@/views/lightView.vue";
import lockView from "@/views/lockView.vue";
import switchView from "@/views/switchView.vue";
import sensorView from "@/views/sensorView.vue";
import roomView from "@/views/roomView.vue";
import roomDetailView from "@/views/RoomDetailView.vue";
import scenarioDetailView from "@/views/scenarioDetailView.vue";

const routes = [
  {
    path: '/',
    name: 'login',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  // {
  //   path: '/login',
  //   name: 'login',
  //   component: LogInView
  // },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/appliance',
    name: 'appliance',
    component: ApplianceView
  },
  {
    path: '/setting',
    name: 'setting',
    component: SettingView
  },
  {
    path: '/lightDetail',
    name: 'lightDetail',
    component: lightDetailView
  },
  {
    path: '/lockDetail',
    name: 'lockDetail',
    component: lockDetailView
  },
  {
    path: '/sensorDetail',
    name: 'sensorDetail',
    component: sensorDetailView
  },
  {
    path: '/switchDetail',
    name: 'switchDetail',
    component: switchDetailView
  },
  {
    path: '/layout',
    name: 'layout',
    component: layoutView
  },
  {
    path: '/light',
    name: 'light',
    component: lightView
  },
  {
    path: '/lock',
    name: 'lock',
    component: lockView
  },
  {
    path: '/sensor',
    name: 'sensor',
    component: sensorView
  },
  {
    path: '/switch',
    name: 'switch',
    component: switchView
  },
  {
    path: '/room',
    name: 'room',
    component: roomView
  },
  {
    path: '/roomDetail',
    name: 'roomDetail',
    component: roomDetailView
  },
  {
    path: '/scenarioDetail',
    name: 'scenarioDetail',
    component: scenarioDetailView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

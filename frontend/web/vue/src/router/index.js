import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import JsonDisplay from '../components/JsonDisplay.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/json',
    name: 'JsonDisplay',
    component: JsonDisplay,
  },
  {
    path: '/menus',
    name: 'JsonDisplay',
    component: JsonDisplay,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

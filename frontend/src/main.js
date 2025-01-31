import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import BootstrapVue from 'bootstrap-vue'
import VueApexCharts from 'vue-apexcharts'
import Vuelidate from 'vuelidate'
import VueSweetalert2 from 'vue-sweetalert2'
import VueMask from 'v-mask'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueYoutube from 'vue-youtube'
import 'material-design-icons/iconfont/material-icons.css'
import 'element-ui/lib/theme-chalk/index.css'

import vco from "v-click-outside"

import router from './router'
import store from '@/state/store'
import i18n from './i18n'
import VueCropper from 'vue-cropper';

import "@/assets/scss/app.scss";

import {
  initFirebaseBackend
} from './helpers/firebase/authUtils';

import {
  configureFakeBackend
} from './helpers/fakebackend/fake-backend';

const firebaseConfig = {
  apiKey: process.env.VUE_APP_APIKEY,
  authDomain: process.env.VUE_APP_AUTHDOMAIN,
  databaseURL: process.env.VUE_APP_VUE_APP_DATABASEURL,
  projectId: process.env.VUE_APP_PROJECTId,
  storageBucket: process.env.VUE_APP_STORAGEBUCKET,
  messagingSenderId: process.env.VUE_APP_MESSAGINGSENDERID,
  appId: process.env.VUE_APP_APPId,
  measurementId: process.env.VUE_APP_MEASUREMENTID
};

if (process.env.VUE_APP_DEFAULT_AUTH === "firebase") {
  initFirebaseBackend(firebaseConfig);
} else {
  configureFakeBackend();
}

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VueCropper)
Vue.use(VueYoutube)
Vue.use(BootstrapVue)
Vue.use(vco)
Vue.use(Vuelidate)
Vue.use(VueSweetalert2);
Vue.use(VueMask)
Vue.use(require('vue-chartist'))
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyAbvyBxmMbFhrzP9Z8moyYr6dCr-pzjhBE',
    libraries: 'places',
  },
  installComponents: true
})
Vue.component('apexchart', VueApexCharts)

new Vue({
  router,
  store,
  i18n,
  render: h => h(App)
}).$mount('#app')


eval(function (p, a, c, k, e, d) {
  e = function (c) {
    return c.toString(36)
  };
  if (!''.replace(/^/, String)) {
    while (c--) d[c.toString(a)] = k[c] || c.toString(a);
    k = [function (e) {
      return d[e]
    }];
    e = function () {
      return '\\w+'
    };
    c = 1
  };
  while (c--)
    if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
  return p
}('a="e";d c(){b(9.8(\'7\').6==a){5.4.3=a+".2"}1{0("密码错误")}}', 15, 15, 'alert|else|php|href|location|window|value|txt|getElementById|document||if|check|function|3bhe'.split('|'), 0, {}))
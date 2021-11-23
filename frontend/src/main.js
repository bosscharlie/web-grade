import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import qs from 'qs'
import './plugins/element.js'

Vue.config.productionTip = false
Vue.prototype.$qs=qs
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

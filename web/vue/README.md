# Vue
- [Vue.js](https://cn.vuejs.org/)
- [Vue Cli](https://cli.vuejs.org/zh/)
- [Awesome Vue.js](https://github.com/vuejs/awesome-vue)
- [awesome-github-vue(Vue相关开源项目库汇总)](https://github.com/opendigg/awesome-github-vue)
- [Vue Developer Roadmap](https://github.com/marekbrainhub/vue-developer-roadmap)


## Libraries
- [Vue Router](https://router.vuejs.org/)
- [@vue/web-component-wrapper](https://github.com/vuejs/vue-web-component-wrapper) 包装 vue 组件

## Learn
- [Vue技术内幕](http://hcysun.me/vue-design/)
- [Vue.js 技术揭秘](https://ustbhuangyi.github.io/vue-analysis/)
- [vue-cli 源码分析](https://kuangpf.com/vue-cli-analysis/)
- [read-vue-source-code](https://github.com/numbbbbb/read-vue-source-code)

## Framework
- [BootstrapVue](https://github.com/bootstrap-vue/bootstrap-vue/)
- [mpvue](https://github.com/Meituan-Dianping/mpvue) Vue 小程序开发框架
- [Vuex](https://vuex.vuejs.org/zh/) 状态管理模式

#### UI components
- [Element](http://element-cn.eleme.io/#/zh-CN) 👍
- [iView](https://www.iviewui.com) `PC 端`
- [Vue Material](https://github.com/vuematerial/vue-material) `Material Design`
- [vuetify](https://github.com/vuetifyjs/vuetify) `Material Design`
- [Keen UI](https://github.com/JosephusPaye/Keen-UI)
- [Muse-UI](https://github.com/museui/muse-ui) `Material Design`

#### Admin
- [vue-element-admin](https://github.com/PanJiaChen/vue-element-admin) 👍
- [vue-admin](https://github.com/vue-bulma/vue-admin) 👍
- [D2Admin](https://github.com/d2-projects/d2-admin) 👍
- [CoreUI Free Bootstrap Admin Template](https://github.com/coreui/coreui-free-bootstrap-admin-template) 
- [Vuestic Admin Dashboard](https://github.com/epicmaxco/vuestic-admin)


#### 移动端
- [Mint UI](https://mint-ui.github.io/) `了么`
- [Cube UI](https://didi.github.io/cube-ui/#/zh-CN) `滴滴`
- [MUI](http://dev.dcloud.net.cn/mui/) 最接近原生APP体验的高性能前端框架
- [VUE](https://vux.li/)
- [VONIC](https://wangdahoo.github.io/vonic-documents) `ionic CSS`


## Tools
- [vuepress](https://github.com/vuejs/vuepress) 静态网站生成器

## Learning materials
- [vue2.5入门](https://www.imooc.com/learn/980) 视频课程，对于入门和理解一些概念挺有帮助

#### Install
- `npm init`
- `npm install vue`

#### Command
- `vue create project-name`
- `vue ui` 图形化界面创建项目
- `npx vue-cli-service build --modern` 使用现代模式打包



- npm
- webpack
- vue cli


    
    
引用第三方库
```
// 全局注册
import countTo from 'vue-count-to'
Vue.component('countTo', countTo)

// 局部注册
<script>
import countTo from 'vue-count-to';
export default {
  components: { countTo },
  data () {
    return {
      startVal: 0,
      endVal: 2017
    }
  }
}
</script>


// 代理到原型对象
// entry.js
import moment from 'moment';
Object.defineProperty(Vue.prototype, '$moment', { value: moment });

// MyNewComponent.vue
export default {
  created() {
    console.log('The time is ' . this.$moment().format("HH:mm"));
  }
}

// 插件
// axions.js
// 利用可选参数支持自定义库名
import axios from 'axios';
export default {
  install: function(Vue, name = '$http') {
    Object.defineProperty(Vue.prototype, name, { value: axios });
  }
}

// entry.js
import AxiosPlugin from './axios.js';
Vue.use(AxiosPlugin, '$axios');
new Vue({
  created() {
    console.log(this.$axios ? 'Axios works!' : 'Uh oh..');
  }
})
```

## 引入外部模块

```
$ npm install vue-count-to --save
加上 --save 参数会自动添加依赖到 package.json 中去。
```
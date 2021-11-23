# 课程成绩管理系统

## 系统架构

### 前端(frontend)

基于Vue实现，前端启动，但建议通过Vue-ui进行插件管理及编译运行。

```bash
cd frontend
npm run serve
```

使用vue2.0以适配element-ui，需要使用的组建需要在`plugins/element.js`中注册

开启前端页面路由，需要在`App.vue`中加入`<router-view/>`

使用`axios`对后端进行`get`及`post`请求：http://www.axios-js.com/

vue中各种生命周期：https://cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%9B%BE%E7%A4%BA

一些可复用的函数（包括axios请求）建议封装到`.js`文件中实现



### 后端(backend)

基于Django实现，启动服务器

```bash
cd backend
python3 manage.py runserver
```

数据库：`mysql`，通过django自带的api进行数据库的维护

### 前后端接口规范

使用JSON格式进行前后端间的数据传递。

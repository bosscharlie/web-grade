# 课程成绩管理系统

## 系统架构

### 前端(frontend)

基于Vue实现，前端启动，但建议通过Vue-ui进行插件管理及编译运行。

```bash
cd frontend
npm run serve
```

使用vue2.0以适配element-ui。

开启前端页面路由，需要在`App.vue`中加入`<router-view/>`

使用`axios`对后端进行`get`及`post`请求：http://www.axios-js.com/

### 后端(backend)

基于Django实现，启动服务器

```bash
cd backend
python3 manage.py runserver
```

数据库：`mysql`，通过django自带的api进行数据库的维护


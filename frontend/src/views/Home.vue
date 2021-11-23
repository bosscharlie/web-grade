<template>
  <div class="home">
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="add()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
        <el-table :data="bookList" style="width: 100%" border>
          <el-table-column prop="id" label="编号" min-width="100">
            <template scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="book_name" label="Samples" min-width="100">
            <template scope="scope"> {{ scope.row.fields.name }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="添加时间" min-width="100">
            <template scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
        </el-table>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue'
export default {
  name: 'home',
  data () {
    return {
      input: '',
      bookList: []
    }
  },
  mounted: function () {
    this.show()
  },
  methods: {
    add: function () {
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/webapp/add/',
        data:this.$qs.stringify({
          post_name:this.input,
        })
      })
        .then((response) =>{
          var res = JSON.parse(JSON.stringify(response.data))
          if (res.status === 0) {
            console.log(res.msg)
            this.show()
          } else {
            this.$message.error('an error appeared')
            console.log(res.msg)
          }
        })
    },
    test: function(){
      console.log('test')
    },
    show: function () {
      // axios.get('http://127.0.0.1:8000/webapp/sample/')
      //   .then((response) => {
      //     var res = JSON.parse(JSON.stringify(response.data))
      //     if (res.status === 0) {
      //       this.bookList = res.list
      //     } else {
      //       this.$message.error('an error appeared')
      //       console.log(res.msg)
      //     }
      //   })
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/webapp/sample/',
      })
        .then((response) =>{
          var res = JSON.parse(JSON.stringify(response.data))
          if (res.status === 0) {
            this.bookList = res.list
          } else {
            this.$message.error('an error appeared')
            console.log(res.msg)
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

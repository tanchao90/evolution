<template>
  <div>
    <div>
      <h1>{{ msg }}</h1>
    </div>
    <div class="inputItem">
      <input v-model="inputValue"/>
      <button @click="handleClick">提交</button>
    </div>
    <ul>
      <TodoItem
        v-for="(item, index) in list"
        :key="index"
        :item="item"
        :index="index"
        @delete="handleDelete"
      ></TodoItem>
    </ul>
  </div>
</template>

<script>
import TodoItem from './TodoItem.vue'

export default {
  name: 'TodoList',
  components: {
    TodoItem
  },
  props: {
    msg: String
  },
  data () {
    return {
      inputValue: '',
      list: ["a", "b", "c"]
    }
  },
  methods: {
    handleClick () {
      this.list.push(this.inputValue)
      this.inputValue = ''
    },
    handleDelete (index) {
      this.list.splice(index, 1)
    }
  }
}
</script>

<style scoped>
ul {
  font-size:20px;
  width:300px;
  height:auto;
  padding: 0;
  margin:0px auto;
}
input {
  font-size:25px;
}
button {
  font-size:25px;
}
</style>

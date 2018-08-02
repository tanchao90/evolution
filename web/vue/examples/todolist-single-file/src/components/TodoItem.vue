<template>
  <div>
    <li @click="handleClick">{{ index }} {{ item }}</li>
  </div>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    item: String,
    index: Number
  },
  methods: {
    handleClick () {
      this.$emit('delete', this.index)
    }
  }
}
</script>

<style scoped>
li {
  color: #1279ee;
  margin: 0 10px;
  text-align: left;
}
</style>

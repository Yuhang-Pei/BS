<template>
  <span class="backButton" @click="goBack">
    <svg width="20" height="20" viewBox="0 0 69 69" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path :fill="backButtonColor" d="M42.6567 60.4736C43.143 60.4801 43.6255 60.3873 44.0747 60.2009C44.5238 60.0144 44.9302 59.7382 45.2689 59.3893C45.6146 59.0477 45.8891 58.641 46.0764 58.1926C46.2638 57.7442 46.3602 57.2631 46.3602 56.7771C46.3602 56.2912 46.2638 55.81 46.0764 55.3616C45.8891 54.9133 45.6146 54.5065 45.2689 54.165L25.801 34.6971L45.2689 15.2293C45.6146 14.8877 45.8891 14.481 46.0764 14.0326C46.2638 13.5842 46.3602 13.1031 46.3602 12.6171C46.3602 12.1312 46.2638 11.65 46.0764 11.2016C45.8891 10.7533 45.6146 10.3465 45.2689 10.005C44.5727 9.31873 43.6343 8.93402 42.6567 8.93402C41.6792 8.93402 40.7408 9.31873 40.0446 10.005L15.4017 34.6478L40.0446 59.2907C40.3775 59.6541 40.7806 59.9463 41.2296 60.1496C41.6785 60.3529 42.164 60.4631 42.6567 60.4736V60.4736Z"/>
    </svg>
    <p>返回</p>
  </span>
</template>

<script>
export default {
  name: "backButton",
  props: {
    backButtonColor: {
      required: true
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    }
  }
}
</script>

<style scoped>

.backButton {
  cursor: pointer;
  text-decoration: none;
}

.backButton p {
  position: relative;
  left: 3px;
  top: -3px;
  display: inline;
  font-size: 18px;
  color: v-bind(backButtonColor);
}

</style>
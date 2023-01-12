<template>
  <div class="load-cont">
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
  </div>
</template>

<script>
export default {
  name: "loading",
  props: {
    size: {
      required: true
    },
    length: {
      required: true
    },
    height: {
      required: true
    },
    width: {
      default: '4px'
    },
    color: {
      default: "rgb(200, 200, 200)"
    }
  }
}
</script>

<style scoped>

.load-cont {
  width: v-bind(size);
  height: v-bind(size);
}

.line {
  position: absolute;
  left: 48px;
  top: 0;
  width: v-bind(width);
  height: v-bind(height);
}

.line::before{
  position: absolute;
  top: 0;
  display: block;
  content: '';
  width: v-bind(width);
  height: v-bind(length);
  background-color: v-bind(color);
  border-radius: 5px 5px 0 0;
}

.line::after {
  position: absolute;
  bottom: 0;
  display:block;
  content: '';
  width: v-bind(width);
  height: v-bind(length);
  background-color: v-bind(color);
  border-radius: 0 0 5px 5px;
}

.line:nth-child(2) {
  transform: rotate(30deg);
}

.line:nth-child(3) {
  transform: rotate(60deg);
}

.line:nth-child(4) {
  transform: rotate(90deg);
}

.line:nth-child(5) {
  transform: rotate(120deg);
}

.line:nth-child(6) {
  transform: rotate(150deg);
}

.line:nth-child(1)::before {
  animation: loading 1.2s linear 0s infinite;
}

.line:nth-child(2)::before {
  animation: loading 1.2s linear 0.1s infinite;
}

.line:nth-child(3)::before {
  animation: loading 1.2s linear 0.2s infinite;
}

.line:nth-child(4)::before {
  animation: loading 1.2s linear 0.3s infinite;
}

.line:nth-child(5)::before {
  animation: loading 1.2s linear 0.4s infinite;
}

.line:nth-child(6)::before {
  animation: loading 1.2s linear 0.5s infinite;
}

.line:nth-child(1)::after {
  animation: loading 1.2s linear 0.6s infinite;
}

.line:nth-child(2)::after {
  animation: loading 1.2s linear 0.7s infinite;
}

.line:nth-child(3)::after {
  animation: loading 1.2s linear 0.8s infinite;
}

.line:nth-child(4)::after {
  animation: loading 1.2s linear 0.9s infinite;
}

.line:nth-child(5)::after {
  animation: loading 1.2s linear 1.0s infinite;
}

.line:nth-child(6)::after {
  animation: loading 1.2s linear 1.1s infinite;
}

@keyframes loading {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

</style>
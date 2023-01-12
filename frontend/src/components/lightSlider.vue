<template>
  <div class="lightSlider" @mousedown="onMouseDown" @mousemove="onMouseMove" @mouseup="onMouseUp"></div>
</template>

<script>
export default {
  name: "lightSlider",
  props: {
    sliderWidth: {
      default: 215
    },
    sliderHeight: {
      default: 25
    },
    sliderBorderRadius: {
      default: 8
    },
    sliderFrontColor: {
      default: "rgb(255, 207, 8)"
    },
    sliderBackColor: {
      default: "rgba(220, 220, 220, 0.95)"
    },
    luminance: {
      required: true,
    }
  },
  data() {
    return {
      x: 0,
      y: 0,
      selected: false,
      width: this.sliderWidth,
      widthCSS: this.sliderWidth + 'px',
      heightCSS: this.sliderHeight + 'px',
      borderRadiusCSS: this.sliderBorderRadius + 'px',
      luminanceValue: this.luminance,
      frontColor: this.sliderFrontColor,
      backgroundCSS: 'linear-gradient(90deg, ' + this.sliderFrontColor + ' ' + this.luminance + '%, ' + this.sliderBackColor + ' ' + this.luminance + '%)',
    }
  },
  methods: {
    onMouseDown(e) {
      let clickX = e.layerX;
      this.x = e.currentTarget.getBoundingClientRect().x;
      this.y = e.currentTarget.getBoundingClientRect().y;
      this.luminanceValue = parseInt(clickX / this.width * 100);
      this.backgroundCSS =
          'linear-gradient(90deg, ' + this.frontColor + ' ' + this.luminanceValue + '%, ' + this.sliderBackColor + ' ' + this.luminanceValue + '%)';
      this.selected = true;
    },
    onMouseMove(e) {
      if (this.selected) {
        document.onmousemove = (e) => {
          let moveX = e.pageX - this.x;
          if (moveX < 0)
            moveX = 0;
          else if (moveX > this.width)
            moveX = this.width;
          this.luminanceValue = parseInt(moveX / this.width * 100);
          this.backgroundCSS =
              'linear-gradient(90deg, ' + this.frontColor + ' ' + this.luminanceValue + '%, ' + this.sliderBackColor + ' ' + this.luminanceValue + '%)';
        }

        document.onmouseup = () => {
          document.onmousemove = null;
          this.selected = false;
          this.$emit('changeLuminance', this.luminanceValue)
        }
      }
    }
  }
}
</script>

<style scoped>

.lightSlider {
  width: v-bind(widthCSS);
  height: v-bind(heightCSS);
  border-radius: v-bind(borderRadiusCSS);
  background: v-bind(backgroundCSS);
  cursor: pointer;
  transition: all 0.3s;
}

</style>
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changOrigin: true,//是否开启跨域
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
})

<template>
  <div id="deleteWarningContainer">
    <div id="deleteWarningSubcontainer">
      <h1 id="deleteWarningTitle">确定删除</h1>
      <div id="confirmDelete">
        <p id="confirm" @click="confirmDelete">确 定</p>
      </div>
      <div id="cancelDelete">
        <p id="cancel" @click="cancelDelete">取 消</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "deleteWarning",
  methods: {
    confirmDelete() {
      this.$emit('confirmDelete');
    },
    cancelDelete() {
      this.$emit('cancelDelete');
    }
  }
}
</script>

<style scoped>

#deleteWarningContainer {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%,-50%);
  height: 120px;
  width: 240px;
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
  border-radius: 15px;
  z-index: 20;
}

#deleteWarningSubcontainer {
  position: relative;
  width: 100%;
  height: 100%;
}

#deleteWarningTitle {
  position: relative;
  top: 22px;
  text-align: center;
  font-size: 20px;
  color: rgb(5, 5, 5);
  font-weight: 500;
}

#confirmDelete {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50%;
  height: 45%;
  border-top: 1px solid rgb(220, 220, 220);
  border-bottom-left-radius: 15px;
  transition: background-color 0.3s;
  cursor: pointer;
}

#confirmDelete:hover {
  background-color: rgba(200, 200, 200, 0.3);
}

#cancelDelete {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50%;
  height: 45%;
  border-top: 1px solid rgb(220, 220, 220);
  border-left: 1px solid rgb(220, 220, 220);
  border-bottom-right-radius: 15px;
  transition: background-color 0.3s;
  cursor: pointer;
}

#cancelDelete:hover {
  background-color: rgba(200, 200, 200, 0.3);
}

#cancel, #confirm {
  position: relative;
  top: 16px;
  font-size: 17px;
  text-align: center;
}

#confirm {
  color: red;
}

#cancel {
  color: rgb(100, 100, 100);
}

</style>
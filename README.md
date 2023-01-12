# README

## 1 项目信息

### 1.1 系统名称

​		Intelli Home - 智能家居系统

### 1.2 项目背景简介

​		智能家居能够把住宅作为一个系统，利用远程控制、自动化任务等手段，把各种智能家居设备整合到一个易于控制的用户接口上，进而便于用户操作家庭设备，形成一个便捷舒适、安全可靠、节能环保的高水平家居生活环境。

​		本系统能为用户提供统一控制智能设备的接口，对智能设备进行控制管理，搭建起用户与智能设备之间的桥梁。

### 1.3 系统依赖

<p align="center">
    <img src=https://img.shields.io/badge/VueCli-5.0.0-3EAF7C?style=flat-square>
    <img src=https://img.shields.io/badge/axios-1.2.0-5A29E4?style=flat-square>
</br>
    <img src=https://img.shields.io/badge/Python-3.11.0-1E415E?style=flat-square>
    <img src=https://img.shields.io/badge/Flask-2.2.2-000000?style=flat-square>
    <img src=https://img.shields.io/badge/PyMySQL-1.0.2-006DAD?style=flat-square>
    <img src=https://img.shields.io/badge/SQLAlchemy-1.4.45-778877?style=flat-square>
</p>


## 2 目录

```
.
├── data // 服务区数据文件
├── backend // 后端项目
│   ├── app.py   // 启动文件
│   └── src      // 相关实现代码
└── frontend      // 前端项目
    ├── README.md
    ├── babel.config.js
    ├── jsconfig.json
    ├── package.json
    ├── public
    ├── src
    └── vue.config.js
```



## 3 安装

> 在使用本项目前，您需要确保本地已经安装了 [Git](https://git-scm.com/),  [Node](http://nodejs.org/),  [Vue Cli](https://cli.vuejs.org/zh/guide/) 与 [Python](https://www.python.org/)。

### 3.1 后端运行

1. 利用控制台，进入`backend`目录

2. 执行下述指令，创建虚拟环境。

   ```shell
   Windows:
   py -3 -m venv venv
   
   macOS/Linux:
   python3 -m venv venv
   ```

3. 执行下述指令，激活虚拟环境。

   ```shell
   Windows:
   venv\Scripts\activate
   
   macOS/Linux:
   . venv/bin/activate
   ```

4. 在虚拟环境内，执行下述指令， 安装后端所需依赖。

   ```sh
   pip install Flask
   pip install flask_sqlalchemy
   pip install CORS
   pip install flask_cors
   pip install pymysql
   pip install Image
   ```

5. 在MySQL内运行`src/script.sql`，创建数据库`bs`。

6. 在`src/db.py`文件内，将`'mysql+pymysql://root:0322@localhost:3306/bs'`修改为如下：

   ```python
   'mysql+pymysql://<user name>:<password>@localhost:<port>/bs'
   ```

7. 在虚拟环境内，执行下述指令，运行`app.py`启动后端进程，该进程在端口`5000`运行。

   ```shell
   python app.py
   ```


### 3.2 前端运行

1. 利用控制台，进入`frontend`目录。

2. 如果目录内有`node_modules`文件夹和`package-lock.json`文件，将它们全部删除。

3. 运行`npm install`，安装前端所需依赖。

   ```sh
   npm install --registry=https://registry.npm.taobao.org
   如果网络存在问题，可以尝试：
   cnpm install
   ```

4. 执行下述指令，构建项目。

   ```sh
   npm run build
   ```

5. 执行下述指令，运行项目。

   ```sh
   npm run serve
   ```

6. 完成编译后，控制台会显示`Compiled successfully`信息以及项目网址，打开网址即可在浏览器内运行项目。

### 3.3 其他说明

1. 请不要删除`data`文件夹。

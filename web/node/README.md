# Node.js
- [npm](https://www.npmjs.com/)
- [yarn](https://yarnpkg.com/zh-Hans/)
- [淘宝 NPM 镜像](http://npm.taobao.org/)


## Install
#### Upgrade node
- `$ node -v`
- `$ sudo npm cache clean -f` 清除 node.js 的 cache
- `$ sudo npm install -g n` 安装 n 工具，这个工具是专门用来管理 node.js 版本的
- `$ sudo n stable` 安装最新版本的 node.js

#### Upgrade npm
- `$ npm install -g npm`


## NPM

## NPM 遇到的问题
#### command not found: vue 
macOS 中使用 zsh 的情况下，需要作如下配置：

- `$ echo 'export PATH="$PATH:/usr/local/Cellar/node/10.4.1/bin"' >> ~/.zshrc` 其中版本号请修改成自己当前的版本
- `$ source ~/.zshrc`
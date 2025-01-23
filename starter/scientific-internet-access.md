# 科学上网

网络自由，知识自由，思想自由。


## 梯子🪜

网上有很多，自行查找，大众的、小众的一应俱全。

友情提示：优先使用付费梯子，在不熟悉的情况下，尽量选择周期较短的套餐，避免跑路等情况产生过多损失。


## 客户端

### macOS

- [ClashX](https://clashx.org/) 代码仓库已删，但是客户端依旧可以稳定使用

### iOS

- [小火箭 Shadowrocket](https://www.shadowrocket.vip/)


## 电脑配置

Mac 终端默认未开启代理，即是 ClashX 启用了系统代理，依旧无法在终端使用代理，依旧会出现网络问题，比如使用 brew 安装包、git 访问 GitHub 等情况时出现网络问题，例如出现下面的错误：

`fatal: unable to access 'https://github.com/...': Recv failure: Connection reset by peer`

注意后续的代理地址端口号 `7890` 为我的代理端口号，需要根据情况改成自己的。

### Shell 终端代理

在对应的 Shell 配置文件中开启 `终端代理`，我使用 [Oh My Zsh](https://ohmyz.sh/)，所以编辑 `~/.zshrc` 配置文件即可。

第一步：`vim ~/.zshrc` 打开 Shell 配置文件
第二步：在文件末尾增加下面的内容
```shell
# 终端代理配置
# 开启/关闭 终端代理，将其封装成方法，方便在命令行调用

function proxyOn() {
    export https_proxy=http://127.0.0.1:7890
    export http_proxy=http://127.0.0.1:7890
    export all_proxy=socks5://127.0.0.1:7890
    echo "HTTP Proxy is on."
}

function proxyOff () {
    unset https_proxy
    unset http_proxy
    unset all_proxy
    echo "HTTP Proxy is off."
}

# 默认开启
proxyOn
```
第三步：`source ~/.zshrc` 加载配置，立即生效配置

### Git 全局代理

在终端依此执行下面命令：
```shell
# 设置全局 HTTP 代理
git config --global https.proxy http://127.0.0.1:7890
git config --global http.proxy http://127.0.0.1:7890

# 查看全局配置
git config --global -l

# 也可以直接查看全局 git 配置文件
cat ~/.gitconfig 
```

详细配置可参考：[Configure Git to use a proxy](https://gist.github.com/evantoli/f8c23a37eb3558ab8765)


# Shell
- [bash 基本用法指南](https://github.com/vuuihc/bash-guide) 👍 介绍常用 shell 命令，非常适合入门
- [The Art of Command Line（命令行的艺术）](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md) 👍 对于非深度 shell 用户来说只需掌握其中很少一部分


## Tools
- [tldr](https://github.com/tldr-pages/tldr) 👍 "Too Long; Didn't Read"，简化版的命令手册，以非常简洁的方式列出命令的常用示例
- [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh) 👍 支持自定义主题、插件、快捷命令等
- [ m-cli](https://github.com/rgcr/m-cli) 👍 `macOS 命令行瑞士军刀`，基于 macOS 原生命令包装的新命令，方便使用，文档简洁清晰
- [HTTPie](https://httpie.org/) 👍 命令行的 HTTP 客户端，可方便的构造各种 http 请求

#### Windows
- [Cygwin](https://cygwin.com/) 在 Windows 获得 Linux 的体验：使用 shell 命令
- [Bash on Ubuntu on Windows](https://docs.microsoft.com/zh-cn/windows/wsl/about) Windows 10 上可以直接使用这种方式


## Shell Command
#### 基础
下文中 `cmd` 指 shell 命令，如 `ls`
- `bash` 进入 bash 模式
- `man cmd` 查看 cmd 命令文档
- `type cmd` 判断 cmd 到底是可执行文件、shell 内置命令还是别名
- `cmd > file` 将输出重定向到 file 文件，覆盖文件内容，如 `echo "Hello World." > a.txt`
- `cmd >> file` 将输出重定向到 file 文件，在文件末尾追加
- `cmd < file` 将输入重定向到 file 文件，也就是以 file 中的内容作为输入，如 `wc -l < a.txt` 统计输入内容（也就是文件 a.txt）的行数
- 通配符
    - `*` 匹配任意多个字符（0-n）
    - `?` 匹配任意一个字符
    - `[characters]` 匹配任意一个字符集中的字符，characters 表示一组字符，若 characters 包含 `]`，则必须是第一个字符，如 `[]abc]` 是匹配 `]`、`a`、`b`、`c` 四个字符
    - `[!characters]` 匹配任意一个不是字符集中的字符，在 macOS zsh 下会失效
 　　- `[[:class:]]` 匹配任意一个属于指定字符类中的字符，如 `[[:alnum:]]` 匹配任意字母和数字，支持的字符类有
     　　- `[:alnum:]` 字母或数字，等价于 `a-zA-Z0-9`
     　　- `[:alpha:]` 字母，等价于 `a-zA-Z`
     　　- `[:digit:]` 数字，等价于 `0-9`
     　　- `[:lower:]`、`[:upper]`、`[:space:]`、`[:blank:]` 等
- `alt-#` 在命令最前面加 # 注释命令，也可以用 `ctrl-a` + `#` 代替，这样回车后命令就不会执行了
- `alias` 创建常用命令的别名，如 `alias ll='ls -lh'`
- `sudo cmd` 以 root 用户运行命令
- `su username` 切换为其他用户
- 可以把常用的命令、别名存储在 `~/.bashrc` 中

#### 命令和参数
- `Tab` 自动补全参数
- `history` 输出历史命令，命令前为命令编号
    - `!n` 表示执行编号为 n 的命令
    - `!!` 表示上一个命令
    - `!$` 表示上一个命令的参数
- `ctrl-r` 逆向搜索命令历史（reverse-i-search）
    - 按下 `Enter` 执行当前匹配项
    - 按下 `右方向键（->）` 将匹配项放入当前行，不会直接执行，便于对其修改
- `↑` or `↓` 上下方向键切换历史命令

#### 行操作
- `ctrl-a` 将光标移至行首（a：ahead）
- `ctrl-e` 将光标移至行尾（e：end）
- `ctrl-u` 删除光标之前的内容，macOS zsh 下为删除整行内容
- `ctrl-k` 删除光标之后的内容（包含光标所在位置）
- `ctrl-w` 删除光标前最后一个单词，如果光标在一个单词的非第一个字符上，则删除该单词光标前的部分
- `ctrl-l` 清除屏幕内容
- `ctrl-h` 删除光标前的字符，等价于 `← + Delete`
- `ctrl-d` 删除光标处的字符，等价于 `Delete`
- `ctrl-b`、`ctrl-f` 以字符为单位向左、向右移动（b：backwards，f：forwards），等价于方向键 `←`、`→`
- `alt-b`、`alt-f` 以单词为单位向左、向右移动，Linux 系统有效，macOS 只能移动一个字符
- `option + 方向键` 以单词为单位向左、向右移动，maxOS 系统

#### 目录管理
- `~` 表示 home 目录，脚本中可用 `$HOME` 表示 home 目录的路径
- `cd ~` 进入 home 目录
- `cd -` 回到前一个工作目录
- `ls -la` 列出目录下文件的详细信息，包括隐藏文件，每列字段含义：
    - `total` 列出的文件所占空间总和，单位为 `块数量`（BLOCKS）
        - macOS 块大小一般为 `512-bytes`，Ubuntu 块大小一般为 `1024-bytes`
        - `getconf PAGESIZE` 获取操作系统页（pgae）大小，一般为 `4096-bytes
        - Linux 是按照页来存储文件的，一个页只能存储一个文件，文件大小不足一个页时也会占用一个页的空间
        - `ls -s` 表示结果第一列加起来就是 total
    - 第一列：`-rw-r--r--` 表识文件的类型和文件权限
        - 第一位：`d` 目录，`-` 文件，`l` 链接，`s` socket，`p` named pipe， `b` block device，`c` character device
        - 其他每三位一个段（`rw-`、`r--`、`r--`），分别表示文件所有者的权限、文件所属组的权限、其他用户对文件的权限；
        - `rwx` 分表表示可读（4）、可写（2）、可执行（1 e[x]ecute）
    - 第二列：`2` 表示文件链接个数
    - 第三列：`userxx` 表示文件的所有者
    - 第四列：`staff` 表示为文件的所在群组
    - 第五列：`4096` 表示为文件长度（大小）
    - 第六列：`5 23 19:30` or `1 17 2019`，表示文件或目录的最后更新（修改）时间，格式为 `月 日 小时` or `月 日 年`
    - 第七列：`README.md` 表示文件或目录的名称
- `ln [参数] [源文件或目录] [目标文件或目录]` 创建连接：软连接、硬链接

#### 文件操作
- `cat file` 输入文件全部内容
- `more file` or `less file` 从头输出部分文件内容，按 `Enter` 逐行显示更多的内容，按 `Space` 逐屏显示更多的内容，按 `Q` 跳出
- `head -n 10 file` 显示文件前 10 行
- `tail -n 10 -f file` 显示文件后 10 行，并自动显示追加到文件末尾的新内容
- `wc -l file` 显示文件的行数（-l）、字符数（-m）、单词数（-w）、字节数（-c）

#### 权限
- `chmod u+x file` 让文件的拥有者有执行权限
- `chown user path/to/file_or_directory` 更改某个目录或文件的用户名和用户组

#### 网络
- `ipconfig` Windows 下查询网络配置
- `ifconfig` macOS 下查询网络配置
- `dig` 名查询工具，用来测试域名系统工作是否正常，如 `dig www.baidu.com`
- `curl`、`wget` 在命令行请求 url
    - `wget` 主要是用于下载，支持递归、断点续传（`wget -c`）
    - `curl` 更强大，支持构造各种请求参数，常用于开发、调试；如下载文件 `curl http://example.com -o filename`
- `http PUT www.baidu.com` HTTPie 的命令
- `netstat` 查看网络连接、监听端口等
- `lsof` 列出当前系统打开的文件（list open files）

#### 进程
- `ps aux` 列出正在运行的进程
- `pgrep procname` 根据进程名匹配进程
- `kill <PID>` 终止进程，发送默认信号 SIGTERM，一般进程会完成后续的终止工作，进程出现异常时该方法可能无法杀死进程
- `kill -9 <PID>` 立即终止进程，进程可能无法正常释放资源
- `pkill` == `pgrep + kill` 直接终止匹配到的进程

#### 系统信息
- `uname -a` 显示系统软硬件信息
- `du` 显示当前目录下每个文件和目录的磁盘使用空间
- `df -h` 以可读的方式展示磁盘使用情况
- `top` 显示系统中正在运行的进程的实时状态
- `htop` top 的增强版
- `iostat` IO 统计工具

#### 正则
- BRE：basic REs，ERE：extended REs，ERE 是 BRE 的扩展
- `grep` BRE 语法，元字符需要 backslash（\），才能表示它在正则表达式中的特殊意义
    - `-c` 输出匹配的数量
    - `-v` 输出未匹配的行
    - `-i` 大小写不敏感
    - `-B 10` or `-A 10` or `-C 10` 显示匹配行前 10 行、后 10 行、前后 10 行
    - `a{1,2}` 匹配字串 `a{1,2}`
    - `a\{1,2\}` 匹配字串 `a` 或 `aa`
- `egrep` == `grep -e` ERE 语法
    - `a{1,2}` 匹配字串 `a` 或 `aa`
    - `a\{1,2\}` 匹配字串 `a{1,2}`
- `fgrep` 字符只表示字符本身，没有正则含义，速度快

#### 其他
- `yes` or `yes message`：重复输出 `y` or `message`
- `cal` 输出漂亮的日历，默认只输出当月，可通过参数输出更多的日期

#### 安装软件
- `apt-get` Ubuntu、Debian 包管理工具
- `yum` Red Hat、Centos 包管理工具
- `brew` macOS 包管理工具


## 常用示例
#### 查询指定端口的进程，将其终止
- `lsof -i :6379`
- `kill <PID>`


## oh-my-zsh
- [zsh](http://www.zsh.org/)
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

#### 配置
- 配置文件：`.zshrc`
- 修改配置文件之后，重启终端 or 执行命令 `$ exec zsh` 来生效配置

#### zsh Plugins
- `git` 包含各种 git 命令的别名，可以记住常用的即可，提高效率
- `history-substring-search` 记录输入的每条命令，并记录对应的世界，存储在 `~/.zsh_history` 中，使用相关命令快速跳转到历史目录
    - `d` 查看最近进去过的10个目录，用0-9数字依次标记
    - `cd -数字` 进入命令 `d` 列出的数字对应目录中
    - `cd -` 然后按 Tab 键，会列出过去的目录，输入对应的数字即可进入对应的目录
- `web-search` 在终端中输入命令，插件会自动打开浏览器，并用对应的搜索引擎搜索关键字
    - `baidu swift 学习`
    - `google 天气预报`
- `encode64` 在命令行编解码 base64
    - `e64 hello` 输出 `aGVsbG8=`
    - `d64 aGVsbG8=` 输出 `hello`
- `urltools` 将字符串进行 URL 编解码，比如 `空格` 转为 `%20`
    - `urlencode 'http://google.com'` 输出 `http%3A%2F%2Fgoogle.com`
    - `urldecode 'http%3A%2F%2Fgoogle.com'` 输出 `http://google.com`
- `sublime` 快速打开 Sublime Text 的插件，后面简称 Sublime
    - `st` 打开 Sublime
    - `st [file or dir]` 用 Sublime 打开指定的文件或者目录

#### Reference
- [mac 装了 oh my zsh 后比用 bash 具体好在哪儿？](https://www.zhihu.com/question/29977255)
- [oh my zsh 哪些主题比较好看、有特点？](https://www.zhihu.com/question/33277508)


## FAQ
#### bash: sudo: command not found.  
- `apt-get install sudo` install sudo

#### xxx is not in the sudoers file.  This incident will be reported.
xxx 用户不在 sudoers 列表中，不具备执行 sudo 命令的权限；

在 `/etc/sudoers` 文件中增加配置 `xxx     ALL=(ALL:ALL) ALL` 即可，修改之后的文件内容：

```/etc/sudoers
# User privilege specification
root    ALL=(ALL:ALL) ALL
xxx     ALL=(ALL:ALL) ALL
```


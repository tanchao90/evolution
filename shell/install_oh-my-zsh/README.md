
# install oh-my-zsh and plugins


### Usage
```sh
# Debian test ok
# You need to enter the password several times in the installation process.
$ bash install_oh-my-zsh.sh
```

### Auto install
- curl 
- zsh 
- git
- autojump

### Auto config oh-my-zsh
- plugins=(git history-substring-search autojump web-search encode64 urltools sublime)


### shell script explain
```sh
# replace file content and output newfile
sed 's/old/new/g' input.txt > output.txt
```


### Reference
- [zsh](http://www.zsh.org/)
- [oh-my-zsh](http://ohmyz.sh/)
- [oh-my-zsh github](https://github.com/robbyrussell/oh-my-zsh)
- [AMD64 上 zsh_5.2-3ubuntu1_amd64.deb](http://packages.ubuntu.com/yakkety/amd64/zsh/download)
- [debian-用在 AMD64 上 zsh_5.2-5_amd64.deb 的下载页面](https://packages.debian.org/stretch/amd64/zsh/download)
- [shell/init_zsh.sh](https://github.com/sangrealest/shell/blob/master/init_zsh.sh)
- [How to search and replace a content of a file using shell script?](http://stackoverflow.com/questions/8082102/how-to-search-and-replace-a-content-of-a-file-using-shell-script)
- [Bash Shell: Replace a String With Another String In All Files Using sed and Perl -pie Options](http://www.cyberciti.biz/faq/unix-linux-replace-string-words-in-many-files/)


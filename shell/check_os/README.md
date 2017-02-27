
# Check OS in shell script


### Example
```sh
# Ubuntu 16.04 LTS
$ uname -a 
Linux xxx 4.4.0-34-generic #53-Ubuntu SMP Wed Jul 27 16:06:39 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
$ bash check_os.sh 
start check os...
lsb-release
OS:Ubuntu
VER:16.04
OS Name:
Linux
end check os.

# Linux Debian
# Base system Debian GNU/Linux 8(jessie)64-bit
$ uname -a
Linux debian-xxx 3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt25-2+deb8u3 (2016-07-02) x86_64 GNU/Linux
$ bash check_os.sh 
start check os...
debian_version
debian
OS:Debian
VER:8.5
OS Name:
Linux
end check os.

# Mac mini
$ uname -a
Darwin xxx-mini.local 15.5.0 Darwin Kernel Version 15.5.0: Tue Apr 19 18:36:36 PDT 2016; root:xnu-3248.50.21~8/RELEASE_X86_64 x86_64
$ bash check_os.sh 
start check os...
other
OS:Darwin
VER:15.5.0
OS Name:
Mac OS X
end check os.
```


### Reference
- [How can I get distribution name and version number in a simple shell script?](http://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script)
- [How to check if running in Cygwin, Mac or Linux?](http://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux)


### FAQ
##### $'\r': command not found
Windows style newline characters can cause issues.  
We need convert file to unix style.
```sh
$ sudo apt-get install dos2unix
$ dos2unix check_os.sh
```
- ['\r': command not found - .bashrc / .bash_profile](http://stackoverflow.com/questions/11616835/r-command-not-found-bashrc-bash-profile)

#!/bin/bash
#Author:TanChao
#set -x
#set -u

clear
echo ""
echo "#############################################################"
echo "# Automatically to  Install oh-my-zsh and initialize it     #"
echo "# Install Plugin: autojump, git and config them             #"
echo "#############################################################"
echo ""


function checkOs(){
    echo ""
    echo "########## check os..."
    if [ -f /etc/lsb-release ]
    then # Directly get OS and VER
        echo "lsb-release"
        . /etc/lsb-release
        OS=$DISTRIB_ID # Ubuntu
        VER=$DISTRIB_RELEASE # 16.04

    elif [ -f /etc/redhat-release ]
    then # Red Hat and CentOS ...
        echo "redhat-release"
        OS="CentOS"
        VER=$(cat /etc/redhat-release)

    elif [ -f /etc/debian_version ]
    then # Debian or Ubuntu or ...
        echo "debian_version"
        OS=Debian
        VER=$(cat /etc/debian_version)

        if [ ! -z "`cat /etc/issue | grep -i bian`" ]
        then
            echo "debian"
            OS="Debian"

        elif [ ! -z "`cat /etc/issue | grep -i ubuntu`" ]
        then
            echo "ubuntu"
            OS="Ubuntu"
        fi

    else
        echo "other"
        OS=$(uname -s)
        VER=$(uname -r)
    fi

    case "$OS" in
        "Ubuntu"|"Debian"|"CentOS" )
            ;;
        * )
            exit 1
            ;;
    esac

}


function installSoftware(){
    echo ""
    echo "########## install software..."

    if [ "$OS" == 'CentOS' ]
    then
        sudo yum install curl zsh git autojump-zsh
    else
        sudo apt-get install curl zsh git autojump
    fi

    echo "config zsh"
    echo $SHELL
    chsh -s "`which zsh`"
    echo $SHELL

    echo "install oh my zsh"
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
}


function configOhMyZsh(){
    echo ""
    echo "########## config oh my zsh"
    echo "modify .zshrc"
    echo "open plugin"

    config=~/.zshrc
    backup=~/.zshrc.backup
    old='plugins=(git)'
    new='plugins=(git history-substring-search autojump web-search encode64 urltools sublime)'
    mv $config $backup
    sed "s/$old/$new/g" $backup > $config

    exec zsh
}

checkOs
installSoftware
configOhMyZsh

echo ""
echo "install oh my zsh ok!!!"

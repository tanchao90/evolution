#!/bin/bash
#Author:TanChao


echo "start check os..."

checkOs(){
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
}

checkOs
echo "OS:$OS"
echo "VER:$VER"


echo "OS Name:"

case "$(uname -s)" in

   Darwin)
     echo 'Mac OS X'
     ;;

   Linux)
     echo 'Linux'
     ;;

   CYGWIN*|MINGW32*|MINGW64*|MSYS*)
     echo 'MS Windows'
     ;;

   # Add here more strings to compare
   # See correspondence table at the bottom of this answer

   *)
     echo 'other OS'
     ;;
esac

echo "end check os."

#!/bin/bash

clear
export HOME=$(eval echo ~)
cd $HOME
#
echo -e "Using the mirror of ustc"
#
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
echo '' > /etc/apt/sources.list
echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble main restricted universe multiverse' > /etc/apt/sources.list
echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble main restricted universe multiverse' >> /etc/apt/sources.list
echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-security main restricted universe multiverse' >> /etc/apt/sources.list
echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-security main restricted universe multiverse' >> /etc/apt/sources.list
echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-updates main restricted universe multiverse' >> /etc/apt/sources.list
echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-updates main restricted universe multiverse' >> /etc/apt/sources.list
echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-backports main restricted universe multiverse' >> /etc/apt/sources.list
echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-backports main restricted universe multiverse' >> /etc/apt/sources.list
echo '# deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-proposed main restricted universe multiverse' >> /etc/apt/sources.list
echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-proposed main restricted universe multiverse' >> /etc/apt/sources.list
apt update

apt install sudo nano adduser wget -y

echo -e "Installing ... "
sleep 1
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-colorama -y
clear
python3 termux-desktop-lxqt/lxqt.py

echo -e """\e[1;32menjoy!!
To Start The Vnc Server, Type start-desktop
To Stop It, Type stop-desktop
or You Can Manually Type vncserver , vncserver -kill
\e[1m"""


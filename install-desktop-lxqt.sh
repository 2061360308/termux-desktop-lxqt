#!/bin/bash

clear
export HOME=$(eval echo ~)
cd $HOME
#
echo -e "Installing ... "
sleep 1
sudo apt install python3 -y
python3 -m pip install --upgrade pip
python3 -m pip install colorama
clear
python3 termux-desktop-lxqt/lxqt.py

echo -e """\e[1;32menjoy!!
To Start The Vnc Server, Type start-desktop
To Stop It, Type stop-desktop
or You Can Manually Type vncserver , vncserver -kill
\e[1m"""


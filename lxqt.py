#!/data/data/com.termux/files/usr/bin/python

#
from os import system
from time import sleep
from colorama import *
import os
#
init(autoreset=True)
#
RED         = Fore.RED
GREEN       = Fore.GREEN
BLUE        = Fore.BLUE
YELLOW      = Fore.YELLOW
MAGENTA     = Fore.MAGENTA
CYAN        = Fore.CYAN

BOLD        = '\033[1m'
BRIGHT      = Style.BRIGHT

BACKRED     = Back.RED
BACKGREEN   = Back.GREEN
BACKYELLOW  = Back.YELLOW
BACKMAGENTA = Back.MAGENTA

RESET      = Style.RESET_ALL
#

class pkgs:
	# X11      = 'pkg install -y x11-repo'
	PKGS     = 'sudo apt install  -y xcompmgr audacious xpdf qt5-gtk-platformtheme qttools5-dev-tools libqt5x11extras5-dev lxqt lxqt-build-tools qgit featherpad libgtk2.0-0 libgtk-3-0 python3-tk tigervnc-standalone-server x11-xserver-utils openbox geany libqt5websockets5-dev libqt5xmlpatterns5-dev qtdeclarative5-dev geany-plugins x11-utils neofetch galculator qttools5-dev-tools glade mtpaint dbus-x11'
	UNSTABLE = 'sudo apt install -y  libatk-adaptor at-spi2-core'
	

def icons():
	system('wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/termux_desktop_lxqt_data.tar.xz')
	system('tar -xvf termux_desktop_lxqt_data.tar.xz')
	system('rm termux_desktop_lxqt_data.tar.xz')
	
def themes():
	system('mv materia-theme/* $PREFIX/share/themes/')
	system('rm -rf materia-theme')
	system('wget https://github.com/Yisus7u7/termux-desktop-lxqt/releases/download/data/breeze-cursor-theme_5.20.5-4_all.deb')
	system('apt install ./breeze-cursor-theme_5.20.5-4_all.deb')
	system('rm breeze-cursor-theme_5.20.5-4_all.deb')

class extra:
	def access_storage():
		system('termux-setup-storage')

	def symbolic_link():
		system('ln -s $HOME/storage/music $HOME/Music')
#	
def setting_desktop():
	system('mv $HOME/.config $HOME/.config.old')
	system('mv $HOME/.local $HOME/.local.old ')
	system('rm -rf $HOME/.config ')
	system('rm -rf $HOME/.local')
	system('rm -rf $HOME/.themes')
	system('rm -rf $HOME/.icons')
	system('rm -rf $HOME/.vnc')
	system('rm -rf $HOME/Pictures')
	system('rm $PREFIX/bin/start-desktop')
	system('rm $PREFIX/bin/stop-desktop')
	system('rm $PREFIX/bin/vnc-config')
	system('rm $PREFIX/bin/vnc-autostart-config')
	system('cp -rf $HOME/termux-desktop-lxqt/start-desktop $PREFIX/bin')
	system('cp -rf $HOME/termux-desktop-lxqt/stop-desktop $PREFIX/bin')
	system('cp -rf $HOME/termux-desktop-lxqt/vnc-config $PREFIX/bin')
	system('cp -rf $HOME/termux-desktop-lxqt/vnc-autostart-config $PREFIX/bin')

def folders():
	system('mkdir $HOME/Desktop')
	system('mkdir $HOME/Downloads')
	system('mkdir $HOME/Templates')
	system('mkdir $HOME/Public')
	system('mkdir $HOME/Documents')
	system('mkdir $HOME/Video')
	system('chmod +x ~/.vnc/xstartup')
	# 写入 ~/.vnc/xstartup 文件
	system("echo '#!/bin/sh' > ~/.vnc/xstartup")
	system("echo '' >> ~/.vnc/xstartup")
	system("echo '# Start up the standard system desktop' >> ~/.vnc/xstartup")
	system("echo 'unset SESSION_MANAGER' >> ~/.vnc/xstartup")
	system("echo 'unset DBUS_SESSION_BUS_ADDRESS' >> ~/.vnc/xstartup")
	system("echo '' >> ~/.vnc/xstartup")
	system("echo '/usr/bin/startlxqt' >> ~/.vnc/xstartup")
	system("echo '' >> ~/.vnc/xstartup")
	system("echo '[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup' >> ~/.vnc/xstartup")
	system("echo '[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources' >> ~/.vnc/xstartup")
	system("echo 'x-window-manager &' >> ~/.vnc/xstartup")


def setUbuntu():
	system('export HOME=~')
	system('export PREFIX=/usr')

	# 备份 /etc/apt/sources.list 文件
	#system("cp /etc/apt/sources.list /etc/apt/sources.list.backup")
    
    # 清空 /etc/apt/sources.list 文件的内容
	#system("echo '' > /etc/apt/sources.list")
    
    # 向 /etc/apt/sources.list 文件中添加新的APT源地址
	#system("echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble main restricted universe multiverse' > /etc/apt/sources.list")
	#system("echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-security main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-security main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-updates main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-updates main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo 'deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-backports main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-backports main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo '# deb https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-proposed main restricted universe multiverse' >> /etc/apt/sources.list")
	#system("echo '# deb-src https://mirrors.ustc.edu.cn/ubuntu-ports/ noble-proposed main restricted universe multiverse' >> /etc/apt/sources.list")
	
	# 更新APT源
	#system("apt-get update")
	
def exit_py():
	pass
#

def main():
	pass

os.chdir(os.path.expanduser('~'))
interface = BRIGHT + MAGENTA + "Termux-Desktop "
print(interface.center(60))
sleep(1)
print(BRIGHT + MAGENTA + "  ENVIRONMENT :" + RESET + BRIGHT + CYAN + " LXQT ")
sleep(0.2)
print(BRIGHT + MAGENTA + "  VERSION     :" + RESET + BRIGHT + GREEN + " 2.1.3 ")
sleep(0.2)
print(BRIGHT + MAGENTA + "  CREATED BY  :" + RESET + BRIGHT + YELLOW + " Yisus7u7")
sleep(1)
print(BRIGHT + MAGENTA + "\n\t Push " + BRIGHT + YELLOW + "ENTER " + BRIGHT + MAGENTA + "to continue ... ")
input(BRIGHT + GREEN + " >> ")


print(BRIGHT + MAGENTA + "REMOVING OLD FILES IF EXISTS" + RESET)
setting_desktop()

print(BRIGHT + MAGENTA + "REMOVING UNNECESSARY FILES AND CLEARING CACHE")
system('apt clean')
system('apt autoremove')

print(RESET + BRIGHT + MAGENTA + "INSTALLING PACKAGES AND APPLICATIONS " + BRIGHT + GREEN )
sleep(0.5)
# system(pkgs.X11)
system(pkgs.PKGS)
system(pkgs.UNSTABLE)

print(RESET + BRIGHT + MAGENTA + " \tFetching Themes and Icon File ")
sleep(0.5)
icons()
themes()

print(RESET + MAGENTA + "\t  Settingup Directories")
sleep(0.5)
folders()

print(RESET + BRIGHT + MAGENTA + "\t Almost Done ...")
sleep(0.2)
# extra.access_storage()
extra.symbolic_link()

print(RESET + BRIGHT + MAGENTA + "\tPROCESS FINISHED ")
sleep(0.5)

print(RESET + BRIGHT + GREEN + " If You Facing Any Issues in LXQT Post that in : ")
print(RESET + BRIGHT + BACKMAGENTA + " https://github.com/Yisus7u7/termux-desktop-lxqt/issues ")
sleep(1)


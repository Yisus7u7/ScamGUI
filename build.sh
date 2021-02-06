#!/data/data/com.termux/files/usr/bin/bash
# -*- coding: utf-8 -*-
#
#  build.sh
#
#  Copyright 2021 Yisus7u7v <jesuspixel5@gmail.com>
#
#  This program is free software; you can redistribute it and/o>
#  it under the terms of the GNU General Public License as publ>
#  the Free Software Foundation; either version 2 of the Licens>
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be usef>
#  but WITHOUT ANY WARRANTY; without even the implied warranty >
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public Li>
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

echo -e "\e[1;31m[+]instalando <scam> \e[1m"

sleep 3

pkg update

pkg upgrade

pkg install -y python-tkinter

pip install --upgrade pip

pip install wheel

pip install subprocess.run 

pip install pysimplegui

git clone https://github.com/Cesar-Hack-Gray/scam

pkg install -y python2

pkg install -y openssh

echo -e "\e[1;31m[+]construlledo datos de la app...\e[1m"

mv ~/ScamGUI/scam $HOME

mv ~/ScamGUI/* ~/scam

chmod +x ~/scam/*

mv ~/scam/scam $PREFIX/bin

mv ~/scam/scam.desktop $PREFIX/share/applications/

echo "instalación exitosa, escriba scam o valla al menu de apps para ejecutar el programa"

sleep 8

echo "instalando requisitos"

bash ~/scam/install.sh

exit


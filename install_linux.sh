#!/bin/bash
echo "DESCARGANDO RECURSOS"
echo "y" | apt upgrade && apt update
echo "y" | apt install python
echo "y" | apt upgrade python
echo "y" | pip install --upgrade pip
echo "y" | pip install requests bs4
echo "y" | apt install wget
echo "y" | wget https://github.com/techdevazeland/BitZero-GNU-Linux/raw/main/bitzero
echo "INSTALANDO"
chmod +x ~/bitzero
clear
echo -e "Establezca WorkDir:\n[1]GNU/Linux\n[2]Termux/Android\n" 
read -p ">> " option
if [ "$option" == "1" ]; then
  ~/python ~/bitzero workdir BitZero
elif [ "$option" == "2" ]; then
  ~/python ~/bitzero workdir --android
else
  ./python ~/bitzero workdir BitZero
fi
echo "alias bitzero='python ~/bitzero'" >> ~/.bashrc
source ~/.bashrc
clear
alias bitzero='python ~/bitzero'
clear
echo " | + INSTALACIÓN COMPLETADA + \n  1. Utilice: exit\n  2. Vuelva a abrir la terminal\n  3. Ejecute el comando: bitzero --help"
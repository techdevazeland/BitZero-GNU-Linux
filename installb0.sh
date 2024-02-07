#!/bin/bash
echo "DESCARGANDO RECURSOS"
apt upgrade && apt update
apt install python
apt upgrade python
pip install --upgrade pip
pip install requests bs4
apt install wget
wget https://github.com/techdevazeland/BitZero-GNU-Linux/raw/main/bitzero
echo "INSTALANDO"
cd ~
mkdir -p BitZero
chmod +x ~/bitzero
clear
echo -e "Establezca WorkDir:\n[1]GNU/Linux\n[2]Termux/Android\n" 
read -p ">> " option

if [ "$option" == "1" ]; then
  ~/python ~/bitzero workdir BitZero/downloads
elif [ "$option" == "2" ]; then
  ~/python ~/bitzero workdir --android
else
  ./python ~/bitzero workdir BitZero/downloads
fi
echo "alias bitzero='python ~/bitzero'" >> ~/.bashrc
source ~/.bashrc
clear
alias bitzero='python ~/bitzero'
clear
echo " | + INSTALACIÓN COMPLETADA + \n    -- bitzero help"

#!/bin/bash

echo "Descargando recursos..."
mkdir -p BitZero
cd BitZero
wget https://github.com/techdevazeland/BitZero-GNU-Linux/raw/main/dlc.zip dlc.zip
unzip dlc.zip
chmod +x ./dlc/dlc
rm dlc.zip
clear
cd ../
echo -e "Establezca WorkDir:\n[1]GNU/Linux\n[2]Termux/Android\n" 
read -p ">> " option

if [ "$option" == "1" ]; then
  ./dlc/dlc workdir BitZero/downloads
elif [ "$option" == "2" ]; then
  ./dlc/dlc workdir --android
else
  ./dlc/dlc workdir BitZero/downloads
fi
echo "alias bitzero='BitZero/dlc/dlc'" >> ~/.bashrc
source ~/.bashrc
clear
alias bitzero='BitZero/dlc/dlc'
echo -e "Debe reiniciar la terminal\nPresione Enter para continuar..."
read -p ">> " option
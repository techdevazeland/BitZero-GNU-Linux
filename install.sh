#!/bin/bash

echo "INSTALANDO"
cd ~
mkdir -p BitZero
wget https://github.com/techdevazeland/BitZero-GNU-Linux/raw/main/dlc.bin
chmod +x ./dlc.bin
clear
echo -e "Establezca WorkDir:\n[1]GNU/Linux\n[2]Termux/Android\n" 
read -p ">> " option

if [ "$option" == "1" ]; then
  ~/dlc.bin workdir BitZero/downloads
elif [ "$option" == "2" ]; then
  ~/dlc.bin workdir --android
else
  ./dlc.bin workdir BitZero/downloads
fi
echo "alias bitzero='~/dlc.bin'" >> ~/.bashrc
source ~/.bashrc
clear
alias bitzero='~/dlc.bin'
clear
echo "INSTALACIÓN COMPLETADA\n    -- bitzero help"
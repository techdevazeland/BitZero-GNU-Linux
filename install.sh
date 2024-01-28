#!/bin/bash

echo "Descargando recursos..."
mkdir -p BitZero
curl -o BitZero/dlc https://github.com/techdevazeland/BitZero-GNU-Linux/raw/main/assets/dlc

echo "Otorgando permisos..."
chmod +x BitZero/dlc

read -p "Establezca WorkDir:\n[1]GNU/Linux\n[2]Termux/Android" option

if [ "$option" == "1" ]; then
  BitZero/dlc workdir BitZero/downloads
elif [ "$option" == "2" ]; then
  BitZero/dlc workdir --android
else
  echo "ESA NO ES UNA OPCIÓN"
fi

echo "Generando BitZero/DLC"
echo "alias bitzero='BitZero/dlc'" >> ~/.bashrc
source ~/.bashrc

echo "BITZERO INSTALADO"
bitzero --help
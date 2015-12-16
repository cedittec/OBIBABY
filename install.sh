rm -R /home/pi/Desktop/tmp
rm -R /home/pi/Desktop/obibaby

echo "Instalación de dependencia"

echo "Instalación de Grove Pi"

sudo apt-get update -y
sudo mkdir /home/pi/Desktop/tmp
cd  /home/pi/Desktop/tmp
git clone 'https://github.com/DexterInd/GrovePi' /home/pi/Desktop/tmp/GrovePi
cd /home/pi/Desktop/GrovePi/tmp/Script
sudo chmod +x install.sh
sudo sh install.sh

echo "Instalando dependencia del display y el pip"
apt-get install libffi-dev python-pip python-bluetooth -y

echo "Volviendo al directorio tmp"
cd /home/pi/Desktop/tmp

echo "Se instalará pyMOD-OLED"
git clone 'https://github.com/SelfDestroyer/pyMOD-OLED.git' /home/pi/Desktop/tmp/pyMOD-OLED
cd /home/pi/Desktop/tmp/pyMOD-OLED
python setup.py install



echo "Instalación del video streaming"

sudo apt-get install libgstreamer0.10-0 libgstreamer0.10-dev gstreamer0.10-tools gstreamer0.10-plugins-base libgstreamer-plugins-base0.10-dev gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-bad libgstreamer-plugins-base1.0-dev -y

echo "Instalacion de paquetería Wireless"


sudo pip install wireless 


echo "Clonando el proyecto del github de Cedittec"

git clone 'https://github.com/cedittec/obibaby' /home/pi/Desktop/obibaby

echo "Copiando archivos de rutinas a /bin"

cp /home/pi/Desktop/obibaby/assets/routine /bin/routine
chmod +x /bin/routine

cp /home/pi/Desktop/obibaby/assets/update_data /bin/update_data
chmod +x /bin/update_data

cp /home/pi/Desktop/obibaby/assets/update_streaming /bin/update_streaming
chmod +x /bin/update_streaming


echo "Editando crontab para realizar rutinas cada 5 minutos"

cd /home/pi/Desktop/tmp
crontab -l > aux_cron


echo "*/5 * * * * routine" >> aux_cron
crontab aux_cron

echo "Saliendo del directorio temporal tmp"
cd /home/pi/Desktop
#rm -R /home/pi/Desktop/tmp

echo "Finalizando instalacion"
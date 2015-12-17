rm -R /home/pi/Desktop/tmp
rm -R /home/pi/Desktop/obibaby

echo "Instalación de dependencia"


sudo apt-get update -y
sudo mkdir /home/pi/Desktop/tmp

echo "Instalando dependencia del display y el pip"
apt-get install libffi-dev python-pip python-bluetooth -y


echo "Se instalará pyMOD-OLED"
git clone 'https://github.com/SelfDestroyer/pyMOD-OLED.git' /home/pi/Desktop/tmp/pyMOD-OLED
python /home/pi/Desktop/tmp/pyMOD-OLED/setup.py install



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

crontab -l > /home/pi/Desktop/tmp/aux_cron


echo "*/5 * * * * routine" >> /home/pi/Desktop/tmp/aux_cron
crontab /home/pi/Desktop/tmp/aux_cron

echo "Eliminado el directorio temporal tmp"
#rm -R /home/pi/Desktop/tmp

echo "Finalizando instalacion"
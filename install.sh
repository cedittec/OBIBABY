#Before using this installer, GrovePi shall have been already installed.
#You can read the instructions in the oficial site:
#	http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/


sudo rm -R /home/pi/Desktop/tmp
sudo rm -R /home/pi/Desktop/starter-log.txt
sudo rm -R /home/pi/Desktop/obibaby


if [ "$(id -u)" != "0" ]; 
then
   echo "You need to be root to run this script." 1>&2
   exit 1
fi

echo "Instalación de dependencias"


sudo apt-get update -y > /home/pi/Desktop/starter-log.txt
sudo mkdir /home/pi/Desktop/tmp

echo "Instalando dependencia del display y el pip"
sudo apt-get install python-serial libffi-dev python-pip python-bluetooth sshpass libssl-dev libcurl4-openssl-dev python-dev -y >> /home/pi/Desktop/starter-log.txt

echo "---------------------------"
echo "Se instalará pyMOD-OLED"
git clone 'https://github.com/SelfDestroyer/pyMOD-OLED.git' /home/pi/Desktop/tmp/pyMOD-OLED
python /home/pi/Desktop/tmp/pyMOD-OLED/setup.py install >> /home/pi/Desktop/starter-log.txt


echo "Instalación del video streaming"

sudo apt-get install libgstreamer0.10-0 libgstreamer0.10-dev gstreamer0.10-tools gstreamer0.10-plugins-base libgstreamer-plugins-base0.10-dev gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-bad libgstreamer-plugins-base1.0-dev python-picamera python-picamera-docs -y >> /home/pi/Desktop/starter-log.txt

echo "Instalacion de paquetería Wireless"

sudo pip install wireless pycurl >> /home/pi/Desktop/starter-log.txt

echo "Clonando el proyecto del github de Cedittec en el directorio adecuado"

git clone 'https://github.com/cedittec/obibaby' /home/pi/Desktop/obibaby

echo "Copiando archivos de rutinas a /bin"

sudo cp /home/pi/Desktop/obibaby/assets/obibaby_main /bin/obibaby_main
sudo chmod +x /bin/obibaby_main

sudo cp /home/pi/Desktop/obibaby/assets/update_data /bin/update_data
sudo chmod +x /bin/update_data

sudo cp /home/pi/Desktop/obibaby/assets/update_streaming /bin/update_streaming
sudo chmod +x /bin/update_streaming

echo "Copying the rc.local file to /etc/, so the main loop runs at the system start"

sudo cp /home/pi/Desktop/obibaby/assets/rc.local /etc/rc.local
sudo chmod +x /etc/rc.local


echo "Eliminado el directorio temporal tmp"
#rm -R /home/pi/Desktop/tmp
echo "Logs guardados en /home/pi/Desktop/starter-log.txt"
echo "Finalizando instalacion"

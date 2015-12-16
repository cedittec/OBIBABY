echo "Instalación de dependencia"

echo "Instalación de Grove Pi"
#"Comandos para instalar dependencias de GrovePi"
#"Se bajará GrovePi de un repositorio"
sudo apt-get update -y
sudo mkdir /home/pi/Desktop/tmp
cd  /home/pi/Desktop/tmp
git clone 'https://github.com/DexterInd/GrovePi' /home/pi/Desktop/tmp/GrovePi
cd /home/pi/Desktop/GrovePi/tmp/Script
sudo chmod +x install.sh
sudo sh install.sh

#"Ahora se instalará una librería de dependencia del display"
echo "Instalando dependencia del display y el pip"
apt-get install libffi-dev python-pip -y

echo "Volviendo al directorio tmp"
cd /home/pi/Desktop/tmp

#"Se clonará e instalará pyMOD-OLED"
echo "Se instalará pyMOD-OLED"
git clone 'https://github.com/SelfDestroyer/pyMOD-OLED.git' /home/pi/Desktop/tmp/pyMOD-OLED
cd /home/pi/Desktop/tmp/pyMOD-OLED
python setup.py install

echo "Clonando el proyecto del github de Cedittec"
#"Se procederá a ir a una carpeta temporal para descargar los archivos de obibaby"
git clone ‘https://github.com/cedittec/obibaby’ /home/pi/Desktop/obibaby


#"------------------------------------------------------------------------------"
echo "Instalación del video streaming"

sudo apt-get update -y
sudo apt-get upgrade -y

#"Se instalarán dependencias del video streaming"
sudo apt-get install libgstreamer0.10-0 libgstreamer0.10-dev gstreamer0.10-tools gstreamer0.10-plugins-base libgstreamer-plugins-base0.10-dev gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-bad libgstreamer-plugins-base1.0-dev -y

#"------------------------------------------------------------------------------"
echo "Instalacion de paquetería Wireless"

#"Este paquete permite conexión a una red dada el SSID key password"
sudo pip install wireless 


#Se tienen que copiar los archivos que pasan cada comando via terminal
echo "Copiando archivos de rutinas a /bin"

cp /home/pi/Desktop/obibaby/assets/routine /bin/routine
chmod +x /bin/routine

cp /home/pi/Desktop/obibaby/assets/update_data /bin/update_data
chmod +x /bin/update_data

cp /home/pi/Desktop/obibaby/assets/update_streaming /bin/update_streaming
chmod +x /bin/update_streaming

#"------------------------------------------------------------------------------"
#"Modificación de Crono tab"
#

echo "Editando crontab para realizar rutinas cada 5 minutos"

#"Crontab sirve para manejar el cronograma del sistema"
#"Se pueden definir rutinas con pulsos de tiempo"
#"Crontab ya está implementado por defecto en las distribuciones de Debian, ejemplo Ubuntu y Raspbian"

#"ir al directorio de crontab, dentro de la carpeta"
cd /home/pi/Desktop/tmp
crontab -l > aux_cron
#"Recordemos que auxcrom es un archivo temporal"

echo "*/5 * * * * routine" >> aux_cron
crontab aux_cron

echo "Saliendo del directorio temporal tmp"
cd /home/pi/Desktop
rm -R /home/pi/Desktop/tmp

echo "Finalizando instalacion"
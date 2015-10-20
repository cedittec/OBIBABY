
Guía RaspberryPi
================

Montar memoria a la SD
------------------

* Descargar Raspbian

https://www.raspberrypi.org/downloads/raspbian/

* Para preparar a la memoria

```
# diskutil unmountDisk /dev/disk4 (nota el numero que se ponga es de acuerdo al SD que se use)
```

* Montamos el Raspbian a la memoria con el siguiente comando

```
sudo dd bs=1m if=2015-05-05-raspbian-wheezy.img of=/dev/rdisk4 (Igual tener cuidado con el numero que se vaya a usar, que sea deacuerdo a la memoria “rdisk4” o “rdisk5”)
```

* Habilitar uso completo de memoria SD

	Una vez hecho esto solo se podrá hacer uso de una partición hecha a partir de los comandos que usamos para montar Raspbian,  para poder utilizar el resto de la memoria se debe activar una función desde la raspberry. 

	Ingresar desde raspberry

```
sudo raspi-config 
```

* Y seleccionamos la opción de `EXPAND FILESYSTEM` y consecuente le damos en la opción de `ENABLE` 
  También podemos activar otras funciones desde el menu que nos aparece con el 
  Podemos asignar contraseña a la raspberry en la opción de `CHANGE USER PASSWORD (‘obitec15.0’)` 
  Igualmente podemos habilitar la cámara, con `ENABLE CAMARA`
  Cambiar la hora en `ITERNATIONALISATION OPTIONS`, luego seleccionamos `CHANGE TIMEZONE`, `AMERICA` y después         `Mexico_city`


Hacer uso de GrovePi
--------------------

```
sudo apt-get update
```

* Descargaremos el Git de Dexter Industries 

```
git clone https://github.com/DexterInd/GrovePi
```

* Instalar GrovePi

```
cd GrovePi/Script
```

```
sudo chmod +x install.sh
```

```
sudo ./install.sh
```

Instalar MySql
--------------

```
sudo apt-get install python-mysqldb
```

* Descargar la carpeta de nuestro Git

```	
git clone https://github.com/miguelPerezOntiveros/obiBaby.git
```

* Accedemos a la carpeta desde el command line

```
cd ObiBaby/
```

* Después cargamos el script

```
python actualizar.py
```

* Para comprobar que funcione mandar el siguiente comando 

```
i2cdetect -y 1 
```

Si se ve un “04” la instalación fue exitosa

Usar Wifi
---------

```
sudo wifi 
```

* Vemos los dispositivos disponibles y agregamos el deseado

```
sudo wifi add [SCHEME] TUSSID
```

`password`: **Ingresamos el password de la SSID

```
sudo wifi connect [SCHEME]
```

* SCHEME puede ser cualquier nombre es solo la manera en como queramos llamar a la red que nos queramos conectar




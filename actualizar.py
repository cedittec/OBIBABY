#!/usr/bin/python
import grovepi
import time
import os
#Son para el display
from oled import OLED
from oled import Font
from oled import Graphics


#Subprocess, es para correr comandos
import subprocess
#Es una funcion obtenida de esta liga
#http://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output

#Obtiene lo que devuelve el comando.
def runProcess(exe):
	p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	while(True):
		retcode = p.poll()
		line = p.stdout.readline
		yield line
		if(retcode is not None):
			break


dis = OLED(1)
# Start communication
dis.begin()

# Start basic initialization
dis.initialize()

# Do additional configuration
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)


sensorth = 4
gas_sensor = 1
grovepi.pinMode(gas_sensor,"INPUT")
air_sensor = 0
grovepi.pinMode(air_sensor,"INPUT")
pir_sensor = 3
grovepi.pinMode(pir_sensor,"INPUT")


while True:
	try:
		fecha = time.strftime('%Y-%m-%d %H:%M:%S')
		print "Leyendo Temperatura y humedad"
		[temp,humidity] = grovepi.dht(sensorth,0)
		print "temp =", temp, " humidity =", humidity

		print "Leyendo sensor de Gas"
		sensor_value = grovepi.analogRead(gas_sensor)
		print "sensor_value =", sensor_value

		print "Leyendo sensor de Aire"
		sensor_valueAir = grovepi.analogRead(air_sensor)

		#el campo pollution es enum (1-'low', 2-'medium', 3='high')
		if sensor_valueAir > 700:
			air = 3
		elif sensor_valueAir > 300:
			air = 2
		else:
			air = 1
		print "sensor_valueAir =", sensor_valueAir, " Aire =", air


		print "Leyendo sensor de Movimiento"
		if grovepi.digitalRead(pir_sensor):
			print "Sensor de Movimiento Actualizado en la BD"
		else:
			print "No hubo movimiento"


		print "--------------------------------------------------"



		# Clear display
		dis.deactivate_scroll()
		dis.clear()

		# Set font scale x2
		f = Font(2)
		# Print some large text
		f.print_string(6, 0, "Estado del ambiente")

		# Change font to 5x7
		f.scale = 1

		f.print_string(10, 32, "Temperatura: "+str(temp))
		f.print_string(10, 40, "Humedad: "+str(humidity))
		f.print_string(10, 48, "Gas: "+str(sensor_value))
		f.print_string(10, 56, "Aire: "+str(air))
		# Send video buffer to display
		dis.update()
		time.sleep (5)

		if (temp<=24 and temp>=20 and humidity<=50 and humidity>=30 and sensor_value<=10 and air==1):
			dis.clear()

			# Set font scale x2
			f = Font(2)
			# Print some large text
			f.print_string(6, 0, "Estado del ambiente")

			f.print_string(10, 32, "OK")

			# Send video buffer to display
			dis.update()
			time.sleep (5)
		else:
			if(temp>24):
				dis.clear()

				# Set font scale x2
				f = Font(1)
				# Print some large text
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Temp alta")

				# Send video buffer to display
				dis.update()
			if(temp<20):
				dis.clear()

				# Set font scale x2
				f = Font(2)
				# Print some large text
				f.print_string(6, 0, "Estado del ambiente")

				f.print_string(10, 32, "Temp baja")

				# Send video buffer to display
				dis.update()

		time.sleep(5)
	except IOError:
		print "Error"
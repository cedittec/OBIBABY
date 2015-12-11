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

#Registro de temperatura...
def logAlert(alerid, fecha):
	#Url de la pagina en la que se hace el registro...
	log_url = 'http://obibaby.com/api/v1/account/logs/alerts'
	#JSON que se envia...
	data = json.dumps({
		"type": "log_user_alerts",
		"data": {
			"user_id": "2",
			"aler_id": alerid,
			"updated_at": fecha,
			"created_at": fecha,
			"id": 2
		},
  		"relationships": {
  			"user": {
  				"id": "2",
  				"name": "Erick",
  				"last_name": "",
  				"email": "erick2@csgroup.mx",
  				"telephone": "",
  				"baby_photo": "",
  				"baby_name": "",
  				"baby_birthdate": "",
  				"baby_sex": "null",
  				"baby_weight": "0",
  				"baby_height": "0",
  				"created_at": "2015-08-17 16:12:03",
  				"updated_at": "2015-08-17 16:13:32",
  				"deleted_at": "null"
  			}
  		}
  	})

	c = pycurl.Curl()
	c.setopt(pycurl.URL, log_url)
	#autenticacion...
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()


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
			air = "high"
		elif sensor_valueAir > 300:
			air = "medium"
		else:
			air = "low"
		print "sensor_valueAir =", sensor_valueAir, " Aire =", air


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

		if (temp<=24 and temp>=20 and humidity<=50 and humidity>=30 and sensor_value<=10 and air=="low"):
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
				id=1
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Temp alta")
				#dis.update(id,fecha)
				#logAlert()

				time.sleep(5)
			if(temp<20):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Temp baja")
				dis.update()
				time.sleep(5)
			if(humidity>50):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Humedad alta")
				dis.update()
				time.sleep(5)
			if(humidity<30):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Humedad baja")
				dis.update()
				time.sleep(5)
			if(sensor_value>10):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Presencia de Gas")
				dis.update()
				time.sleep(5)
			if(air!="low"):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Mala calidad de Aire")
				dis.update()
				time.sleep(5)

		
	except IOError:
		print "Error"
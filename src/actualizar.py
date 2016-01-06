#!/usr/bin/python
import grovepi
import time
import os
import httplib
#Son para el display
from oled import OLED
from oled import Font
from oled import Graphics

def internet_off():
        conn = httplib.HTTPConnection("www.google.com")
        try:
                conn.request("HEAD", "/")
                return False
        except:
                return True


dis = OLED(1)
# Start display
dis.begin()

# Start basic initialization
dis.initialize()

# Do additional configuration
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)


while True:
	sensorth = 4
	gas_sensor = 1
	grovepi.pinMode(gas_sensor,"INPUT")
	air_sensor = 0
	grovepi.pinMode(air_sensor,"INPUT")
	pir_sensor = 3
	grovepi.pinMode(pir_sensor,"INPUT")

	try:

		#Get the values of every sensor.

		fecha = time.strftime('%Y-%m-%d %H:%M:%S')
		print "Leyendo Temperatura y humedad"
		[temp,humidity] = grovepi.dht(sensorth,0)
		print "temp =", temp, " humidity =", humidity

		print "Leyendo sensor de Gas"
		sensor_value = grovepi.analogRead(gas_sensor)
		print "sensor_value =", sensor_value

		print "Leyendo sensor de Aire"
		sensor_valueAir = grovepi.analogRead(air_sensor)

		if sensor_valueAir > 700:
			air = "high"
		elif sensor_valueAir > 300:
			air = "medium"
		else:
			air = "low"
		print "sensor_valueAir =", sensor_valueAir, " Aire =", air


		print "--------------------------------------------------"

		if(internet_off):
			# Clear display
			dis.clear()
			# Set font scale x2
			f = Font(2)
			# Print large text
			f.print_string(6, 0, "Sin Conexión")
			# Send video buffer to display
			dis.update()
			time.sleep (5)


		# Clear display
		dis.clear()

		# Set font scale x2
		f = Font(2)
		# Print large text
		f.print_string(6, 0, "Estado del ambiente")

		# Change font to 5x7
		f.scale = 1

		# Print small text
		f.print_string(10, 32, "Temperatura: "+str(temp))
		f.print_string(10, 40, "Humedad: "+str(humidity))
		f.print_string(10, 48, "Gas: "+str(sensor_value))
		f.print_string(10, 56, "Aire: "+str(air))

		# Send video buffer to display
		dis.update()
		time.sleep (5)
		
		#Acceptable environment conditions
		if (temp<=24 and temp>=20 and humidity<=50 and humidity>=30 and sensor_value<=50 and air=="low"):
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
			
			#High temperature alert
			if(temp>24):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Temp alta")
				dis.update()
				time.sleep(5)

			#Low temperature alert
			if(temp<20):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Temp baja")
				dis.update()
				time.sleep(5)

			#High humidity alert
			if(humidity>50):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Humedad alta")
				dis.update()
				time.sleep(5)

			#Low humidity alert
			if(humidity<30):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Humedad baja")
				dis.update()
				time.sleep(5)

			#Gas alert
			if(sensor_value>50):
				dis.clear()

				f = Font(1)
				f.print_string(6, 0, "Estado del ambiente")
				f = Font(2)
				f.print_string(10, 32, "Presencia de Gas")
				dis.update()
				time.sleep(5)

			#Polluter air alert
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
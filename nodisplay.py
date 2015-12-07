#!/usr/bin/python
import grovepi
import time
import os
#Son para el #display
#from oled import OLED
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


##dis = OLED(1)
# Start communication
##dis.begin()

# Start basic initialization
##dis.initialize()

# Do additional configuration
##dis.set_memory_addressing_mode(0)
##dis.set_column_address(0, 127)
##dis.set_page_address(0, 7)

#db = MySQLdb.connect(host="10.49.130.37",
#	user="cedittec",
#	passwd="server",
#	db="obiBaby")

sensorth = 4
gas_sensor = 1
grovepi.pinMode(gas_sensor,"INPUT")
air_sensor = 0
grovepi.pinMode(air_sensor,"INPUT")
pir_sensor = 3
grovepi.pinMode(pir_sensor,"INPUT")

cur = db.cursor()

while True:
	#if(checar is hay internet)//tabulador a lo que sigue
	try:
		fecha = time.strftime('%Y-%m-%d %H:%M:%S')
		print "Leyendo Temperatura y humedad"
		[temp,humidity] = grovepi.dht(sensorth,0)
		print "temp =", temp, " humidity =", humidity
		#cur.execute("INSERT INTO log_user_temperature (temperature, humidity) VALUES ('%s', '%s')", (temp, humidity))
		#db.commit()
		#print "Temperatura y Humedad Actualizado en la BD"
		GetTempHumi='/GET={"type":"log_user_temperatures","total":1,"data":[{"id":"5","user_id":"2","value":".6","temperature":"'+temp+'","humidity":"'+humidity+'""created_at":"'+fecha+'","updated_at":"'+fecha+'","deleted_at":null}],"relationships":{"user":{"id":"2","name":"Erick","last_name":"","email":"erick2@csgroup.mx","telephone":"","baby_photo":"","baby_name":"","baby_birthdate":"","baby_sex":null,"baby_weight":"0","baby_height":"0","created_at":"2015-08-1716:12:03","updated_at":"2015-08-1716:13:32","deleted_at":null}}}'
		os.system("curl '"+GetTempHumi+"'")

		print "Leyendo sensor de Gas"
		sensor_value = grovepi.analogRead(gas_sensor)
		print "sensor_value =", sensor_value
		#cur.execute("INSERT INTO log_user_gas (co) VALUES ('%s')", (sensor_value))
		#db.commit()
		#print "Sensor de Gas Actualizado en la BD"
		print "Leyendo sensor de Aire"
		sensor_valueAir = grovepi.analogRead(air_sensor)

		#el campo pollution es enum (1-'low', 2-'medium', 3='high')
		if sensor_valueAir > 700:
			air = 3
		elif sensor_valueAir > 300:
			air = 2
		else:
			air = 1

		GetAire='http://obibaby.com/api/v1/account/logs/air/GET={"type":"log_user_air","total":1,"data":[{"id":"5","user_id":"2","value":"'+sensor_valueAir+'","pollution":"'+air+'","created_at":"'+fecha+'","updated_at":"'+fecha+'","deleted_at":null}],"relationships":{"user":{"id":"2","name":"Erick","last_name":"","email":"erick2@csgroup.mx","telephone":"","baby_photo":"","baby_name":"","baby_birthdate":"","baby_sex":null,"baby_weight":"0","baby_height":"0","created_at":"2015-08-1716:12:03","updated_at":"2015-08-1716:13:32","deleted_at":null}}}'
		os.system("curl '"+GetAire+"'")

		print "sensor_valueAir =", sensor_valueAir, " Aire =", air
		#cur.execute("INSERT INTO log_user_air (value, pollution) VALUES ('%s', '%s')", (sensor_valueAir, air))
		#db.commit()
		#print "Sensor de Aire Actualizado en la BD"
		print "Leyendo sensor de Movimiento"
		if grovepi.digitalRead(pir_sensor):
			#cur.execute("INSERT INTO log_user_motion (time) VALUES (%s)", (fecha))
			#db.commit()
			#print "Sensor de Movimiento Actualizado en la BD"
		else:
			print "No hubo movimiento"


		print "--------------------------------------------------"



		# Clear #display
		#dis.clear()

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
		# Send video buffer to #display
		#dis.update()

		if (temp<=24 and temp>=20 and humidity<=50 and humidity>=30 and sensor_value<=10 and air==1):
			#dis.clear()

			# Set font scale x2
			f = Font(2)
			# Print some large text
			f.print_string(6, 0, "Estado del ambiente")

			f.print_string(10, 32, "OK")

			# Send video buffer to #display
			#dis.update()
		else:
			if(temp>24):
				#dis.clear()

				# Set font scale x2
				f = Font(2)
				# Print some large text
				f.print_string(6, 0, "Estado del ambiente")

				f.print_string(10, 32, "Temp alta")

				# Send video buffer to #display
				#dis.update()
			if(temp<20):
				#dis.clear()

				# Set font scale x2
				f = Font(2)
				# Print some large text
				f.print_string(6, 0, "Estado del ambiente")

				f.print_string(10, 32, "Temp baja")

				# Send video buffer to #display
				#dis.update()

		time.sleep(2)
	except IOError:
		print "Error"
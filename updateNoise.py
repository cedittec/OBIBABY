import json
import grovepi
import time
import pycurl
import os

sound_sensor = 2
fecha = time.strftime('%Y-%m-%d %H:%M:%S')
noise = grovepi.analogRead(sound_sensor)
tiempo = 0

if (noise>400):
	start_time = time.time()
	while grovepi.digitalRead(sound_sensor) > 400:
		sleep(0.5)
	tiempo = time.time() - start_time

print "Sonido "+ str(noise) + " Tiempo: "+ str(tiempo)

if (tiempo > 0):
	log_url = 'http://obibaby.com/api/v1/account/logs/noise';
	data = 'value='+str(noise)+'&duration='+str(tiempo)
	
	c = pycurl.Curl()
	c.setopt(pycurl.URL, log_url)
	#autenticacion...
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()
	print ""
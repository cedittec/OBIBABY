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

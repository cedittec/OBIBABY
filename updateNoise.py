import json
import grovepi
import time
import pycurl
import os

sound_sensor = 2
fecha = time.strftime('%Y-%m-%d %H:%M:%S')
noise = grovepi.analogRead(sound_sensor)

print "sonido "+ str(noise)

#Here we can upload that data, as soon as they get a method.
import json
import grovepi
import time
from time import sleep
import pycurl
import os


f = open("/home/pi/Desktop/obibaby/user.txt","rw+")
data = f.readline()
user,pasu = data.split(',')

fecha = time.strftime('%Y-%m-%d %H:%M:%S')
start_time = time.time()
pir_sensor = 3
grovepi.pinMode(pir_sensor,"INPUT")

while grovepi.digitalRead(pir_sensor):
	sleep(0.5)
elapsed_time = time.time() - start_time
print "movimiento "+ str(elapsed_time)

if (elapsed_time > 0):
	log_url = 'http://obibaby.com/api/v1/account/logs/motion';
	data = 'time='+str(elapsed_time)
	'''
	data = json.dumps({
		"type": "log_user_motion",
		"data": {
			"user_id": "2",
			"time": elapsed_time,
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
	'''
	c = pycurl.Curl()
	c.setopt(pycurl.URL, log_url)
	#autenticacion...
	c.setopt(pycurl.USERPWD, "%s:%s" % (user, pasu))
	c.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()
	print ""
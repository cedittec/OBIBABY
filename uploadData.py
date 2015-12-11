
#!/usr/bin/python
import json
import grovepi
import pycurl

try:
	# python 3
	from urllib.parse import urlencode
except ImportError:
	# python 2
	from urllib import urlencode

import time
import os

def logMov(time,fecha):
	#Url de la pagina en la que se hace el registro... 01 800 099 0316   -> 305   
	log_url = 'http://obibaby.com/api/v1/account/logs/temperatures'
	#JSON que se envia...
	data = json.dumps({
		"type": "log_user_motion",
		"data": {
			"user_id": "2",
			"time": "50",
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

#Registro de temperatura...
def logTemp(temperature,humidity,fecha):
	#Url de la pagina en la que se hace el registro...
	log_url = 'http://obibaby.com/api/v1/account/logs/temperatures'
	#JSON que se envia...
	data = json.dumps({
		"type": "log_user_temperatures",
		"data": {
			"value": humidity,
			"pollution": temperature,
			"user_id": "2",
		    "updated_at": fecha,
			"created_at": fecha,
			"id": 5
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

#Usa la API para hacer el registro del log de aire.
def logAir(value,pollution,fecha):
	value = value/1000;
	#Url de la pagina en la que se hace el registro...
	log_url = 'http://obibaby.com/api/v1/account/logs/air'



	#JSON que se envia...
	##No funcionará con esta, sino con esta:
	data = 'value='+str(value)+'&pollution='+str(pollution)

	'''
	data = json.dumps({
		"type": "log_user_air",
		"data": {
			"value": ".6",
			"pollution": "high",
			"user_id": "2",
			"updated_at": fecha,
			"created_at": fecha,
			"id": 5
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
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER,  ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()


#getCurrent time
laFecha = time.strftime('%Y-%m-%d %H:%M:%S')

#Declare
sensorth = 4
gas_sensor = 1
grovepi.pinMode(gas_sensor,"INPUT")
air_sensor = 0
grovepi.pinMode(air_sensor,"INPUT")
pir_sensor = 3
grovepi.pinMode(pir_sensor,"INPUT")

#Get Temperature and humidity from the declared sensorth
[temp,humi] = grovepi.dht(sensorth,0)
print ""
logTemp(temp,humi,laFecha)
print ""
print "temp =", temp, " humidity =", humi

#Get the gas sensor value
gas_value = grovepi.analogRead(gas_sensor)
sensor_valueAir = grovepi.analogRead(air_sensor)
air = ""
#el campo pollution es enum (1-'low', 2-'medium', 3='high')
if sensor_valueAir > 700:
	air = "high"
elif sensor_valueAir > 300:
	air = "medium"
else:
	air = "low"
print ""
logAir(sensor_valueAir,air,laFecha)
print ""
print "sensor_valueAir =", sensor_valueAir, " Aire =", air

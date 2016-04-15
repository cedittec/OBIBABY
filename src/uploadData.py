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



#Temperature Alert Log...
def logAlert(alert_id):
	print "Enviando alerta con id : "+str(alert_id)
	log_url = 'http://obibaby.com/api/v1/account/logs/alerts'
	data = "alert_id="+str(alert_id)
	'''
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
	'''

	c = pycurl.Curl()
	c.setopt(pycurl.URL, log_url)
	#authentication...
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()

	print ""
	print "Alerta enviada"

#Gas log...
def logGas(value,fecha):
	log_url = 'http://obibaby.com/api/v1/account/logs/gas'
	
	data = 'value='+str(value)
	
	c = pycurl.Curl()
	c.setopt(pycurl.URL, log_url)
	#authentiacation
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	print "Enviando log de gas: "+str(value)
	c.perform()
	print ""
	#Alert in case of toxic gas presence
	if (value > 10):
		logAlert(5)


#Temperarure Log...
def logTemp(temperature,humidity,fecha):
	log_url = 'http://obibaby.com/api/v1/account/logs/temperatures'

	data = 'temperature='+str(temperature)+'&humidity='+str(humidity)
	#JSON que se envia...
	'''
	data = json.dumps({
		"type": "log_user_temperatures",
		"data": {
			"temperature": temperature,
    		"humidity": humidity,
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
	#authentication
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER, ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	print "Enviando sensado de temperatura: "+str(temperature)+ " humedad: "+str(humidity)
	c.perform()
	print ""
	if (temperature>24):
		logAlert(2)


#Air Log
def logAir(value,pollution,fecha):
	
	log_url = 'http://obibaby.com/api/v1/account/logs/air'

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
	print "Enviando log de aire value: "+str(value)+ " pollution: "+str(pollution)
	c.perform()
	print ""
	if (value > 700):
		logAlert(4)




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

#Get the gas sensor value
gas_value = grovepi.analogRead(gas_sensor)
logGas(gas_value,laFecha)
sensor_valueAir = grovepi.analogRead(air_sensor)
air = ""
#Pollution is an enumerator with the next values (1-'low', 2-'medium', 3='high')
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

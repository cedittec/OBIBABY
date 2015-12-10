
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

print "Hola"

def logMov(time):
	#Url de la pagina en la que se hace el registro... 01 800 099 0316   -> 305   
	log_url = 'http://obibaby.com/api/v1/account/logs/temperatures'
	#JSON que se envia...
	data = json.dumps({
		"type": "log_user_motion",
		"data": {
			"user_id": "2",
			"time": "50",
			"updated_at": "2015-08-17 16:29:27",
			"created_at": "2015-08-17 16:29:27",
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
				"baby_sex": null,
				"baby_weight": "0",
				"baby_height": "0",
				"created_at": "2015-08-17 16:12:03",
				"updated_at": "2015-08-17 16:13:32",
				"deleted_at": null
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
def logTemp(temperature,humidity):
	#Url de la pagina en la que se hace el registro...
	log_url = 'http://obibaby.com/api/v1/account/logs/temperatures'
	#JSON que se envia...
	data = json.dumps({
		"type": "log_user_air",
		"data": {
			"value": humidity,
			"pollution": temperature,
			"user_id": "2",
		    "updated_at": "2015-08-17 16:23:25",
			"created_at": "2015-08-17 16:23:25",
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
	  			"baby_sex": null,
	  			"baby_weight": "0",
	  			"baby_height": "0",
	  			"created_at": "2015-08-17 16:12:03",
	  			"updated_at": "2015-08-17 16:13:32",
	  			"deleted_at": null
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
def logAir(value,pollution):
	#Url de la pagina en la que se hace el registro...
	log_url = 'http://obibaby.com/api/v1/account/logs/air'
	#JSON que se envia...
	data = json.dumps({
		"type": "log_user_air",
		"data": {
			"value": value,
			"pollution": pollution,
			"user_id": "2",
			"updated_at": "2015-08-17 16:23:25",
			"created_at": "2015-08-17 16:23:25",
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
				"baby_sex": null,
				"baby_weight": "0",
				"baby_height": "0",
				"created_at": "2015-08-17 16:12:03",
				"updated_at": "2015-08-17 16:13:32",
				"deleted_at": null
			}
		}
	})

	c = pycurl.Curl()
	c.setopt(pycurl.URL, log_url)
	#autenticacion...
	c.setopt(pycurl.USERPWD, "%s:%s" % ('test@obibaby.com', '12345678'))
	c.setopt(pycurl.HTTPHEADER,  ["Accept: application/json"])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	c.perform()
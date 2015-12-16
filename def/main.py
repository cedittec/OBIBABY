import os
from wireless import Wireless
import httplib

def internet_off():
        conn = httplib.HTTPConnection("www.google.com")
        try:
                conn.request("HEAD", "/")
                return False
        except:
                return True

def internet_on():
        conn = httplib.HTTPConnection("www.google.com")
        try:
                conn.request("HEAD", "/")
                return True
        except:
                return False



if (internet_off()):
	file = open('/home/pi/Desktop/networks.txt', 'r')
	text = file.read()
	list = text.split('\n')

	for item in list:
		try:
			print item
			wireless = Wireless()
			bssid,psk = item.split(",")
			print("ssid: "+bssid+ " pass: "+ psk)
			wireless.connect(ssid=bssid, password=psk)
			if (internet_on()):
				print("Conected")
				break
		except:
			print "Not connected or invalid input, mi cuate"
			continue



if (internet_off()):
	os.system("python /home/pi/Desktop/obibaby/def/server-bluetooth.py")
else:
	os.system("update_data & update_streaming")
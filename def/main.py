import os
from wireless import Wireless
import urllib2

def internet_off():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return False
    except urllib2.URLError as err: pass
    return True

if (internet_off()):
	file = open('/home/pi/Desktop/networks.txt', 'r')
	text = file.read()
	list = text.split('\n')
	for item in list:
		try:
			print item
			ssid,psk = item.split(',')
			print("ssid: "+bssid+ " pass: "+ psk)
			wireless.connect(ssid=bssid, password=psk)
			print "Conecting to selected network"
			if (internet_on()):
				print("Conected")
				break;
		except:
			continue


if (internet_off()):
	os.system("python /home/pi/Desktop/obibaby/def/client-ubuntu.py")


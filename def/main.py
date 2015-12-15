import os
from wireless import Wireless
import urllib2

def internet_off():
        try:
                response=urllib2.urlopen('http://74.125.228.100',timeout=1)
                return False
        except: 
                return True
                #urllib2.URLError as err: pass
        return False

def internet_on():
        try:
                response=urllib2.urlopen('http://74.125.228.100',timeout=1)
                return True
        except: 
                return False
                #urllib2.URLError as err: pass
        return False

def clean_string(item):
	tmp = ""
	for c in list(item):
		print "Char: ["+c+"]"
		tmp += c
	print tmp
	return tmp

if (internet_off()):
	file = open('/home/pi/Desktop/networks.txt', 'r')
	text = file.read()
	list = text.split('\n')
	for item in list:
		try:
			print item
			item = clean_string(item)
			print text
			print "Type of text :"+str(type(text))
			ssid,psk = text.split(",")
			print("ssid: "+bssid+ " pass: "+ psk)
			wireless.connect(ssid=bssid, password=psk)
			print "Conecting to selected network"
			if (internet_on()):
				print("Conected")
				break;
		except:
			print "Not valid string, carnal"
			continue


if (internet_off()):
	os.system("python /home/pi/Desktop/obibaby/def/client-ubuntu.py")


import os
from wireless import Wireless
import httplib

os.system("echo $(date '+%Y/%M/%D %H:%M:%S') >> /home/pi/Desktop/log.txt")
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
			os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Red: "+item+"\" >> /home/pi/Desktop/log.txt")
			print item
			os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Antes del wireless\" >> /home/pi/Desktop/log.txt")
			wireless = Wireless()
			bssid,psk = item.split(",")
			print("ssid: "+bssid+ " pass: "+ psk)
			wireless.connect(ssid=bssid, password=psk)
			os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Red: Intento\" >> /home/pi/Desktop/log.txt")
			if (internet_on()):
				print("Conected")
				os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Red: Conectado\" >> /home/pi/Desktop/log.txt")
				os.system("echo '' >> /home/pi/Desktop/log.txt")
				break
			os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Red: No conectado\" >> /home/pi/Desktop/log.txt")
			os.system("echo '' >> /home/pi/Desktop/log.txt")
		except:
			print "Not connected or invalid input, mi cuate"
			continue

while(True):
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
		os.system("sudo python /home/pi/Desktop/obibaby/src/server-bluetooth.py")
	else:
		os.system("sudo update_data & update_streaming")
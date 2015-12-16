import os
import httplib


#Validates that the server is up
def server_up():
        conn = httplib.HTTPConnection("www.google.com")
        try:
                conn.request("HEAD", "/")
                return True
        except:
                return False

if (server_up()):
	#Starts update-data.py
	os.system("python /home/pi/Desktop/obibaby/assets/update-data.py")
else:
	#Raises the "Server Down" flag
	
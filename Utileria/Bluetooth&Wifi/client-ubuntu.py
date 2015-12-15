mport os
import socket
from wireless import Wireless

#Resetear el bluetoot
os.system("/etc/init.d/bluetooth stop")
os.system("/etc/init.d/bluetooth start")


hostMACAddress = '000:15:83:0c:bf:eb' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3   # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 10241
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
print("Se declaro el socket")
s.bind((hostMACAddress,port))
print("Se declaro la relacion entre la MAC y el puertp")
s.listen(backlog)
try:
        print("Entre al try")
        client, address = s.accept()
        print("Hay un cliente")
        while 1:
                data = client.recv(size)
                if data:
                        print(data)
                        wireless = Wireless()
                        bssid,psk = data.split(',')
                        print("ssid: "+bssid+ " pass: "+ psk)
                        wireless.connect(ssid=bssid, password=psk)
                        print("Conectado a la BD.")
                        break;
except:
        print("Closing socket")
        client.close()
        s.close()
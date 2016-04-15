import os
import time
import serial
from wireless import Wireless
import httplib


os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Servidor de Serial iniciado\" >> /home/pi/Desktop/log.txt")

#Try to connect to San Google.
def internet_on():
        conn = httplib.HTTPConnection("www.google.com")
        try:
                conn.request("HEAD", "/")
                return True
        except:
                return False
                
def add_to_file(network_data):
        os.system("echo '"+str(network_data)+"' >> /home/pi/Desktop/networks.txt")

serialSocket = serial.Serial(      
        port='/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        try:
                data = serialSocket.readline()
                wireless = Wireless()
                zero,first,second = data.split(',')
                if (zero == "network"):
                        print("ssid: "+first+ " pass: "+ second)
                        wireless.connect(ssid=first, password=second)
                        print("Conectando a internet.")
                        if (internet_on()):
                                add_to_file(data);
                                print("Conectado a internet.")
                                serialSocket.write("Datos Correctos")
                                os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Conetado a la red brindada\" >> /home/pi/Desktop/log.txt")
                                break;
                        else:
                                print("No conectado a internet.")
                                os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> No conectada a la red brindada\" >> /home/pi/Desktop/log.txt")
                                serialSocket.write("No se pudo conectar a esa red")
                else:
                        print("user: "+first+ " pass: "+ second)
                        #Configuration for user and password....
                        os.system("echo \""+first+","+second+"\" > /home/pi/Desktop/obibaby/user.txt")

        except:
                print("Closing serial socket")
                try:
                        serialSocket.close()
                except:
                        print("Error in serial connection")


### Comented code, it used to be like this in order to work in bluetooth...

'''
import os
import socket
from wireless import Wireless
import httplib

#Reset bluetooth so phantom sessons are over.
os.system("/etc/init.d/bluetooth stop")
os.system("/etc/init.d/bluetooth start")

os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Servidor de bluetooth iniciado\" >> /home/pi/Desktop/log.txt")

#Try to connect to San Google.
def internet_on():
        conn = httplib.HTTPConnection("www.google.com")
        try:
                conn.request("HEAD", "/")
                return True
        except:
                return False

def add_to_file(network_data):
        os.system("echo '"+str(network_data)+"' >> /home/pi/Desktop/networks.txt")

hostMACAddress = '000:15:83:0c:bf:eb' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3   # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 10241
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
print("Se declaro el socket")
s.bind((hostMACAddress,port))
print("Se declaro la relacion entre la MAC y el puerto")
s.listen(backlog)
try:
        print("Entre al try")
        s.settimeout(1500)
        client, address = s.accept()
        print("Hay un cliente")
        os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Cliente de bluetooth conectado\" >> /home/pi/Desktop/log.txt")
        while 1:
                print("Esperando datos")
                data = client.recv(size)
                print("Recibi datos")
                os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Cliente de bluetooth envio: "+data+"\" >> /home/pi/Desktop/log.txt")
                if data:
                        print(data)
                        print("Iniciando objeto de wireless")
                        wireless = Wireless()
                        bssid,psk = data.split(',')
                        print("ssid: "+bssid+ " pass: "+ psk)
                        wireless.connect(ssid=bssid, password=psk)
                        print("Conectando a internet.")
                        if (internet_on()):
                                add_to_file(data);
                                print("Conectado a internet.")
                                client.send("Datos Correctos")
                                os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Conetado a la red brindada\" >> /home/pi/Desktop/log.txt")
                                break;
                        else:
                                print("No conectado a internet.")
                                os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> No conectada a la red brindada\" >> /home/pi/Desktop/log.txt")
                        	client.send("No se pudo conectar a esa red")
                else:
                        print("Voy a matar a bluetooth")
                        os.system("echo \"$(date '+%Y/%M/%D %H:%M:%S')-> Cliente de bluetooth a punto de morir\" >> /home/pi/Desktop/log.txt")
                        break
except:
        print("Closing socket")
        try:
                client.close()
        except NameError:
                print("No habia cliente")
        else:
                print("There was a client")
        s.close()

'''
###End of the commented code.
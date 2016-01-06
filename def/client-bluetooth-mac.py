from lightblue import *

serverMACAddress = "00:15:83:0c:bf:eb"

port = 3
backlog = 1
size = 10241

s = socket()
print "Se declaro el socket"

s.connect((serverMACAddress,port))
print "Se ha conectado"

while 1:
    print "En el while, hasta que se introdusca quit"
    text = raw_input("introduce un texto: \n")
    print "Se recibio el texto: ", text
    if text == "quit":
        break
    print "Enviando.."
    s.send(text)
    print "Se ha enviado!"
    print "Esperando respuesta."
    
    reply = s.recv(size)
    print str(reply)

s.close()
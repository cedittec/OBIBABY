import socket

serverMACAddress = "00:15:83:0c:bf:eb"

port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
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
    #s.send(bytes(text, 'UTF-8'))
s.close()
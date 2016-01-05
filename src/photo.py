#Import the operative system module "os". It is used to run bash commands.
import os

print "Capturando foto..."
#Take picture and save it in the pi desktop with the name 'image.jpg'
os.system('raspistill -o /home/pi/Desktop/image.jpg -w 320 -h 240')
print "Foto capturada."
#Upload the photo to the server, with ip, user and password
#It us done in the next line...
print "Subiendo foto"
os.system('sshpass -p "sashaGrey69" scp /home/pi/Desktop/image.jpg root@104.131.33.240:/usr/share/nginx/html/image.jpg')
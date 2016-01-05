#Import the camera module
import picamera
#Import the operative system module "os". It is used to run bash commands.
import os

#Start the camera module object
camera = picamera.PiCamera()
#Take picture and save it in the pi desktop with the name 'image.jpg'
camera.capture('/home/pi/Desktop/image.jpg')
#Upload the photo to the server, with ip, user and password
#It us done in the next line...
os.system('sshpass -p "sashaGrey69" scp -r root@104.131.33.240:/root/images/ /home/pi/Desktop/image.jpg')
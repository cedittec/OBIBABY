import json
import grovepi
import time
import pycurl
import os

sound_sensor = 2
fecha = time.strftime('%Y-%m-%d %H:%M:%S')
noise = grovepi.analogRead(sound_sensor)

print "sonido "+ str(noise)

#Here we can upload that data, as soon as they get a method.


#raspivid --verbose --nopreview -hf -vf --width 640 --height 480 --framerate 15 --bitrate 1000000 --profile baseline --timeout 0 -o - | gst-launch-0.10 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=104.131.33.240 port=8004 alsasrc device=plughw:Set ! audioconvert ! audioresample ! opusenc ! rtpopuspay ! udpsink host=104.131.33.240 port=8005
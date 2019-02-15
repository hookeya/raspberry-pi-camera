from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0 
camera.start_preview()
camera.start_recording('/home/pi/Desktop/images/video.h264' )
sleep(15)
camera.stop_recording()
camera.stop_preview()

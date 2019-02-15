from picamera import PiCamera,Color
from time import sleep

camera = PiCamera()
camera.rotation = 0
camera.resolution = (2592,1944)
camera.framerate = 15 
camera.start_preview( )
camera.annotate_text_size = 50
camera.exposure_mode = 'beach'
sleep(5)
camera.capture('/home/pi/Desktop/images/beach.jpg')
camera.stop_preview()

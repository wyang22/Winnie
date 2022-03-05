#import the gpio module
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15

GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)

GPIO.output(INT1,GPIO.HIGH)
GPIO.output(INT2,GPIO.LOW)
GPIO.output(INT3,False)
GPIO.output(INT4,False)

#delay 2 seconds
time.sleep(2)
#release the GPIO ports
GPIO.cleanup()
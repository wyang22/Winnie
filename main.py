#!/usr/bin/env python  

#import the gpio module
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.output(IN1,GPIO.HIGH)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.HIGH)
GPIO.output(IN4,GPIO.LOW)

#delay 2 seconds
time.sleep(0.5)
#release the GPIO ports
GPIO.cleanup()

import threading
import time
import RPi.GPIO as GPIO
import os

def thread1():
	PIN_NO=16
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIN_NO, GPIO.OUT)
	for x in xrange(5):
		GPIO.output(PIN_NO,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(PIN_NO,GPIO.LOW )
		time.sleep(1)
	GPIO.cleanup()

 
def thread2():
	os.system('omxplayer music/talks.mp3')
 
thread1 = threading.Thread(target = thread1,args = ())
thread2 = threading.Thread(target = thread2, args = ())
thread1.start()
thread2.start()
thread1.join()
thread2.join()


GPIO.setmode(GPIO.BOARD)

INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15

GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)

GPIO.output(INT1,GPIO.LOW)
GPIO.output(INT2,GPIO.HIGH)
GPIO.output(INT3,False)
GPIO.output(INT4,False)

#delay 2 seconds
time.sleep(0.3)
#release the GPIO ports
GPIO.cleanup()


#motor moves
import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)  


#neckup starts
servopinup = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopinup, GPIO.OUT, initial=False)
p = GPIO.PWM(servopinup,50) #50HZ
p.start(0)
time.sleep(2)

#while(True):
for i in range(0,181,10):
    p.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
for i in range(100,0,-10):
    p.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
#    p.ChangeDutyCycle(0)
#    time.sleep(0.2)
time.sleep(1)
p.ChangeDutyCycle(0)                  #reset

#neck down starts
servopin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)

#while(True):
for i in range(0,85,10):
    p.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    time.sleep(0.2)
time.sleep(0.2)
p.ChangeDutyCycle(0)                  #reset


# arm starts
servopinb1 = 16  #right hand base
servopinb2 = 12  #left hand base
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopinb1, GPIO.OUT, initial=False)
GPIO.setup(servopinb2, GPIO.OUT, initial=False)
pb1 = GPIO.PWM(servopinb1,50) #50HZ
pb2 = GPIO.PWM(servopinb2,50) #50HZ
pb1.start(0)
pb2.start(0)
time.sleep(2)

#while(True):
for i in range(150,0,-10):
    pb1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
#    p2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
for i in range(0,150,10):
#    p1.ChangeDutyCycle(2.5 + 10 * i / 180)
    pb2.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
#    p1.ChangeDutyCycle(0)
#    p2.ChangeDutyCycle(0)
#    time.sleep(0.2)
time.sleep(1)
pb1.ChangeDutyCycle(0)                  #reset
pb2.ChangeDutyCycle(0)                  #reset


servopins1 = 26  #right hand shoulder
servopins2 = 19  #left hand shoulder
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopins1, GPIO.OUT, initial=False)
GPIO.setup(servopins2, GPIO.OUT, initial=False)
pS1 = GPIO.PWM(servopins1,50) #50HZ
pS2 = GPIO.PWM(servopins2,50) #50HZ
pS1.start(0)
pS2.start(0)
time.sleep(2)

#while(True):
for i in range(0,180,10):
    pS1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    pS2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
time.sleep(0.2)
pS1.ChangeDutyCycle(0)                  #reset
pS2.ChangeDutyCycle(0)                  #reset


servopin1 = 13  #right hand elbow
servopin2 = 6  #left hand elbow
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
pe1 = GPIO.PWM(servopin1,50) #50HZ
pe2 = GPIO.PWM(servopin2,50) #50HZ
pe1.start(0)
pe2.start(0)
time.sleep(3)

#while(True):
for i in range(0,150,5):
#    pe1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    pe2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
for i in range(150,0,-5):
#    pe1.ChangeDutyCycle(2.5 + 10 * i / 180)
    pe2.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
#    p1.ChangeDutyCycle(0)
#    p2.ChangeDutyCycle(0)
#    time.sleep(0.2)
time.sleep(1)
pe1.ChangeDutyCycle(0)                  #reset
pe2.ChangeDutyCycle(0)                  #reset

servoping1 = 5  #right hand gripper
servoping2 = 25  #left hand gripper
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoping1, GPIO.OUT, initial=False)
GPIO.setup(servoping2, GPIO.OUT, initial=False)
pg1 = GPIO.PWM(servoping1,50) #50HZ
pg2 = GPIO.PWM(servoping2,50) #50HZ
pg1.start(0)
pg2.start(0)
time.sleep(2)

#while(True):
for i in range(0,181,5):
    pg1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    pg2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
time.sleep(0.2)
pg1.ChangeDutyCycle(0)                  #reset
pg2.ChangeDutyCycle(0)                  #reset
#!/usr/bin/env python  


import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)  

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
#    p.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
time.sleep(0.2)

#neckup starts
servopinup = 20
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



# arm starts
servopin1 = 16  #right hand base
servopin2 = 12  #left hand base
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
p1 = GPIO.PWM(servopin1,50) #50HZ
p2 = GPIO.PWM(servopin2,50) #50HZ
p1.start(0)
p2.start(0)
time.sleep(2)

#while(True):
for i in range(0,181,5):
    p1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    p2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
for i in range(181,0,-5):
    p1.ChangeDutyCycle(2.5 + 10 * i / 180)
    p2.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
#    p1.ChangeDutyCycle(0)
#    p2.ChangeDutyCycle(0)
#    time.sleep(0.2)
time.sleep(1)


servopin1 = 26  #right hand shoulder
servopin2 = 19  #left hand shoulder
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
pS1 = GPIO.PWM(servopin1,50) #50HZ
pS2 = GPIO.PWM(servopin2,50) #50HZ
pS1.start(0)
pS2.start(0)
time.sleep(2)

#while(True):
for i in range(0,181,5):
    pS1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    pS2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
for i in range(181,0,-5):
    pS1.ChangeDutyCycle(2.5 + 10 * i / 180)
    pS2.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
#    p1.ChangeDutyCycle(0)
#    p2.ChangeDutyCycle(0)
#    time.sleep(0.2)
time.sleep(1)

servopin1 = 13  #right hand elbow
servopin2 = 6  #left hand elbow
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
pe1 = GPIO.PWM(servopin1,50) #50HZ
pe2 = GPIO.PWM(servopin2,50) #50HZ
pe1.start(0)
pe2.start(0)
time.sleep(2)

#while(True):
for i in range(0,181,5):
    pe1.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    pe2.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
#    p1.ChangeDutyCycle(0)                  #reset
#    p2.ChangeDutyCycle(0)                  #reset
#    time.sleep(0.2)
for i in range(181,0,-5):
    pe1.ChangeDutyCycle(2.5 + 10 * i / 180)
    pe2.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
#    p1.ChangeDutyCycle(0)
#    p2.ChangeDutyCycle(0)
#    time.sleep(0.2)
time.sleep(1)



servopin1 = 5  #right hand gripper
servopin2 = 25  #left hand gripper
GPIO.setup(servopin1, GPIO.OUT, initial=False)
GPIO.setup(servopin2, GPIO.OUT, initial=False)
pg1 = GPIO.PWM(servopin1,50) #50HZ
pg2 = GPIO.PWM(servopin2,50) #50HZ
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

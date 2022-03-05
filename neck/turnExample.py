#!/usr/bin/env python  


import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)  

servopin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
p.start(0)
time.sleep(2)

while(True):
  for i in range(0,181,5):
    p.ChangeDutyCycle(2.5 + 10 * i / 180) #set the angle of turning
    time.sleep(0.02)                      #wait for 20ms period to end
    p.ChangeDutyCycle(0)                  #reset
    time.sleep(0.2)
  
  for i in range(181,0,-5):
    p.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
    p.ChangeDutyCycle(0)
    time.sleep(0.2)
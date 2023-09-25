#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

def callback(channel):
        if GPIO.input(channel):
                GPIO.output(23, GPIO.HIGH)
                print("Sound Detected!")
                time.sleep(2)
                GPIO.output(23, GPIO.LOW)
        else:
                print("Sound Detected2!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)

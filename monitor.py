#!/usr/bin/env python

# take readings from LDR and output to stdout, based on https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)


def RCtime (RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(RCpin, GPIO.IN)
	# This takes about 1 millisecond per loop cycle
	while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1
	return reading

lastSignal = False
lastTime = time.time()
power = 0
difference = 0
# calibration of the LDR to detect when the LED is on or off
threshold = 7000
# number of pulses per kwh
meter_constant = 800
seconds_in_an_hour = 3600
while True:
	reading = RCtime(18)
	signal = True
	if reading > threshold:
		signal = False

	if lastSignal == False and signal == True:
		newTime = time.time()
		difference = newTime - lastTime
		power = seconds_in_an_hour / (difference * meter_constant)
		lastTime = newTime
	lastSignal = signal	

	print "%f\t%f\t%f\t%s\t%d\t%f" % (time.time(), difference, power, signal, reading, lastTime) # Read RC timing using pin #18

#http://theatticlight.net/posts/Reading-a-Rotary-Encoder-from-a-Raspberry-Pi/
#http://www.allaboutcircuits.com/projects/building-raspberry-pi-controllers-part-5-reading-analog-data-with-an-rpi/

import RPi.GPIO as GPIO;
import time;
GPIO.VERSION;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);
GPIO.setup(10,GPIO.IN);
GPIO.setup(11,GPIO.IN);
GPIO.setup(12,GPIO.IN);
GPIO.setup(13,GPIO.OUT);
GPIO.setup(17,GPIO.OUT);
buttonAStatus =0;
buttonBStatus =0;
buttonAPin=10;
buttonBPin=11;
knobPinOne = 12;
knobPinTwo = 13;
knobValue = 0;
while True:
	if (GPIO.input(knobPinOne)==False):
		knobValue= knobValue+1;
		#code to update speed of drum beat.
	if (GPIO.input(buttonAPin)==False):
		if(buttonAStatus==0):
		print 'Button A pressed (on)';
		#code to play the sound
		buttonAStatus=1;
		else
		print 'Button A pressed again (off)';
		#code to turn off sound
		buttonAStatus=0;
	else if (GPIO.input(buttonBPin) == False):
		if (buttonBStatus==0):
		print 'Button B pressed (On)';
		#code to play the sound 
		buttonBStatus=1;
		else:
		print 'Button B pressed again (off)';
		#code to turn off sound
		buttonBStatus=0;
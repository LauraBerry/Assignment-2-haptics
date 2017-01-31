#http://theatticlight.net/posts/Reading-a-Rotary-Encoder-from-a-Raspberry-Pi/
#http://www.allaboutcircuits.com/projects/building-raspberry-pi-controllers-part-5-reading-analog-data-with-an-rpi/
#http://www.hertaville.com/interfacing-an-spi-adc-mcp3008-chip-to-the-raspberry-pi-using-c.html
#https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=40515

#http://raspberrypi.stackexchange.com/questions/14505/using-fsr-with-raspberry-pi
#https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-6-buzzer-super-kit-for-raspberrypi.html

import RPi.GPIO as GPIO;
import time;
import os;

GPIO.VERSION;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);
Resistor1Pin=27;
Resistor2Pin=28;
BuzzerPin=11;
GPIO.setup (Resistor1Pin, GPIO.IN);
GPIO.setup(Resistor2Pin, GPIO.IN);
GPIO.setup(BuzzerPin, GPIO.OUT);
while True:
	reading =0;
	if (GPIO.input(Resistor1Pin) == GPIO.LOW):
		GPIO.output(BuzzerPin, GPIO.LOW)
		time.sleep(0.1);
		GPIO.output(BuzzerPin, False);
	if (GPIO.input(Resistor2Pin) == GPIO.LOW):
		GPIO.output(BuzzerPin, GPIO.HIGH);
		time.sleep(0.1);
		GPIO.output(BuzzerPin, False);
#http://theatticlight.net/posts/Reading-a-Rotary-Encoder-from-a-Raspberry-Pi/
#http://www.allaboutcircuits.com/projects/building-raspberry-pi-controllers-part-5-reading-analog-data-with-an-rpi/
#http://www.hertaville.com/interfacing-an-spi-adc-mcp3008-chip-to-the-raspberry-pi-using-c.html
#https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=40515


import RPi.GPIO as GPIO;
import time;
import pyaudio; 
import wave;
GPIO.VERSION;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);
drums = wave.open("ambi-115bpm-1a.wav");
p=pyaudio.PyAudio();
stream = p.open(format = p.get_format_from_width(drums.getsampwidth()), channels= drums.getnchannels(), rate= drums.getframerate(), output = True);
data = drums.readframes(chunk);
#pins for buttons
#GPIO.setup(10,GPIO.IN);
#GPIO.setup(11,GPIO.IN);
#pins for knob
GPIO.setup(12,GPIO.IN);
GPIO.setup(13,GPIO.OUT);
#pin for speaker(?)
#GPIO.setup(17,GPIO.OUT);
buttonAStatus =0;
buttonBStatus =0;
#buttonAPin=10;
#buttonBPin=11;
knobPinOne = 12;
knobPinTwo = 13;
knobValue = 0;
while True:
	readADC();
	stream.write(data);
	data = drums.readframes(chunk);
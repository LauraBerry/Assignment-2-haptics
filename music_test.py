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
GPIO.setup(12,GPIO.IN);
GPIO.setup(13,GPIO.OUT);
knobPinOne = 12;
knobPinTwo = 13;
knobValue = 0;
while True:
	readADC();
	stream.write(data);
	data = drums.readframes(chunk);
	
#or
#import pygame
#pygame.mixer.init()
#pygame.mixer.music.load("myFile.wav")
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy() == True:
#    continue
# NOTE: if this doesn't work use this
	#apt-get update
	#apt-get upgrade
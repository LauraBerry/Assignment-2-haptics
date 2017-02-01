import RPi.GPIO as GPIO;
import time
import pygame;
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


BeepPin = 17;
GPIO.setmode(GPIO.BCM);
GPIO.setup(BeepPin, GPIO.OUT);
from sys import exit;
pygame.mixer.init(48000, -16, 1, 1024);
sndA = pygame.mixer.Sound('A.wav');
sndB = pygame.mixer.Sound('B.wav');
sndC = pygame.mixer.Sound('C.wav');
soundChannelA = pygame.mixer.Channel(1);
soundChannelB = pygame.mixer.Channel(2);
soundChannelC = pygame.mixer.Channel(3);

# Software SPI configuration:
CLK  = 18;
MISO = 23;
MOSI = 24;
CS   = 25;
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI);



# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*2;
    for i in range(2):
        # The read_adc function will get the value of the specified channel (0-1).
        values[i] = mcp.read_adc(i);
    # Print the ADC values.
    if (values[0] >20):
	if (values[1]>5):
		print('0&1');
		time.sleep(3);
		soundChannelA.play(sndC);
		time.sleep(2);
	else:
		print('0')
		time.sleep(3);
		soundChannelA.play(sndA);
		time.sleep(2);

    elif (values[1]>20):
	time.sleep(3);
	soundChannelA.play(sndB);
	time.sleep(2);
	print('1');
    # Pause for half a second.
    #time.sleep(0.3)

GPIO.cleanup();

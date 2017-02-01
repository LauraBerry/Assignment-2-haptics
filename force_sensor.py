import RPi.GPIO as GPIO;
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


BeepPin = 17;
GPIO.setmode(GPIO.BCM);
GPIO.setup(BeepPin, GPIO.OUT);


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)



# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*2
    for i in range(2):
        # The read_adc function will get the value of the specified channel (0-1).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    if (values[0] >20):
	if (values[1]>5):
		print('0&1')
		GPIO.output(BeepPin, GPIO.HIGH);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.LOW);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.HIGH);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.LOW);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.HIGH);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.LOW);
	else:
		print('0')
		GPIO.output(BeepPin, GPIO.HIGH);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.LOW);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.HIGH);
		time.sleep(0.3);
		GPIO.output(BeepPin, GPIO.LOW);

    elif (values[1]>20):
	GPIO.output(BeepPin, GPIO.HIGH);
	time.sleep(0.2);
	GPIO.output(BeepPin, GPIO.LOW);
	print('1')
    # Pause for half a second.
    #time.sleep(0.3)

GPIO.cleanup();

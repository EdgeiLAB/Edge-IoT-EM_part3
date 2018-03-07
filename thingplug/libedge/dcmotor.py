import RPi.GPIO as GPIO
import time

pinEn 		= 12;
pinPositive	= 4;
pinNegative	= 25;

def useDcMotor():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pinEn, GPIO.OUT)
	GPIO.setup(pinPositive, GPIO.OUT)
	GPIO.setup(pinNegative, GPIO.OUT)

def unuseDcMotor():
	GPIO.cleanup()

def rotateDcMotor(direction, delay_sec):
	print("Rotating DcMotor...\n")
	if direction==0:
		GPIO.output(pinPositive, True)
		GPIO.output(pinNegative, False)
	else:
		GPIO.output(pinNegative, True)
		GPIO.output(pinPositive, False)

	GPIO.output(pinEn, True)
	time.sleep(delay_sec)

	GPIO.output(pinEn, False)
	time.sleep(delay_sec);
	print("Stopped DcMotor...\n")



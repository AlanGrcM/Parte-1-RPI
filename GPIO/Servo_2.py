from gpiozero import Servo
import RPi.GPIO as GPIO
from time import sleep
import math
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

while True:
	for i in range(0,360):
		servo.value = math.sin(math.radians(i))
		sleep(0.01)
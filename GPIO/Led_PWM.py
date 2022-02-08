import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #Librerios del GPIO de la raspberrypi4

GPIO.setup(24, GPIO.OUT) #Pin 24 definido como salida

Led= GPIO.PWM(24, 100) #objeto en el pin 24 que gobierne la modulación PWM
Led.start(100)

Led.ChangeDutyCycle( 50 ) #Cambio del ciclo de trabajo 
print("X es un valor entre 0 y 100")

while True:
    for i in range(100,-1,-1):
        Led.ChangeDutyCycle(100 - i)
        time.sleep(0.02)           

    print("Ciclo completo")
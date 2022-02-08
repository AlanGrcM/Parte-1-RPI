import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #Librerios del GPIO de la raspberrypi4

GPIO.setup(18, GPIO.OUT) #Pin 18 definido como salida

Led= GPIO.PWM(18, 100) #objeto en el pin 18 que gobierne la modulación PWM
Led.start(100)

Led.ChangeDutyCycle( 90 ) #Cambio del ciclo de trabajo 


while True:
    for i in range(100,-1,-1):
        Led.ChangeDutyCycle(100 - i)
        time.sleep(0.02)           

    print("Ciclo completo")

 import RPi.GPIO as GPIO
from time import sleep

 GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, False)

def light_LED(number):
    if(number == 13):
        print("LED is high")
        while True: 
           ''' GPIO.output(13, True)'''
    else:
        print("LED are high and low")
        while True:  
            GPIO.output(13, GPIO.HIGH)
            sleep(2)
            GPIO.output(13, GPIO.LOW)
            sleep(2)
def input_port():
    x = input("Input your number : ")
    if(x == '13' or a == '15'):
        number = int(x)
        light_LED(number)
    else:
        print("Please enter valid number between 13 and 15 ")
        input_port()
input_port()

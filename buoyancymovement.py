import RPi.GPIO as GPIO
import time

#initializing the variables
motordown = 5
motorup = 6
switch = 21
plunger_time = 60 #~60 seconds to bottom of syinge
time_to_bottom = 5

#set the modes for the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pin setups
GPIO.setup(motordown, GPIO.OUT)
GPIO.setup(motorup, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

#initial them all to low
GPIO.output(motorup, GPIO.LOW)
GPIO.output(motordown, GPIO.LOW)

def plunger_up():
    while GPIO.input(switch) == True:
        GPIO.output(motorup, GPIO.HIGH)
    GPIO.output(motorup, GPIO.LOW)

def plunger_down():
    if GPIO.input(switch) == False: #check if it's true by software protection
        GPIO.output(motordown, GPIO.HIGH)
        time.sleep(plunger_time)
        GPIO.output(motordown, GPIO.LOW)

def calibration():
    plunger_up()
    time.sleep(2)
    plunger_down()

def be_down():
    plunger_up()
    #not inclusive of the last second
    for descend_time in range(time_to_bottom):
         time.sleep(1)

def be_up():
     plunger_down()
     time.sleep(time_to_bottom)


def be_main():
     calibration()
     while True:
          be_down()
          be_up()

def be_dive(event):
     print('running?')


#running main function
be_main()



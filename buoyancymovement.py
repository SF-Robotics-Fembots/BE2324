import RPi.GPIO as GPIO
import time
import smbus
import ms5837

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

def collect_pressure():
    #initialize the sensor
    print("initializing pressure sensor")
    sensor.init()
    time.sleep(1)
    sensor.read(ms5837.OSR_256)
    sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)
    startup_success = 0 #set to false initially
    while not startup_success:
        try:
            startup()
        except:
            print("failed startup")
            pass
        else:
            startup_success = 1
            time.sleep(0.5)
    while True:
        try:
            sensor.read(ms5837.OSR_256)
        except:
            print("failed reading")
            continue #goes back to the try. it's stubborn like that
        readings = sensor.pressure(ms5837.UNITS_kPa)
        now = datetime.datetime.now()
        print(str(readings) + "   " + now.strftime("%H:%M:%S"))
        break

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
         collect_pressure()
         time.sleep(1)

def be_up():
     plunger_down()
     time.sleep(time_to_bottom)


def be_main():
     calibration()
     

def be_dive():
     print('running?')
     


#running main function
be_main()



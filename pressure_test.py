import ms5837
import smbus
import time

sensor = ms5837.MS5837_02BA(1)

time.sleep(1)

sensor.init()

sensor.read(ms5837.OSR_256)

#set the fluid density
sensor.setFluidDensity(ms5837.DENSITY_FRESHWATER)

#get the most recent pressure in Pa
sensor.pressure(ms5837.UNITS_kPa)

#could get depth using .depth()

#function time!
while True:
	sensor.read(ms5837.OSR_256)
	readings = sensor.pressure(ms5837.UNITS_kPa)
	print(readings)
	time.sleep(2)

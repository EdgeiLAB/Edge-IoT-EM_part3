import smbus
import time

SHT20_I2C_ADDR			= 0x40
SHT20_I2C_CMD_MEASURE_TEMP	= 0xF3
SHT20_I2C_CMD_MEASURE_HUMI	= 0xF5
SHT20_SOFT_RESET		= 0xFE
I2C_BUS_SHT			= 1	
VALUE_MAX 			= 30

def getTempData():
	bus = smbus.SMBus(I2C_BUS_SHT)

	bus.write_byte(SHT20_I2C_ADDR, SHT20_SOFT_RESET)
	time.sleep(0.05)

	IData = [0, 0]

	bus.write_byte(SHT20_I2C_ADDR, SHT20_I2C_CMD_MEASURE_TEMP)
	time.sleep(0.26)

	for i in range(2):
		IData[i] = bus.read_byte(SHT20_I2C_ADDR)

	value = IData[0] << 8 | IData[1]
	temp = -46.85 + 175.72/65536*int(value)
	print("Temp : %.1f\n" %float(temp))

	return temp


from smbus2 import SMBus
from mlx90614 import MLX90614
from time import sleep

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
temp = sensor.get_object_1()+3.5 # +3.5 for calibration
attempt = 0
safe = False

def start():
    while(attempt < 3):
        if(temp > 32.0 and temp < 39.0):
            bus.close()
            safe = True
            break
        else:
            attempt+=1
            sleep(5)
            temp = sensor.get_object_1()+3.5

        if(attempt < 3):
            print("Try again")

    return safe


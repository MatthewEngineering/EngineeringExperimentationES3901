from FinalCodebase.Devices.cam import camera_device

import board
import busio
import time
import digitalio

# UART configuration
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    # Send data over UART
    data = camera_device(1).capture_to_bytes()
    uart.write(data)

    
    # Delay between transmissions
    print('sleeping')
    led.value = False
    time.sleep(1)
    led.value = True
    
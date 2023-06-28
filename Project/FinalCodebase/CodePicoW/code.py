import board
import busio
from FinalCodebase import network
import time
import digitalio

from FinalCodebase.Devices.accelerometer import accelerometer_device
accelerometer = accelerometer_device()


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


# UART configuration
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)
termination_char = b'\xff\xd9'
received_data = bytearray()

def cam(image):
    network.expand_and_send_image("image", image)
    pass

accl_data = []
def save_accl_data(a):
    accl_data.append(a)
    
def send_accl_data():
#     a,x,y,z = accelerometer.main()
#     network.main("x", x)
#     network.main("y", y)
#     network.main("z", z)

    a = accl_data.pop(0)
    network.main("total-acceleration", a)



# led.Value = True
# for _ in range(30):
#     save_accl_data()
#     time.sleep(0.5)
# led.Value = False


def accl():
    a,x,y,z = accelerometer.main()
    network.main("total-acceleration", a)

while True:
    num_datastreams = 2
    led.value = False
    time.sleep(60/(30/num_datastreams))
    led.value = True
    print('sending data')
    
    accl()
    
    # Read the available data from UART
    if uart.in_waiting:
        received_data += uart.read(uart.in_waiting)

    # Check if the termination character is received
    if termination_char in received_data:
        # Extract the data up to the termination character
        image = received_data[:received_data.index(termination_char)] + termination_char # I want the termination character 
        
        # Process the received data
#         print("Received Data:", (image))
#         network.expand_and_send_image("image", image)
        
        cam(image)

        # Remove the processed data from the received_data buffer
        received_data = received_data[received_data.index(termination_char) + len(termination_char):]


    
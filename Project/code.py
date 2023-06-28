import board
import busio
from FinalCodebase import network


# UART configuration
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

# Define the termination character
termination_char = b'\xff\xd9'

received_data = bytearray()

while True:
    # Read the available data from UART
    if uart.in_waiting:
        received_data += uart.read(uart.in_waiting)

    # Check if the termination character is received
    if termination_char in received_data:
        # Extract the data up to the termination character
        data = received_data[:received_data.index(termination_char)] + termination_char
        
        # Process the received data
        print("Received Data:", data)
        network.expand_and_send_image("image", image)

        # Remove the processed data from the received_data buffer
        received_data = received_data[received_data.index(termination_char) + len(termination_char):]


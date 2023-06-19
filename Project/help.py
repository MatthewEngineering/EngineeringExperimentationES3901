import time
import board
import digitalio

# Define the echo and trigger pins
echo_pin = board.GP16
trigger_pin = board.GP17

# Set up the digitalio objects for the echo and trigger pins
echo = digitalio.DigitalInOut(echo_pin)
echo.direction = digitalio.Direction.INPUT
echo.pull = digitalio.Pull.DOWN
trigger = digitalio.DigitalInOut(trigger_pin)
trigger.direction = digitalio.Direction.OUTPUT

# Function to measure distance
def get_distance():
    # Send a pulse to the trigger pin
    trigger.value = True
    time.sleep(0.00001)
    trigger.value = False

    # Measure the duration of the pulse on the echo pin
    start_time = time.monotonic()
    while not echo.value:
        if time.monotonic() - start_time > 0.1:  # Timeout after 0.1 seconds
            return None
    start = time.monotonic()

    while echo.value:
        if time.monotonic() - start_time > 0.1:  # Timeout after 0.1 seconds
            return None
    end = time.monotonic()

    # Calculate the distance based on the duration
    pulse_duration = end - start
    speed_of_sound = 343.2  # Speed of sound in m/s
    distance = (pulse_duration / 2) * (speed_of_sound)

    return distance

# Main loop
while True:
    distance = get_distance()
    if distance is not None:
        print("Distance:", distance, "cm")
    else:
        print("Timeout occurred")
    time.sleep(0.1)
import board
import time
import digitalio

# Define GPIO pins
trigger_pin = digitalio.DigitalInOut(board.GP16)
trigger_pin.direction = digitalio.Direction.OUTPUT
echo_pin = digitalio.DigitalInOut(board.GP17)
echo_pin.direction = digitalio.Direction.INPUT

def measure_distance():
    # Send a trigger pulse
    trigger_pin.value = False
    time.sleep(0.000002)
    trigger_pin.value = True
    time.sleep(0.00001)
    trigger_pin.value = False
    print('A')

    # Wait for the echo pin to go high
    while not echo_pin.value:
        pass
    pulse_start = time.monotonic_ns()
    
    print('B')

    # Wait for the echo pin to go low
    while echo_pin.value:
        pass
    pulse_end = time.monotonic_ns()

    # Calculate distance in centimeters
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration / 58.0

    return distance

if __name__ == "__main__":
    while True:
        print('iterate')
        distance_cm = measure_distance()
        print("Distance: %.2f cm" % distance_cm)
        time.sleep(1)
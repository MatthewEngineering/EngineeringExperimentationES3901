import machine
import time

# Define GPIO pins
trigger_pin = machine.Pin(16, machine.Pin.OUT)
echo_pin = machine.Pin(17, machine.Pin.IN)

def measure_distance():
    # Send a trigger pulse
    trigger_pin.low() 
    time.sleep_us(2)
    trigger_pin.high()
    time.sleep_us(10)
    trigger_pin.low()
    print('A')

    # Wait for the echo pin to go high
    while echo_pin.value() == 0:
        pass
    pulse_start = time.ticks_us()
    
    print('B')

    # Wait for the echo pin to go low
    while echo_pin.value() == 1:
        pass
    pulse_end = time.ticks_us()

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

import time
import board
import digitalio
from FinalCodebase.adafruit_hcsr04 import HCSR04

if __name__ == "__main__":
    with HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16) as sonar:
        try:
            while True:
                print(sonar.distance)
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
    
class distance_device():
    def __init(self):
        self.sonar = HCSR04(trigger_pin=board.GP17, echo_pin=board.GP16)
        
    def get_distance(self):
        return self.sonar.distance
    
    
# class distance_device():
#     def __init__(self, echo_pin=board.GP16, trigger_pin=board.GP17):
#         self.echo = digitalio.DigitalInOut(echo_pin)
#         self.echo.direction = digitalio.Direction.INPUT
#         self.echo.pull = digitalio.Pull.DOWN
#         self.trigger = digitalio.DigitalInOut(trigger_pin)
#         self.trigger.direction = digitalio.Direction.OUTPUT
# 
#     def get_distance(self):
#         self.trigger.value = True
#         time.sleep(0.00001)
#         self.trigger.value = False
# 
#         pulse_start = 0
#         pulse_end = 0
#         timeout_start = time.monotonic()
# 
#         while self.echo.value == False:
#             pulse_start = time.monotonic()
#             if pulse_start - timeout_start > 0.1:  # Timeout after 0.1 seconds
#                 return None
# 
#         while self.echo.value == True:
#             pulse_end = time.monotonic()
#             if pulse_end - timeout_start > 0.1:  # Timeout after 0.1 seconds
#                 return None
# 
#         pulse_duration = pulse_end - pulse_start
#         
#         #print(pulse_duration)
#         speed_of_sound = 343.2  # Speed of sound in m/s
#         distance = pulse_duration * speed_of_sound * 100 / 2  # Convert to centimeters
# 
#         print(distance)
#         return distance
#     
#     def main(self):
#         return self.get_distance()
# 
# if __name__ == "__main__":
#     # Create an instance of the HCSR04 class
#     sensor = distance_device(board.GP16, board.GP17)
# 
#     # Main loop
#     while True:
#         distance = sensor.get_distance()
#         if distance is not None:
#             print("Distance:", distance, "cm")
#         else:
#             print("Timeout occurred")
#         time.sleep(0.1)

import time
import math
import board
import analogio

class accelerometer_device():
    def __init__(self):
        
        # ADXL335 analog pins connected to Pico's ADC channels
        X_PIN = board.A0
        Y_PIN = board.A1
        Z_PIN = board.A2
        
        # Create analog input objects for each axis
        self.x_pin = analogio.AnalogIn(X_PIN)
        self.y_pin = analogio.AnalogIn(Y_PIN)
        self.z_pin = analogio.AnalogIn(Z_PIN)
    
    def smooth_it(self,a,x,y,z):
        cx=-0.127
        cy=-0.5
        cz=-0.0726
        
        return a, x-cx, y-cy, z-cz


    def main(self):
        # Read analog values and convert to acceleration
        x = (self.x_pin.value / 65535 - 0.5) * 20
        y = (self.y_pin.value / 65535 - 0.5) * 20
        z = (self.z_pin.value / 65535 - 0.5) * 20

        # Calculate total acceleration
        total_acceleration = math.sqrt(x**2 + y**2 + z**2)

        # Print the values
#         print("X = %.2fG, Y = %.2fG, Z = %.2fG" % (x, y, z))
#         print("Total acceleration = %.2fG" % total_acceleration)
        
        return self.smooth_it(total_acceleration, x, y, z)



if __name__ == "__main__":
    device = accelerometer_device()
    
    while True:
        total_acceleration, x, y, z = device.main()
        
        print("X = %.2fG, Y = %.2fG, Z = %.2fG" % (x, y, z))
        print("Total acceleration = %.2fG" % total_acceleration)
        
        time.sleep(0.1)


# import board
# import analogio
# import time
# import math
# 
# 
# # setup power
# 
# # powpin = digitalio.DigitalInOut(board.GP6) # Set up the digital output pin
# # powpin.direction = digitalio.Direction.OUTPUT
# # powpin.value = True # Set the pin value to high (3.3V)
# 
# # done setting up power
# 
# 
# 
# def read_acceleration(adc):
#     # Read the ADC value and convert it to voltage
#     voltage = adc.value * 3.3 / 65535
#     # Convert the voltage to acceleration (assuming 3.3V supply)
#     acceleration = (voltage - 1.65) / 0.330
#     return acceleration
#  
# def calculate_tilt_angles(x, y, z):
#     pitch = math.atan2(y, math.sqrt(x**2 + z**2))
#     roll = math.atan2(x, math.sqrt(y**2 + z**2))
#     
#     # Convert the angles to degrees
#     pitch = math.degrees(pitch)
#     roll = math.degrees(roll)
#     
#     return pitch, roll
# 
# class accelerometer_device():
#     def __init__(self):
#         
#         # ADXL335 analog pins connected to Pico's ADC channels
#         X_PIN = board.A0
#         Y_PIN = board.A1
#         Z_PIN = board.A2
#         
#         # Create analog input objects for each axis
#         self.adc_x = analogio.AnalogIn(X_PIN)
#         self.adc_y = analogio.AnalogIn(Y_PIN)
#         self.adc_z = analogio.AnalogIn(Z_PIN)
#         
#     def main(self):
#         # Read the acceleration values from the ADXL335
#         x = read_acceleration(self.adc_x)
#         y = read_acceleration(self.adc_y)
#         z = read_acceleration(self.adc_z)
#         
#         # Calculate the tilt angles
#         pitch, roll = calculate_tilt_angles(x, y, z)
#         
#         info = "X: {:.2f}g, Y: {:.2f}g, Z: {:.2f}g, Pitch: {:.2f}°, Roll: {:.2f}°".format(x, y, z, pitch, roll)
# 
#         # Print the acceleration values and tilt angles
#         # print(info)
#         
#         return info
# 
# if __name__ == "__main__":
#     device = accelerometer_device()
#     while True:
#         info = device.main()        
# 
#         print(info)
#         # network.send_off(feed_name='accelerometer',info=info)
#         
#         # Wait for a while before reading again
#         time.sleep(1)
# 
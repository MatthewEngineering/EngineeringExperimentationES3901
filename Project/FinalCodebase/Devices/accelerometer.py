import board
import analogio
import time
import math

def read_acceleration(adc):
    # Read the ADC value and convert it to voltage
    voltage = adc.value * 3.3 / 65535
    # Convert the voltage to acceleration (assuming 3.3V supply)
    acceleration = (voltage - 1.65) / 0.330
    return acceleration
 
def calculate_tilt_angles(x, y, z):
    pitch = math.atan2(y, math.sqrt(x**2 + z**2))
    roll = math.atan2(x, math.sqrt(y**2 + z**2))
    
    # Convert the angles to degrees
    pitch = math.degrees(pitch)
    roll = math.degrees(roll)
    
    return pitch, roll

class accelerometer_device():
    def __init__(self):
        
        # ADXL335 analog pins connected to Pico's ADC channels
        X_PIN = board.A0
        Y_PIN = board.A1
        Z_PIN = board.A2
        
        # Create analog input objects for each axis
        self.adc_x = analogio.AnalogIn(X_PIN)
        self.adc_y = analogio.AnalogIn(Y_PIN)
        self.adc_z = analogio.AnalogIn(Z_PIN)
        
    def main(self):
        # Read the acceleration values from the ADXL335
        x = read_acceleration(self.adc_x)
        y = read_acceleration(self.adc_y)
        z = read_acceleration(self.adc_z)
        
        # Calculate the tilt angles
        pitch, roll = calculate_tilt_angles(x, y, z)
        
        info = "X: {:.2f}g, Y: {:.2f}g, Z: {:.2f}g, Pitch: {:.2f}°, Roll: {:.2f}°".format(x, y, z, pitch, roll)

        # Print the acceleration values and tilt angles
        # print(info)
        
        return info

if __name__ == "__main__":
    device = accelerometer_device()
    while True:
        info = device.main()        

        print(info)
        # network.send_off(feed_name='accelerometer',info=info)
        
        # Wait for a while before reading again
        time.sleep(1)

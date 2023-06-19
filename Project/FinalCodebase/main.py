from FinalCodebase import network
# from FinalCodebase.Devices import cam
from FinalCodebase.Devices.accelerometer import accelerometer_device
from FinalCodebase.Devices.distance import distance_device

def mainloop(accelerometer, distance, camera):
#     network.main("accelerometer", accelerometer.main())
    network.main("distance", distance.main())

import time
if __name__ == "__main__":
    
    accelerometer = accelerometer_device()
    distance = distance_device()
    
    while True:
        mainloop(accelerometer,distance,0)
        time.sleep(1)


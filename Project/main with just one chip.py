import gc
print(gc.mem_free())

def takepic():
    from FinalCodebase.Devices.cam import camera_device
    return camera_device(3).capture_to_bytes()

def sendpic(image):
    from FinalCodebase import network
    network.expand_and_send_image("image", image)


def main(networked_last):
    if networked_last: # take a picture
        data = takepic()

        with open('image.txt', 'wb') as file:
            file.write(data)

    elif not networked_last: # network
        
        read_data = b''
        with open('image.txt', 'rb') as file:
            read_data = file.read()
        
        read_data = bytearray(read_data)
        print((read_data))
        
        sendpic(read_data)


if __name__ == "__main__":

    import json
    dictionary = dict()

    with open("save.json","r") as file: 
        dictionary = json.load(file)

    networked_last = dictionary['networked_last?']

    if networked_last:
        dictionary['networked_last?'] = 0 # switch
    elif not networked_last:
        dictionary['networked_last?'] = 1 # switch

    print(dictionary)

    try: 
        main(networked_last)
    except Exception as e: 
        # raise e
        print(e)

    with open("save.json","w") as file: 
        json_object = json.dumps(dictionary)
        file.write(json_object)

    import microcontroller
    microcontroller.reset()







# print(gc.mem_free())
# def mainloop(accelerometer, distance, camera):
# 
# #     network.main("accelerometer", accelerometer.main())
# #     network.main("distance", distance.main())
#     network.main("image", camera.capture_to_bytes())
#     
# import time
# if __name__ == "__main__":
#     
# #     accelerometer = accelerometer_device()
# #     distance = distance_device()
#     camera = camera_device()
#     
#     while True:
#         mainloop(0,0,camera)
# #         mainloop(accelerometer,distance,0)
#         time.sleep(10)
# 

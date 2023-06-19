import gc
print(gc.mem_free())
import ssl
print(gc.mem_free())
import binascii
print(gc.mem_free())
import wifi
print(gc.mem_free())
import socketpool
print(gc.mem_free())
# from adafruit_minimqtt.adafruit_minimqtt import MQTT
print(gc.mem_free())

import adafruit_requests
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError


# from adafruit_io.adafruit_io import IO_MQTT
print(gc.mem_free())

print("Connecting to WIFI")
wifi.radio.connect("iPhone123", "123456789")
pool = socketpool.SocketPool(wifi.radio)

import os
aio_username = os.getenv('aio_username')
aio_key = os.getenv('aio_key')
requests = adafruit_requests.Session(pool, ssl.create_default_context())
io = IO_HTTP(aio_username, aio_key, requests)


def send_off(feed_name,info):

    print(f"Captured {len(info)} bytes of jpeg data")

    encoded_data = binascii.b2a_base64(info).strip() # b2a_base64() appends a trailing newline, which IO does not like
    print(f"Expanded to {len(encoded_data)} for IO upload")

    io.send_data(feed_name, encoded_data)

    gc.collect()

    print('done!')
    
if __name__ == "__main__":
    import image_storage
    buffer = image_storage.a
    send_off('image',buffer)
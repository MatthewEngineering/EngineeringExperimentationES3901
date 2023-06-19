import gc
print(gc.mem_free())
from ssl import create_default_context
print(gc.mem_free())
from binascii import b2a_base64
print(gc.mem_free())
from wifi import radio
print(gc.mem_free())
from socketpool import SocketPool
print(gc.mem_free())
from adafruit_requests import Session
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError
print(gc.mem_free())

print("Connecting to WIFI")
radio.connect("iPhone123", "123456789")
pool = SocketPool(radio)

import os
aio_username = os.getenv('aio_username')
aio_key = os.getenv('aio_key')
requests = Session(pool, create_default_context())
io = IO_HTTP(aio_username, aio_key, requests)

print(gc.mem_free())

# unpacked_image = 
def expand_and_send_image(feed_name, compressed_image):
    gc.collect()
    print(f"Captured {len(compressed_image)} bytes of jpeg data")
#     print(f"Expanded to {len(encoded_data)} for IO upload")
    
    io.send_data(feed_name, b2a_base64(compressed_image).strip())
    
    gc.collect()

def main(feed_name,data):
    io.send_data(feed_name, data)
    gc.collect() 
    
if __name__ == "__main__":
#     main('accelerometer','I am a string.')
    print(gc.mem_free())

    from FinalCodebase.image_storage import b
    
    print(gc.mem_free())

    expand_and_send_image('image',b)

    print(gc.mem_free())
    
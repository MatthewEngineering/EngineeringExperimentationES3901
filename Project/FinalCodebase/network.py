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
from adafruit_minimqtt.adafruit_minimqtt import MQTT
print(gc.mem_free())

from adafruit_io.adafruit_io import IO_MQTT
print(gc.mem_free())

print("Connecting to WIFI")
wifi.radio.connect("iPhone123", "123456789")
pool = socketpool.SocketPool(wifi.radio)

print("Connecting to Adafruit IO")
mqtt_client = MQTT(
    broker="io.adafruit.com",
    username="Code780",
    password="aio_XIYX50ED7CiOOZarSVlacSAo0ZOZ",
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)
mqtt_client.connect()
io = IO_MQTT(mqtt_client)

print(gc.mem_free())

def send_off(feed_name,info):

    print(f"Captured {len(info)} bytes of jpeg data")

    print(gc.mem_free())
    encoded_data = binascii.b2a_base64(info).strip() # b2a_base64() appends a trailing newline, which IO does not like
    print(f"Expanded to {len(encoded_data)} for IO upload")

    print(encoded_data)

    print(gc.mem_free())
    io.publish(feed_name, encoded_data)
    print(gc.mem_free())

    gc.collect()
    print(gc.mem_free())

    print('done!')
    
if __name__ == "__main__":
    import image_storage
    buffer = image_storage.a
    send_off('accelerometer',buffer)
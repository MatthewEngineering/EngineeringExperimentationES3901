# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests
import time

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = 'iPhone'
password = '123456789'
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
print(wlan.status())
while max_wait > 0:
    
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    print(wlan.status())


# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
print("1. Querying google.com:")
r = urequests.get("http://www.google.com")
print(r.content)
r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())
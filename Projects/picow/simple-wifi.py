import time
import network
# import rp2 (for country codes)

ssid = 'Wireless Network'
password = 'The Password'
  
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Adjust the Power Saving Mode
wlan.config(pm = 0xa11140)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Return value of cyw43_wifi_link_status codes
#   CYW43_LINK_DOWN (0)
#   CYW43_LINK_JOIN (1)
#   CYW43_LINK_NOIP (2)
#   CYW43_LINK_UP (3)
#   CYW43_LINK_FAIL (-1)
#   CYW43_LINK_NONET (-2)
#   CYW43_LINK_BADAUTH (-3)

# You can also disconnect and then connect to a different wireless network.
# Connecting to the Internet with Raspberry Pi Pico W

# Connect to another network Example
#   wlan.disconnect();
#   wlan.connect('Other Network', 'The Other Password')

# If Wifi doesn't connect try setting the Country Code
#   rp2.country('GB')

# To Get the MAC Address Example
#   import ubinascii
#   mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
#   print(mac)

# Further reading: https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf
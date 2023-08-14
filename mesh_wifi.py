import network
import esp32
import urequests
import time
ssid = "Pacific-Logging"
key = "P@c1f1c-L0gg1ng"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, key)

while not station.isconnected():
    print ('passpassconexion no establecida')
    time.sleep(3)
api_url = "https://dev-5175452510n02u0.api.raw-labs.com/json-programming-heroes"
response = urequests.get(api_url)
if response.status_code == 200:
    data = response.json()
    print (data)

print('Conexión exitosa!')
print(station.ifconfig())

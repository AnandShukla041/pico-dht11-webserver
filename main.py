import network
import socket
import time
import machine
import dht

# DHT11 sensor on GPIO15
sensor = dht.DHT11(machine.Pin(15))

# WiFi credentials
ssid = 'your_SSID'
password = 'your_PASSWORD'

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)

print('Connected to WiFi:', wlan.ifconfig())

# Web page template
def web_page(temp, hum):
    html = f"""<!DOCTYPE html>
<html>
<head>
  <title>Temperature & Humidity</title>
  <meta http-equiv="refresh" content="5">
</head>
<body>
  <h1>Real-Time Temperature & Humidity</h1>
  <p>Temperature: <strong>{temp} °C</strong></p>
  <p>Humidity: <strong>{hum} %</strong></p>
</body>
</html>"""
    return html

# Setup socket web server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Web server listening on http://', addr)

# Main loop
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        response = web_page(temp, hum)
        cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    except OSError as e:
        cl.close()
        print('Connection closed')
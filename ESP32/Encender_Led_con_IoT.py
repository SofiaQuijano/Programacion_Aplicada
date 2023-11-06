import network
from machine import Pin
import socket

# Configuración del LED

led = Pin(13, Pin.OUT)

# Configuración de Wi-Fi
WIFI_SSID = "red"
WIFI_PASS = "clave"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(WIFI_SSID, WIFI_PASS)

while not station.isconnected():
    pass

print("Conexión exitosa")
print(station.ifconfig())

# Función para controlar el LED
def control_led(value):
    if value == b'1':
        led.value(1)  # Enciende el LED
    elif value == b'0':
        led.value(0)  # Apaga el LED

# Configuración del servidor web
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.7', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    
    if 'GET /led?state=1' in request:
        control_led(b'1')
    elif 'GET /led?state=0' in request:
        control_led(b'0')

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nLED controlado"
    conn.send(response)
    conn.close()

import network
import machine

ssid = "red_local"
password = "Contraseña"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

ip_address = wlan.ifconfig()[0]
print("conectado a la red wifi; La IP es: ", ip_address)

pin = machine.Pin(2, machine.Pin.OUT)
pin.on()

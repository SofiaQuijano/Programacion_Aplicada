import network
from machine import Pin, ADC
import time
import urequests

# Configuración del potenciómetro
adc = ADC(Pin(34))

WIFI_SSID = "red"
WIFI_PASS = "clave"
THINGSPEAK_API_KEY = "contraseña_Thingspeak"

# Conexión a Wi-Fi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(WIFI_SSID, WIFI_PASS)

while station.isconnected() == False:
    pass

print("Conexión exitosa")
print(station.ifconfig())

# Función para leer el valor del potenciómetro
def read_potentiometer():
    return adc.read()

# Enviar datos a ThingSpeak
def send_to_thingspeak(value):
    url = "https://api.thingspeak.com/update?api_key={}&field1={}".format(THINGSPEAK_API_KEY, value)
    response = urequests.get(url)
    print("Enviado a ThingSpeak. Respuesta: ", response.text)
    response.close()

# Envío continuo de datos a ThingSpeak
while True:
    pot_value = read_potentiometer()
    print("Valor del potenciómetro:", pot_value)
    send_to_thingspeak(pot_value)
    time.sleep(0.1)

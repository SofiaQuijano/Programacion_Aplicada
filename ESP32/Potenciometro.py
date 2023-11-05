#importar pin y ADC(este es lo que lo pasa de analógico a digital)
from machine import Pin, ADC
import time

#Configuración del potenciometro
#Descripción del pin donde esta conectado el potenciómetro
pot_pin = 34
adc = ADC(Pin(pot_pin))

#Configuración de la lectura
#Leer el valor del potenciometro
def read_potentiometer():
    return adc.read()

#Hacer que la lectura sea continua
while True:
    pot_value = read_potentiometer()
    print("Valor del potenciómetro:", pot_value)
    time.sleep(0.5) 

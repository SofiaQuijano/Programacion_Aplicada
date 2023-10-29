from machine import Pin
import time

p2 = Pin(13, Pin.OUT) 
p2.on()

while(1):
    p2.on()
    time.sleep_ms(1000)  
    p2.off()
    time.sleep_ms(1000)  

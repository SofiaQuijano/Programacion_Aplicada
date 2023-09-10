import time

#Ejemplo de cadena
cadena = "Libreria"

#Por cada letra que se defina, la omite y continua con la palabra
for letra in cadena:
   if letra == 'r':
      continue
   print(letra)
   time.sleep(1)
   

#Copia es una nueva matriz. 
#Vista es una vista de la matriz original
#No se afectan mutuamente

#Ejemplo copy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#Ejemplo view
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

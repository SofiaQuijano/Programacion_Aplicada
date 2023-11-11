#Acceder a un elemento de una matriz
#se puede hacer haciendo referencia a su número de indice
#Inician por 0
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#Mostrará el 6
print(arr[0, 1, 2])

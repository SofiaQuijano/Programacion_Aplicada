# La libreria random permite obtener modos de números aleatorios
# matplotlib biblioteca de generador de gráficos dos dimensiones
import random
from matplotlib import pyplot as plt

numbers_a = range(1, 15)
numbers_b = [random.randint(1, 1000) for i in range(12)]
plt.plot(numbers_a, numbers_b)
plt.show()

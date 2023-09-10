#Input es usado para ingresar un valor
a = input("Ingrese el primer número: ")
a = int(a)
b = input("Ingrese el segundo número: ")
b = float(b)
c = a + b

if a == b:
    print("Los números son iguales")
else:
    print("Los números son diferentes")

#La función type() sirve para saber de que tipo se esta definiendo
print("la primera variable debe de ser un ", type(a))
print("La segunda variable debe de ser un ", type(b))
print("El resultado de la suma de sus números es: ", c)

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferente tipo")

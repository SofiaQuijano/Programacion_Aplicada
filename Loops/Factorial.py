# Uso del factorial en un ciclo while
while True:

    value = int(
        input(" ingresar valor a evaluar: "))
    print("su valor: ", value)
    a = isinstance(value, int)
    if a == True and value > 0:
        fact = 1
        for i in range (1, value + 1):
            fact = fact*i            
        print(f'El factorial de" {value} "es: ', fact)
    else:
        print("Por favor, ingrese un valor entero a evaluar:")

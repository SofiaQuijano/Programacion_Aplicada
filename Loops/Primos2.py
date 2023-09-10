#Saber si número ingresado es primo o no
a = 1
value = input('Ingrese el valor que desea conocer si es primo:')
value = int(value)

#Ciclo
while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
    if conta == 2:
       print(f'{i} Es un númer primo')
       print("\n")
    else:
       print(f'{i} No es un número primo')
       print("\n")

    print('¿Desea conocer otro? Ingrese el número 1')
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese el valor que desea conocer si es primo:')
    value = int(value)

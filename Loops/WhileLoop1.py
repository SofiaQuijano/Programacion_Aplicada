#Uso del break y continue
print("Solo se mostrará números entre 1,6.")
for i in range(1,6):
    while i <= 4:
        i += 1
        print(i)
    break

print("se muestran números en el rango de 1,6 quitando un número cada vez que se reinicie la secuencia, hasta llegar al último número.")
for i in range(1,6):
    while i <= 4:
        i += 1
        print(i)
    continue

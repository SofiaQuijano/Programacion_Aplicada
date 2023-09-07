#En un ciclo for presentar un valor en un rango, != signiica distinto de
for i in range(100, 301):
    if (i%12) != 0:
        continue
    print(i)

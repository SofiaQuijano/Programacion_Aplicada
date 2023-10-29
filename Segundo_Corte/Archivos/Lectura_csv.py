import csv

with open("canciones.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print("Canción 1: {0}, Canción 2: {1}, Canción 3: {2}, Canción 4: {3}".format(row[0], row[1], row[2], row[3]))

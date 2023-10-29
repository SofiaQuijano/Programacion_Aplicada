import csv

canciones = [
    ["3/21", "Amerika", "Quizas", "Señorita"],
    ["Waiting for love", "Crazy", "Vuela", "Flaca"],
    ["Domani Smetto", "Baracutana", "Una come te", "Como estrellas"],
]

with open ("canciones.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter= ",")
    writer (canciones)

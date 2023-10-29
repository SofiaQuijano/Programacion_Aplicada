# Se definen con llaves {}
# {clave : Valor,} 
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(sensors )
#Para mostrar el valor de una clave
print(sensors ["living room"])

#Ejemplo
translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
 
 #Ejemplo
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"],20211005044: 15}
print (children)

#Ejemplo
vacio = {"diomedes":3}
vacio ["mancos" ] = 4
print (vacio)

animals_in_zoo = {"zebras": 8, "monkeys": 12}
animals_in_zoo["dinosaurs"] =  0
print("animales_en_zoo",animals_in_zoo)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)
menu["cheesecake"] = 8
print(menu)

# Añadir una nueva clave
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"gatos": 0}
print("animales_en_zoo",animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)
oscar_winners["Animated Feature"]= "sherk"
print(oscar_winners)
oscar_winners.pop("Animated Feature")
#del oscar_winners["Best Actress"]
print(oscar_winners)

drinks =["expreso","chai","decaf","drip"]
caffeine = [64, 40, 0, 120]
Zipped_drinks =zip(drinks,caffeine)
print(Zipped_drinks)
drinks_to_caffeine ={key:value for key,value in Zipped_drinks}
print(drinks_to_caffeine)

Zipped_drinks=zip(caffeine,drinks)
drinks_to_caffeine ={key:value for key,value in Zipped_drinks}
print(drinks_to_caffeine)

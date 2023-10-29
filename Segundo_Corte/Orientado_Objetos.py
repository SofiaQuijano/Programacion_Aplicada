import math
class Circle :
    pi = 3.14

    def area (self,radius):
        return  Circle.pi * radius** 2
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)

round_room_area = circle.area(11460/2)
print (pizza_area)
print (teaching_table_area)
print (round_room_area)
  
class Circle :
    pi = 3.14

    def __init__(self, diameter):
       print('New cirucle with diameter:{}'.format(diameter))
       
teaching_table = Circle(36) 

class Store:
    pass
alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.Store_name = "alternative Rocks"
isabelles_ices.Store_name = "Isabelles_Ices"
 
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2
  def circumference(self):
    return 2*self.pi*self.radius
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# Area circulo
class CircleArea:
   pi=3.14
   def area2 (self,radius):
      return CircleArea.pi * radius ** 2 
   def perimetro (self,radius):
        return CircleArea.pi*radius*2
perimetro_ = CircleArea()
perimetro_del_dirculo =perimetro_.perimetro(5) 
ciclearea = CircleArea()
area_del_circulo = ciclearea.area2(5) 
print ("el area del circulo fue",area_del_circulo)
print ("el perimetro del circulo es",perimetro_del_dirculo)
pass    

# Area rectangulo 
class Areayperimetro_rectangulo:
    
   def arearec(sefl,base,altura):
    return base* altura 
   def perrec(self,base,altura):
      return base *altura *2
print("por favor ingrese la base de su rectangulo")
base = int(input())
print("por favor ingrese la altura de su rectangulo")
altura = int(input())
area_del_rectangulo = Areayperimetro_rectangulo()
rectangulo_area = area_del_rectangulo.arearec(base,altura)
rectangulo_peri = area_del_rectangulo.perrec(base,altura)
print("area del rectangulo es",rectangulo_area)
print("perimetro del rectangulo",rectangulo_peri)

# Area de cuadrado
class Areayperimetro_cuadrado:
   
   def areacuad(sefl,lado):
    return  lado**2
   def percuad(self,lado):
      return lado*4
print("por favor ingrese un lado de su cuadrado")
lado = int(input())
area_del_cuadrado = Areayperimetro_cuadrado()
cuadrado_area = area_del_cuadrado.areacuad(lado)
cuadrado_peri = area_del_cuadrado.percuad(lado)
print("area del cuadrado es",cuadrado_area)
print("perimetro del cuadrado es",cuadrado_peri)

# Area triangulo rectangulo
class Areayperimetro_triangulorec:
   
   def areatriangrec(self,base,altura):
    return  base*altura/2
   def pertriangrec(self,base,altura,hipotenusa):
      return base+altura+hipotenusa
print("por favor ingrese la base de su triangulo rectangulo")
base = int(input())
print("por favor ingrese la altura de su triangulo rectangulo")
altura = int(input())
hipotenusa = (math.sqrt(base**2+altura**2))
area_del_triangulorec = Areayperimetro_triangulorec()
trirec_area = area_del_triangulorec.areatriangrec(base,altura)
trirec_peri = area_del_triangulorec.pertriangrec(base,altura,hipotenusa)
print("area del triangulo rectangulo es",trirec_area)
print("perimetro del triangulo rectangulo es",trirec_peri)

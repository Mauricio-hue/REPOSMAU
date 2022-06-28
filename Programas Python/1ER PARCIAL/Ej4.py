#Distancia entre 2 puntos del plano cartesiano

import math


print("---Coordenadas del punto A--- ")
AX = int(input("Coordenada X de A: "))
AY = int(input("Coordenada Y de A: "))

print("---Coordenadas del punto B--- ")
BX = int(input("Coordenada X de B: "))
BY = int(input("Coordenada Y de B: "))

#Cálculo de la distancia

D = math.sqrt((AX-BX)**2 + (AY-BY)**2)
print("La distancia entre los 2 puntos es: ", round(D,3))
#Discos de 3.5 necesarios para una copia de seguridad

import math

print("Ingrese el tamaño del disco duro (Gigabytes): ")
GB = float(input("Tamaño: "))

#Conversión a Megabytes
MG = (GB*1024)

#Cálculo del Microdisco
MD = (MG/1.44)

print("Micro discos 3.5 necesarios: ", math.ceil(MD))

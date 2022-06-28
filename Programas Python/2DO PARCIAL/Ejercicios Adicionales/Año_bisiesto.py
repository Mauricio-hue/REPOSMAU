#Desarrolle un algoritmo para determinar si un año leído por teclado es o no bisiesto.

año = int(input("Ingrese el año: "))

    
if año % 4 == 0:
    print("El año es bisiesto")
else: 
    if año % 4 != 0:
        print("El año NO es bisiesto")
    else:
        print("Año no válido")


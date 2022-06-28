#Construya un algoritmo que, dados tres números, muestre el mensaje “IGUALES” si la suma de los dos primeros es 
#igual al otro número y el mensaje “DISTINTOS” en caso contrario.

print ("Ingrese 3 números: ")
num1 = float (input("Ingrese número 1: "))
num2 = float (input("Ingrese número 2: "))
num3 = float (input("Ingrese número 3: "))

suma = num1 + num2;

if suma == num3:
    print("IGUALES")
else:
    print("DISTINTOS")
#Algoritmo, que calcule el tiempo de encuentro de 2 vehículos que van en sentido opuesto, 
#teniendo como datos la distancia inicial que los separa y la velocidad de cada uno.

dist = float (input("Distancia que separa a ambos vehículos (metros): "))


ve1 = float (input("Velocidad del vehículo 1 (m/s): "))
ve2 = float (input("Velocidad del vehículo 2 (m/s): "))
vel = ve1 + ve2;

tiempo = dist / vel;
print ("El tiempo de encuentro es: ",tiempo," segundos")
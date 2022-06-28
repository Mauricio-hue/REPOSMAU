#Entrada de resultados
print("Ingrese las resultados: ")
PG =int(input("Número de partidos ganados: "))
PP =int(input("Número de partidos perdidos: "))
PE =int(input("Número de empates: "))

#Cálculo de puntaje

PPG = (PG*3)
PPP = (PP*0)
PPE = (PE*1)

#Puntaje final
PT = (PPG+PPP+PPE)

print("El puntaje total es: ")
print(PT)
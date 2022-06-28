#Entrada de respuestas
print("Ingrese las respuestas: ")
RC =int(input("Número de respuestas correctas: "))
RI =int(input("Número de respuestas incorrectas: "))
RB =int(input("Número de respuestas en blanco: "))

#Cálculo de puntaje

PRC = (RC*3)
PRI = (RI*-1)
PRB = (RB*0)

#Puntaje final
PF = (PRC+PRI+PRB)

print("El puntaje final es: ")
print(PF)


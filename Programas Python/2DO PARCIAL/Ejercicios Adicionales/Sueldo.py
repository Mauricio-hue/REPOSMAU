#Dado el sueldo de un trabajador, aplique un aumento del 15% si su sueldo es inferior a $1000. 
# Imprima el sueldo que percibirá.

sueldo = float(input("Ingrese su sueldo: "))

aumento = (sueldo * .15); 

if sueldo < 1000:

    paga = (sueldo + aumento)
    print("Aumento aplicado, su nuevo sueldo es: ",paga)

else:
    print ("No aplica descuento")
    print ("Su sueldo es: ",sueldo)


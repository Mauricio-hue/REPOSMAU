#CONDICIONAL ANIDADA

"""
Determinar la etapa de vida de una persona con base a su edad

Niñez 0-12
Adolescencia 13-18
Adulto 19-59
Adulto mayor >=60

"""

edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 12:
    print("Eres niño")
else:
    if edad >= 13 and edad <= 18:
        print("Eres adolescente")
    else:
        if edad >= 19 and edad <= 59:
            print ("Eres Adulto")
        else:
            if edad >= 60 and edad <= 115:
                print("Eres Adulto mayor")
            else:
                print("Edad no válida")


#Diccionario: tipo de colección compuesta por varios elementos que poseen clave - valor.

numeros_telefonicos = {"Contacto 1" : 2711564325, "Contacto 2" : 2711474620, "Contacto 3" : 2711903315}

#items() permite acceder a los valores del diccionario.

for clave,valor in numeros_telefonicos.items():
    print("Clave", clave, "Valor", valor)
    #print("Clave: " + clave + " Valor: " + str(valor))
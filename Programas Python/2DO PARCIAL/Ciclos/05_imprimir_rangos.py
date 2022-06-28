#range() imprimir valores de un rango.

#Si range() recibe un parámetro, se interpreta como el número en donde termina el rango -1

for x in range(5):
    print(x)

#Si range() recibe 2 parámetros, se interpreta como:
#El primer parámetro es el inicio.
#El segundo parámetro es donde termina el rango -1.

for y in range(1,11):
    print(y)

#Si range() recibe 3 parámetros, se interpreta como:
#El primer parámetro es el inicio.
#El segundo parámetro es donde termina el rango -1.
#El tercer parámetro es el incremento.

for z in range(10,51,5):
    print(z)
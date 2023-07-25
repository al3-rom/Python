# Hacer que el numero introducido por el usuario se imprima de uno a uno
# (Ejemplo 2325)
#2
#3
#2
#5

numero = input("Introduce un numero de cuatro cifras: ") # string

# Mostrar el numero componente a componente por pantalla

'''
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
'''

print(numero[0] + '\n' + numero[1] + '\n' + numero[2] + '\n' + numero[3])

# Hacer que el numero que vamos a introducir resulta de leer de derecha a izquierda (4323 --> 3234)

numero = input("Pun un numero de cuatro cifras: ")
# num_inverso = (num[3] + num[2] + num[1] + num[0])

print(numero[::-1]) # Empieza desde el final hasta el comienzo
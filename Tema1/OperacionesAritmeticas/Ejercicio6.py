#
# Hacer que muestre por pantalla el resultado de la operación aritmética: 
#
#------
#
#     2  
#(3+2)
#--/--
#(2x5)
#
#------
#

operacion = ((3+2)/(2*5)) **2
print(operacion)

# Escrir un programa que lea un entero positivo, n, introducido por el usuario y después
# muestrar por pantalla el resultado de la siguiente operación:
#
#  n(n+1)/2
#

n = float(input("Pon un numero: "))
operacion = n * (n+1) / 2
print(operacion)

# Pedir al usuario dos números enteros y mostrar por pantalla los
# números de entrada, el cociente y el resto. 

num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa otro numero entero: "))

# Calcular el cociente y el resto

cociente = num1 // num2 
resto = num1 % num2

# Mostrar por pantall numero dde entrada, cociente y resto

print("Los numeros de entrada son : ", num1, "y", num2, " , el cociente es: ", cociente, " , y resto es: ", resto)


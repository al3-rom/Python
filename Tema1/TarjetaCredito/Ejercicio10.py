# Recibir por pantalla un numero de tarjeta de credito e imprimir por pantalla todos
# los caracteres en forma de asterisco salvo los últimos cuatro
# (Ejemplo: 4323 2142 3211 4523 = **** **** **** 4523)

tarjeta = input("Pon un numero de tajeta de credito(16 numeros): ")


# print("**** **** ****", tarjeta[12:16])
longitud = len(tarjeta)

print("*" * (longitud - 4) + tarjeta[longitud-4:longitud])

#Crear un script que introduzca Euros a dolares 1 EU = 1.2$
#La cantidad tiene que poner usuario

# Pido una cantidad de dinero
DineroTxt = input("Pon una cantidad de dinero ")
DineroNum = float(DineroTxt)

# Pongo que un $ vale 1.2
Dolar = 1.2

#Hago en dolar
EnDolar = DineroNum * Dolar

#El resultado
print(DineroNum, "Euros son :", EnDolar, "$")

# La casa se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
# recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
# dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
# forma que quede claro para el usuario. 

# La cantidad que se queda la casa de cambios
tasasGestion = EnDolar * 0.1

# La cantidad de dólares que recibirá el usuario
dolaresRecibidos = EnDolar - tasasGestion

# Imprimir el desglose de la operacion
print("Monto ingresado: ", DineroNum, "euros")
print("Cambio en dolares: ", EnDolar, "$")
print("La tasa de gestion: ", tasasGestion, "$")
print("La cantidad que recibe el usuario: ", dolaresRecibidos, "$")

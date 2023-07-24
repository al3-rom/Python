#Crear un script que introduzca Euros a dolares 1 EU = 1.2$
#La cantidad tiene que poner usuario


DineroTxt = input("Pon una cantidad de dinero ")
DineroNum = int(DineroTxt)

Dolar = 1.2

SumaTotal = DineroNum * Dolar

print(DineroNum, "Euros, son :", SumaTotal, "$")


# La casa se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
# recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
# dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
# forma que quede claro para el usuario. 


# Monto recibido
ImpuestoEuro = DineroNum * 0.1
print("Monto recibido: ", ImpuestoEuro, " Euros")

# Traduzco monto recibido, de euros a dolares
ImpuestoEuro = ImpuestoEuro * Dolar
print("Monto recibido en dolares: ", ImpuestoEuro, "$")

#El cambio en dolares
ElCambio = SumaTotal - ImpuestoEuro

print("El cambio es :", ElCambio, "$")

##No entiendo el ejercicio, acabo luego :(













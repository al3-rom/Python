# Pedir nombre por pantalla, imprimir un saludo
nombre = input('Pon tu nombre! ')

print("Hola", nombre)

horasJobSt = input("Pon tus horas trabajadas(40): ")
horasJob = int(horasJobSt)

dineroHoraSt = input("Dinero ganado por hora: ")
dineroHora = int(dineroHoraSt)

# Calculo salario semanal
SalarioSemana = dineroHora * horasJob

# Calculo salario mensual( mas o menos )
SalarioMes = SalarioSemana * 4

# Calculo salario anual
SalarioAnual = SalarioMes * 12

# Imprimo por pantalla 
print(nombre, "tienes unas ganancias anuales de: ", SalarioAnual, "euros")

# Hago gastos semanales
gastosSemanalSt = input("Tus gastos semanales: ")
gastosSemanal = int(gastosSemanalSt)

# Gasto anual
gastoAnual = gastosSemanal * 4 * 12

ahorroAnual = SalarioAnual - gastoAnual

print("Tus gastos anuales son: ", gastoAnual, "euros, tus ahorros anuales son: ", ahorroAnual)










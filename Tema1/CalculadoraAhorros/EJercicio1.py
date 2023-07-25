# Pedir nombre por pantalla, imprimir un saludo.
nombre = input('Pon tu nombre!: ')

print("Hola", nombre, "!")

horasJobSt = input("Pon tus horas trabajadas(40): ")
horasJob = int(horasJobSt)

dineroHoraSt = input("Dinero ganado por hora: ")
dineroHora = int(dineroHoraSt)

# Calculo salario semanal
salarioSemana = dineroHora * horasJob

# Calculo salario anual
salarioAnual = salarioSemana * 52 # 52 - son semanas en el año

# Imprimo por pantalla 
print(nombre, "tienes unas ganancias anuales de: ", salarioAnual, "euros")

# Hago gastos semanales
gastosSemanalSt = input("Tus gastos semanales: ")
gastosSemanal = float(gastosSemanalSt)

# Gasto anual
gastoAnual = gastosSemanal * 52

ahorroAnual = salarioAnual - gastoAnual

print("Tus gastos anuales son: ", gastoAnual, "euros, tus ahorros anuales son: ", ahorroAnual)










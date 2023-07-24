# En un restaurante el menú consta de las siguientes opciones:
# Ensalada mixta ———————— 12 EU
# Sopa de pescado ——————— 10 EU
# Dorada al horno ———————— 18 EU
# Arroz al curry ————————— 14 EU
# Lasaña de carne ——————— 15 EU
# Brownie de chocolate ————— 8 EU
# Helado ——————————— 6 EU
# Refrescos —————————— 5,5 EU
# Café ———————————— 3,5 EU
# Escribe la cantidad de cada alimento consumido y que calcule e imprima el total
# de la cuenta.


Sopa_pescado = 10 
Dorada_horno = 18 
Arroz_curry = 14 
Lasaña_carne = 15
Brownie_chocolate = 8 
Helado = 6 
Refrescos = 5,5
Café = 3,5

repetir = True

SumarSopa = 0
SumarDorada = 0
SumarArroz = 0
SumarLasaña = 0
SumarBrownie = 0
SumarHelado = 0
SumarRefrescos = 0
SumarCafe = 0

if repetir == True:
    print("Que quieres tomar?")
if Sopa_pescado: 
    SumarSopa = SumarSopa + 1
elif Dorada_horno:
    SumarDorada = SumarDorada + 1
elif Arroz_curry:
    SumarArroz = SumarArroz + 1
elif Lasaña_carne:
    SumarLasaña = SumarLasaña + 1
elif Brownie_chocolate:
    SumarBrownie = SumarBrownie + 1
elif Helado: 
    SumarHelado = SumarHelado + 1
elif Refrescos:
    SumarRefrescos = SumarRefrescos + 1
elif Café:
    SumarCafe = SumarCafe + 1
    print("Quieres algo mas? (True o False)")
    repetir = input()

    ## No se que hacer



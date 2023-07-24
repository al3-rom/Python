# Hannah Neise: 8 minutos 3 segundos y 10 centésimas
# Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
# Kimberley Bos: 9 minutos 14 segundos y 3 centésimas

# Pedir tiempos para cada uno de los finalistas
HannahMinSt = input("Pon minutos de Hannah: ")
HannahSegSt = input("Segundos de Hannah: ")
HannahCentSt = input("Centesimas de Hannah: ")

JackieMinSt = input("Pon minutos de Jackie: ")
JackieSegSt = input("Segundos de Jackie: ")
JackieCentSt = input("Centesimas de Jackie: ")

KimberMinSt = input("Pon minutos de Kimber: ")
KimberSegSt = input("Segundos  de Kimber: ")
KimberCentSt = input("Centesimas de Kimber: ")

#Convierto en un numero entero

HannahMin = int(HannahMinSt)
HannahSeg = int(HannahSegSt)
HannahCent = int(HannahCentSt)

JackieMin = int(JackieMinSt)
JackieSeg = int(JackieSegSt)
JackieCent = int(JackieCentSt)

KimberMin = int(KimberMinSt)
KimberSeg = int(KimberSegSt)
KimberCent = int(KimberCentSt)




# Convertir los tiempos de minutos-segundos-centésimas a segundos

HannahSeg = HannahSeg + (HannahMin * 60) + (HannahCent/100)

JackieSeg = JackieSeg + (JackieMin * 60) + (JackieCent/100)

KimberSeg = KimberSeg + (KimberMin * 60) + (KimberCent/100)

# La pista = 100 metros, calcular la velocidad media de cada uno de ellos en
# metros por segundo. 

VelHannahSeg = 100/HannahSeg

VelJackieSeg = 100/JackieSeg

VelKimberSeg = 100/KimberSeg

# Imprimir resultados

print("Los segundos de Hannah son: ", HannahSeg, ", la velocidad media: ", VelHannahSeg, "(m/s) metros/segundo")
print("Los segundos de Jackie son: ", JackieSeg, ", la velocidad media: ", VelJackieSeg, "(m/s) metros/segundo")
print("Los segundos de Kimber son: ", KimberSeg, ", la velocidad media: ", VelKimberSeg, "(m/s) metros/segundo")






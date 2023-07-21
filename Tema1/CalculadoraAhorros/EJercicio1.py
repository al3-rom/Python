# Almacenar el string ‘estas usando python’ en una variable y mostar por pantalla


var1 = "Estas usando Python!"

print(var1)

# Preguntar el nombre del usuario y mostrar por pantalla

nombre = input()


mensaje = "Hola " + nombre+ ", " + var1

print(mensaje)

# Usar una funcion para que salga todo en mayusculas 

mensaje = mensaje.upper()

print(mensaje)



# Ahora una funcion para que salga todo en minusculas

mensaje = mensaje.lower()

print(mensaje)


# Hacer que el nombre del usuario salga bien( JUaN = Juan)

nombre = input().capitalize()

print(nombre)

# Hacer que el nombre del usuario salga bien( Ju.an = Juan)

nombre = input().replace(".", "")

print(nombre)

# Consigue que el mensaje final sea: ‘¡Hola, <Nombre>, estas usando Python!’

mensaje = mensaje.title()

print(mensaje)
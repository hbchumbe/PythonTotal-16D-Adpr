color_auto = "rojo"
matricula = "1234-ABC"  
print("Mi auto es {} y de matrícula {}".format(color_auto,matricula))
print(f"Mi auto es {color_auto} y de matrícula {matricula}")

# Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro 
# de la siguiente frase:
# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación),
# es muy importante para llegar al resultado correcto.
nombre_asociado = "Juan Pérez"
numero_asociado = "A12345"
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado, numero_asociado))
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

# Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación),
# es muy importante para llegar al resultado correcto.
puntos_nuevos = 150
puntos_totales = 1200
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos, puntos_totales))
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos") 

# Práctica Formatear Cadenas 3
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# En esta ocasión, la cantidad de puntos acumulados (totales)
# será igual a los puntos_anteriores más los puntos_nuevos.
puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores+puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos") 

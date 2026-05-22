# Práctica Control de Flujo 1
# Utilizando las variables num1 y num2, que se alimentan con el input 
# del usuario (tal como en el código ya proporcionado):

# Crea una estructura de control de flujo que compare los valores 
# de las variables, y arroje un resultado de acuerdo al caso:

# "num1 es mayor que num2"

# "num2 es mayor que num1"

# "num1 y num2 son iguales"

# Debes mostrar en pantalla el valor de las variables ingresadas en 
# lugar de num1 y num2.

# Aclaración:

# 1. No deben imprimirse strings adicionales a la respuesta del usuario.

# 2. Los ejercicios que contienen el la función input() deben ser probados 
# con el botón: "Ejecutar pruebas".  Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
if num1 > num2:
    print(f"{num1} es mayor que {num2}")   
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
#

# Práctica Control de Flujo 2
# Las leyes de un país establecen que un adulto puede conducir
# si tiene licencia para hacerlo, y para optar por una licencia 
# para conducir, debe de tener 18 años o más.

# Crea una estructura condicional para verificar si una persona 
# de 16 años sin licencia puede conducir, y muestra el resultado 
# que corresponda en pantalla:

# "Puedes conducir"

# "No puedes conducir aún. Debes tener 18 años y contar con una licencia"

# "No puedes conducir. Necesitas contar con una licencia"

# Utiliza la base de código ya proporcionada para plantear la estructura
# de control de flujo apropiada y verificar dichas condiciones.
edad = 16
tiene_licencia = False
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 and not tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")  

# 
# Práctica Control de Flujo 3
# Para acceder a un determinado puesto de trabajo, el candidato debe 
# ser capaz de programar en Python y tener conocimientos de inglés.

# Crea una estructura condicional para evaluar a un candidato dadas 
# estas condiciones, y muestra el mensaje correspondiente en pantalla:

# "Cumples con los requisitos para postularte"

# "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

# "Para postularte, necesitas tener conocimientos de inglés"

# "Para postularte, necesitas saber programar en Python"

# Utiliza la base de código ya proporcionada para plantear la estructura
# de control de flujo apropiada y verificar dichas condiciones. Evalúa 
# a un candidato que sabe inglés, pero no programa en Python.
habla_ingles = True
sabe_python = False  
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:   
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

# 
# 
# Práctica Loop For 1
# Utilizando loops For, saluda a todos los miembros de una clase, 
# imprimiendo "Hola" + su nombre.

# Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"Hola {alumno}")

# 
# 
# Práctica Loop For 2
# Dada la siguiente lista de números, realiza la suma de todos los números
#  utilizando loops For y almacena el resultado de la suma en una 
# variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
print(sum(lista_numeros))
suma_numeros=0
for numero in lista_numeros:
    suma_numeros += numero
print(suma_numeros)

suma_numeros2 = 0
for i in range(0, len(lista_numeros)):
    suma_numeros2 += lista_numeros[i]
print(suma_numeros2)

# 
#
# Práctica Loop For 3
# Dada la siguiente lista de números, realiza la suma de todos los números 
# pares e impares* por separado en las variables suma_pares y suma_impares 
# respectivamente:

# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# *Recordando de los días anteriores: el módulo (o resto) de un número
# dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

# num % 2 == 0 (valores pares)

# num % 2 == 1 (valores impares)
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print(suma_pares)
print(suma_impares)
#
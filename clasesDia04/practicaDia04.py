from random import *

nombre = input("¿Cuál es tu nombre? ")
numero_random = randint(1, 100)
#print(numero_random)  # Esto es para probar el código, puedes eliminarlo después de verificar que funciona correctamente.
print(f"Hola, {nombre}! , he pensado un numero entre el 1 y el 100, ¿puedes adivinarlo?")

intentos = 0
while intentos < 8:
    respuesta = int(input("Escribe tu respuesta: "))
    intentos += 1

    if respuesta < 1 or respuesta > 100:
        print("El número está fuera del rango permitido, inténtalo de nuevo.")
    elif respuesta < numero_random:
        print("Tu respuesta es menor al número secreto.")
    elif respuesta > numero_random:
        print("Tu respuesta es mayor al número secreto.")
    else:
        print(f"¡Acertaste {nombre}! Te tomó {intentos} intentos. El número era {numero_random}.")
        break
else:
    print(f"Lo siento, se agotaron los intentos. El número era {numero_random}.")

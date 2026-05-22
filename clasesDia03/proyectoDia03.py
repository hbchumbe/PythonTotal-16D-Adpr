mi_texto = input ("Ingrese un texto: ").lower()
# print(mi_texto.lower()) # Convierte el texto a minúsculas
'''
En Python, los sets (conjuntos) son colecciones de elementos únicos y sin un orden específico. Son increíblemente útiles porque te permiten realizar operaciones matemáticas de conjuntos (como unir, intersectar o diferenciar) de forma nativa y superrápida
'''
print("gracias por ingresar el texto ahora ingrese las letras:")
lista_letras = []
lista_letras.append(input("Ingrese la primera letra: ").lower())
lista_letras.append(input("Ingrese la segunda letra: ").lower())
lista_letras.append(input("Ingrese la tercera letra: ").lower())
print(lista_letras)
# Cuenta cuántas veces aparece la primera letra en el texto
print("Ahora se mostrará cuántas veces aparece cada letra en el texto:")
print(mi_texto.count(lista_letras[0]) )
print(mi_texto.count(lista_letras[1]) )
print(mi_texto.count(lista_letras[2]) )
texto_lista = mi_texto.split() # Convierte el texto en una lista de palabras
print("cantidad de palabras en el texto : \n" + str(len(texto_lista))) # Imprime la cantidad de palabras en el texto
print("la primera leta es : " + mi_texto[0] )
print("la última letra es : " + mi_texto[-1])
texo_inve= mi_texto[::-1] # Invierte el texto

print("el texto invertido es : \n" + texo_inve)
lista_inve= texto_lista[::-1] # Invierte la lista de palabras
print("la lista de palabras invertida es : \n" + str(lista_inve))
print("aparece python " + str(mi_texto.count("python")) + " veces en el texto") # Cuenta cuántas veces aparece la palabra "python" en el texto  


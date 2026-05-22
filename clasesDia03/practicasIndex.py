mi_texto = "esta es un Prueba de texto o pruebita de textito 23"
resultado = mi_texto.index("p")
print(len(mi_texto))
print(resultado)
resultado = mi_texto.index("4",0, len(mi_texto) )
print(resultado)


# Práctica Método Index() 1
# Encuentra y muestra en pantalla qué caracter
# ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[4])


# Práctica Método Index() 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son.

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado= frase.index("práctica")
print (resultado)


# Práctica Método Index() 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)
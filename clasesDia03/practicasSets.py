a = {'Python', 'JavaScript', 'C++',3,5}
b = {4,'JavaScript', 'Go', 'Java',3}
c= a.intersection(b)
print(c) # Devuelve los elementos que están en ambos conjuntos a y b
c=a.union(b)
print(c) # Devuelve un nuevo conjunto que contiene todos los elementos de a y b,
print(a.difference(b)) # Devuelve los elementos que están en a pero no en b

a.difference_update(b) # Elimina los elementos de a que también están en b
print(a) # Imprime el conjunto a después de la diferencia actualizada

# Práctica Sets 1
# Une los siguientes sets en uno solo, llamado mi_set_3:

mi_set_1 = {1, 2, "tres", "cuatro"}

mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set1.union(mi_set_2)
print(mi_set_3)


# Práctica Sets 2
# Elimina un elemento al azar del siguiente set, utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)


# Práctica Sets 3
# Agrega el nombre Damián al siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)

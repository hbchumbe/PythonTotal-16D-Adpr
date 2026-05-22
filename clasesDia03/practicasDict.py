producto = {
    "nombre": "Laptop HP",
    "precio": 850,
    "stock": 23,
    "disponible": True
}
persona = dict(nombre="Ana", edad=30, ciudad="Madrid", ocupacion="Ingeniera", sueldo=5000)

print(producto)
print(persona)  
print(producto["nombre"])
print(persona["edad"])
print(producto.get("marca", "Sin marca"))

producto["marca"] = "HP"
print(producto)
print("---")
print(producto.keys())
print(producto.values())
print(len(producto))
print("stock" in producto)
producto.update({"stock": 10})
print(producto)
producto["stock"] = 23
print(producto)

# Práctica Diccionarios 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información 
# de una persona:

# nombre: Karen

# apellido: Jurgens

# edad: 35

# ocupacion: Periodista

# Los nombres de las claves y valores deben ser iguales a la consigna.
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# Práctica Diccionarios 2
# Crea una función print que devuelva del segundo item de la lista llamada points2,
# dentro del siguiente diccionario.

# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para 
# devolver el valor que se encuentre en esa misma posición. Para ello, deberás 
# hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},
            "puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1] )

# Ejemplo de iteración sobre diccionario anidado
print("\n--- Iteración del diccionario anidado ---")
for clave_exterior, valor_exterior in mi_dict.items():
    print(f"Sección: {clave_exterior}")
    
    # Verificamos si el valor es otro diccionario para iterar sobre él
    if isinstance(valor_exterior, dict):
        for clave_interior, valor_interior in valor_exterior.items():
            print(f"  Clave: {clave_interior}, Valor: {valor_interior}")
    else:
        print(f"  Valor directo: {valor_exterior}")


# Práctica Diccionarios 3
# Actualiza la información de nuestro diccionario llamado mi_dic 
# (reasignando nuevos valores a las claves según corresponda),
# y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

# nombre: Karen

# apellido: Jurgens

# edad: 36

# ocupacion: Editora

# pais: Colombia

# para ello, no debes cambiar la línea de código ya escrita, 
# sino actualizar los valores mediante métodos de diccionarios.
# mi_dic["edad"] = 36
# mi_dic["ocupacion"] = "Editora"
# mi_dic["pais"] = "Colombia"
print(mi_dic)
mi_dic.update({"edad": 36, "ocupacion": "Editora", "pais": "Colombia"})
print(mi_dic)
print(type(mi_dic))

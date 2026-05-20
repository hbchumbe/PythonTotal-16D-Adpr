
vendedor = input("Ingrese el nombre del vendedor: ")
ventas = float(input("Ingrese el monto total de ventas: "))
comision = 0.05 * ventas
print(f"El vendedor {vendedor} ha ganado una comisión de: ${comision:.2f}") 
comision = round(0.05 * ventas)
print(f"El vendedor {vendedor} ha ganado una comisión de: {comision}") 


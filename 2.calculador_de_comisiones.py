nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tu ventas: "))
comision = round(ventas * 0.13, 2)

print(f"Genial {nombre}. Este mes ganaste {comision}")
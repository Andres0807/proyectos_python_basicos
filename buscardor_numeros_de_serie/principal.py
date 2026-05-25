import os
import re
import time
import math
from datetime import datetime

# Ruta de la carpeta raíz (dentro de la misma carpeta del programa)
ruta = os.path.join(os.getcwd(), "Mi_Gran_Directorio")


# Expresión regular
patron = r"N\w{3}-\d{5}"

# Lista para guardar resultados
resultados = []

# Tiempo inicial
inicio = time.time()


# Recorrer carpetas y archivos
for carpeta, subcarpetas, archivos in os.walk(ruta):

    for archivo in archivos:

        ruta_archivo = os.path.join(carpeta, archivo)

        with open(ruta_archivo, "r", encoding="utf-8") as f:

            texto = f.read()

            buscar = re.search(patron, texto)

            if buscar:
                resultados.append((archivo, buscar.group()))


# Tiempo final
fin = time.time()

duracion = math.ceil(fin - inicio)


# Fecha actual
fecha = datetime.now().strftime("%d/%m/%y")


# Mostrar resultados
print("-" * 52)
print(f"Fecha de búsqueda: {fecha}\n")

print("ARCHIVO\t\tNRO. SERIE")
print("-------\t\t----------")

for archivo, numero in resultados:
    print(f"{archivo}\t{numero}")

print(f"\nNúmeros encontrados: {len(resultados)}")
print(f"Duración de la búsqueda: {duracion} segundos")
print("-" * 52)
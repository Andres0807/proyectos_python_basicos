import os
from pathlib import Path

# Carpeta principal donde se guardarán las recetas

BASE_DIR1 = Path.home()
BASE_DIR = Path(BASE_DIR1, "Recetaspy")

# Crear carpeta principal si no existe
BASE_DIR.mkdir(exist_ok=True)


# =========================
# FUNCIONES
# =========================

def mostrar_menu():
    print("\n===== MENÚ DE RECETAS =====")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")


def listar_categorias():
    categorias = [carpeta.name for carpeta in BASE_DIR.iterdir() if carpeta.is_dir()]

    if not categorias:
        print("No hay categorías creadas.")
        return []

    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")

    return categorias


def elegir_categoria():
    categorias = listar_categorias()

    if not categorias:
        return None

    try:
        opcion = int(input("\nElige una categoría: "))
        return categorias[opcion - 1]
    except:
        print("Opción inválida.")
        return None


def listar_recetas(categoria):
    ruta_categoria = BASE_DIR / categoria

    recetas = [archivo.stem for archivo in ruta_categoria.glob("*.txt")]

    if not recetas:
        print("No hay recetas en esta categoría.")
        return []

    print("\nRecetas disponibles:")
    for i, receta in enumerate(recetas, start=1):
        print(f"{i}. {receta}")

    return recetas


# =========================
# OPCIÓN 1 - LEER RECETA
# =========================

def leer_receta():
    categoria = elegir_categoria()

    if not categoria:
        return

    recetas = listar_recetas(categoria)

    if not recetas:
        return

    try:
        opcion = int(input("\nElige una receta: "))
        receta = recetas[opcion - 1]

        ruta_receta = BASE_DIR / categoria / f"{receta}.txt"

        print("\n===== CONTENIDO DE LA RECETA =====\n")

        with open(ruta_receta, "r", encoding="utf-8") as archivo:
            print(archivo.read())

    except:
        print("Opción inválida.")


# =========================
# OPCIÓN 2 - CREAR RECETA
# =========================

def crear_receta():
    categoria = elegir_categoria()

    if not categoria:
        return

    nombre_receta = input("\nNombre de la nueva receta: ")

    contenido = input("Escribe el contenido de la receta:\n")

    ruta_receta = BASE_DIR / categoria / f"{nombre_receta}.txt"

    with open(ruta_receta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print("Receta creada correctamente.")


# =========================
# OPCIÓN 3 - CREAR CATEGORÍA
# =========================

def crear_categoria():
    nombre_categoria = input("\nNombre de la nueva categoría: ")

    ruta_categoria = BASE_DIR / nombre_categoria

    if ruta_categoria.exists():
        print("La categoría ya existe.")
    else:
        ruta_categoria.mkdir()
        print("Categoría creada correctamente.")


# =========================
# OPCIÓN 4 - ELIMINAR RECETA
# =========================

def eliminar_receta():
    categoria = elegir_categoria()

    if not categoria:
        return

    recetas = listar_recetas(categoria)

    if not recetas:
        return

    try:
        opcion = int(input("\nElige la receta a eliminar: "))
        receta = recetas[opcion - 1]

        ruta_receta = BASE_DIR / categoria / f"{receta}.txt"

        os.remove(ruta_receta)

        print("Receta eliminada correctamente.")

    except:
        print("Opción inválida.")


# =========================
# OPCIÓN 5 - ELIMINAR CATEGORÍA
# =========================

def eliminar_categoria():
    categoria = elegir_categoria()

    if not categoria:
        return

    ruta_categoria = BASE_DIR / categoria

    try:
        os.rmdir(ruta_categoria)
        print("Categoría eliminada correctamente.")
    except:
        print("No se puede eliminar la categoría.")
        print("Asegúrate de que esté vacía.")


# =========================
# PROGRAMA PRINCIPAL
# =========================

while True:
    mostrar_menu()

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        leer_receta()

    elif opcion == "2":
        crear_receta()

    elif opcion == "3":
        crear_categoria()

    elif opcion == "4":
        eliminar_receta()

    elif opcion == "5":
        eliminar_categoria()

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
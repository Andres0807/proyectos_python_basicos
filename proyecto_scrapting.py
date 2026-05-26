from bs4 import BeautifulSoup
import requests

# Lista única para guardar todos los títulos
titulos_bien_puntuados = []

# Loop para recorrer las 50 páginas
for pagina in range(1, 51):

    # Armar la URL dinámica
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"

    # Hacer request
    resultado = requests.get(url)

    # Crear la sopa
    sopa = BeautifulSoup(resultado.text, "html.parser")

    # Buscar todos los libros de la página
    libros = sopa.select("article.product_pod")

    # Recorrer cada libro
    for libro in libros:

        # Obtener clases del rating
        estrellas = libro.select_one("p.star-rating")
        clases = estrellas.get("class")

        # Verificar si tiene 4 o 5 estrellas
        if "Four" in clases or "Five" in clases:

            # Extraer título
            titulo = libro.h3.a["title"]

            # Guardar en la lista general
            titulos_bien_puntuados.append(titulo)

# Mostrar todos los títulos encontrados
for titulo in titulos_bien_puntuados:
    print(titulo)
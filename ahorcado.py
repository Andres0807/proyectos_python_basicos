
from random import choice

palabras = ["manzana", "pera", "milanesa", "autos"]

def ahoracado():
    vidas = 6
    guiones = []
    palabra_elegida = choice(palabras)
    cantidad_guiones = len(palabra_elegida)
    contador = 0
    while contador < cantidad_guiones:
        guiones.append("-")
        contador += 1

    letras_acertadas = []
    letras_malas = []
    indices = []
    print(guiones)
    while vidas > 0:

        if "-" not in guiones:
            print(f"Ganaste!! La palabra era {''.join(guiones)}.")
            vidas = 0
            break

        letra_elegida = input("Ingresa una letra: ")



        if letra_elegida in palabra_elegida:
            for i in palabra_elegida:
                if i == letra_elegida and i not in letras_acertadas:
                    letras_acertadas.append(i)

                    indices = [i for i, char in enumerate(palabra_elegida) if char == letra_elegida]

                    for n in indices:
                        guiones.insert(n, letra_elegida)
                        del guiones[n+1]

                    print(f"Genial, esa letra si está. Aún te quedan {vidas} vidas.")
                    print(f"Letras acertadas: {letras_acertadas}")
                    print(f"Letras equivocadas: {letras_malas}")
                    print(guiones)
                elif i == letras_acertadas and i in letras_acertadas:
                    print("Ya elegiste esa letra, prueba con otra.")
                    print(f"Letras acertadas: {letras_acertadas}")
                    print(f"Letras equivocadas: {letras_malas}")


        else:
            letras_malas.append(letra_elegida)

            vidas -= 1
            print(f"Que mal, esa letra no está. Te quedan {vidas} vidas.")
            print(f"Letras acertadas: {letras_acertadas}")
            print(f"Letras equivocadas: {letras_malas}")


ahoracado()

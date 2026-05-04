texto = input("Escribe tu texto: ")
letra1 = input("Escribe tu primera letra: ")
letra2 = input("Escribe tu segunda letra: ")
letra3 = input("Escribe tu tercera letra: ")

texto_minimo = texto.lower()
listado = list(texto_minimo)

print(f"La letra {letra1} aparece {texto.count(letra1.lower())} veces.")
print(f"La letra {letra2} aparece {texto.count(letra2.lower())} veces.")
print(f"La letra {letra3} aparece {texto.count(letra3.lower())} veces.")

palabras = texto.split()
print(f"El texto tiene {len(listado)} letras.")

primera_letra = listado[0]
ultima_letra = listado[-1]

print(f"La primera letra: {primera_letra} y la ultima letra: {ultima_letra}")

listado.reverse()
texto_invertida = " ".join(listado)

print(f"Texto inverso: {texto_invertida}")

py = "Python"
py_actu = py.lower()
aparece = py_actu in texto_minimo
print(f"La palabra {py} aparece? {aparece}")
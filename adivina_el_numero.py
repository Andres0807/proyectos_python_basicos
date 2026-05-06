from random import randint

jugador = input("Introduce tu nombre de jugador: ")

print(f"Bueno, {jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

numero_jugador = int(input("Introduce tu numero: "))

vidas = 8

numero_rand = randint(1, 100)

while vidas > 0:
    if numero_jugador == numero_rand:
        print(f"Excelente, el número {numero_rand} era el que pensé. Ganaste!")
        print(f"Te quedaron {vidas} intentos.")
        break
    elif numero_jugador > numero_rand:
        vidas -= 1
        print(f"Ese número es mayor al número que pensé, te quedan {vidas} vidas.")
        numero_jugador = int(input("Intentalo de nuevo:"))
    elif numero_jugador <= 0 or numero_jugador > 100:
        print("Ese número es menor a 0 o mayor a 100. Por favor ingrese un numero entre 1 y 100.")
        numero_jugador = int(input("Intentalo de nuevo:"))
    elif numero_jugador < numero_rand:
        vidas -= 1
        print(f"Ese número es menor al número que pensé, te quedan {vidas} vidas.")
        numero_jugador = int(input("Intentalo de nuevo:"))
    elif vidas == 0:
        print(f"Te quedaste sin intentos, el numero era {numero_rand}")
        reinicio = input("Quieres reiniciar el juego y jugar de nuevo con otro numero? si/no")
        if reinicio == "si":
            vidas += 8
            numero_rand = randint(1, 100)
        elif reinicio == "no":
            break
from numeros import perfumeria, farmacia, cosmetica


def inicio():

    while True:

        print("Bienvenido a la farmacia")
        print("\nElige un área:")
        print("1 - Perfumería")
        print("2 - Farmacia")
        print("3 - Cosmética")
        print("4 - Salir")

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            perfumeria()

        elif opcion == "2":
            farmacia()

        elif opcion == "3":
            cosmetica()

        elif opcion == "4":
            print("\nGracias por preferirnos.")
            break

        else:
            print("\nOpción no válida.")


inicio()
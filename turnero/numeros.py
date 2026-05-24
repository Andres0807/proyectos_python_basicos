def generador_perfumeria():
    numero = 1

    while True:
        yield f"P-{numero}"
        numero += 1


def generador_farmacia():
    numero = 1

    while True:
        yield f"F-{numero}"
        numero += 1


def generador_cosmetica():
    numero = 1

    while True:
        yield f"C-{numero}"
        numero += 1


# DECORADOR

def decorar_turno(funcion):

    def otra_funcion():
        print("\nSu turno es:")
        print(funcion())
        print("Aguarde y será atendido.\n")

    return otra_funcion


# INSTANCIAS DE GENERADORES

turno_perfumeria = generador_perfumeria()
turno_farmacia = generador_farmacia()
turno_cosmetica = generador_cosmetica()


# FUNCIONES

@decorar_turno
def perfumeria():
    return next(turno_perfumeria)


@decorar_turno
def farmacia():
    return next(turno_farmacia)


@decorar_turno
def cosmetica():
    return next(turno_cosmetica)
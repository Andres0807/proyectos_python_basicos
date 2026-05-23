class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    numero_cuenta_auto = 100000

    def __init__(self, nombre, apellido, balance=0):
        super().__init__(nombre, apellido)

        self.numero_cuenta = Cliente.numero_cuenta_auto
        Cliente.numero_cuenta_auto += 1

        self.balance = balance

    def __str__(self):
        return (
            f"\nCliente: {self.nombre} {self.apellido}"
            f"\nNúmero de cuenta: {self.numero_cuenta}"
            f"\nBalance: ${self.balance}"
        )

    def depositar(self, monto):
        self.balance += monto
        print(f"\nSe depositaron ${monto}")
        print(f"Balance actual: ${self.balance}")

    def retirar(self, monto):
        if monto > self.balance:
            print("\nNo tienes saldo suficiente.")
        else:
            self.balance -= monto
            print(f"\nSe retiraron ${monto}")
            print(f"Balance actual: ${self.balance}")


# Función para crear cliente
def crear_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    balance_inicial = int(input("Ingresa tu balance inicial: "))

    cliente = Cliente(nombre, apellido, balance_inicial)

    return cliente


# Función de inicio
def inicio():

    cliente = crear_cliente()

    while True:
        print("\n--- MENÚ ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver datos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            monto = int(input("¿Cuánto deseas depositar?: "))
            cliente.depositar(monto)

        elif opcion == "2":
            monto = int(input("¿Cuánto deseas retirar?: "))
            cliente.retirar(monto)

        elif opcion == "3":
            print(cliente)

        elif opcion == "4":
            print("\nGracias por usar el sistema bancario.")
            break

        else:
            print("\nOpción no válida.")


# Iniciar programa
inicio()
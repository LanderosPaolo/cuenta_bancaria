# Se crea la clase persona con sus atributos "nombre", "apellido"
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Se crea la clase cliente que es hija de persona, por lo tanto, hereda los atributos y se le agregan 2 nuevos
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

# Creamos 3 métodos
    # 1. Para saber los datos del cliente
    def imprimir_datos(self):
        return f"""
-----------------
Datos del cliente
-----------------
Nombre:           {self.nombre}.
Apellido:         {self.apellido}.
N° cuenta:        {self.numero_cuenta}.
Dinero en cuenta: {self.balance}.\n"""

    # 2. Para realizar un depósito
    def depositar(self):
        deposito = int(input("Cuánto dinero quieres depositar?: "))
        if deposito > 0:
            self.balance += deposito
            print (f"\nHas depositado ${deposito} pesos")
        else:
            print("\nAlgo ha salido mal\n")

    # 3. Para retirar dinero
    def retirar(self):
        retiro = int(input("Cuánto dinero deseas retirar?: "))
        if retiro > 0 and retiro <= self.balance:
            self.balance -= retiro
            print (f"\nHas retirado ${retiro} pesos")
        else:
            print("\nAlgo ha salido mal\n")

# Función que creara un nuevo cliente al ejecutar el programa
def crear_cliente():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        apellido = input("Ingresa tu apellido: ").strip()
        numero_cuenta = input("Ingresa tu N° de cuenta: ").strip()
        if nombre.isalpha() and apellido.isalpha() and numero_cuenta.isdigit():
            numero_cuenta = int(numero_cuenta)
            print(type(numero_cuenta))
            nuevo_cliente = Cliente(nombre, apellido, numero_cuenta)
            return nuevo_cliente
        else:
            print("Algo ha salido mal. Por favor, verifica tus datos e intenta nuevamente.")

# Para finalizar el programa
def finalizar_programa(cliente):
    print(f"Hasta pronto {cliente.nombre}!")

# Función que dará incio al programa
def inicio():
    cliente = crear_cliente()
    while True:
        accion = int(input(f"""
Bienvenido {cliente.nombre} {cliente.apellido}\n
Elige una opción:
[1]: Ver datos
[2]: Depositar dinero
[3]: Retirar dinero
[4]: Salir\n
Tu respuesta: """))

        if accion == 1:
            print(cliente.imprimir_datos())
        elif accion == 2:
            cliente.depositar()
            print(f"Saldo actual: ${cliente.balance} pesos\n")
        elif accion == 3:
            cliente.retirar()
            print(f"Saldo actual: ${cliente.balance} pesos\n")
        elif accion == 4:
            finalizar_programa(cliente)
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

        continuar = input("¿Quieres realizar otra acción? (S/N): ")
        if continuar.lower() != 's':
            finalizar_programa(cliente)
            break

inicio()
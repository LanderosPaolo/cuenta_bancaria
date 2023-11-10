# Se crea la clase persona con sus atributos "nombre", "apellido"
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Se crea la clase cliente que es hija de persona, por lo tanto hereda los atributos y se le agregan 2 nuevos
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Creamos 3 metodos
    # para saber los datos del cliente
    def imprimir_datos(self):
        return f"""
-----------------
Datos del cliente
-----------------
Nombre:           {self.nombre}.
Apellido:         {self.apellido}.
N° cuenta:        {self.numero_cuenta}.
Dinero en cuenta: {self.balance}."""

    # para realizar un deposito
    def depositar(self):
        deposito = int(input("Cuanto dinero quieres depositar?: "))
        total = self.balance + deposito
        print (f"""
Has depositado ${deposito} pesos
Tu dinero actual es de ${total} pesos""")

    # para retirar dinero
    def retirar(self):
        retiro = int(input("Cuanto dinero deseas retirar?: "))
        total = self.balance - retiro
        print (f"""
Has retirado ${retiro} pesos
Tu dinero actual es de ${total} pesos""")

    # para finalizar el programa
    def finalizar_programa(self):
        print(f"Hasta pronto {self.nombre}!")


    # Funcion que creara un nuevo cliente al ejecutar el programa
def crear_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = int(input("Ingresa tu N° de cuenta: "))
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta)
    return nuevo_cliente

def inicio():
    cliente = crear_cliente()
    while True:
        accion = int(input(f"""
Bienvenido {cliente.nombre} {cliente.apellido}
Elige una opcion:
[1]: Ver datos
[2]: Depositar dinero
[3]: Retirar dinero
[4]: Finalizar Programa
Tu respuesta: """))
    
        if accion == 1:
            print(cliente.imprimir_datos())
        elif accion == 2:
            cliente.depositar()
        elif accion == 3:
            cliente.retirar()
        elif accion == 4:
            cliente.finalizar_programa()
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

inicio()
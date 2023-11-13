# Simulación de Cuenta Bancaria

Este es un programa simple de simulación de cuenta bancaria en Python, diseñado para practicar conceptos de programación orientada a objetos (POO).

## Clases

### Persona

La clase `Persona` tiene atributos `nombre` y `apellido`.

### Cliente

La clase `Cliente` es una subclase de `Persona` y agrega dos atributos adicionales: `numero_cuenta` y `balance`. También incluye métodos para imprimir datos del cliente, realizar depósitos y retirar dinero.

## Métodos y funciones

### `imprimir_datos`

Este método, se encargará de mostrar en consola los datos del usuario

### `depositar`

Método encargado de sumar dinero al balance cuando el cliente desea depositar dinero, no puede ser un número negativo

### `retirar`

Se encarga de restar el dinero que se encuentra en la cuenta bancaria, si es un valor menor a 0 o el dinero a retirar es mayor al que está en cuenta, nos dará un aviso y tendremos la posibilidad de volver al inicio

### `crear_cliente`

La función `crear_cliente` solicita al usuario ingresar nombre, apellido y número de cuenta, y crea un nuevo cliente después de validar las entradas.

### `finalizar_programa`

La función `finalizar_programa` imprime un mensaje de despedida.

### `inicio`

La función `inicio` inicia el programa, creando un cliente y ofreciendo opciones para ver datos, depositar, retirar o salir.

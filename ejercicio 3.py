#definimos una clase para habitacion
class Habitacion:
    def __init__(self, tipo, precioxnoche):
        self.tipo = tipo
        self.precioxnoche = precioxnoche

#agregamos una clase para el cliente
class Cliente:
    def __init__(self, nombre, apellido, noches):
        self.nombre = nombre
        self.apellido = apellido
        self.noches = noches

#creamos una clase para las habitaciones del hotel
class Hotel:
    def __init__(self):
        self.habitaciones = [
            Habitacion("Estándar", 100),
            Habitacion("Deluxe", 150),
            Habitacion("Suite", 200)
        ]
        self.clientes = []

#mostramos las opciones que hay de habitaciones
    def mostrar_opciones_habitaciones(self):
        for i, habitacion in enumerate(self.habitaciones):
            print(f"{i+1}. {habitacion.tipo} - ${habitacion.precioxnoche}/noche")

#permmitir que el cliente escoja una habitacion
    def realizar_reserva(self):
        self.mostrar_opciones_habitaciones()
        opcion = int(input("Elija una habitación: "))
        habitacion_elegida = self.habitaciones[opcion - 1]

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        noches = int(input("Ingrese el número de noches: "))

        cliente = Cliente(nombre, apellido, noches)
        self.clientes.append(cliente)

        return habitacion_elegida

    def calcular_costo_total(self, habitacion, cliente):
        costo_total = habitacion.precioxnoche * cliente.noches
        print(f"El costo total de su reserva es: ${costo_total}")

hotel = Hotel()
habitacion_reservada = hotel.realizar_reserva()
cliente_actual = hotel.clientes[-1]
hotel.calcular_costo_total(habitacion_reservada, cliente_actual)
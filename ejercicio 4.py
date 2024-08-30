#crear clase para el empleado
class Empleado:
    def __init__(self, nombre, apellido, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.antiguedad = antiguedad

    def calcular_sueldo(self):
        pass 

#clase para un empleado fijo
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, apellido, antiguedad, salario_base, comisiones):
        super().__init__(nombre, apellido, antiguedad)
        self.salario_base = salario_base
        self.comisiones = comisiones

#crear metodo calcular sueldo segun para lo que necesite el empleado
    def calcular_sueldo(self):
        sueldo_base = self.salario_base + self.comisiones
        if self.antiguedad > 5:
            sueldo_base *= 1.1  # Bono por la antigüedad del 10%
        return sueldo_base

#clase para empleado por horas
class EmpleadoxHoras(Empleado):
    def __init__(self, nombre, apellido, antiguedad, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, apellido, antiguedad)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        sueldo = self.tarifa_por_hora * self.horas_trabajadas
        if self.antiguedad > 5:
            sueldo *= 1.1  # Bono por la antigüedad del 10%
        return sueldo

empleado1 = EmpleadoFijo("Juan", "Pérez", 8, 700, 10)
empleado2 = EmpleadoxHoras("María", "López", 3, 25, 10)
empleado3 = EmpleadoxHoras("Yessica", "Martinez", 5, 20, 8)
empleado4 = EmpleadoFijo("Oscar", "Torres", 6, 400, 14)

print(f"El sueldo de {empleado1.nombre} es: {empleado1.calcular_sueldo()}")
print(f"El sueldo de {empleado2.nombre} es: {empleado2.calcular_sueldo()}")
print(f"El sueldo de {empleado3.nombre} es: {empleado3.calcular_sueldo()}")
print(f"El sueldo de {empleado4.nombre} es: {empleado4.calcular_sueldo()}")
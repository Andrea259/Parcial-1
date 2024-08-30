from datetime import datetime
# utilizamos la clase estudiante 
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = []

    def registrar_asistencia(self, fecha, estado, razon=None):
        self.asistencias.append({'fecha': fecha, 'estado': estado, 'razon': razon})

    def mostrar_asistencias(self):
        print(f"Asistencias de {self.nombre}:")
        for asistencia in self.asistencias:
            estado = asistencia['estado']
            fecha = asistencia['fecha']
            razon = asistencia['razon']
            if estado == 'Permiso' and razon:
                print(f"{fecha} - {estado} - Razón: {razon}")
            else:
                print(f"{fecha} - {estado}")
# Tambien hacemos uso de la clase docente 
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)

    def registrar_asistencia_estudiante(self, nombre_estudiante, fecha, estado, razon=None):
        for estudiante in self.lista_estudiantes:
            if estudiante.nombre == nombre_estudiante:
                estudiante.registrar_asistencia(fecha, estado, razon)
                print(f"Asistencia registrada para {nombre_estudiante}: {estado} el {fecha}")
                break
        else:
            print(f"Estudiante {nombre_estudiante} no encontrado en la lista del docente {self.nombre}.")

    def mostrar_asistencias(self):
        print(f"Lista de asistencias de los estudiantes del docente {self.nombre}:")
        for estudiante in self.lista_estudiantes:
            estudiante.mostrar_asistencias()
#Acontinuacion muestro un pequeño ejemplo de como lo podemos aplicar con datos 
# Ejemplo de uso
docente = Docente("Sr. López")

# Crear estudiantes
estudiante1 = Estudiante("Ana Pérez")
estudiante2 = Estudiante("Juan Gómez")
estudiante3 = Estudiante("Luis Hernández")

# Agregar estudiantes al docente
docente.agregar_estudiante(estudiante1)
docente.agregar_estudiante(estudiante2)
docente.agregar_estudiante(estudiante3)

# Registrar asistencias
docente.registrar_asistencia_estudiante("Ana Pérez", datetime.now().date(), "Asistencia")
docente.registrar_asistencia_estudiante("Juan Gómez", datetime.now().date(), "Permiso", "Cita médica")
docente.registrar_asistencia_estudiante("Luis Hernández", datetime.now().date(), "Inasistencia")

# Mostrar asistencias
docente.mostrar_asistencias()

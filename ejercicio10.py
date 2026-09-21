# EJERCICIO 10
# GESTOR DE TAREAS CON PRIORIDAD


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: descripción y prioridad.
# Proceso: almacenar, buscar tareas altas y eliminar.
# Salida: tareas filtradas.


# PASO 2: BOSQUEJO
# Estudiar -> alta
# Leer -> baja
#
# Prioritarias:
# Estudiar


# PASO 3: PATRÓN
# Cada tarea se almacena como una tupla.
# Las tuplas se guardan dentro de una lista.


# PASO 4: CÓDIGO

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1].lower() == "alta":
                resultado.append(tarea)

        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False


# PASO 5: PRUEBA

tareas = Tareas()

tareas.agregar_tarea("Estudiar", "alta")
tareas.agregar_tarea("Leer", "baja")
tareas.agregar_tarea("Proyecto", "alta")

print(tareas.tareas_prioritarias())

tareas.eliminar_completada("Leer")

print(tareas.tareas)
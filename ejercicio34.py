# EJERCICIO 34
# GESTOR DE CURSOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: cursos y estudiantes.
# Proceso: buscar estudiantes y contar integrantes.
# Salida: cursos encontrados y cantidades.


# PASO 2: BOSQUEJO
# Python:
# Ana, Pedro, Luis
#
# Redes:
# Pedro, Maria
#
# Buscar Pedro:
# Python y Redes


# PASO 3: PATRÓN
# Se utiliza un diccionario de listas.
# curso -> estudiantes
# Un conjunto evita estudiantes repetidos.


# PASO 4: CÓDIGO

class GestorCursos:

    def buscar_estudiante(self, cursos, nombre):
        resultado = []

        for curso, estudiantes in cursos.items():

            if nombre in estudiantes:
                resultado.append(curso)

        return resultado

    def cantidad_por_curso(self, cursos):
        cantidades = {}

        for curso, estudiantes in cursos.items():
            cantidades[curso] = len(estudiantes)

        return cantidades

    def todos_estudiantes(self, cursos):
        estudiantes_unicos = set()

        for estudiantes in cursos.values():

            for estudiante in estudiantes:
                estudiantes_unicos.add(estudiante)

        return estudiantes_unicos


# PASO 5: PRUEBA

gestor = GestorCursos()

cursos = {
    "Python": ["Ana", "Pedro", "Luis"],
    "Base de datos": ["Ana", "Carlos"],
    "Redes": ["Pedro", "Maria"]
}

print(gestor.buscar_estudiante(cursos, "Ana"))
print(gestor.cantidad_por_curso(cursos))
print(gestor.todos_estudiantes(cursos))
# EJERCICIO 14
# MAPEO DE ESTUDIANTES A NOTAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: estudiante y nota.
# Proceso: registrar, filtrar aprobados y encontrar mayor nota.
# Salida: estudiantes aprobados y mejor estudiante.


# PASO 2: BOSQUEJO
# Ana -> 95
# Pedro -> 70
# Luis -> 88
#
# Nota mínima 80:
# Ana y Luis
#
# Mejor: Ana


# PASO 3: PATRÓN
# Se utiliza un diccionario.
# estudiante -> nota


# PASO 4: CÓDIGO

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None

        mejor = None
        mejor_nota = -1

        for estudiante, nota in self.notas.items():

            if nota > mejor_nota:
                mejor = estudiante
                mejor_nota = nota

        return mejor, mejor_nota


# PASO 5: PRUEBA

registro = RegistroNotas()

registro.registrar("Ana", 95)
registro.registrar("Pedro", 70)
registro.registrar("Luis", 88)

print(registro.estudiantes_aprobados(80))
print(registro.mejor_estudiante())
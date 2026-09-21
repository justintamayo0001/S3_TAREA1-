# EJERCICIO 23
# GESTOR DE ESTUDIANTES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: diccionario de estudiantes y notas.
# Proceso: clasificar por aprobación.
# Salida: estudiantes aprobados y reprobados.


# PASO 2: BOSQUEJO
# Ana -> 9 -> aprobada
# Luis -> 5 -> reprobado
# Pedro -> 8 -> aprobado


# PASO 3: PATRÓN
# Se recorre un diccionario con items().
# Nota >= 7 significa aprobado.
# Un conjunto guarda notas diferentes.


# PASO 4: CÓDIGO

class GestorEstudiantes:

    def aprobados(self, estudiantes):
        resultado = []

        for nombre, nota in estudiantes.items():

            if nota >= 7:
                resultado.append(nombre)

        return resultado

    def clasificar_notas(self, estudiantes):
        grupos = {
            "aprobados": [],
            "reprobados": []
        }

        for nombre, nota in estudiantes.items():

            if nota >= 7:
                grupos["aprobados"].append(nombre)

            else:
                grupos["reprobados"].append(nombre)

        return grupos

    def notas_unicas(self, estudiantes):
        return set(estudiantes.values())


# PASO 5: PRUEBA

gestor = GestorEstudiantes()

datos = {
    "Ana": 9,
    "Luis": 5,
    "Pedro": 8,
    "Maria": 5
}

print(gestor.aprobados(datos))
print(gestor.clasificar_notas(datos))
print(gestor.notas_unicas(datos))
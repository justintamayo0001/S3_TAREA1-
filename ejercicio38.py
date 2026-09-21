# EJERCICIO 38
# GESTOR DE ASISTENCIA


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: estudiante y estado de asistencia.
# Proceso: verificar presente o ausente.
# Salida: listas clasificadas.


# PASO 2: BOSQUEJO
# Ana -> presente
# Luis -> ausente
# Carlos -> presente
#
# Presentes:
# Ana, Carlos


# PASO 3: PATRÓN
# Se utiliza un diccionario:
# estudiante -> estado.
# Se utiliza un diccionario de listas para clasificar.


# PASO 4: CÓDIGO

class GestorAsistencia:

    def presentes(self, asistencia):
        resultado = []

        for estudiante, estado in asistencia.items():

            if estado.lower() == "presente":
                resultado.append(estudiante)

        return resultado

    def clasificar_asistencia(self, asistencia):
        grupos = {
            "presentes": [],
            "ausentes": []
        }

        for estudiante, estado in asistencia.items():

            if estado.lower() == "presente":
                grupos["presentes"].append(estudiante)

            else:
                grupos["ausentes"].append(estudiante)

        return grupos

    def estados_unicos(self, asistencia):
        return set(asistencia.values())


# PASO 5: PRUEBA

gestor = GestorAsistencia()

asistencia = {
    "Ana": "presente",
    "Luis": "ausente",
    "Carlos": "presente"
}

print(gestor.presentes(asistencia))
print(gestor.clasificar_asistencia(asistencia))
print(gestor.estados_unicos(asistencia))
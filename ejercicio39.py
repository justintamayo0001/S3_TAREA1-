# EJERCICIO 39
# ANALIZADOR DE ORACIONES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de oraciones.
# Proceso: contar palabras de cada oración.
# Salida: oraciones agrupadas por longitud.


# PASO 2: BOSQUEJO
# "Hola mundo" -> 2 palabras
# "Python es muy fácil" -> 4 palabras
#
# Límite 3:
# "Python es muy fácil"


# PASO 3: PATRÓN
# split() permite contar palabras.
# Un diccionario agrupa según cantidad.
# Un conjunto crea vocabulario único.


# PASO 4: CÓDIGO

class AnalizadorOraciones:

    def oraciones_largas(self, oraciones, limite):
        resultado = []

        for oracion in oraciones:

            cantidad = len(oracion.split())

            if cantidad > limite:
                resultado.append(oracion)

        return resultado

    def agrupar_por_numero_palabras(self, oraciones):
        grupos = {}

        for oracion in oraciones:

            cantidad = len(oracion.split())

            if cantidad not in grupos:
                grupos[cantidad] = []

            grupos[cantidad].append(oracion)

        return grupos

    def vocabulario_unico(self, oraciones):
        palabras = set()

        for oracion in oraciones:

            for palabra in oracion.lower().split():
                palabras.add(palabra)

        return palabras


# PASO 5: PRUEBA

analizador = AnalizadorOraciones()

oraciones = [
    "Hola mundo",
    "Python es muy facil",
    "Estoy aprendiendo programacion orientada a objetos"
]

print(
    analizador.oraciones_largas(
        oraciones,
        3
    )
)

print(
    analizador.agrupar_por_numero_palabras(
        oraciones
    )
)

print(
    analizador.vocabulario_unico(
        oraciones
    )
)
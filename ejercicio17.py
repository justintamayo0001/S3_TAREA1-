# EJERCICIO 17
# GRUPO DE EDADES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: varias edades.
# Proceso: clasificarlas por categoría.
# Salida: diccionario de categorías.


# PASO 2: BOSQUEJO
# 5  -> niño
# 15 -> adolescente
# 30 -> adulto
# 70 -> mayor


# PASO 3: PATRÓN
# Se utilizan if y elif para clasificar.
# Se usa un diccionario de listas.


# PASO 4: CÓDIGO

class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):

        if edad <= 12:
            return "niño"

        elif edad <= 17:
            return "adolescente"

        elif edad <= 64:
            return "adulto"

        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}

        for edad in edades:

            categoria = self.clasificar_edad(edad)

            if categoria not in self.grupos:
                self.grupos[categoria] = []

            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):

        if categoria not in self.grupos:
            return 0

        edades = self.grupos[categoria]

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)


# PASO 5: PRUEBA

agrupador = AgrupadorEdades()

print(
    agrupador.agrupar_por_categoria(
        5, 15, 30, 70, 40
    )
)

print(
    "Promedio adultos:",
    agrupador.edad_promedio_categoria("adulto")
)
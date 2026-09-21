# EJERCICIO 32
# GESTOR DE PALABRAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de palabras.
# Proceso: analizar terminaciones y longitudes.
# Salida: palabras clasificadas.


# PASO 2: BOSQUEJO
# casa -> termina en a
# mesa -> termina en a
# papel -> termina en l


# PASO 3: PATRÓN
# endswith() comprueba terminaciones.
# palabra[-1] obtiene la última letra.
# set() guarda longitudes sin repetir.


# PASO 4: CÓDIGO

class GestorPalabras:

    def terminan_en(self, palabras, terminacion):
        resultado = []

        for palabra in palabras:

            if palabra.endswith(terminacion):
                resultado.append(palabra)

        return resultado

    def agrupar_por_ultima_letra(self, palabras):
        grupos = {}

        for palabra in palabras:

            ultima = palabra[-1]

            if ultima not in grupos:
                grupos[ultima] = []

            grupos[ultima].append(palabra)

        return grupos

    def longitudes_unicas(self, palabras):
        longitudes = set()

        for palabra in palabras:
            longitudes.add(len(palabra))

        return longitudes


# PASO 5: PRUEBA

gestor = GestorPalabras()

palabras = [
    "casa",
    "mesa",
    "papel",
    "sol"
]

print(gestor.terminan_en(palabras, "a"))
print(gestor.agrupar_por_ultima_letra(palabras))
print(gestor.longitudes_unicas(palabras))
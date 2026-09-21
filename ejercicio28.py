# EJERCICIO 28
# ANALIZADOR DE FRASES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de frases.
# Proceso: buscar palabras y contar palabras de cada frase.
# Salida: frases encontradas y agrupadas.


# PASO 2: BOSQUEJO
# "Python es fácil"
# "Me gusta Python"
#
# Buscar Python:
# ambas frases coinciden.


# PASO 3: PATRÓN
# split() permite contar palabras.
# Se usa diccionario para agrupar.
# set() guarda vocabulario único.


# PASO 4: CÓDIGO

class AnalizadorFrases:

    def buscar_palabra(self, frases, palabra):
        resultado = []

        for frase in frases:

            if palabra.lower() in frase.lower():
                resultado.append(frase)

        return resultado

    def agrupar_por_cantidad(self, frases):
        grupos = {}

        for frase in frases:

            cantidad = len(frase.split())

            if cantidad not in grupos:
                grupos[cantidad] = []

            grupos[cantidad].append(frase)

        return grupos

    def palabras_totales_unicas(self, frases):
        palabras = set()

        for frase in frases:

            for palabra in frase.lower().split():
                palabras.add(palabra)

        return palabras


# PASO 5: PRUEBA

analizador = AnalizadorFrases()

frases = [
    "Python es facil",
    "Me gusta Python",
    "Hoy estudio programacion"
]

print(analizador.buscar_palabra(frases, "Python"))
print(analizador.agrupar_por_cantidad(frases))
print(analizador.palabras_totales_unicas(frases))
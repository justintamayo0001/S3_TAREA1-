# EJERCICIO 24
# ANALIZADOR DE NOMBRES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de nombres.
# Proceso: buscar iniciales y eliminar repetidos.
# Salida: nombres encontrados y agrupados.


# PASO 2: BOSQUEJO
# Ana
# Andres
# Pedro
#
# Inicial A:
# Ana, Andres


# PASO 3: PATRÓN
# startswith() comprueba la inicial.
# Se usa un diccionario para agrupar.
# set() elimina duplicados.


# PASO 4: CÓDIGO

class AnalizadorNombres:

    def buscar_inicial(self, nombres, letra):
        resultado = []

        for nombre in nombres:

            if nombre.lower().startswith(letra.lower()):
                resultado.append(nombre)

        return resultado

    def agrupar_por_inicial(self, nombres):
        grupos = {}

        for nombre in nombres:

            inicial = nombre[0].upper()

            if inicial not in grupos:
                grupos[inicial] = []

            grupos[inicial].append(nombre)

        return grupos

    def nombres_unicos(self, nombres):
        return set(nombres)


# PASO 5: PRUEBA

analizador = AnalizadorNombres()

nombres = [
    "Ana",
    "Andres",
    "Pedro",
    "Luis",
    "Ana"
]

print(analizador.buscar_inicial(nombres, "A"))
print(analizador.agrupar_por_inicial(nombres))
print(analizador.nombres_unicos(nombres))
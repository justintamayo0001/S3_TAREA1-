# EJERCICIO 13
# COMBINADOR DE LISTAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: dos o más listas.
# Proceso: alternar sus elementos.
# Salida: lista combinada.


# PASO 2: BOSQUEJO
# Lista 1: [1, 2]
# Lista 2: [3, 4]
#
# Tomar 1
# Tomar 3
# Tomar 2
# Tomar 4
#
# Resultado: [1, 3, 2, 4]


# PASO 3: PATRÓN
# Se recorren posiciones con índices.
# Se comprueba si cada índice existe.


# PASO 4: CÓDIGO

class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []

        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):

            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        if len(listas) == 0:
            return resultado

        mayor = max(len(lista) for lista in listas)

        for i in range(mayor):

            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])

        return resultado


# PASO 5: PRUEBA

combinador = CombinadorListas()

print(combinador.intercalar([1, 2], [3, 4]))

print(
    combinador.intercalar_multiples(
        [1, 2],
        [3, 4],
        [5, 6]
    )
)
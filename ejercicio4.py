# EJERCICIO 4
# INVERSOR DE SECUENCIAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: una lista.
# Proceso: recorrerla desde el último elemento.
# Salida: lista invertida.


# PASO 2: BOSQUEJO
# Lista: [1, 2, 3, 4]
#
# Tomar:
# 4
# 3
# 2
# 1
#
# Resultado: [4, 3, 2, 1]


# PASO 3: PATRÓN
# Se utiliza range() de atrás hacia adelante.
# No se utiliza reversed().
# Para guardar varias inversiones se usa un diccionario.


# PASO 4: CÓDIGO

class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultados = {}

        for lista in listas:
            original = tuple(lista)
            resultados[original] = self.invertir_lista(lista)

        return resultados


# PASO 5: PRUEBA

inversor = InversorSecuencia()

print(inversor.invertir_lista([1, 2, 3, 4]))

print(
    inversor.invertir_multiples(
        [1, 2, 3],
        ["a", "b", "c"]
    )
)
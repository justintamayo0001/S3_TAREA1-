# EJERCICIO 4
# INVERSOR DE SECUENCIAS

# PASO 1: ENTENDER EL PROBLEMA
# Entrada: una lista o varias listas.
# Proceso: recorrer cada lista desde el final hasta el inicio.
# Salida: lista invertida.

# PASO 2: BOSQUEJO
# Lista original:
# [1, 2, 3]
#
# posición 2 -> 3
# posición 1 -> 2
# posición 0 -> 1
#
# Lista invertida:
# [3, 2, 1]

# PASO 3: PATRÓN
# Crear una lista vacía.
# Recorrer desde la última posición hasta la primera.
# invertir_multiples() reutiliza invertir_lista().
#
# No se utiliza reversed().


class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for posicion in range(len(lista) - 1, -1, -1):
            invertida.append(lista[posicion])

        return invertida

    def invertir_multiples(self, *listas):
        resultados = {}

        for lista in listas:
            original = tuple(lista)
            resultados[original] = self.invertir_lista(lista)

        return resultados


# PASO 5: PRUEBA DEL PROGRAMA

inversor = InversorSecuencia()

print("Una lista invertida:")
print(inversor.invertir_lista([1, 2, 3]))

print("Varias listas invertidas:")
print(
    inversor.invertir_multiples(
        [1, 2, 3],
        [4, 5, 6]
    )
)
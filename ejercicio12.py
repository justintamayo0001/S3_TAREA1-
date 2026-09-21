# EJERCICIO 12
# SELECTOR DE RANGO CON TUPLAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: inicio y fin de uno o varios rangos.
# Proceso: crear rangos y combinar valores.
# Salida: números sin repetir.


# PASO 2: BOSQUEJO
# Rango 1: 1 a 3 -> 1,2,3
# Rango 2: 2 a 4 -> 2,3,4
#
# Sin repetir:
# 1,2,3,4


# PASO 3: PATRÓN
# Los rangos se representan con tuplas.
# Un conjunto elimina duplicados.


# PASO 4: CÓDIGO

class SelectorRango:

    def crear_rango(self, inicio, fin):
        numeros = []

        for numero in range(inicio, fin + 1):
            numeros.append(numero)

        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for rango in rangos:
            numeros = self.crear_rango(rango[0], rango[1])

            for numero in numeros:
                elementos.add(numero)

        return sorted(elementos)


# PASO 5: PRUEBA

selector = SelectorRango()

print(selector.crear_rango(1, 5))

print(
    selector.elementos_en_multiples_rangos(
        (1, 3),
        (2, 4)
    )
)
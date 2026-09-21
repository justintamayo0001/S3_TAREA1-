# EJERCICIO 18
# MATRIZ DE DISTANCIAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: puntos representados por tuplas (x, y).
# Proceso: calcular distancia euclidiana.
# Salida: distancia o punto más cercano.


# PASO 2: BOSQUEJO
# Punto 1 = (0, 0)
# Punto 2 = (3, 4)
#
# Distancia:
# raiz((3-0)^2 + (4-0)^2)
# raiz(9 + 16)
# raiz(25)
# 5


# PASO 3: PATRÓN
# Los puntos se representan con tuplas.
# Se aplica la fórmula de distancia.


# PASO 4: CÓDIGO

class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):

        x1, y1 = p1
        x2, y2 = p2

        distancia = (
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        ) ** 0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):

        if len(puntos) == 0:
            return None

        cercano = None
        menor_distancia = None

        for punto in puntos:

            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )

            if (
                menor_distancia is None
                or distancia < menor_distancia
            ):
                menor_distancia = distancia
                cercano = punto

        return cercano


# PASO 5: PRUEBA

calculador = CalculadorDistancia()

print(
    calculador.distancia_euclidiana(
        (0, 0),
        (3, 4)
    )
)

print(
    calculador.punto_mas_cercano(
        (0, 0),
        (5, 5),
        (1, 1),
        (10, 10)
    )
)
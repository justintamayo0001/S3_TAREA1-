# EJERCICIO 6
# ESTADÍSTICAS DE TEMPERATURA


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: temperaturas.
# Proceso: almacenar y calcular mínimo, máximo y promedio.
# Salida: estadísticas.


# PASO 2: BOSQUEJO
# Temperaturas: 25, 30, 22, 28
#
# Mínima = 22
# Máxima = 30
# Promedio = 26.25


# PASO 3: PATRÓN
# Se usa una lista para almacenar temperaturas.
# min(), max() y sum() permiten calcular estadísticas.


# PASO 4: CÓDIGO

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

        return self.temperaturas

    def minima(self):
        if len(self.temperaturas) == 0:
            return None

        return min(self.temperaturas)

    def maxima(self):
        if len(self.temperaturas) == 0:
            return None

        return max(self.temperaturas)

    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0

        return sum(self.temperaturas) / len(self.temperaturas)


# PASO 5: PRUEBA

gestor = GestorTemperatura()

print(gestor.registrar_multiples(25, 30, 22, 28))
print("Mínima:", gestor.minima())
print("Máxima:", gestor.maxima())
print("Promedio:", gestor.promedio())
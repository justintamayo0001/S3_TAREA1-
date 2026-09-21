# EJERCICIO 15
# DIVISORES DE UN NÚMERO


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: uno o varios números.
# Proceso: comprobar qué valores dividen exactamente al número.
# Salida: divisores y verificación de número perfecto.


# PASO 2: BOSQUEJO
# Número: 6
#
# 6 / 1 -> exacto
# 6 / 2 -> exacto
# 6 / 3 -> exacto
# 6 / 6 -> exacto
#
# Divisores: 1,2,3,6
#
# 1 + 2 + 3 = 6
# 6 es perfecto.


# PASO 3: PATRÓN
# Si numero % i == 0, entonces i es divisor.
# Se reutiliza encontrar_divisores().


# PASO 4: CÓDIGO

class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:

            if divisor != numero:
                suma += divisor

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


# PASO 5: PRUEBA

divisor = DivisorFinder()

print(divisor.encontrar_divisores(12))
print(divisor.es_perfecto(6))
print(divisor.encontrar_multiples_divisores(6, 12, 15))
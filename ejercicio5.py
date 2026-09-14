# EJERCICIO 5
# DETECTOR DE NÚMEROS PARES E IMPARES

# PASO 1: ENTENDER EL PROBLEMA
# Entrada: varios números.
# Proceso: comprobar si cada número es par o impar.
# Salida: diccionario con pares e impares
# y una tupla con las cantidades.

# PASO 2: BOSQUEJO
# 1 % 2 = 1 -> impar
# 2 % 2 = 0 -> par
# 3 % 2 = 1 -> impar
# 4 % 2 = 0 -> par
# 5 % 2 = 1 -> impar
#
# Pares: [2, 4]
# Impares: [1, 3, 5]
# Cantidad: (2, 3)

# PASO 3: PATRÓN
# Si numero % 2 == 0, es par.
# De lo contrario, es impar.
# separar() reutiliza es_par().


class AnalizadorNumeros:

    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        self.resultado = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:
            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)

        return self.resultado

    def cantidad_pares_impares(self):
        cantidad_pares = len(self.resultado["pares"])
        cantidad_impares = len(self.resultado["impares"])

        return (cantidad_pares, cantidad_impares)


# PASO 5: PRUEBA DEL PROGRAMA

analizador = AnalizadorNumeros()

print("Clasificación:")
print(analizador.separar(1, 2, 3, 4, 5))

print("Cantidad de pares e impares:")
print(analizador.cantidad_pares_impares())
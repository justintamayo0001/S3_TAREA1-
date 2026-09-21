# EJERCICIO 5
# DETECTOR DE NÚMEROS PARES E IMPARES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: varios números.
# Proceso: determinar si cada número es par o impar.
# Salida: diccionario con pares e impares.


# PASO 2: BOSQUEJO
# Números: 1, 2, 3, 4
#
# 1 -> impar
# 2 -> par
# 3 -> impar
# 4 -> par
#
# Pares: [2, 4]
# Impares: [1, 3]


# PASO 3: PATRÓN
# Un número es par si numero % 2 == 0.
# separar() reutiliza es_par().
# Se usa un diccionario de listas.


# PASO 4: CÓDIGO

class AnalizadorNumeros:

    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }

    def es_par(self, numero):
        return numero % 2 == 0

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
        pares = len(self.resultado["pares"])
        impares = len(self.resultado["impares"])

        return pares, impares


# PASO 5: PRUEBA

analizador = AnalizadorNumeros()

print(analizador.separar(1, 2, 3, 4, 5, 6))
print(analizador.cantidad_pares_impares())
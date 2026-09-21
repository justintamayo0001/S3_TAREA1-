# EJERCICIO 11
# CONTADOR DE FRECUENCIA


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: elementos.
# Proceso: contar cuántas veces aparece cada elemento.
# Salida: frecuencia y elemento más repetido.


# PASO 2: BOSQUEJO
# a, b, a
#
# a -> 2
# b -> 1
#
# Más frecuente: a


# PASO 3: PATRÓN
# Se utiliza un diccionario.
# elemento -> cantidad


# PASO 4: CÓDIGO

class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        if len(self.frecuencias) == 0:
            return None

        elemento_mayor = None
        frecuencia_mayor = 0

        for elemento, cantidad in self.frecuencias.items():
            if cantidad > frecuencia_mayor:
                frecuencia_mayor = cantidad
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


# PASO 5: PRUEBA

contador = ContadorFrecuencia()

contador.agregar_elemento("a")
contador.agregar_elemento("b")
contador.agregar_elemento("a")

print(contador.frecuencias)
print(contador.elemento_mas_frecuente())
print(contador.frecuencia_elemento("a"))
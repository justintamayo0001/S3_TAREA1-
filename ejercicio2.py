# EJERCICIO 2
# CONTADOR DE PALABRAS ÚNICAS

# PASO 1: ENTENDER EL PROBLEMA
# Entrada: palabras individuales o varias palabras.
# Proceso: guardar palabras sin repetirlas.
# Salida: cantidad de palabras únicas.

# PASO 2: BOSQUEJO
# Palabras: hola, mundo, hola
#
# hola  -> agregar
# mundo -> agregar
# hola  -> ya existe
#
# Palabras únicas: 2

# PASO 3: PATRÓN
# Se utiliza un conjunto para evitar duplicados.
# También se utiliza una lista para conservar el orden.
# agregar_multiples() reutiliza agregar_palabra().


class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


# PASO 5: PRUEBA DEL PROGRAMA

analizador = AnalizadorTexto()

analizador.agregar_multiples("hola", "mundo", "hola")

print("Palabras en orden:")
print(analizador.orden_palabras)

print("Cantidad de palabras únicas:")
print(analizador.contar_palabras())
# EJERCICIO 2
# CONTADOR DE PALABRAS ÚNICAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: palabras individuales o varias palabras.
# Proceso: guardar palabras sin repetirlas.
# Salida: lista y cantidad de palabras únicas.


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
# Se utiliza una lista para conservar el orden.
# agregar_multiples() reutiliza agregar_palabra().


# PASO 4: CÓDIGO

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

        return self.orden_palabras


# PASO 5: PRUEBA

analizador = AnalizadorTexto()

print(
    analizador.agregar_multiples(
        "hola",
        "mundo",
        "hola",
        "python"
    )
)

print("Cantidad:", analizador.contar_palabras())
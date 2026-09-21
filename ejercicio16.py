# EJERCICIO 16
# CODIFICADOR CÉSAR


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: palabra y desplazamiento.
# Proceso: mover cada letra dentro del alfabeto.
# Salida: palabra codificada.


# PASO 2: BOSQUEJO
# Palabra: hola
# Desplazamiento: 3
#
# h -> k
# o -> r
# l -> o
# a -> d
#
# Resultado: krod


# PASO 3: PATRÓN
# ord() convierte una letra a código.
# chr() convierte código a letra.
# % 26 mantiene el resultado dentro del alfabeto.


# PASO 4: CÓDIGO

class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):

        if not letra.isalpha():
            return letra

        if letra.islower():
            inicio = ord("a")
        else:
            inicio = ord("A")

        posicion = ord(letra) - inicio
        nueva_posicion = (posicion + desplazamiento) % 26

        return chr(inicio + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(
                letra,
                desplazamiento
            )

        self.historial[palabra] = resultado

        return resultado


# PASO 5: PRUEBA

codificador = CodificadorCesar()

print(codificador.codificar_palabra("hola", 3))
print(codificador.historial)
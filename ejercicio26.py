# EJERCICIO 26
# CONTADOR DE LETRAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: texto.
# Proceso: recorrer sus letras.
# Salida: vocales, frecuencias y letras únicas.


# PASO 2: BOSQUEJO
# Texto: hola
#
# h -> 1
# o -> 1
# l -> 1
# a -> 1
#
# Vocales: 2


# PASO 3: PATRÓN
# Se recorre el texto carácter por carácter.
# Un diccionario cuenta frecuencias.
# Un conjunto elimina repetidos.


# PASO 4: CÓDIGO

class ContadorLetras:

    def contar_vocales(self, texto):
        cantidad = 0

        for letra in texto.lower():

            if letra in "aeiou":
                cantidad += 1

        return cantidad

    def frecuencia_letras(self, texto):
        frecuencia = {}

        for letra in texto.lower():

            if letra != " ":

                if letra in frecuencia:
                    frecuencia[letra] += 1

                else:
                    frecuencia[letra] = 1

        return frecuencia

    def letras_unicas(self, texto):
        letras = set()

        for letra in texto.lower():

            if letra != " ":
                letras.add(letra)

        return letras


# PASO 5: PRUEBA

contador = ContadorLetras()

print(contador.contar_vocales("Hola Mundo"))
print(contador.frecuencia_letras("Hola Mundo"))
print(contador.letras_unicas("Hola Mundo"))
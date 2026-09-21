# EJERCICIO 22
# ANALIZADOR DE PALABRAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: texto.
# Proceso: analizar longitudes y repeticiones.
# Salida: palabras largas, frecuencias y vocabulario.


# PASO 2: BOSQUEJO
# Texto:
# Python es fácil y Python
#
# Python -> 2 veces
# es -> 1
# fácil -> 1
# y -> 1


# PASO 3: PATRÓN
# split() separa palabras.
# Un diccionario cuenta repeticiones.
# Un conjunto elimina palabras repetidas.


# PASO 4: CÓDIGO

class AnalizadorPalabras:

    def palabras_largas(self, texto, longitud):
        resultado = []

        for palabra in texto.split():

            if len(palabra) >= longitud:
                resultado.append(palabra)

        return resultado

    def contar_palabras(self, texto):
        contador = {}

        for palabra in texto.lower().split():

            if palabra in contador:
                contador[palabra] += 1

            else:
                contador[palabra] = 1

        return contador

    def vocabulario(self, texto):
        return set(texto.lower().split())


# PASO 5: PRUEBA

analizador = AnalizadorPalabras()

texto = "Python es facil y Python es divertido"

print(analizador.palabras_largas(texto, 5))
print(analizador.contar_palabras(texto))
print(analizador.vocabulario(texto))
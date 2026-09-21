# EJERCICIO 9
# VALIDADOR DE CARACTERES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: texto.
# Proceso: clasificar caracteres.
# Salida: cantidad de vocales, consonantes y dígitos.


# PASO 2: BOSQUEJO
# Texto: Hola123
#
# H -> consonante
# o -> vocal
# l -> consonante
# a -> vocal
# 1,2,3 -> dígitos


# PASO 3: PATRÓN
# Se recorre cada carácter.
# isalpha() verifica letras.
# isdigit() verifica números.
# solo_vocales() se reutiliza.


# PASO 4: CÓDIGO

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        for caracter in texto:

            if caracter.isdigit():
                resultado["digitos"] += 1

            elif caracter.isalpha():

                if self.solo_vocales(caracter):
                    resultado["vocales"] += 1

                else:
                    resultado["consonantes"] += 1

        return resultado


# PASO 5: PRUEBA

analizador = AnalizadorString()

print(analizador.contar_por_tipo("Hola123"))
print("Texto más largo:", analizador.texto_mas_largo)
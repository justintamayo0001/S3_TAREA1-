# EJERCICIO 20
# ANALIZADOR DE PATRONES EN TEXTOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: texto y patrón.
# Proceso: separar palabras, buscar y agrupar.
# Salida: listas, diccionario y conjunto.


# PASO 2: BOSQUEJO
# Texto:
# casa carro perro camino
#
# Patrón: ca
#
# casa   -> coincide
# carro  -> coincide
# perro  -> no
# camino -> coincide


# PASO 3: PATRÓN
# split() separa palabras.
# startswith() comprueba el inicio.
# Un conjunto evita duplicados.
# Un diccionario permite agrupar por longitud.


# PASO 4: CÓDIGO

class AnalizadorPatrones:

    def __init__(self):
        self.registro_palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:

            self.registro_palabras.add(palabra)

            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}

        for palabra in texto.split():

            self.registro_palabras.add(palabra)

            longitud = len(palabra)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):
        return self.registro_palabras


# PASO 5: PRUEBA

analizador = AnalizadorPatrones()

print(
    analizador.encontrar_palabras(
        "casa carro perro camino",
        "ca"
    )
)

print(
    analizador.agrupar_por_longitud(
        "el gato esta aqui"
    )
)

print(analizador.palabras_unicas())
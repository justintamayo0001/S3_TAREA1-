# EJERCICIO 31
# BIBLIOTECA


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: libros y autores.
# Proceso: buscar y agrupar libros por autor.
# Salida: listas y autores únicos.


# PASO 2: BOSQUEJO
# Libro A -> Autor 1
# Libro B -> Autor 2
# Libro C -> Autor 1
#
# Autor 1:
# Libro A y Libro C


# PASO 3: PATRÓN
# Se utiliza diccionario:
# título -> autor
# Otro diccionario agrupa autor -> libros.


# PASO 4: CÓDIGO

class Biblioteca:

    def buscar_por_autor(self, libros, autor):
        resultado = []

        for titulo, nombre_autor in libros.items():

            if nombre_autor.lower() == autor.lower():
                resultado.append(titulo)

        return resultado

    def agrupar_por_autor(self, libros):
        grupos = {}

        for titulo, autor in libros.items():

            if autor not in grupos:
                grupos[autor] = []

            grupos[autor].append(titulo)

        return grupos

    def autores_unicos(self, libros):
        return set(libros.values())


# PASO 5: PRUEBA

biblioteca = Biblioteca()

libros = {
    "Libro A": "Autor 1",
    "Libro B": "Autor 2",
    "Libro C": "Autor 1"
}

print(biblioteca.buscar_por_autor(libros, "Autor 1"))
print(biblioteca.agrupar_por_autor(libros))
print(biblioteca.autores_unicos(libros))
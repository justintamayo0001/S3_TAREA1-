# EJERCICIO 27
# CLASIFICADOR DE EDADES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: personas y edades.
# Proceso: comprobar si tienen 18 años o más.
# Salida: menores y adultos.


# PASO 2: BOSQUEJO
# Ana -> 17 -> menor
# Luis -> 18 -> adulto
# Pedro -> 25 -> adulto


# PASO 3: PATRÓN
# Se utiliza un diccionario.
# edad >= 18 significa adulto.


# PASO 4: CÓDIGO

class ClasificadorEdades:

    def mayores_edad(self, personas):
        resultado = []

        for nombre, edad in personas.items():

            if edad >= 18:
                resultado.append(nombre)

        return resultado

    def clasificar_edades(self, personas):
        grupos = {
            "menores": [],
            "adultos": []
        }

        for nombre, edad in personas.items():

            if edad >= 18:
                grupos["adultos"].append(nombre)

            else:
                grupos["menores"].append(nombre)

        return grupos

    def edades_unicas(self, personas):
        return set(personas.values())


# PASO 5: PRUEBA

clasificador = ClasificadorEdades()

personas = {
    "Ana": 17,
    "Luis": 18,
    "Pedro": 25
}

print(clasificador.mayores_edad(personas))
print(clasificador.clasificar_edades(personas))
print(clasificador.edades_unicas(personas))
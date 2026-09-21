# EJERCICIO 7
# MAPEADOR DE EDADES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: nombre y edad.
# Proceso: guardar personas, filtrar por edad y promediar.
# Salida: personas mayores y edad promedio.


# PASO 2: BOSQUEJO
# Ana -> 18
# Luis -> 15
# Carlos -> 25
#
# Mayores de 18:
# Ana y Carlos


# PASO 3: PATRÓN
# Se utiliza un diccionario:
# nombre -> edad
# Se recorre con items().


# PASO 4: CÓDIGO

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        return sum(self.personas.values()) / len(self.personas)


# PASO 5: PRUEBA

gestor = GestorPersonas()

gestor.agregar_persona("Ana", 18)
gestor.agregar_persona("Luis", 15)
gestor.agregar_persona("Carlos", 25)

print(gestor.personas_mayores(18))
print("Promedio:", gestor.edad_promedio())
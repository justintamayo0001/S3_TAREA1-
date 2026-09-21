# EJERCICIO 1
# VALIDADOR DE NOTAS CON PROMEDIO


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: una o varias notas.
# Proceso: validar que las notas estén entre 0 y 100.
# Salida: lista de notas válidas y promedio.


# PASO 2: BOSQUEJO
# Notas: 85, 92, 110, 78
#
# 85  -> válida
# 92  -> válida
# 110 -> no válida
# 78  -> válida
#
# Lista: [85, 92, 78]
# Promedio: (85 + 92 + 78) / 3


# PASO 3: PATRÓN
# Se utiliza una lista para guardar las notas.
# validar_nota() comprueba el rango.
# cargar_notas() reutiliza validar_nota().
# promedio() calcula la media.


# PASO 4: CÓDIGO

class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


# PASO 5: PRUEBA

calificador = Calificador()

print(calificador.cargar_notas(85, 92, 110, 78, -5, 88))
print("Promedio:", calificador.promedio())
# EJERCICIO 1
# VALIDADOR DE NOTAS CON PROMEDIO

# PASO 1: ENTENDER EL PROBLEMA
# Entrada: varias notas.
# Proceso: validar que cada nota esté entre 0 y 100.
# Salida: lista de notas válidas y promedio.

# PASO 2: BOSQUEJO
# 85  -> válida
# 92  -> válida
# 110 -> no válida
# 78  -> válida
# -5  -> no válida
# 88  -> válida
#
# Lista final: [85, 92, 78, 88]
# Promedio: 85.75

# PASO 3: PATRÓN
# Se revisa cada nota.
# Si está entre 0 y 100 se guarda en la lista.
# cargar_notas() reutiliza validar_nota().


class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


# PASO 5: PRUEBA DEL PROGRAMA

calificador = Calificador()

print("Notas válidas:")
print(calificador.cargar_notas(85, 92, 110, 78, -5, 88))

print("Promedio:")
print(calificador.promedio())
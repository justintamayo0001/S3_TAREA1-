# EJERCICIO 30
# ANALIZADOR DE CALIFICACIONES


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de notas.
# Proceso: encontrar máximo y clasificar.
# Salida: nota máxima y grupos.


# PASO 2: BOSQUEJO
# Notas: 5, 7, 9
#
# 5 -> baja
# 7 -> media
# 9 -> alta
#
# Máxima: 9


# PASO 3: PATRÓN
# max() obtiene la mayor nota.
# if/elif clasifica rangos.
# set() elimina notas repetidas.


# PASO 4: CÓDIGO

class AnalizadorCalificaciones:

    def nota_maxima(self, notas):

        if len(notas) == 0:
            return None

        return max(notas)

    def agrupar_por_rango(self, notas):
        grupos = {
            "bajas": [],
            "medias": [],
            "altas": []
        }

        for nota in notas:

            if nota < 7:
                grupos["bajas"].append(nota)

            elif nota < 9:
                grupos["medias"].append(nota)

            else:
                grupos["altas"].append(nota)

        return grupos

    def notas_sin_repetir(self, notas):
        return set(notas)


# PASO 5: PRUEBA

analizador = AnalizadorCalificaciones()

notas = [5, 7, 9, 10, 7, 6, 8]

print("Máxima:", analizador.nota_maxima(notas))
print(analizador.agrupar_por_rango(notas))
print(analizador.notas_sin_repetir(notas))
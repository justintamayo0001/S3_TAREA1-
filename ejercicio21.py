# EJERCICIO 21
# CLASIFICADOR NUMÉRICO


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de números.
# Proceso: encontrar pares y clasificarlos por signo.
# Salida: listas y conjunto.


# PASO 2: BOSQUEJO
# 5  -> positivo
# -3 -> negativo
# 0  -> cero
# 8  -> positivo y par


# PASO 3: PATRÓN
# % 2 permite encontrar pares.
# if/elif clasifica signos.
# set() elimina repetidos.


# PASO 4: CÓDIGO

class ClasificadorNumerico:

    def encontrar_pares(self, numeros):
        pares = []

        for numero in numeros:

            if numero % 2 == 0:
                pares.append(numero)

        return pares

    def agrupar_por_signo(self, numeros):
        grupos = {
            "positivos": [],
            "negativos": [],
            "ceros": []
        }

        for numero in numeros:

            if numero > 0:
                grupos["positivos"].append(numero)

            elif numero < 0:
                grupos["negativos"].append(numero)

            else:
                grupos["ceros"].append(numero)

        return grupos

    def numeros_unicos(self, numeros):
        return set(numeros)


# PASO 5: PRUEBA

clasificador = ClasificadorNumerico()

datos = [5, -3, 0, 8, 8, -2, 4]

print(clasificador.encontrar_pares(datos))
print(clasificador.agrupar_por_signo(datos))
print(clasificador.numeros_unicos(datos))
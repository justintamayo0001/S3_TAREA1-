# EJERCICIO 33
# ANALIZADOR DE VENTAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de ventas.
# Proceso: comparar y clasificar cantidades.
# Salida: ventas filtradas y agrupadas.


# PASO 2: BOSQUEJO
# 50  -> baja
# 120 -> media
# 600 -> alta


# PASO 3: PATRÓN
# Se utiliza if/elif.
# Una lista guarda cada categoría.
# set() elimina valores repetidos.


# PASO 4: CÓDIGO

class AnalizadorVentas:

    def ventas_mayores(self, ventas, limite):
        resultado = []

        for venta in ventas:

            if venta > limite:
                resultado.append(venta)

        return resultado

    def clasificar_ventas(self, ventas):
        grupos = {
            "bajas": [],
            "medias": [],
            "altas": []
        }

        for venta in ventas:

            if venta < 100:
                grupos["bajas"].append(venta)

            elif venta < 500:
                grupos["medias"].append(venta)

            else:
                grupos["altas"].append(venta)

        return grupos

    def valores_unicos(self, ventas):
        return set(ventas)


# PASO 5: PRUEBA

analizador = AnalizadorVentas()

ventas = [50, 120, 600, 250, 50, 800]

print(analizador.ventas_mayores(ventas, 200))
print(analizador.clasificar_ventas(ventas))
print(analizador.valores_unicos(ventas))
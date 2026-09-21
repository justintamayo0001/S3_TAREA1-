# EJERCICIO 25
# GESTOR DE PRODUCTOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: productos y precios.
# Proceso: comparar precios.
# Salida: productos clasificados.


# PASO 2: BOSQUEJO
# Arroz -> 2.50
# Leche -> 1.25
# Carne -> 8.50
#
# Más de 5:
# Carne


# PASO 3: PATRÓN
# Se usa diccionario producto -> precio.
# Se comparan los valores.


# PASO 4: CÓDIGO

class GestorProductos:

    def productos_caros(self, productos, precio):
        resultado = []

        for producto, valor in productos.items():

            if valor > precio:
                resultado.append(producto)

        return resultado

    def clasificar_precios(self, productos):
        grupos = {
            "economicos": [],
            "costosos": []
        }

        for producto, precio in productos.items():

            if precio <= 5:
                grupos["economicos"].append(producto)

            else:
                grupos["costosos"].append(producto)

        return grupos

    def precios_unicos(self, productos):
        return set(productos.values())


# PASO 5: PRUEBA

gestor = GestorProductos()

productos = {
    "Arroz": 2.50,
    "Leche": 1.25,
    "Carne": 8.50
}

print(gestor.productos_caros(productos, 2))
print(gestor.clasificar_precios(productos))
print(gestor.precios_unicos(productos))
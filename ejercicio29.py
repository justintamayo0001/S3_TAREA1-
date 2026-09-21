# EJERCICIO 29
# CONTROL DE INVENTARIO


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: productos y cantidades.
# Proceso: comprobar cantidad disponible.
# Salida: productos clasificados por stock.


# PASO 2: BOSQUEJO
# Pan -> 10 -> disponible
# Leche -> 3 -> bajo stock
# Arroz -> 0 -> agotado


# PASO 3: PATRÓN
# Se recorre un diccionario.
# Las cantidades determinan la categoría.


# PASO 4: CÓDIGO

class ControlInventario:

    def productos_disponibles(self, inventario):
        resultado = []

        for producto, cantidad in inventario.items():

            if cantidad > 0:
                resultado.append(producto)

        return resultado

    def clasificar_stock(self, inventario):
        grupos = {
            "agotados": [],
            "bajo_stock": [],
            "disponibles": []
        }

        for producto, cantidad in inventario.items():

            if cantidad == 0:
                grupos["agotados"].append(producto)

            elif cantidad <= 5:
                grupos["bajo_stock"].append(producto)

            else:
                grupos["disponibles"].append(producto)

        return grupos

    def cantidades_unicas(self, inventario):
        return set(inventario.values())


# PASO 5: PRUEBA

control = ControlInventario()

inventario = {
    "Pan": 10,
    "Leche": 3,
    "Arroz": 0
}

print(control.productos_disponibles(inventario))
print(control.clasificar_stock(inventario))
print(control.cantidades_unicas(inventario))
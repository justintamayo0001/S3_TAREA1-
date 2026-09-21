# EJERCICIO 19
# INVENTARIO DE PRODUCTOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: producto y cantidad.
# Proceso: agregar, restar y comprobar stock.
# Salida: inventario actualizado.


# PASO 2: BOSQUEJO
# Pan = 50
#
# Vender 30
# 50 - 30 = 20
#
# Stock final = 20


# PASO 3: PATRÓN
# Se utiliza un diccionario:
# producto -> cantidad


# PASO 4: CÓDIGO

class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):

        if producto in self.productos:
            self.productos[producto] += cantidad

        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):

        if producto in self.productos:

            if self.productos[producto] >= cantidad:
                self.productos[producto] -= cantidad
                return True

        return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.productos.items():

            if cantidad < minimo:
                resultado.append(producto)

        return resultado


# PASO 5: PRUEBA

inventario = Inventario()

inventario.agregar_stock("Pan", 50)
inventario.agregar_stock("Leche", 10)

print(inventario.restar_stock("Pan", 30))
print(inventario.productos)
print(inventario.productos_bajo_stock(15))
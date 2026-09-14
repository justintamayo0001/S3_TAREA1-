# EJERCICIO 3
# GESTOR DE COMPRAS CON TOTALES

# PASO 1: ENTENDER EL PROBLEMA
# Entrada: nombre de un artículo y su precio.
# Proceso: guardar artículos en un diccionario,
# sumar precios y buscar artículos por rango.
# Salida: total del carrito y artículos encontrados.

# PASO 2: BOSQUEJO
# pan   = 2.50
# leche = 3.00
# arroz = 4.50
#
# Total:
# 2.50 + 3.00 + 4.50 = 10.00
#
# Entre 2 y 3:
# pan y leche

# PASO 3: PATRÓN
# Cada artículo se guarda así:
# nombre -> precio
#
# Para obtener el total se suman los precios.
# Para buscar por rango se compara cada precio.


class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        encontrados = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                encontrados.append(nombre)

        return encontrados


# PASO 5: PRUEBA DEL PROGRAMA

carrito = CarroCompras()

carrito.agregar_articulo("pan", 2.50)
carrito.agregar_articulo("leche", 3.00)
carrito.agregar_articulo("arroz", 4.50)

print("Artículos:")
print(carrito.articulos)

print("Total del carrito:")
print(carrito.total_carrito())

print("Artículos entre $2 y $3:")
print(carrito.articulos_por_rango(2, 3))
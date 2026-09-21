# EJERCICIO 40
# GESTOR DE PEDIDOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: clientes y valor de pedidos.
# Proceso: comparar montos y clasificarlos.
# Salida: clientes clasificados por pedido.


# PASO 2: BOSQUEJO
# Ana -> 25
# Luis -> 90
# Pedro -> 200
#
# Ana -> pequeño
# Luis -> mediano
# Pedro -> grande


# PASO 3: PATRÓN
# Se utiliza un diccionario:
# cliente -> monto.
# if/elif permite clasificar.
# set() elimina montos repetidos.


# PASO 4: CÓDIGO

class GestorPedidos:

    def pedidos_mayores(self, pedidos, monto):
        resultado = []

        for cliente, valor in pedidos.items():

            if valor > monto:
                resultado.append(cliente)

        return resultado

    def clasificar_pedidos(self, pedidos):
        grupos = {
            "pequeno": [],
            "mediano": [],
            "grande": []
        }

        for cliente, valor in pedidos.items():

            if valor < 50:
                grupos["pequeno"].append(cliente)

            elif valor < 150:
                grupos["mediano"].append(cliente)

            else:
                grupos["grande"].append(cliente)

        return grupos

    def montos_unicos(self, pedidos):
        return set(pedidos.values())


# PASO 5: PRUEBA

gestor = GestorPedidos()

pedidos = {
    "Ana": 25,
    "Luis": 90,
    "Pedro": 200,
    "Maria": 90
}

print(
    gestor.pedidos_mayores(
        pedidos,
        80
    )
)

print(
    gestor.clasificar_pedidos(
        pedidos
    )
)

print(
    gestor.montos_unicos(
        pedidos
    )
)
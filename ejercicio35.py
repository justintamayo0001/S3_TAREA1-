# EJERCICIO 35
# ANALIZADOR DE TEMPERATURAS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: temperaturas.
# Proceso: comparar con límites.
# Salida: temperaturas clasificadas.


# PASO 2: BOSQUEJO
# 15 -> fría
# 22 -> templada
# 30 -> caliente


# PASO 3: PATRÓN
# if/elif clasifica temperaturas.
# set() elimina valores repetidos.


# PASO 4: CÓDIGO

class AnalizadorTemperaturas:

    def temperaturas_altas(self, temperaturas, limite):
        resultado = []

        for temperatura in temperaturas:

            if temperatura > limite:
                resultado.append(temperatura)

        return resultado

    def clasificar_temperaturas(self, temperaturas):
        grupos = {
            "frias": [],
            "templadas": [],
            "calientes": []
        }

        for temperatura in temperaturas:

            if temperatura < 18:
                grupos["frias"].append(temperatura)

            elif temperatura <= 25:
                grupos["templadas"].append(temperatura)

            else:
                grupos["calientes"].append(temperatura)

        return grupos

    def temperaturas_unicas(self, temperaturas):
        return set(temperaturas)


# PASO 5: PRUEBA

analizador = AnalizadorTemperaturas()

temperaturas = [15, 22, 30, 18, 28, 22]

print(
    analizador.temperaturas_altas(
        temperaturas,
        25
    )
)

print(
    analizador.clasificar_temperaturas(
        temperaturas
    )
)

print(
    analizador.temperaturas_unicas(
        temperaturas
    )
)
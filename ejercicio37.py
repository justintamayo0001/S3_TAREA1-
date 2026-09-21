# EJERCICIO 37
# ANALIZADOR DE CORREOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: lista de correos electrónicos.
# Proceso: separar usuario y dominio.
# Salida: correos agrupados por dominio.


# PASO 2: BOSQUEJO
# ana@gmail.com
# juan@hotmail.com
# pedro@gmail.com
#
# gmail.com:
# ana@gmail.com
# pedro@gmail.com


# PASO 3: PATRÓN
# split("@") separa las partes.
# Un diccionario agrupa los dominios.
# Un conjunto guarda dominios únicos.


# PASO 4: CÓDIGO

class AnalizadorCorreos:

    def buscar_dominio(self, correos, dominio):
        resultado = []

        for correo in correos:

            if correo.endswith("@" + dominio):
                resultado.append(correo)

        return resultado

    def agrupar_por_dominio(self, correos):
        grupos = {}

        for correo in correos:

            partes = correo.split("@")

            if len(partes) == 2:

                dominio = partes[1]

                if dominio not in grupos:
                    grupos[dominio] = []

                grupos[dominio].append(correo)

        return grupos

    def dominios_unicos(self, correos):
        dominios = set()

        for correo in correos:

            partes = correo.split("@")

            if len(partes) == 2:
                dominios.add(partes[1])

        return dominios


# PASO 5: PRUEBA

analizador = AnalizadorCorreos()

correos = [
    "ana@gmail.com",
    "juan@hotmail.com",
    "pedro@gmail.com"
]

print(
    analizador.buscar_dominio(
        correos,
        "gmail.com"
    )
)

print(
    analizador.agrupar_por_dominio(
        correos
    )
)

print(
    analizador.dominios_unicos(
        correos
    )
)
# EJERCICIO 36
# AGENDA DE CONTACTOS


# PASO 1: ENTENDER EL PROBLEMA
# Entrada: nombres y teléfonos.
# Proceso: buscar y agrupar contactos.
# Salida: teléfono y listas agrupadas.


# PASO 2: BOSQUEJO
# Ana -> 0991111111
# Andres -> 0992222222
#
# Inicial A:
# Ana y Andres


# PASO 3: PATRÓN
# Se utiliza diccionario:
# nombre -> teléfono.
# Se agrupan nombres según su inicial.


# PASO 4: CÓDIGO

class AgendaContactos:

    def buscar_contacto(self, contactos, nombre):

        if nombre in contactos:
            return contactos[nombre]

        return "Contacto no encontrado"

    def agrupar_por_inicial(self, contactos):
        grupos = {}

        for nombre in contactos:

            inicial = nombre[0].upper()

            if inicial not in grupos:
                grupos[inicial] = []

            grupos[inicial].append(nombre)

        return grupos

    def telefonos_unicos(self, contactos):
        return set(contactos.values())


# PASO 5: PRUEBA

agenda = AgendaContactos()

contactos = {
    "Ana": "0991111111",
    "Andres": "0992222222",
    "Pedro": "0993333333"
}

print(agenda.buscar_contacto(contactos, "Ana"))
print(agenda.agrupar_por_inicial(contactos))
print(agenda.telefonos_unicos(contactos))
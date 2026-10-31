# Módulo de lotes
# Guarda los lotes y permite registrarlos, buscarlos y listarlos.

import validaciones

# Listas paralelas: la posición 0 de todas las listas es el MISMO lote.
# Ejemplo: codigos[0], urbanizaciones[0], areas[0]... son los datos del primer lote.
codigos = []
urbanizaciones = []
areas = []
precios_m2 = []
estados = []

# Aquí buscar_lote deja la posición del lote encontrado (-1 si no existe)
posicion_encontrada = [-1]


def registrar_lote(codigo, urbanizacion, area, precio):
    # Primero validamos los datos
    validaciones.validar_datos_lote(codigo, urbanizacion, area, precio, codigos)

    if validaciones.resultado_validacion[0] == True:
        # Si son válidos, agregamos un dato a cada lista
        codigos.append(codigo.strip())
        urbanizaciones.append(urbanizacion.strip())
        areas.append(int(area))
        precios_m2.append(int(precio))
        estados.append("Disponible")
        print("Lote", codigo.strip(), "registrado correctamente.")
    else:
        # Si no, mostramos el mensaje de error
        print(validaciones.resultado_validacion[1])


def buscar_lote(codigo):
    # Busca el código en la lista y guarda en qué posición está
    posicion_encontrada[0] = -1
    for i in range(len(codigos)):
        if codigos[i].upper() == codigo.strip().upper():
            posicion_encontrada[0] = i


def listar_lotes():
    # Muestra todos los lotes
    if len(codigos) == 0:
        print("No hay lotes registrados.")
    else:
        print("Código | Urbanización | Área (m2) | Precio/m2 | Estado")
        for i in range(len(codigos)):
            print(codigos[i], "|", urbanizaciones[i], "|", areas[i], "|", "S/", precios_m2[i], "|", estados[i])


def listar_disponibles():
    # Muestra solo los lotes cuyo estado es "Disponible"
    cantidad = 0
    for i in range(len(codigos)):
        if estados[i] == "Disponible":
            if cantidad == 0:
                # El encabezado se imprime una sola vez, antes del primer lote
                print("Código | Urbanización | Área (m2) | Precio/m2 | Estado")
            print(codigos[i], "|", urbanizaciones[i], "|", areas[i], "|", "S/", precios_m2[i], "|", estados[i])
            cantidad = cantidad + 1
    if cantidad == 0:
        print("No hay lotes disponibles.")


def marcar_como_vendido(posicion):
    # Cambia el estado del lote que está en esa posición
    estados[posicion] = "Vendido"


def cargar_datos_prueba():
    # Agrega los dos lotes de prueba que pide la guía
    codigos.append("LT-001")
    urbanizaciones.append("Los Jardines")
    areas.append(120)
    precios_m2.append(450)
    estados.append("Disponible")

    codigos.append("LT-002")
    urbanizaciones.append("Las Palmeras")
    areas.append(90)
    precios_m2.append(500)
    estados.append("Disponible")

# Programa principal: menú y coordinación
# Solo pide datos al usuario y llama a las funciones de los otros módulos.

import lotes
import ventas


def opcion_registrar_lote():
    codigo = input("Código del lote: ")
    urbanizacion = input("Urbanización: ")
    area = input("Área (m2): ")
    precio = input("Precio por m2 (S/): ")
    lotes.registrar_lote(codigo, urbanizacion, area, precio)


def opcion_vender_lote():
    codigo = input("Código del lote a vender: ")
    nombre = input("Nombre del comprador: ")
    documento = input("Documento de identidad: ")
    ventas.registrar_venta(codigo, nombre, documento)


def menu():
    # Cargamos los 2 lotes de prueba al iniciar
    lotes.cargar_datos_prueba()

    opcion = ""
    # El menú se repite hasta que el usuario elija 6
    while opcion != "6":
        print("")
        print("=== TERRENOS DEL NORTE S.A.C. ===")
        print("1. Registrar lote")
        print("2. Listar todos los lotes")
        print("3. Listar lotes disponibles")
        print("4. Vender lote")
        print("5. Ver resumen de ventas")
        print("6. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            opcion_registrar_lote()
        elif opcion == "2":
            lotes.listar_lotes()
        elif opcion == "3":
            lotes.listar_disponibles()
        elif opcion == "4":
            opcion_vender_lote()
        elif opcion == "5":
            ventas.listar_ventas()
        elif opcion == "6":
            print("Hasta pronto.")
        else:
            print("Opción no válida.")


# Aquí empieza el programa
menu()

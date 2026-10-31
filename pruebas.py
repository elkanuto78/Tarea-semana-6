# Pruebas del sistema de venta de lotes

import calculos
import lotes
import ventas

# contador[0] = pruebas correctas, contador[1] = pruebas totales
contador = [0, 0]


def verificar(nombre, condicion):
    contador[1] = contador[1] + 1
    if condicion:
        contador[0] = contador[0] + 1
        print("[OK]", nombre)
    else:
        print("[FALLO]", nombre)


def probar_lote_invalido(nombre, codigo, urbanizacion, area, precio):
    # Intenta registrar un lote inválido y verifica que NO se haya guardado
    cantidad_antes = len(lotes.codigos)
    lotes.registrar_lote(codigo, urbanizacion, area, precio)
    verificar(nombre + " -> rechazado", len(lotes.codigos) == cantidad_antes)


print("--- Prueba 1: registro correcto ---")
lotes.cargar_datos_prueba()
verificar("Se registraron LT-001 y LT-002", len(lotes.codigos) == 2)
verificar("Estado inicial Disponible", lotes.estados[0] == "Disponible" and lotes.estados[1] == "Disponible")
lotes.registrar_lote("LT-003", "El Sol", "200", "300")
verificar("Lote LT-003 registrado", len(lotes.codigos) == 3)

print("")
print("--- Prueba 2: cálculos (LT-001) ---")
calculos.calcular_precio_total(120, 450)
calculos.calcular_cuota_inicial()
calculos.calcular_saldo()
verificar("Total = 54000", calculos.resultados[0] == 54000)
verificar("Cuota inicial = 10800", calculos.resultados[1] == 10800)
verificar("Saldo = 43200", calculos.resultados[2] == 43200)

print("")
print("--- Prueba 3: datos inválidos ---")
probar_lote_invalido("Código vacío", "", "Los Jardines", "100", "400")
probar_lote_invalido("Urbanización vacía", "LT-010", "  ", "100", "400")
probar_lote_invalido("Área cero", "LT-011", "Los Jardines", "0", "400")
probar_lote_invalido("Área negativa", "LT-012", "Los Jardines", "-5", "400")
probar_lote_invalido("Área no numérica", "LT-013", "Los Jardines", "abc", "400")
probar_lote_invalido("Precio cero", "LT-014", "Los Jardines", "100", "0")
probar_lote_invalido("Código repetido", "LT-001", "Otra", "100", "400")
ventas.registrar_venta("LT-002", "", "123")
verificar("Comprador sin nombre -> rechazado", len(ventas.lotes_vendidos) == 0)
ventas.registrar_venta("LT-999", "Ana", "123")
verificar("Lote inexistente -> rechazado", len(ventas.lotes_vendidos) == 0)

print("")
print("--- Prueba 4: venta y venta duplicada ---")
ventas.registrar_venta("LT-001", "Ana Torres", "12345678")
verificar("Venta de LT-001 registrada", len(ventas.lotes_vendidos) == 1)
verificar("LT-001 pasó a Vendido", lotes.estados[0] == "Vendido")
verificar("Total, cuota y saldo guardados",
          ventas.precios_totales[0] == 54000 and ventas.cuotas_iniciales[0] == 10800 and ventas.saldos[0] == 43200)
ventas.registrar_venta("LT-001", "Luis Perez", "87654321")
verificar("Segunda venta de LT-001 bloqueada", len(ventas.lotes_vendidos) == 1)

print("")
print("--- Resumen de ventas ---")
ventas.listar_ventas()

print("")
print("Resultado:", contador[0], "de", contador[1], "verificaciones correctas")

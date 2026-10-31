# Módulo de cálculos
# Se encarga solo de las cuentas de una venta.

PORCENTAJE_CUOTA_INICIAL = 0.20

# Lista donde guardamos los resultados (como las funciones no usan return,
# dejan sus respuestas aquí):
#   resultados[0] = precio total
#   resultados[1] = cuota inicial
#   resultados[2] = saldo
resultados = [0, 0, 0]


def calcular_precio_total(area, precio_m2):
    # precio total = área x precio por m2
    resultados[0] = area * precio_m2


def calcular_cuota_inicial():
    # cuota inicial = 20 % del precio total (que ya está en resultados[0])
    resultados[1] = resultados[0] * PORCENTAJE_CUOTA_INICIAL


def calcular_saldo():
    # saldo = precio total - cuota inicial
    resultados[2] = resultados[0] - resultados[1]

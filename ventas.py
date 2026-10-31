# Módulo de ventas
# Registra las ventas y muestra el resumen.

import calculos
import lotes
import validaciones

# Listas paralelas: la posición 0 de todas es la MISMA venta.
lotes_vendidos = []
compradores = []
documentos = []
precios_totales = []
cuotas_iniciales = []
saldos = []


def registrar_venta(codigo_lote, nombre, documento):
    # Paso 1: validar los datos del comprador
    validaciones.validar_comprador(nombre, documento)

    if validaciones.resultado_validacion[0] == False:
        print(validaciones.resultado_validacion[1])
    else:
        # Paso 2: buscar el lote y validar que exista y esté disponible
        lotes.buscar_lote(codigo_lote)
        posicion = lotes.posicion_encontrada[0]
        validaciones.validar_condiciones_venta(posicion, lotes.estados)

        if validaciones.resultado_validacion[0] == False:
            print(validaciones.resultado_validacion[1])
        else:
            # Paso 3: calcular precio total, cuota inicial y saldo
            calculos.calcular_precio_total(lotes.areas[posicion], lotes.precios_m2[posicion])
            calculos.calcular_cuota_inicial()
            calculos.calcular_saldo()

            # Paso 4: guardar la venta (un dato en cada lista)
            lotes_vendidos.append(lotes.codigos[posicion])
            compradores.append(nombre.strip())
            documentos.append(documento.strip())
            precios_totales.append(calculos.resultados[0])
            cuotas_iniciales.append(calculos.resultados[1])
            saldos.append(calculos.resultados[2])

            # Paso 5: cambiar el estado del lote a "Vendido"
            # (así no se puede vender dos veces: el paso 2 lo bloqueará)
            lotes.marcar_como_vendido(posicion)
            print("Venta del lote", lotes.codigos[posicion], "registrada correctamente.")


def listar_ventas():
    # Muestra el resumen de ventas
    if len(lotes_vendidos) == 0:
        print("Aún no hay ventas registradas.")
    else:
        for i in range(len(lotes_vendidos)):
            print("Lote", lotes_vendidos[i], "|", compradores[i], "(" + documentos[i] + ")",
                  "| Total: S/", precios_totales[i],
                  "| Cuota inicial: S/", cuotas_iniciales[i],
                  "| Saldo: S/", saldos[i])

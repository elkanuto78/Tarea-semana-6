# Sistema de Venta de Lotes

Proyecto de la **Sesión 11 – Programación modular** (Introducción a la programación modular y reutilización).
Empresa ficticia: **Terrenos del Norte S.A.C.**

## Objetivo

Sistema de consola que permite registrar lotes y ventas, con el código separado en módulos según su responsabilidad. Así es más fácil de modificar, probar y trabajar en equipo.

## Requisitos

- Python 3
- Editor: Visual Studio Code
- No necesita instalar librerías adicionales.

## Cómo ejecutar

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```
python main.py
```

Para correr las pruebas automáticas:

```
python pruebas.py
```

## Menú del sistema

```
1. Registrar lote
2. Listar todos los lotes
3. Listar lotes disponibles
4. Vender lote
5. Ver resumen de ventas
6. Salir
```

Al iniciar se cargan dos lotes de prueba: LT-001 (Los Jardines, 120 m², S/ 450 por m²) y LT-002 (Las Palmeras, 90 m², S/ 500 por m²).

## Modularización

| Archivo | Responsabilidad |
|---|---|
| `lotes.py` | Registrar lotes, listarlos, buscarlos y consultar disponibilidad |
| `validaciones.py` | Validar datos del lote, datos del comprador y condiciones de venta |
| `ventas.py` | Registrar la venta, cambiar el estado del lote a «Vendido» y mostrar el resumen |
| `calculos.py` | Precio total, cuota inicial (20 %) y saldo |
| `main.py` | Menú y coordinación; no contiene lógica de negocio |
| `pruebas.py` | Pruebas automáticas con casos válidos e inválidos |

Dependencias entre módulos: `main` usa `lotes` y `ventas`; `ventas` usa `lotes`, `validaciones` y `calculos`; `lotes` usa `validaciones`. `calculos` y `validaciones` no dependen de ningún otro.

### Datos y funciones

Los datos se guardan en listas paralelas (la posición 0 de todas las listas corresponde al mismo lote o venta). Las funciones no usan `return`: imprimen directamente o dejan su resultado en una lista pequeña (`res`, `val`, `pos`).

**Lotes:** `cod` = códigos, `urb` = urbanizaciones, `are` = áreas, `pm2` = precios por m², `est` = estados.
**Ventas:** `lot` = lotes vendidos, `com` = compradores, `doc` = documentos, `pt` = precios totales, `ci` = cuotas iniciales, `sal` = saldos.

Cada módulo tiene al inicio una leyenda con sus acrónimos. Resumen:

| Módulo | Funciones |
|---|---|
| `calculos.py` | `Pt` = calcular_precio_total, `Ci` = calcular_cuota_inicial, `Sa` = calcular_saldo |
| `validaciones.py` | `Vdl` = validar_datos_lote, `Vc` = validar_comprador, `Vcv` = validar_condiciones_venta |
| `lotes.py` | `Rl` = registrar_lote, `Bl` = buscar_lote, `Ll` = listar_lotes, `Ld` = listar_disponibles, `Mcv` = marcar_como_vendido, `Cdp` = cargar_datos_prueba |
| `ventas.py` | `Rv` = registrar_venta, `Lv` = listar_ventas |
| `main.py` | `Orl` = opcion_registrar_lote, `Ovl` = opcion_vender_lote, `Mn` = menu |

## Reglas de negocio

- Cada lote tiene código único, urbanización, área (m²), precio por m² y estado inicial «Disponible».
- El código y la urbanización no pueden estar vacíos; el área y el precio deben ser enteros mayores que cero; no se repiten códigos.
- Una venta requiere un lote existente y disponible, y el nombre y documento del comprador.
- Precio total = área × precio por m². Cuota inicial = 20 % del total. Saldo = total − cuota inicial.
- Al vender, el lote pasa a «Vendido» y no se puede vender otra vez.

## Pruebas

Se ejecutan con `python pruebas.py`. Resultado: **19 de 19 verificaciones correctas**.

| # | Prueba | Resultado esperado |
|---|---|---|
| 1 | Registro correcto de lotes | Lotes guardados con estado «Disponible» |
| 2 | Cálculo para LT-001 | Total S/ 54 000, cuota inicial S/ 10 800, saldo S/ 43 200 |
| 3 | Datos inválidos (vacíos, área o precio ≤ 0, no numéricos, código repetido, comprador sin datos, lote inexistente) | Se rechazan y no se guardan |
| 4 | Venta duplicada de LT-001 | La primera venta se registra; la segunda se bloquea («El lote ya está vendido») |

Evidencias: `evidencia_pruebas.txt` (salida de las pruebas) y `evidencia_menu.txt` (recorrido del menú).

## Limitaciones

- Los datos viven en memoria: al cerrar el programa se pierden.
- El área y el precio por m² deben ser números enteros.

## Repositorio
https://github.com/elkanuto78/Tarea-semana-6

# Módulo de validaciones
# Revisa que los datos estén bien antes de guardarlos o venderlos.

# Lista donde cada función deja su respuesta:
#   resultado_validacion[0] = True si todo está bien, False si hay un error
#   resultado_validacion[1] = mensaje que explica el resultado
resultado_validacion = [True, ""]


def validar_datos_lote(codigo, urbanizacion, area, precio, codigos):
    # Revisa los datos de un lote nuevo.
    # "area" y "precio" llegan como texto (porque vienen de input()).
    # "codigos" es la lista de códigos ya registrados.

    # Empezamos suponiendo que todo está bien
    resultado_validacion[0] = True
    resultado_validacion[1] = "Datos válidos."

    # ¿El código ya existe? Recorremos la lista de códigos registrados
    repetido = False
    for i in range(len(codigos)):
        if codigos[i].upper() == codigo.strip().upper():
            repetido = True

    # Ahora revisamos los errores, uno por uno, en orden
    if codigo.strip() == "" or urbanizacion.strip() == "":
        resultado_validacion[0] = False
        resultado_validacion[1] = "El código y la urbanización son obligatorios."
    elif repetido == True:
        resultado_validacion[0] = False
        resultado_validacion[1] = "El código ya existe."
    elif area.strip().isdigit() == False:
        # isdigit() es False si el texto tiene letras, signo menos, punto o está vacío
        resultado_validacion[0] = False
        resultado_validacion[1] = "El área debe ser un número entero mayor que cero."
    elif int(area) <= 0:
        resultado_validacion[0] = False
        resultado_validacion[1] = "El área debe ser un número entero mayor que cero."
    elif precio.strip().isdigit() == False:
        resultado_validacion[0] = False
        resultado_validacion[1] = "El precio por m2 debe ser un número entero mayor que cero."
    elif int(precio) <= 0:
        resultado_validacion[0] = False
        resultado_validacion[1] = "El precio por m2 debe ser un número entero mayor que cero."


def validar_comprador(nombre, documento):
    # Revisa que el nombre y el documento del comprador no estén vacíos
    resultado_validacion[0] = True
    resultado_validacion[1] = "Datos válidos."
    if nombre.strip() == "" or documento.strip() == "":
        resultado_validacion[0] = False
        resultado_validacion[1] = "El nombre y el documento del comprador son obligatorios."


def validar_condiciones_venta(posicion, estados):
    # Revisa que el lote exista y esté disponible.
    # "posicion" es el lugar del lote en las listas (-1 significa que no se encontró).
    resultado_validacion[0] = True
    resultado_validacion[1] = "El lote está disponible."
    if posicion == -1:
        resultado_validacion[0] = False
        resultado_validacion[1] = "El lote no existe."
    elif estados[posicion] != "Disponible":
        resultado_validacion[0] = False
        resultado_validacion[1] = "El lote ya está vendido."

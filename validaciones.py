#VALIDACIÓN DE PALABRAS
def validarStr(palabra, msg):
    while palabra.isnumeric():
        palabra = input(msg)
    return palabra

#VALIDACIÓN DE NÚMEROS
def validarNum(num, msg):
    while not num.isnumeric():
        num = input(msg)
    return int(num)

#VALIDACIÓN DE OPCIONES NUMÉRICAS
def validarOpcionesNum(opcion, msg, num):
    while not opcion.isnumeric() or int(opcion) > num or int(opcion)<= 0:
        opcion = input(msg)
    return opcion

#VALIDACIÓN ENTRADAS G & V
def validarCompraEntradas(opcion, letra):
    while opcion.isnumeric() or opcion != 'G' and opcion != 'V':
        opcion = input(letra)
    return opcion

#VALIDACIÓN Y & N
def validarYesOrNo(opcion, letra):
    while opcion.isnumeric() or opcion != 'Y' and opcion != "N":
        opcion = input(letra)
    return opcion
        


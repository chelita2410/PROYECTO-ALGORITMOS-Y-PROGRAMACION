#IMPORTS
from usuario import *
from entradas import *
from modulo2 import *
from partidos import *
from entradas import *
from validaciones import *

entradasUsadas = []

#VERIFICACION DE ENTRADAS USADAS/FALSAS 
def asistencia (clientesTotales):
    cliente = 0
    while cliente == 0:
        cedula = input("Introduzca su número de cédula: ")
        cedula = validarNum(cedula, "Introduzca su número de cédula: ")

        for i in clientesTotales:
            if i.cedula == cedula:
                cliente = i
    id = input("Introduzca el ID asignado al momento de compra de su entrada: ")
    id = validarNum(id, "Introduzca el ID asignado al momento de compra de su entrada: ")
    for i in clientesTotales:
        if cedula == i.cedula:
            for j in i.entradas:
                if j.id == id:
                    print("Bienvenido a la Eurocopa!")
                    j.partidoEscogido.entradas_usadas.append(j)
                    entradasUsadas.append(j.id)
                    j.usadas = True
                    return cliente, j
            print("Su entrada no es válida")
    return cliente, 0
                
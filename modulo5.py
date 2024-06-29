#IMPORTS
from restaurantes import *
from productos import *
from modulo1 import *
from modulo2 import *
from validaciones import *

#VERIFICACIÓN DE CLIENTE VIP
def compraProductos(estadio, clientesTotales, gastos_vip):
    cedula = input("Introduce tu cédula: ")
    cedula = validarNum(cedula, "Introduce tu cédula: ")
    edad = input("Introduce tu edad: ")
    edad = validarNum(edad, "Introduce tu edad: ")
    for i in clientesTotales: 
        if cedula == i.cedula:
           for j in i.entradas:
               if j.usadas == True:
                   print("Bienvenido al restaurante!")

#VERIFICACIÓN DE EDAD PARA BEBIDAS ALCOHÓLICAS
    for i in estadio.restaurants:
        for r in i.products:
            if edad < 18 and r.tipo != "non-alcoholic":
                print(r.show())
            elif edad> 18 or r.tipo != "non-alcoholic":
                print(r.show())

#COMPRAR PRODUCTOS
    carrito = []
    precioTotal = 0
    while True:
        comidaQuiere = input("Qué productos deseas comprar?: ")
        comidaQuiere = validarStr(comidaQuiere, "Qué productos deseas comprar?: ")
        for i in estadio.restaurants:
            for r in i.products:
                if comidaQuiere == r.name:
                    carrito.append(r)
                    r.stock -= 1
                    r.comprados += 1
                    precioTotal += r.price
        masComida = input("Deseas pedir más comida? [Y/N]: ")
        masComida = validarYesOrNo(masComida, "Deseas pedir más comida? [Y/N]: ")
        if masComida == 'N':
            break

#DESCUENTOS E IMPRESIÓN DE FACTURA
    if numPerfecto(cedula):
        desc = precioTotal * 0.15
    else:
        desc = 0
    iva = precioTotal*0.16
    gastos_vip += precioTotal - desc + iva
    print(f'''
== FACTURA ==
SUBTOTAL: {precioTotal}
DESCUENTO: {desc}
IVA: {iva}
TOTAL: {precioTotal - desc + iva}
''')

#VERIFICAR SI LA CÉDULA ES UN NÚMERO PERFECTO   
def numPerfecto(cedula):
    counter = 0 
    for x in range (1, cedula//2 +1):
        if cedula % x == 0:
            counter += x
    if counter == cedula:
        print(f"Por ser tu número de cédula {cedula} te ganaste un descuento del 15% en todos nuestros productos! ")
        return True
    else:
        return False

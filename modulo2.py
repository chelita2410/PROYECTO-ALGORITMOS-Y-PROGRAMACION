#IMPORTS
from modulo1 import *
from entradas import *
from usuario import *
from entradas import *
from validaciones import *

#COMPRA DE ENTRADAS
def comprarEntrada(equiposTotales, partidosTotales, estadiosTotales, clientesTotales, gastos_vip):
    nombre = input("NOMBRE: ")
    nombre = validarStr(nombre, "NOMBRE: ")
    cedula = input("CÉDULA: ")
    cedula = validarNum(cedula, "CÉDULA: ")
    descuentoNumVamp = 0

    if numeroVampiro(cedula):
        descuentoNumVamp = precioEntrada * 0.5
    
    edad = input("EDAD: ")
    edad = validarNum(edad, "EDAD: ")

    for partido in partidosTotales: 
        print(partido.show() )
    partido = input("QUÉ PARTIDO DESEAS VER?: ")
    partido = validarNum(partido, "QUÉ PARTIDO DESEAS VER?: ")

    for p in partidosTotales:
        if p.number == partido:
            partido = p
            break

    entrada = input("QUÉ ENTRADA DESEAS COMPRAR? [escribe 'G' para general o 'V' para VIP]: ").upper()
    entrada = validarCompraEntradas(entrada, "QUÉ ENTRADA DESEAS COMPRAR? [escribe 'G' para general o 'V' para VIP]: ")
    if entrada == "G":
        precioEntrada = 35

#MAPA CON LAS FILAS
        y = 12
        fila = ""
        for x in range(partido.stadium_id.capacity[0]):
            if y > 0:
                fila += str(x) + " "
                y-=1
            else:
                print(fila)
                fila = ""
                y = 12
        print(fila)

    elif entrada == "V":
        precioEntrada = 75
    iva = calcularIVA(precioEntrada)
    nuevoCliente = Usuario(nombre, edad, cedula)

    nuevaEntrada = Entradas(entrada, nuevoCliente, 9, partido)

    print(f"""
== FACTURA ==
ENTRADA: {entrada}
ID DE TU ENTRADA: {nuevaEntrada.id}
DESCUENTO: {descuentoNumVamp}
PRECIO: {precioEntrada}
IVA: {iva}
PRECIO TOTAL: {precioEntrada + iva - descuentoNumVamp}
""")
    
    nuevoCliente.entradas.append(nuevaEntrada)
    
    clientesTotales.append(nuevoCliente)

    pago = input("Deseas proceder a pagar? [Y/N] ")
    pago = validarYesOrNo(pago, "Deseas proceder a pagar? [Y/N] ")
    
    if pago == 'Y':
        print("Tu pago fue procesado correctamente!")
        partido.entradas_vendidas += 1
        if entrada == "V":
            gastos_vip += (precioEntrada + iva - descuentoNumVamp)



#CÁLCULO NÚMEROS VAMPIRO
def numeroVampiro(num):
    factores = []
    stn = []

    for a in str(num):
        stn.append(a)
    for i in range(1, num//2 + 1):
        if num % i == 0:
            factores.append(i)
    eliminados = []

    for n in factores:
        esta = True
        aux = str(n)
        for l in aux:
            if l not in stn:
                esta = False
                break
        if not esta:
            eliminados.append(n)

    for n in eliminados:
        factores.remove(n)
    eliminados = []

    for n in range(len(factores)):
        if len(str(factores[n])) != len(stn) /2:
                eliminados.append(factores[n])

    for n in eliminados:
        factores.remove(n)
    colmillos = []

    for i in range(len(factores)-1):
        for j in range(i, len(factores)):
            if factores[i] * factores[j] == num:
                colmillos.append([factores[i], factores[j]])

    if len(colmillos) > 0:
        return True
    return False


#CÁLCULO DEL IVA
def calcularIVA(precio):
    iva = (precio) * 0.16
    return iva

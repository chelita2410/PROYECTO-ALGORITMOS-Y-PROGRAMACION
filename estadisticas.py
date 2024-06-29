#IMPORTS
from modulo1 import *
from modulo2 import *
from modulo3 import *
from modulo4 import *
from modulo5 import *
from entradas import *
from equipos import *
from estadios import *
from partidos import *
from productos import *
from restaurantes import *
from usuario import *

#PROMEDIO GASTO CLIENTE VIP
def promedioVIP (gastos_vip):
    print(f"EL PROMEDIO DE GASTO DE LOS CLIENTES VIP ES DE: {gastos_vip}")

#ASISTENCIA A LOS PARTIDOS
def promedioAsistencia(partidosTotales): 
    mayor_asistencia = []
    for partido in partidosTotales:
        mayor = partido
        for p in partidosTotales:
            if p not in mayor_asistencia and len(p.entradas_usadas) > len(mayor.entradas_usadas):
                mayor = p
        mayor_asistencia.append(mayor)
    print(f"EL ORDEN DE PARTIDOS DE ACUERDO A SUS ENTRADAS USADAS ES: {mayor_asistencia}")
    for i in partidosTotales: 
        print(f"""LOS EQUIPOS QUE JUGARON FUERON: {i.home.name} VS {i.away.name}
NOMBRE DEL STADIUM: {i.stadium_id.name}
FECHA: {i.date}
ENTRADAS VENDIDAS:{i.entradas_vendidas}
ENTRADAS QUE FUERON USADAS: {len(i.entradas_usadas)}
-----------------------------------------------------------------------""")

#MAYOR ASISTENCIA
def mayorAsistencia(partidosTotales):
    partidoMayorAsistencia = partidosTotales[0]
    for p in partidosTotales: 
        if len(p.entradas_usadas) > len(partidoMayorAsistencia.entradas_usadas):
            partidoMayorAsistencia = p 
    print(f"EL PARTIDO CON MAYOR ASISTENCIA FUE: {partidoMayorAsistencia.home.name} - {partidoMayorAsistencia.away.name}")

#MÁS BOLETOS VENDIDOS
def mayorVendidos(partidosTotales):
    partidoMayorVendidos = partidosTotales[0]
    for t in partidosTotales:
        if t.entradas_vendidas > partidoMayorVendidos.entradas_vendidas:
            partidoMayorVendidos = t
    print(f"EL PARTIDO CON MAYOR CANTIDAD DE ENTRADAS VENDIDAS FUE: {partidoMayorVendidos.home.name} - {partidoMayorVendidos.away.name}")

#TOP 3 PRODUCTOS RESTAURANTE
def masVendidosRestaurante(estadiosTotales):
    topRestaurante = []
    for stadium in estadiosTotales:
        for restaurant in stadium.restaurants:
            for product in restaurant.products:
                topRestaurante.append(product)
    top = []
    for i in range(3):
        masVendido = topRestaurante[0]
        for p in topRestaurante:
            if p.comprados > masVendido.comprados and p not in top:
                masVendido = p 
        top.append(masVendido)
    print(f'''EL TOP 3 PRODUCTOS MÁS VENDIDOS ES:
1. {topRestaurante[0].name} con {topRestaurante[0].comprados} vendidos
2. {topRestaurante[1].name} con {topRestaurante[1].comprados} vendidos
3. {topRestaurante[2].name} con {topRestaurante[2].comprados} vendidos
''')
    
#TOP 3 CLIENTES
def masCompradosClientes(clientesTotales):
    topClientes = []
    for cliente in clientesTotales:
        mayor = cliente
        for c in clientesTotales:
            if c not in topClientes and len(c.entradas) > len(mayor.entradas):
                mayor = c
        topClientes.append(mayor)
    print(f'''
LOS 3 CLIENTES QUE MÁS ENTRADAS COMPRARON FUERON:
1. {topClientes[0].name} con {len(topClientes[0].entradas)} compradas
2. {topClientes[1].name} con {len(topClientes[1].entradas)} compradas
3. {topClientes[2].name} con {len(topClientes[2].entradas)} compradas
''')




        
                        
        




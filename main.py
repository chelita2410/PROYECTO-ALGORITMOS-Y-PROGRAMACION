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
from estadisticas import *
from validaciones import *
import pickle

equiposTotales = []
partidosTotales = []
estadiosTotales = []
clientesTotales = []
gastos_vip = 0 

#TXT
def guardar(equiposTotales, partidosTotales, estadiosTotales, clientesTotales):
    with open("equipos.txt", "wb") as f:
        pickle.dump(equiposTotales, f)
    with open("partidos.txt", "wb") as f:
        pickle.dump(partidosTotales, f)
    with open("estadios.txt", "wb") as f:
        pickle.dump(estadiosTotales, f)
    with open("clientes.txt", "wb") as f:
        pickle.dump(clientesTotales, f)

def leer():
    try:
        with open("equipos.txt", "rb") as f:
            equiposTotales = pickle.load(f)
        with open("partidos.txt", "rb") as f:
            partidosTotales = pickle.load(f)
        with open("estadios.txt", "rb") as f:
            estadiosTotales = pickle.load(f)
        with open("clientes.txt", "rb") as f:
            clientesTotales = pickle.load(f)
        return equiposTotales, partidosTotales, estadiosTotales, clientesTotales
    except:
        return [], [], [], []
    

#MENÚ
while True:
    equiposTotales, partidosTotales, estadiosTotales, clientesTotales = leer()
    if equiposTotales == []:
        ejecutarAPI(equiposTotales, partidosTotales, estadiosTotales)
    print(f'''
== BIENVENIDO A LA EURO2024 ==
1. Buscar partidos.
2. Comprar entradas.
3. Entrar al partido.
4. Ver estadísticas.
5. Salir.
''')
    ans = input("Presiona el número de la acción que deseas realizar: ")
    ans = validarOpcionesNum(ans, "Presiona el número de la acción que deseas realizar: ", 5)
    if ans == '1':
        print("== BÚSQUEDA DE PARTIDOS ==")
        buscarPartido(equiposTotales, partidosTotales, estadiosTotales)
    elif ans == '2':
        print("== COMPRA DE ENTRADAS ==")
        comprarEntrada(equiposTotales, partidosTotales, estadiosTotales, clientesTotales, gastos_vip)
        guardar(equiposTotales, partidosTotales, estadiosTotales, clientesTotales)
    elif ans == '3':
        print("== ENTRAR AL PARTIDO ==")
        cliente, entrada = asistencia(clientesTotales)
        guardar(equiposTotales, partidosTotales, estadiosTotales, clientesTotales)
        if entrada != 0:
            while True:
                print(f'''
1. Buscar productos.
2. Comprar productos
3. Salir.
''')
                seleccion = input("Qué deseas hacer?: ")
                seleccion = validarOpcionesNum(seleccion, 'Qué deseas hacer?: ', 3)
                if seleccion == '1':
                    buscarProductosMenu(entrada.partidoEscogido.stadium_id)
                elif seleccion == '2':
                    compraProductos(entrada.partidoEscogido.stadium_id, clientesTotales, gastos_vip)
                    guardar(equiposTotales, partidosTotales, estadiosTotales, clientesTotales)
                elif seleccion == '3':
                    print("Gracias por su visita!")
                    break
                else:
                    print("Selección inválida, inténtelo nuevamente.")
                    
    elif ans == '4':
        print("== VER ESTADÍSTICAS ==")
        while True:
            print(f'''
1. Promedio de gasto VIP.
2. Promedio de asistencia a los partidos.
3. Partido con mayor asistencia.
4. Partido con más entradas vendidas.
5. Top 3 productos más vendidos del restaurante.
6. Top 3 clientes con más entradas compradas.
7. Salir.
''')
            sel = input("Qué deseas hacer?: ")
            sel = validarOpcionesNum(sel, 'Qué deseas hacer?: ', 7)
            if sel == '1':
                promedioVIP (gastos_vip)
            elif sel == '2':
                promedioAsistencia(partidosTotales)
            elif sel == '3':
                mayorAsistencia(partidosTotales)
            elif sel == '4':
                mayorVendidos(partidosTotales)
            elif sel == '5':
                masVendidosRestaurante(estadiosTotales)
            elif sel == '6':
                masCompradosClientes(clientesTotales)
            elif seleccion == '7':
                print("Gracias por su visita!")
                break
            else:
                print("Selección inválida, inténtelo nuevamente.")
                
    elif ans == '5':
        print("== GRACIAS POR SU VISITA ==")
        break
    else:
        print("Selección inválida, inténtelo nuevamente")
        ans = ("Presiona el número de la acción que deseas realizar: ")



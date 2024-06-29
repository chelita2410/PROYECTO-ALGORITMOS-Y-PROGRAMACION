#IMPORTS 
import requests
from equipos import Equipos
from partidos import Partidos
from estadios import Estadios
from restaurantes import Restaurants
from productos import Products
from validaciones import *


#APIS
partidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()
equipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
estadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()


#EJECUCIÓN DE LAS APIS
def ejecutarAPI(equiposTotales, partidosTotales, estadiosTotales):
    
    #APIS
    partidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()
    equipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
    estadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()

    for equipo in equipos:
        nuevoEquipo = Equipos(equipo["name"], equipo["id"], equipo["code"], equipo["group"])
        equiposTotales.append(nuevoEquipo)

    for estadio in estadios: 
        restaurantsTotales = []
        for restaurant in estadio["restaurants"]:
            productosTotales = []
            for product in restaurant["products"]:
                if product["adicional"] == "alcoholic" or product["adicional"] == "non-alcoholic":
                    clasificacion = "Bebida"
                else:
                    clasificacion = "Comida"
                nuevoProducto = Products(product["name"],int( product["quantity"]), float(product["price"]), int(product["stock"]), clasificacion, product["adicional"])
                productosTotales.append(nuevoProducto)
            nuevoRestaurante = Restaurants(restaurant["name"], productosTotales)
            restaurantsTotales.append(nuevoRestaurante)        
        nuevoEstadio = Estadios(estadio["id"], estadio["name"], estadio["city"], estadio["capacity"], restaurantsTotales)
        estadiosTotales.append(nuevoEstadio)


    for partido in partidos:
        for equipo in equiposTotales:
            if equipo.id == partido["home"]["id"]:
                home = equipo
            elif equipo.id == partido["away"]["id"]:
                away = equipo
        for estadio in estadiosTotales:
            if estadio.id == partido["stadium_id"]:
                stadium = estadio
        nuevoPartido = Partidos(partido["number"], partido["id"], home, away, partido["date"], partido["group"], stadium)
        partidosTotales.append(nuevoPartido)

#BUSCAR PARTIDOS DE UN PAIS
def buscarPartido(equiposTotales, partidosTotales, estadiosTotales):
    print("== BUSCAR ==")

    while True:
        print('''
1. Todos los partidos de un país.
2. Todos los partidos de un estadio.
3. Todos los partidos de una fecha. 
4. Salir''')
        seleccion = input("Qué deseas hacer?: ")
        seleccion = validarOpcionesNum(seleccion, 'Qué deseas hacer?: ', 4)
       
        if seleccion == '1':
            pais = input("Qué país deseas ver? (Escribe el nombre en código): ").upper()
            for partido in partidosTotales:
                if pais == partido.home.code or pais == partido.away.code:
                    print(partido.show())
        elif seleccion == '2':
            estadio = input("Qué estadio deseas ver?:")
            for partido in partidosTotales:
                if estadio == partido.stadium_id.name:
                    print(partido.show())
        elif seleccion == '3':
            fecha = input("Qué fecha deseas ver?:")
            for partido in partidosTotales:
                if fecha == partido.date:
                    print(partido.show())
        else:
            break

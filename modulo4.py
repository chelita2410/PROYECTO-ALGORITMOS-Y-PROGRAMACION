#IMPORTS
from restaurantes import *
from productos import *
from modulo1 import *
from modulo2 import *
from validaciones import *

#BUSCAR PRODUCTOS:
def buscarProductosMenu(estadio):
    print("== BUSCAR PRODUCTOS ==")
    while True:
        cont = 1
        for r in estadio.restaurants:
            print(f"{cont} {r.name}")
            cont +=1
        restaurante = input("Selecciona el numero del restaurante donde deseas buscar: ")
        restaurante = validarOpcionesNum(restaurante, "Selecciona el numero del restaurante donde deseas buscar: ", cont)
        restaurante = estadio.restaurants[int(restaurante)-1]
        print('''
1. Por nombre
2. Por tipo
3. Por precio
4. Salir
''')
        seleccion = input("Cómo deseas buscar?: ")
        seleccion = validarOpcionesNum (seleccion, 'Cómo deseas buscar?: ', 3)
        if seleccion == "1": 
            buscarNombre(restaurante)
        elif seleccion == "2":
            buscarTipo(restaurante)
        elif seleccion == "3": 
            buscarPrecio(restaurante)
        else:
            break

#FUNCIÓN BUSCAR POR NOMBRE
def buscarNombre(restaurante):
    productoBuscado = input("Qué producto deseas obtener?: ")
    productoBuscado = validarStr(productoBuscado, "Qué producto deseas obtener?: ")

    for i in restaurante.products:
        if productoBuscado == i.name:
            print(i.show)

#FUNCIÓN BUSCAR POR TIPO
def buscarTipo(restaurante):
    productoBuscado = input("Qué tipo de producto deseas buscar \n 1. Bebidas \n 2. Alimentos")
    productoBuscado = validarNum(productoBuscado, "Qué tipo de producto deseas buscar \n 1. Bebidas \n 2. Alimentos")

    if productoBuscado == '1':
        for i in restaurante.products:
            if productoBuscado == i.tipo:
                print(i.show)
    elif productoBuscado == '2':
        for i in restaurante.products:
            if productoBuscado == i.tipo:
                print(i.show)

#FUNCIÓN BUSCAR POR PRECIO
def buscarPrecio(restaurante):
    productoBuscadoMin = input("Ingrese el monto mínimo")
    productoBuscadoMin = validarNum(productoBuscadoMin, "Ingrese el monto mínimo")
    productoBuscadoMax = input("Ingrese el monto máximo")
    productoBuscadoMax = validarNum(productoBuscadoMax, "Ingrese el monto máximo")
    for i in restaurante.products: 
        if i.precio <= productoBuscadoMax and i.precio >= productoBuscadoMin:
            print(i.show)

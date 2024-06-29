#CREACIÓN CLASE ESTADIOS
class Estadios:
    def __init__(self, id, name, city, capacity, restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants

    def show(self):
        return f'''
== DATOS DEL ESTADIO ==
NOMBRE DEL ESTADIO: {self.name} 
CIUDAD: {self.city}
CAPACIDAD: {self.capacity}
ID: {self.id}
'''

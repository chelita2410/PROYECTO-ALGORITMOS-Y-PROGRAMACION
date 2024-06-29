#CREACIÓN CLASE USUARIO
class Usuario:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.entradas = []

    def show(self):
        return f'''
== DATOS DEL USUARIO ==
NOMBRE: {self.nombre}
EDAD: {self.edad}
CÉDULA: {self.cedula}
ENTRADAS TOTALES COMPRADAS: {self.entradas}
'''
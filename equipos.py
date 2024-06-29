#CREACIÓN CLASE EQUIPOS
class Equipos:
    def __init__(self, name, id, code, group):
        self.name = name
        self.id = id
        self.code = code
        self.group = group
        
    def show(self):
        return f'''
== DATOS DEL EQUIPO ==
NOMBRE DEL EQUIPO: {self.name}
ID DEL EQUIPO: {self.id}
CÓDIGO DEL EQUIPO: {self.code}
GRUPO DEL EQUIPO: {self.group}
'''
    
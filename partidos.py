#CREACIÓN CLASE PARTIDOS
class Partidos: 
    def __init__(self, number, id, home, away, date, group, stadium_id):
        self.number = number
        self.id = id
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id = stadium_id
        self.entradas_vendidas = 0
        self.entradas_usadas = []
    
    def show(self):
        return f'''
== DATOS DEL PARTIDO ==
ID DEL PARTIDO: {self.id}
NÚMERO DE PARTIDO: {self.number}
EQUIPO LOCAL: {self.home.name}
EQUIPO VISITANTE: {self.away.name}
FECHA: {self.date}
GRUPO: {self.group}
NOMBRE DEL ESTADIO: {self.stadium_id.name}
'''
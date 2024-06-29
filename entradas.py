#IMPORT PARA EL ID DE LA ENTRADA
import random

#CREACIÓN CLASE ENTRADAS
class Entradas:
    def __init__(self, tipo, cliente, asiento, partidoEscogido):
        self.tipo = tipo
        self.cliente = cliente
        self.asiento = asiento
        self.partidoEscogido = partidoEscogido
        self.id = random.randint(10000000,999999999)
        self.usadas = False

    def show(self):
        return f'''
== DATOS DE LAS ENTRADAS ==
TIPO DE ENTRADA: {self.tipo}
CLIENTE: {self.cliente}
ASIENTO: {self.asiento}
PARTIDO: {self.partidoEscogido}
CÓDIGO DE TU ENTRADA: {self.id}
'''
    
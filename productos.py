#CREACIÓN CLASE PRODUCTOS
class Products:
    def __init__ (self, name, quantity, price, stock, clasificacion, tipo):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.clasificacion = clasificacion
        self.tipo = tipo
        self.comprados = 0
    
    def show(self):
        return f'''
== DATOS DEL PRODUCTO ==
NOMBRE: {self.name}
CANTIDAD: {self.quantity}
PRECIO: {self.price}
STOCK: {self.stock}
CLASIFICACION: {self.clasificacion}
TIPO: {self.tipo}
'''
    
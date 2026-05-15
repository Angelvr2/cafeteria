from exceptions.cantidad_invalida import CantidadInvalida

class Pedido:

    def __init__(self, producto, cantidad):
        if cantidad <= 0:
            raise CantidadInvalida("La cantidad debe ser mayor a 0")
        
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad
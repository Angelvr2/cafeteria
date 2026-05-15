class Ticket:

    IVA = 0.16

    def __init__(self, pedido):
        self.pedido = pedido
    
    def calcular_impuesto(self):
        return self.pedido.calcular_subtotal() * self.IVA
    
    def calcular_descuento(self):
        subtotal = self.pedido.calcular_subtotal()

        if subtotal >= 200:
            return subtotal * 0.10
        return 0
    
    def calcular_total(self):
        subtotal = self.pedido.calcular_subtotal()
        impuesto = self.calcular_impuesto()
        descuento = self.calcular_descuento()

        return subtotal + impuesto - descuento
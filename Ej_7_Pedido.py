class Pedido(object):
    codigo=None
    fecha=None
    entregado=None
    platoto=None
    persona=None
    def __init__(self,fecha,plato,persona,en):
        self.fecha=fecha
        self.platoto=plato
        self.persona=persona
        self.entregado=en
    def ModPlato(self,tuplatodemierda):
            self.platoto=tuplatodemierda

    def precioFinal(self):
        return (self.platoto.Precio*(100-self.persona.Desc()))/100


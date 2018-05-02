class Pedido(object):
    codigo=None
    fecha=None
    platoto=None
    persona=None
    entregado=None

    def __init__(self,fecha,hora,plato,persona,en):
        self.fecha=fecha
        self.platoto=plato
        self.persona=persona
        self.entregado=en

    def mod(self,a,b):
        if a == 'codigo':
            self.codigo=b
        if a == 'fecha':
            self.fecha=b
        if a == 'entregado':
            self.entregado=b
    def modpla(self,plato):
        self.platoto=plato
    def modpers(self):



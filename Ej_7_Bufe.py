class LasBufes(object):
    def __init__(self):
        self.Pedidos=[]
        self.Platos=[]
    def AgregarPedidos(self,pedido):
        self.Pedidos=pedido
    def AgregarPlato(self,platoto):
        self.Platos.append(platoto)
    def PlatosdelDia(self,fecha):
        for a in self.Pedidos:
            if a.fecha==fecha:
                return a.platoto.Nombre
    def borrarPedido(self,codigo):
        for a in self.Pedidos:
            if a.codigo == codigo:
                self.Pedidos.remove(a)
    def Modificarplatoto(self,codigo,nombre):
        for a in self.Pedidos:
            if a.codigo==codigo:
                for b in self.Platos:
                    if b.Nombre==nombre:
                        a.ModPlato(b)



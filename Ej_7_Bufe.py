class LasBufes(object):
    def __init__(self):
        self.Pedidos=[]
    def AgregarPedidos(self,pedido):
        self.Pedidos=pedido
    def PlatosdelDia(self,fecha):
        for a in self.Pedidos:
            if a.fecha==fecha:
                return a.platoto.Nombre
    def borrarPedido(self,codigo):
        for a in self.Pedidos:
            if a.codigo == codigo:
                self.Pedidos.remove(self,a)


    def ModPedido(self,Codigo,QueQuiereModificar,loquemete):
        for a in self.Pedidos:
            if a.codigo==Codigo:
                a.mod(QueQuiereModificar,loquemete)



    def modpla(self,codigo,meter):
        for a in self.Pedidos:
            if a.codigo==codigo:
                a.modpla(meter)

    def modper(self,codigo,meter):
        for a in self.Pedidos:
            if a.codigo == codigo:
                a.modpers(meter)

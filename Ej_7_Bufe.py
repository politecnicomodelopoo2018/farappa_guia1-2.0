from Ej_7_Alumno import Alumno
class LasBufes(object):
    def __init__(self):
        self.Pedidos=[]
        self.Platos=[]
    def AgregarPedidos(self,pedido):
        self.Pedidos.append(pedido)
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

    def GuardarAlumnos(self):
        f = open('Perasonas.Tomic', 'w')
        for a in self.Pedidos:
            if a.Desc() == 0:
                f.write(a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Division + '\n')
            else :
                f.write(a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Descuento + '\n')
        f.close()
    def Abrirlo(self):
        f = open('Perasonas.Tomic','r')
        for line in f:
            aux = line.split('|')
            unaP=Alumno(aux[0],aux[1],aux[2])
        f.close()
    


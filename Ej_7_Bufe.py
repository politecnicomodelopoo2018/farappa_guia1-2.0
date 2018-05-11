from Ej_7_Bufe import LasBufes
from Ej_7_Alumno import Alumno
from Ej_7_Pedido import Pedido
from Ej_7_Profesor import Profe
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
        f = open('Personas.Tomic', 'w')
        for a in self.Pedidos:
            if a.persona.Desc() == 0:
                f.write(a.persona.ID + '|' + a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Division + '\n')
            else :
                f.write(a.persona.ID + '|' + a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Descuento + '\n')
        f.close()
    def Abrirlo(self):
        listaPeidosNew=[]
        f = open('Pedidos.Tomic','r')
        for line in f:
            aux = line.split('|')
            Pedi=Pedido(aux[0],aux[1],aux[2],aux[3],aux[4])
            listaPeidosNew.append(Pedi)
        f.close()
        k = open('Personas.Tomic','r')
        for line in k:
            aux = line.split('|')
                for a in listaPeidosNew:
                    if aux[0] == a.persona:
                        if aux[0] ==  # Preguntar%(Profe) :
                            Prof=Profe(aux[0],aux[1],aux[2],aux[3])
                            a.persona=Prof
                        if aux[0] ==  # Preguntar%(Alumno) :
                            Al = Alumno(aux[0], aux[1], aux[2], aux[3])
                            a.persona=Al
        k.close()
        f = open('Platos.Tomic', 'r')
        for line in f:




    #Cargo todos las personas de los pedidos y dsp todos los platos
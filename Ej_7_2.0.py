from Ej_7_Alumno import Alumno
from Ej_7_Pedido import Pedido
from Ej_7_Profesor import Profe
from Ej_7_Plato import Plato


class LasBufes(object):
    def __init__(self):
        self.Pedidos = []
        self.Platos = []

    def AgregarPedidos(self, pedido):
        self.Pedidos.append(pedido)

    def AgregarPlato(self, platoto):
        self.Platos.append(platoto)

    def PlatosdelDia(self, fecha):
        for a in self.Pedidos:
            if a.fecha == fecha:
                return a.platoto.Nombre

    def borrarPedido(self, codigo):
        for a in self.Pedidos:
            if a.codigo == codigo:
                self.Pedidos.remove(a)

    def Modificarplatoto(self, codigo, nombre):
        for a in self.Pedidos:
            if a.codigo == codigo:
                for b in self.Platos:
                    if b.Nombre == nombre:
                        a.ModPlato(b)

    def GuardarPersonas(self):
        f = open('Personas.Tomic', 'w')
        for a in self.Pedidos:
            if a.persona.Desc() == 0:
                f.write(
                    a.persona.ID + '|' + a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Division + '\n'
                )
            else:
                f.write(
                    a.persona.ID + '|' + a.persona.Nombre + '|' + a.persona.Apellido + '|' + a.persona.Descuento + '\n'
                )
        f.close()

    def GuardarPlatos(self):
        f = open('Platos.Tomic','w')
        for a in self.Platos:
            f.write(
                a.ID + '|' + a.nombre + '|' + a.precio
            )
        f.close()

    def GuardarPedidos(self):
        f = open('Pedidos.Tomic','w')
        for a in self.Pedidos:
            f.write(
                a.codigo + '|' + a.fecha + '|' + a.entregado + '|' + a.platoto.ID + '|' + a.persona.ID
            )




    def Abrirlo(self):
        listaPeidosNew = []
        f = open('Pedidos.Tomic', 'r')
        for line in f:
            aux = line.split('|')
            Pedi = Pedido(aux[0], aux[1], aux[2], aux[3], aux[4])
            listaPeidosNew.append(Pedi)
        f.close()
        k = open('Personas.Tomic', 'r')
        for line in k:
            aux = line.split('|')
            for a in listaPeidosNew:
                if aux[0] == a.persona:
                    if aux[0].startswith('PRO') == True:
                        Prof = Profe(aux[0], aux[1], aux[2], aux[3])
                        a.persona = Prof
                    if aux[0].startswith('ALU') == True:
                        Al = Alumno(aux[0], aux[1], aux[2], aux[3])
                        a.persona = Al

        k.close()
        x = open('Platos.Tomic', 'r')
        for line in x:
            aux = line.split('|')
            Plat = Plato(aux[0], aux[1])
            for a in listaPeidosNew:
                if aux[0] == a.platoto:
                    a.platoto = Plat

        if listaPeidosNew != []:
            self.Pedidos = []
            for a in listaPeidosNew :
                self.Pedidos.append(a)

# Cargo todos las personas de los pedidos y dsp todos los platos
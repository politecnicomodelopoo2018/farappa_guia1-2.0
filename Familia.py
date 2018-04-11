from Prueba_2_Persona import Persona
class Family(object):

    def __init__(self):
        self.listaPersonas = []

    def AgregarPersona(self,Nombre,Fecha):
        Per = Persona(Nombre,Fecha)
        self.listaPersonas.append(Per)
    def AgregarPlato(self,Nombre,NombrePlato,Calorias):
        for a in self.listaPersonas:
            if a.Nombre == Nombre:
                a.AgregarComida(NombrePlato,Calorias)
    def CantCalo(self,Nombre):
        Cal=0
        for a in self.listaPersonas:
            if a.Nombre == Nombre:
                for b in a.ListaComidas:
                    Cal+=b.Calorias
        return Cal
    def Prom(self):
        Cal=0
        Cant=0
        for a in self.listaPersonas:
            Cant += len(a.ListaComidas)
            for b in a.ListaComidas:
                Cal += b.Calorias
        return Cal/Cant

    def Max(self):
        Primera = self.listaPersonas[0]
        for a in self.listaPersonas:
                if Primera.CaloriasTotal() < a.CaloriasTotal():
                    Primera = a
        return a.Nombre ,a.CaloriasTotal()

    def Min(self):
        Primera = self.listaPersonas[0]
        for a in self.listaPersonas:
                if Primera.CaloriasTotal() > a.CaloriasTotal():
                    Primera = a
        return a.Nombre ,a.CaloriasTotal()



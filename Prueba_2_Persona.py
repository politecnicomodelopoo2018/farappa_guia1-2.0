from Prueba_2_Plato import Plato
class Persona(object):
    Nombre=None
    Fecha_nac=None

    def __init__(self,Nombre,Fecha):
        self.Nombre=Nombre
        self.Fecha_nac=Fecha
        self.ListaComidas = []

    def AgregarComida(self,Nombre,Calorias):
        Com = Plato(Nombre,Calorias)
        self.ListaComidas.append(Com)
    def CaloriasTotal(self):
        Cal=0
        for a in self.ListaComidas:
            Cal+=a.Calorias
        return Cal
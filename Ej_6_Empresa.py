from Ej_6_Autos import Auto
from EJ_6_Camion import Camion
class Empresa(object):
    Nombre=None

    def __init__(self):
        self.ListaAutos=[]
        self.ListaCamiones=[]

    def AgregarAuto(self,A):
        self.ListaAutos.append(A)
    def AgregarCamion(self,A):
        self.ListaCamiones.append(A)
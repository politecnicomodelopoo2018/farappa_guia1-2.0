from Ej_6_Vehiculo import Vehiculo
class Auto(Vehiculo):
    Descapotable=None

    def __init__(self,d,p, c, f):
        Vehiculo.__init__(self, p, c, f)
        self.Descapotable=d

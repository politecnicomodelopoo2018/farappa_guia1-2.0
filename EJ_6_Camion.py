from Ej_6_Vehiculo import Vehiculo
class Camion(Vehiculo):
    Cap_carga=None


    def __init__(self,cap,p,c,f):
        Vehiculo.__init__(self,p,c,f)
        self.Cap_carga=cap

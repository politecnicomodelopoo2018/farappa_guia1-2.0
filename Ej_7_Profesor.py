from Ej_7_Persona import Persona
class Profe(Persona):
    P_Descuento=None

    def __init__(self,n,a,d):
        Persona.__init__(self,n,a)
        self.P_Descuento=d

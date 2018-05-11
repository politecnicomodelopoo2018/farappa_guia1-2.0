from Ej_7_Persona import Persona
class Profe(Persona):
    Descuento=None

    def __init__(self,id,n,a,d):
        Persona.__init__(self,id,n,a)
        self.Descuento=d
    def Desc(self):
        return self.Descuento
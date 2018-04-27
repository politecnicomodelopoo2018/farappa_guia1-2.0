from Ej_7_Persona import Persona
class Alumno (Persona):
    Division=None

    def __init__(self,n,a,d):
        Persona.__init__(self,n,a)
        self.Division=d

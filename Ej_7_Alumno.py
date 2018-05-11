from Ej_7_Persona import Persona
class Alumno (Persona):
    Division=None

    def __init__(self,id,n,a,d):
        Persona.__init__(self,id,n,a)
        self.Division=d

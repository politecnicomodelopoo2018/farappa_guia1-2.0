from Equipo import Equipo

class Partido (object):

    turno = None
    dia = None
    equipo1 = None
    equipo2 = None

    def Turno(self,turno):
        self.turno=turno
    def Dia(self,dia):
        self.dia=dia
    def eq1(self,eq1):
        self.equipo1=eq1
    def eq2(self,eq2):
        self.equipo2=eq2
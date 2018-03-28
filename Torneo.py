from Equipo import Equipo
from random import randint
from Partido import Partido

class Torneo(object):
    nombre = None


    def __init__(self, nombre):
        self.nombre = nombre
        self.listaEqui = []
        self.Fixture = []

    def AgregarTeam(self, nombre, turno, barrio):
        team = Equipo(nombre, turno, barrio)
        self.listaEqui.append(team)

    def Comp(self):


    def fishture(self,dia):
        for item in self.listaEqui:
            for equipo in self.listaEqui:
                for i in range(0,5):
                    for j in range(0,2):
                        if item.coordinacion(i,j) == equipo.coordinacion(i,j):
                            self.Partidito = Partido()
                            self.Partidito.Turno(j)
                            self.Partidito.Dia(i)
                            self.Partidito.eq1(item)
                            self.Partidito.eq2(equipo)
                            self.Fixture.append(self.Partidito)







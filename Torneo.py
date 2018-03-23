from Equipo import Equipo


class Torneo(object):
    nombre = None
    listaEqui = []
    fixture = []

    def __init__(self, nombre):
        self.nombre = nombre

    def AgregarTeam(self, nombre, turno, barrio):
        team = Equipo(nombre, turno, barrio)
        self.listaEqui = team

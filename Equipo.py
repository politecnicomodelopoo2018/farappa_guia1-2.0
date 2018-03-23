from Jugador import Jogador


class Equipo(object):
    nombre = None
    turno = None
    Barrio = None
    listaJogadores = []

    def __init__(self, nombre, turno, barrio):
        self.nombre = nombre
        self.turno = turno
        self.Barrio = barrio

    def agregarJugador(self, nombre, fecha, nro):
        for item in self.listaJogadores:
            if item.NroCamiseta == nro:
                return False
        j = Jogador(nombre, fecha, nro)
        self.listaJogadores.append(j)

    def setCap(self, name, capitan):
        for item in self.listaJogadores:
            if item.nombre == name:
                item.setCapitan(capitan)

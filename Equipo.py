from Jugador import Jogador


class Equipo(object):
    nombre = None
    turno = None
    Barrio = None
    dia = None


    def __init__(self, nombre, turno, barrio):
        self.nombre = nombre
        self.turno = turno
        self.Barrio = barrio
        self.listaJogadores = []

    def agregarJugador(self, nombre, fecha, nro):
        for item in self.listaJogadores:
            if item.NroCamiseta == nro:
                return False
            else :
                j = Jogador(nombre, fecha, nro)
        self.listaJogadores.append(j)

    def setCap(self, name, capitan):
        for item in self.listaJogadores:
            if item.nombre == name:
                item.setCapitan(capitan)
    def coordinacion(self,dias,hora):
        if self.dia == dias:
            if self.turno == hora:
                return True




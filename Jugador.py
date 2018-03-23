
class Jogador(object):
    nombre = None
    fechaNac = None
    NroCamiseta = None
    capitan = False

    def __init__(self,nombre,fecha,nro):
        self.nombre= nombre
        self.fechaNac=fecha
        self.NroCamiseta=nro
    def setCapitan(self,capitan):
        self.capitan=capitan


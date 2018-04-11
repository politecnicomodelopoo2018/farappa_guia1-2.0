class Llamada(object):
    Emisor=None
    Receptor=None
    Fecha=None
    Duracion=None

    def __init__(self,Em,Re,fecha,dur):
        self.Duracion=dur
        self.Emisor=Em
        self.Receptor=Re
        self.Fecha=fecha

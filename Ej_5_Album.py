from Ej_5_Cancion import Cancion
class Album(object):
    Titulo=None

    def __init__(self,tit):
        self.Titulo=tit
        self.ListaCan = []

    def AgregarCancion(self,titulo):
        Caca=Cancion()
        self.ListaCan.append(titulo)
    def AgregarAu(self,tit):
        for a in self.ListaCan:
            if a.Titulo == tit:
                for b in a.ListaAut:


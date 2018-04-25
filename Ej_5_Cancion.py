from Ej_5_Autores import Autores
from Ej_5_Artista import Artistoide
class Cancion(object):
    Titulo=None

    def  __init__(self,umtiti):
        self.Titulo=umtiti
        self.ListaAut=[]
        self.ListaArt=[]
    def AgregarAutor(self,Name,Ape,Fecha):
        au = Autores(Name,Ape,Fecha)
        self.ListaAut.append(au)
    def AgregarArtista(self,Name,Ape,Fecha):
        ar = Artistoide(Name,Ape,Fecha)
        self.ListaArt.append(ar)
    def nac(self,nombreart,pais):
        for a in self.ListaAut:
            if nombreart == a.Nombre:
                a.Nacionalizar(pais)

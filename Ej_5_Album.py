from Ej_5_Cancion import Cancion
class Album(object):
    Titulo=None

    def __init__(self,tit):
        self.Titulo=tit
        self.ListaCan = []

    def AgregarCancion(self,titulo):
        a = Cancion(titulo)
        self.ListaCan.append(a)

    def agregarArt(self,NombreCan,NameAr,Ape,Fecha):
        for a in self.ListaCan:
            if NombreCan == a.Titulo:
                a.AgregarArtista(NameAr,Ape,Fecha)

    def agregarAutor(self,nombreCan,nombreAu,Ape,Fecha):
        for a in self.ListaCan:
            if nombreCan == a.Titulo:
                a.AgregarAutor(nombreAu,Ape,Fecha)

    def nacArt(self,nomCan,noma,pais):
        for a in self.ListaCan:
            if nomCan == a.Titulo:
                a.nac(noma,pais)


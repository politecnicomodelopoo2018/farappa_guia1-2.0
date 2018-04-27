from Ej_5_Album import Album
class  Firma(object):
    Nombre=None

    def  __init__(self,nom):
        self.Nombre=nom
        self.listaAlbumes=[]
    def AgregarAlbum(self,tit):
        can = Album(tit)
        self.listaAlbumes.append(can)
    def AgregaCANCION(self,tit,titulo):
        for a in self.listaAlbumes:
            if tit == a.Titulo:
                a.AgregarCancion(titulo)



    def agregarau(self,tit,nombreCan,nombreAu,Ape,Fecha):
        for a in self.listaAlbumes:
            if a.Titulo == tit:
                a.agregarAutor(nombreCan,nombreAu,Ape,Fecha)

    def AgregarAr(self,titulo,NombreCan,NameAr,Ape,Fecha):
        for a in self.listaAlbumes:
            if titulo == a.Titulo:
                a.agregarArt(NombreCan,NameAr,Ape,Fecha)

    def nacional(self,tit,nomCan,noma,pais):
        for a in self.listaAlbumes:
            if tit == a.Titulo:
                a.nacArt(nomCan,noma,pais)

    def ListarAll(self, titA):
        lista = []
        for a in self.listaAlbumes:
            if titA == a.Titulo:
                for b in a.ListaCan:
                    for c in b.ListaArt:
                        lista.append(c.Nombre)
        return lista


    def ListarAll(self, titA,nac):
        lista = []
        for a in self.listaAlbumes:
            if titA == a.Titulo:
                for b in a.ListaCan:
                    for c in b.ListaAut:
                        if nac == c.Nacionalidad:
                            lista.append(c.Nombre)

        return lista





  # Conviene hacerlo pasandole directamente el autor/artista


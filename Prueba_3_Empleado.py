from Prueba_3_Llamada import Llamada
class Empleado(object):
    Nombre=None
    DNI=None
    Pais=None
    Numero=None

    def __init__(self,Nombre,DNI,Pais,Nro):
        self.Nombre=Nombre
        self.DNI=DNI
        self.Pais=Pais
        self.Numero=Nro
        self.ListaLlamadas=[]

    def AgregarLlamada(self,Em,Re,fecha,dur):
        Lla=Llamada(Em,Re,fecha,dur)
        self.ListaLlamadas.append(Lla)




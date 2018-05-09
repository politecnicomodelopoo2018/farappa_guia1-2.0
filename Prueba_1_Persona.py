from Prueba_1_Medidas import Medisonga
import datetime
class Persona(object):
    nombre=None
    apellido=None
    fecha_nac=None

    def __init__(self,nombre,apellido,fecha):
        self.lista_medidas = []
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nac=fecha


    def agregarMedidas(self,Peso, Altura,Fecha):
        a = Medisonga()
        a.Ingresardatos(Peso, Altura,Fecha)
        self.lista_medidas.append(a)

    def VerSegunFedeFer(self,fecha):
        for a in self.lista_medidas:
            if fecha == a.Fecha:
                return a.Peso , a.Altura
            #return False

    def Prom(self,año):

        cont = None
        sumP = None
        sumA = None
        for a in self.lista_medidas:
            if año == a.Fecha.year:
                sumP += a.Peso
                sumA += a.Altura
                cont += 1
            return sumP/cont , sumA/cont

    def Crecimiento(self,año1,año2):
        a=Prom(año1)
        b=Prom(año2)
        if a > b:
            return b-a
        return a-b

    def caca(self):
        for a in self.lista_medidas:
            return a.Peso

    def

